# Workflow Determinism

Workflow code must be deterministic so replay matches event history. Use the SDK's workflow APIs for time/random; put I/O and external calls in activities; version changes with patching; and add replay tests. For **workflow structure** (Continue-As-New, loop shape) see [workflows-continue-as-new.md](workflows-continue-as-new.md). For **testing** and **Replayer** see [testing.md](testing.md).

---

## Why determinism matters

Workflows are **replayed** from event history (worker restart, retries, signals, timers, after code deploy). Replay re-runs workflow code and checks that the **sequence of commands** (schedule activity, start timer, etc.) matches the recorded history. If the code produces a different sequence, the SDK raises **`NondeterminismError`** (or sandbox **`RestrictedWorkflowAccessError`**) and the workflow task fails.

---

## Allowed in workflow vs must be in activities

| In workflow (orchestration only)                                               | In activities (non-determinism OK)                         |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| `workflow.execute_activity()` / `execute_activity_method()`                    | HTTP, DB, file I/O, external APIs                          |
| `workflow.execute_child_workflow()`                                            | `time.time()`, `datetime.now()`, system time               |
| `workflow.start_timer()` / `asyncio.sleep()` (SDK-managed)                     | `random.random()`, `random.randint()`, `uuid.uuid4()`      |
| `workflow.now()`, `workflow.time()`, `workflow.time_ns()`                      | Any call that can return different results for same inputs |
| `workflow.random()` (e.g. `workflow.random().randint(a, b)`)                   |                                                            |
| `workflow.uuid4()`                                                             |                                                            |
| `workflow.logger`                                                              |                                                            |
| Pure logic, branching on activity/child results, Pydantic models (passthrough) |                                                            |

**Rule:** Workflow code may only use **inputs + results of workflow APIs** (activities, timers, child workflows, signals) to decide what to do next. Anything that reads “the outside world” (clock, RNG, network, disk) must go in an activity.

---

## Isolating non-determinism

1. **Time** — Use `workflow.now()` or `workflow.time()` / `workflow.time_ns()`, not `datetime.now()` or `time.time()`. Use `asyncio.sleep()` (and/or `workflow.start_timer()`) for delays.
2. **Random** — Use `workflow.random()` (e.g. `workflow.random().randint(1, 100)`), not `random` module. Use `workflow.uuid4()` for UUIDs.
3. **I/O and external systems** — No direct HTTP, DB, or file access in workflow code. Invoke activities and branch only on their returned values.
4. **Iteration order** — Use structures with deterministic iteration (e.g. Python dicts). Avoid relying on `set` iteration order for logic that affects the command sequence.
5. **Run ID** — Be careful storing or branching on workflow run ID; it can differ across runs/replays.

---

## Sandbox (Temporal Python)

Workflows run in a **sandbox**: restricted imports block known non-deterministic stdlib calls (e.g. `time.time()`, `random.randint()`). Using them typically raises **`RestrictedWorkflowAccessError`**. Non-stdlib modules are reloaded per workflow run unless passed through; only passthrough side-effect-free, deterministic modules. **Do not** use `sandboxed=False` or `sandbox_unrestricted()` — that removes determinism checks.

---

## Versioning and patching

When you **change workflow logic** in a way that would change the command sequence for existing histories (e.g. add/remove/reorder activities or timers), use **versioning with Patching** so in-flight workflows keep the old path and new runs use the new path.

- **`workflow.patched("patch-id")`** — Branch: run new code only when the patch is present; on replay, returns true/false from history so the same path is replayed.
- **`workflow.deprecate_patch("patch-id")`** — After all old runs are gone, call this and then remove the branch; later you can remove the deprecation call.

**Replay tests:** Use `Replayer` with saved event history JSON to ensure current workflow code replays old histories without `NondeterminismError`. See [testing.md](testing.md).

---

## Pitfalls

- Using **`time` / `datetime` / `random`** in workflow instead of `workflow.now()`, `workflow.time()`, `workflow.random()`, `workflow.uuid4()`.
- Doing **I/O or external calls** in the workflow instead of in activities.
- **Adding/removing/reordering** activities or timers without a patch when there are still running workflows on the old code path.
- Relying on **set iteration order** or **run ID** for control flow that affects the command sequence.
- Disabling the sandbox and then using non-deterministic APIs.

---

## Minimal examples

**Bad (non-deterministic):**

```python
@workflow.run
async def run(self) -> str:
    if random.randint(0, 1):  # RestrictedWorkflowAccessError / nondeterministic
        await asyncio.sleep(60)
    return await workflow.execute_activity(activity_fn, args)
```

**Good (deterministic):**

```python
@workflow.run
async def run(self) -> str:
    if workflow.random().randint(0, 1):
        await asyncio.sleep(60)  # SDK records timer; replay reproduces it
    return await workflow.execute_activity(activity_fn, args)
```

**Versioned change (patch):**

```python
if workflow.patched("use-new-activity"):
    result = await workflow.execute_activity(new_activity, ...)
else:
    result = await workflow.execute_activity(old_activity, ...)
```
