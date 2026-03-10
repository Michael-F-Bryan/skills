# Testing Workflows and Activities

Testing strategy and utilities for Temporal Python: activity unit tests, workflow + worker tests with time-skipping, and replay for determinism. For **activity design** see [activities.md](activities.md). For **determinism** and **versioning** see [determinism.md](determinism.md). For **workflow structure** see [workflows-continue-as-new.md](workflows-continue-as-new.md).

---

## Testing utilities (`temporalio.testing`)

### WorkflowEnvironment

- **Purpose:** Run workflows (and workers) against a test server without a real Temporal cluster.
- **Entry points:**
  - **`WorkflowEnvironment.start_time_skipping()`** — Recommended. In-memory test server that **skips time** when you await workflow results. Timers/sleeps are fast-forwarded except while activities run. Use for most workflow + worker tests.
  - **`WorkflowEnvironment.start_local()`** — Full local server (e.g. Temporal CLI dev server). No time skipping; heavier, use when you need full server behaviour.
  - **`WorkflowEnvironment.from_client(client)`** — Wraps an existing client (e.g. dev cluster). No time skipping.
- **Usage:** Async context manager; use `env.client` to start workflows and run workers. Time control (time-skipping env): `env.get_current_time()`, `env.sleep(duration)`, and `env.auto_time_skipping_disabled()` (context manager to turn off auto time skip while awaiting). Time is global to the environment.

### ActivityEnvironment

- **Purpose:** Run activity code **in isolation** (no worker, no server). Mocks activity context so `activity.info()`, `activity.heartbeat()`, cancellation work.
- **Run an activity:** `await env.run(callable, *args, **kwargs)`.
- **Customisation:** Set `env.info` (e.g. `ActivityEnvironment.default_info()` and `dataclasses.replace()`), `env.on_heartbeat` (callback for assertions), `env.metric_meter`, `env.payload_converter` before `run`. Use `env.cancel()` and `env.worker_shutdown()` to simulate cancellation and shutdown.

---

## Strategy: what to test and how

| Layer                 | Tool / approach                                                        | When to use                                                      |
| --------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Activity logic**    | Plain pytest, no Temporal                                              | Pure business logic called by activities (no `activity.*` usage) |
| **Activity + SDK**    | `ActivityEnvironment` + `env.run()`                                    | Code that uses `activity.info`, `heartbeat`, cancellation        |
| **Workflow + worker** | `WorkflowEnvironment.start_time_skipping()` + Worker + mock activities | Full workflow behaviour, timers, signals, queries                |
| **Determinism / CI**  | `Replayer` + saved or exported event histories                         | Before deploy, on workflow code changes                          |

- **Recommendation:** Prefer **integration tests** (workflow + worker against time-skipping env with mocked activities) for coverage; add activity unit tests with `ActivityEnvironment` where heartbeat/cancellation/info matter; keep business logic tests free of Temporal.
- **Isolation:** Use a unique task queue per test (e.g. UUID) when running multiple tests against the same env to avoid collisions.

---

## Activity unit tests

- **Tool:** `ActivityEnvironment` only. No Worker or server.
- **Pattern:** Instantiate `ActivityEnvironment`, optionally set `info`, `on_heartbeat`, etc., then `await env.run(activity_fn, arg1, arg2)`.
- **Heartbeats:** Set `env.on_heartbeat = lambda *args: heartbeats.append(args[0])`, run the activity, then assert on `heartbeats`.
- **Cancellation:** Call `env.cancel()` (e.g. from a background task) while the activity runs to test cancellation handling.
- Keep business logic in a separate function; unit test that logic with plain pytest. Use `ActivityEnvironment` for code paths that depend on `activity.*`.

---

## Integration / worker tests

- **Server:** Use time-skipping test server via `WorkflowEnvironment.start_time_skipping()` so timer-heavy workflows finish quickly.
- **Worker:** Create a `Worker` with `client=env.client`, your workflow and activity definitions, and a dedicated task queue (e.g. `str(uuid.uuid4())` per test).
- **Mocking activities:** Register mock activity implementations with the Worker (same `@activity.defn` name and compatible signature). The workflow runs against the test server but calls your mock instead of the real activity.
- **Running a workflow:** `await env.client.execute_workflow(YourWorkflow.run, args, id=..., task_queue=...)` then assert on the result. Use normal `assert` in workflow code; the test environment will fail the workflow with the assertion error.

---

## Time skipping (summary)

- **Automatic:** With `start_time_skipping()`, when you **await** a workflow **result**, the test server advances time as needed (e.g. past sleeps). Timers are fast-forwarded except when activities are running.
- **Manual:** Use `await env.sleep(seconds)` (or timedelta) to advance time explicitly.
- **Disable auto skip:** Use `with env.auto_time_skipping_disabled():` when you want to await a result without the server auto-advancing time (e.g. to assert intermediate state).
- Time is global; don’t rely on independent time lines for concurrent tests on the same env.

---

## Replay (workflow history)

- **Purpose:** Re-run workflow code against recorded event history to detect **non-determinism** and validate changes before deploy.
- **API:** `temporalio.worker.Replayer(workflows=[...], ...)`. Methods: `replay_workflow(history)`, `replay_workflows(histories)`.
- **History source:** Export from CLI (`temporal workflow show --output json`), Web UI, or client listing with `map_histories()` (Advanced Visibility).
- **CI:** Run replay on a representative set of histories (e.g. per task queue or workflow type); fail CI if any replay raises (non-determinism or incompatible change). Use versioning (e.g. `workflow.patched()`) when you change the command sequence; add replay tests with saved history. See [determinism.md](determinism.md).
