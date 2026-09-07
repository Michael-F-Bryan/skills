# Validating observability review findings

Use this when an external reviewer recommends tracing or logging changes to a CLI, protocol driver, or interactive terminal path.

## Validation sequence

1. **Classify each output write before replacing it.**
   - Final command results and remote combined streams may intentionally belong on stdout.
   - Interactive validation belongs through the terminal library's writer so it can repaint the prompt.
   - Infrastructure degradation that is not command output belongs in structured logging, provided no live renderer currently owns the stream.
2. **Place spans around finite operator or protocol operations, not transport chunks.** Good boundaries include command execution, remote-shell attachment, and bounded release. Reject per-frame, per-read, and per-payload spans.
3. **Keep sensitive and high-cardinality values out.** Do not attach arbitrary command lines, console output, payload bytes, or credentials to spans or logs. Low-cardinality target IDs, device kind, mode, attempt count, and duration are useful.
4. **Check error semantics against the authoritative producer.** Do not downgrade a cleanup error to a warning because a reviewer assumes a remote timeout or recovery path. Inspect the protocol implementation first. A failed release remains a failed operation when the producer does not guarantee expiry.
5. **Bound retry telemetry.** A bounded retry loop may log each attempt. An unbounded 500 ms loop must not warn forever; emit one warning when degraded behaviour begins, then keep an attempt count on the operation span or log only at deliberately sparse intervals.
6. **Preserve trace context while detaching cancellation.** For bounded teardown that must outlive caller cancellation, use `context.WithTimeout(context.WithoutCancel(ctx), limit)` rather than `context.Background()`.
7. **Verify OpenTelemetry API claims against current docs and local precedent.** In Go, `span.RecordError(err)` does not set error status. When the operation failed, also call `span.SetStatus(codes.Error, "")` unless the error text is intentionally excluded. For sensitive operator-entered errors, marking status without recording the error body is valid.
8. **Avoid test-only telemetry APIs.** Test structured logs through the repository's existing logger replacement hook. If the tracer is intentionally private, verify instrumentation through focused compilation, behavioural tests around context propagation, and exact diff inspection rather than exporting a setter solely for tests.

## Useful focused tests

- A context value survives cancellation into detached teardown.
- A degraded optional capability emits one structured warning and does not write raw diagnostic bytes to an injected stderr buffer.
- Multiple unbounded-handshake retries emit one warning, not one warning per interval.
- A failed remote release remains observable as an error when the remote protocol has no authoritative timeout.
- Existing stdout tests continue to pin exact remote output and combined-stream semantics.

## Reviewer-premise traps

- “The repository never does X” — search the whole owning package before accepting it.
- “The remote timeout cleans this up” — read the producer; timeout fields are often ignored.
- “Every print should be a log” — command output is a public interface, not diagnostic noise.
- “More telemetry is better” — hot-path logs and spans can make an incident less observable.
