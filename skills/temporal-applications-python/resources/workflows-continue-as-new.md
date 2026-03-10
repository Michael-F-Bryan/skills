# Workflows with Dynamic Inputs and Continue-As-New

Guidance for workflows that process a **dynamic number of inputs** and must use **Continue-As-New** to avoid exceeding Temporal's history size. For **determinism** rules in workflow code see [determinism.md](determinism.md). For **testing** workflow + worker see [testing.md](testing.md).

---

## When to use

- Workflow processes a **list or queue that can grow over time** (e.g. crawl N articles, discover more from results, keep going).
- Temporal history is bounded; long-running loops must periodically "continue as new" and pass state via new params.

**Rule of thumb:** Each for-loop in a workflow should probably be extracted to its own child workflow. The parent starts one child per item (or per batch); the child does the per-item work. That keeps history small and aligns with Continue-As-New when the list is dynamic.

---

## Params model

- Pydantic model that carries the **current state** for the next run.
- Example fields: `to_crawl: Sequence[ArticleInfo]`, `already_crawled: Sequence[ArticleInfo]`, `crawl_id: int`, `batch_size: int`.
- Use `Field(default_factory=list)` for optional/accumulated fields.
- **All state that must survive Continue-As-New must be in this model** (and must be serialisable).

---

## Workflow class state

- In `__init__`, initialise **mutable** workflow-only state used during the current run: e.g. `self.to_crawl: list[ArticleInfo] = []`, `self.already_crawled: set[ArticleInfo] = set()`, and any metrics.
- Do not store large or unbounded data only in `self`; it goes in history.
- At the start of `run(self, params)`, copy from params into `self` (e.g. `self.to_crawl = list(params.to_crawl)`).

---

## Loop shape

1. **Loop:** `while self.to_crawl:` (or similar).
2. **Take a batch:** e.g. `n = min(params.batch_size, len(self.to_crawl))`, `batch = [self.to_crawl.pop() for _ in range(n)]`.
3. **Start child workflows:** e.g. `workflow.execute_child_workflow(ChildWorkflow.run, ChildParams(...))` for each item. Collect tasks in a list.
4. **Await and collate results:** `asyncio.gather(..., return_exceptions=True)`, then `match result:` with success type, `ChildWorkflowError`, `BaseException` (re-raise with context), and `case _: typing.assert_never(result)` for exhaustiveness.
5. **Update workflow state:** e.g. `self.already_crawled.update(batch)`; extend `self.to_crawl` from result data (e.g. URLs discovered from each processed item).
6. **Before next iteration:** Check `if workflow.info().is_continue_as_new_suggested():` then `workflow.continue_as_new(Params(crawl_id=..., to_crawl=self.to_crawl, already_crawled=list(self.already_crawled), ...))` so the next "run" gets a fresh history with the current state in params. If not suggested, continue the loop.
7. **Return:** When the loop exits (e.g. `self.to_crawl` is empty), return a Pydantic result (e.g. `CrawlAllResult()`).

---

## Progress queries (optional)

Use `@workflow.query` to expose progress so callers can poll without waiting for completion:

```python
@workflow.query
def progress(self) -> Progress:
    return Progress(
        crawled=len(self.already_crawled),
        to_crawl=len(self.to_crawl),
        total=len(self.already_crawled) + len(self.to_crawl),
    )
```

---

## Example 1: Batch-at-a-time (simpler)

Process one batch of N items at a time; one slow child blocks the whole batch (workers can sit idle). Good when batch size is small or item durations are similar.

```python
@workflow.run
async def run(self, params: CrawlAllParams) -> CrawlAllResult:
    self.to_crawl = list(params.to_crawl)
    self.already_crawled = set(params.already_crawled)

    while self.to_crawl:
        n = min(params.batch_size, len(self.to_crawl))
        batch = [self.to_crawl.pop() for _ in range(n)]

        tasks = [
            workflow.execute_child_workflow(
                ProcessArticleWorkflow.run,
                ProcessArticleParams(url=item.url, version_number=item.version_number, crawl_id=params.crawl_id),
            )
            for item in batch
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            match result:
                case ProcessArticleResult(): ...
                case ChildWorkflowError(): ...
                case BaseException() as e: raise RuntimeError("Unexpected") from e
                case _: typing.assert_never(result)

        self.already_crawled.update(batch)
        self._extend_to_crawl_from_results(...)

        if workflow.info().is_continue_as_new_suggested():
            workflow.continue_as_new(
                CrawlAllParams(
                    crawl_id=params.crawl_id,
                    to_crawl=self.to_crawl,
                    already_crawled=list(self.already_crawled),
                )
            )

    return CrawlAllResult()
```

---

## Example 2: N in flight (higher throughput)

Keep **N child workflows in flight** with `asyncio.wait(..., return_when=asyncio.FIRST_COMPLETED)`. As one completes, process it and start another; workers stay busy. Trades code complexity for throughput. **Before Continue-As-New, drain remaining in-flight tasks** (e.g. `await asyncio.gather(*active_tasks)`), then clear task maps and pass aggregated state in the new params.

```python
# Refill up to concurrency; wait for first completed; process done; repeat.
# When workflow.info().is_continue_as_new_suggested():
#   await asyncio.gather(*active_tasks)  # drain remaining
#   active_tasks.clear(); item_by_task.clear()
#   workflow.continue_as_new(CrawlAllParams(crawl_id=..., stats_so_far=self.stats))
```

---

## Throughput consideration

- **Batch-at-a-time:** Easier to implement and debug. However, one very slow child in a batch delays the next batch; workers may sit idle.
- **N in flight:** More complex (task set, `asyncio.wait`, draining before continue_as_new). Keeps N children running so workers stay busy; better throughput when child runtimes vary a lot.
