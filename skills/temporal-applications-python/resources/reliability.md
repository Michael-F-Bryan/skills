# Reliability — Timeouts, Retries, and Idempotency

Activity execution policy and side-effect safety: timeouts, retry policy, and idempotent design. For activity **class shape and params/result** see [activities.md](activities.md). For **testing** see [testing.md](testing.md).

---

## Activity timeouts

At least **one** of **start-to-close** or **schedule-to-close** must be set. Set timeouts on `execute_activity()` / `start_activity()` (e.g. `start_to_close_timeout=timedelta(...)`).

| Timeout               | Purpose                                                                     | Recommendation                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schedule-to-close** | Max time from first schedule until completion (all retries).                | Use to cap total duration; good for “give up after N minutes”.                                                                                                                   |
| **Start-to-close**    | Max time for a **single** attempt (one run from start to completion).       | **Always set.** Detects crashed/hung workers so the activity can retry. Must be longer than longest legitimate run; for very long activities use heartbeats + heartbeat_timeout. |
| **Schedule-to-start** | Max time the task may sit in the queue before a worker starts it.           | Optional; prefer metrics and scaling; set only if you have reroute or compensation logic.                                                                                        |
| **Heartbeat timeout** | Max time between two heartbeats; no heartbeat → activity failed, can retry. | Use for long-running activities so failures are detected sooner than one long start-to-close. Call `activity.heartbeat(...)` in the activity.                                    |

---

## Retry policy

Override default (exponential backoff, unlimited attempts) via `retry_policy=` on `execute_activity()` / `start_activity()`.

- **maximum_attempts** — Cap attempts; 1 = no retries.
- **initial_interval**, **backoff_coefficient**, **maximum_interval** — Backoff timing.
- **non_retryable_error_types** — List of `ApplicationError` type strings that must not be retried.

**Non-retryable errors:** For permanent failures (e.g. invalid input, validation errors) raise `ApplicationError(..., non_retryable=True)` or list the error type in `non_retryable_error_types` so the workflow fails fast instead of burning retries.

**Optional:** `ApplicationError(..., next_retry_delay=timedelta(...))` to override the next retry interval (e.g. rate-limit backoff).

---

## Recommended timeout/retry patterns

1. **Always set start_to_close_timeout** so a single attempt cannot hang forever.
2. **Use schedule_to_close_timeout** to cap total time (including retries).
3. **Long-running activities:** Use `activity.heartbeat()` in a loop and set `heartbeat_timeout`; set `start_to_close_timeout` to allow the longest run between heartbeats.
4. **Permanent failures:** Mark non-retryable so the workflow can fail or compensate quickly.
5. **Idempotency:** Design activities for at-least-once execution; timeouts and retries cause re-execution (see below).

---

## Common mistakes

- No start-to-close → crashed worker never completes; workflow can stall.
- Start-to-close too short → false timeouts; use heartbeats for long work.
- Unlimited retries without schedule-to-close → retries can run very long.
- Retrying permanent failures → burn retries; mark them non-retryable.
- Long activities without heartbeats → slow failure detection; use heartbeat_timeout.
- Non-idempotent activities with retries → duplicate side effects; design for idempotency.

---

## Idempotency

Activities run **at least once**. They can execute multiple times due to retries or worker crash before completion is reported. The **commit–notify gap** (worker commits to DB then crashes before notifying Temporal) means Temporal may retry after the side effect is already done. Correctness is the application’s responsibility: any activity that performs writes or external API calls with side effects should be designed so that running it again with the same logical input produces the same outcome and no extra side effects.

### Patterns

1. **Idempotency keys** — Use a stable key per logical operation; pass to systems that support it (payments, many REST APIs). In Python use `activity.info().workflow_run_id` and `activity.info().activity_id` to build a key (e.g. `f"{info.workflow_run_id}-{info.activity_id}"`). The downstream service stores the key and returns the original result for duplicate keys.

2. **Conditional writes / unique constraints** — Unique constraint on business key (e.g. `order_id`); first run inserts, retry hits constraint → treat as success or return existing row. Upsert / `INSERT ... ON CONFLICT DO NOTHING` (or UPDATE). Idempotency table: dedicated table with `idempotency_key UNIQUE`; insert key in same transaction as business write; if insert fails (duplicate), skip business write and return stored outcome; prune old keys periodically.

3. **Check pre-existing result** — “If desired outcome already exists, return it; else do the work.” Safe only if the write is itself deduplicated (e.g. unique constraint) or you have external serialisation (e.g. lock workflow per entity). Avoid check-then-act races without a unique constraint.

4. **Idempotent handlers / natural keys** — If the business operation already has a natural key (e.g. “create order for order_id”), use it; if the API/DB treats duplicate as no-op or returns existing result, no extra key needed. When the API/DB doesn’t support keys, add an idempotency key in your own layer (e.g. workflow_run_id + activity_id) and map to “do once per key”.

### Pitfalls

- **Commit at end is not enough** — The gap between commit and “Temporal sees success” still exists; the DB write must be idempotent (key or constraint).
- **Check-then-act races** — “If not exists then insert” without a unique constraint allows double-insert; prefer unique constraints or insert-first idempotency keys.
- **Non-idempotent APIs** — If the external system has no idempotency support: (1) at-most-once (e.g. `maximum_attempts=1`) and handle failure in the workflow (compensation or human handoff), or (2) wrap in an idempotent layer you control.

### Best practices

- Activities that write should be idempotent (keys, unique constraints, or upserts).
- Prefer `workflow_run_id` + `activity_id` for keys when the downstream accepts a client-chosen key.
- Keep activities small and atomic; don’t rely on in-memory state across retries.
- If you use at-most-once for a non-idempotent operation, document the failure path (compensation or manual resolution).
