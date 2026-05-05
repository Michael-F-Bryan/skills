# Labeling Sample: Dimension 13 - Testability by Construction

Dimension reminder: how strongly code is shaped for deterministic, isolated tests via explicit seams and dependency injection (without unnecessary abstraction).

---

```rust
use reqwest::blocking::Client;
use std::time::{SystemTime, UNIX_EPOCH};

pub fn issue_receipt(order_id: &str, amount_cents: u64) -> Result<String, String> {
    let now = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map_err(|_| "clock failure".to_string())?
        .as_secs();

    let payload = format!(r#"{{"order_id":"{order_id}","amount":{amount_cents},"ts":{now}}}"#);

    let client = Client::new();
    let response = client
        .post("https://payments.example.com/receipts")
        .body(payload)
        .send()
        .map_err(|e| e.to_string())?;

    if !response.status().is_success() {
        return Err(format!("receipt API failed: {}", response.status()));
    }

    Ok(format!("rcpt-{order_id}-{now}"))
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - Eww...
  - We should be able to inject the time instead of having it hard-coded from `SystemTime::now()`
  - Creating a new `Client` for each request is also a bit of a smell. We should be able to reuse the same client for the lifetime of the application (e.g. to enable connection pooling and use a consistent User-Agent)
  - We're hard-coding the way we send the receipt here, rather than passing in some sort of receipt issuing dependency to the code that needs it
  - Stringly-typed errors are pretty useless. at the very least, we should be using `anyhow::Error` so we get backtraces and can chain onto the cause

---

```go
package receipts

import (
	"context"
	"fmt"
	"time"
)

type Clock interface {
	Now() time.Time
}

type API interface {
	CreateReceipt(ctx context.Context, req CreateReceiptRequest) error
}

type CreateReceiptRequest struct {
	OrderID     string
	AmountCents uint64
	Timestamp   time.Time
}

type Service struct {
	clock Clock
	api   API
}

func NewService(clock Clock, api API) Service {
	return Service{clock: clock, api: api}
}

func (s Service) Issue(ctx context.Context, orderID string, amountCents uint64) error {
	if orderID == "" {
		return fmt.Errorf("orderID required")
	}
	if amountCents == 0 {
		return fmt.Errorf("amount must be > 0")
	}
	req := CreateReceiptRequest{
		OrderID:     orderID,
		AmountCents: amountCents,
		Timestamp:   s.clock.Now(),
	}
	return s.api.CreateReceipt(ctx, req)
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence:
  - I like that the `Clock`, `API`, and `CreateReceiptRequest` have been factored out into interfaces
  - however, I feel like `Service` isn't pulling its weight. I'd inline the whole thing and just construct the `CreateReceiptRequest` and call `s.api.CreateReceipt()` directly in whatever code is wanting to issue a receipt

---

```python
import datetime as dt
import requests


class MetricsReporter:
    def report_job_success(self, job_name: str, duration_ms: int) -> None:
        payload = {
            "job": job_name,
            "duration_ms": duration_ms,
            "reported_at": dt.datetime.utcnow().isoformat(),
        }
        requests.post("https://metrics.example.com/job-success", json=payload, timeout=5)
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - I like that we're pulling the metric emission out into a method on the `MetricsReporter` type - that allows the metric to be standardized, which in turn means our alerting and dashboards can rely on always having access to certain fields
  - I probably wouldn't hard-code the request posting logic though, the `MetricsReporter` should probably store an otel metrics provider and submit the metrics through that - that way we aren't hard-coding that metrics are done by sending a HTTP request to a hard-coded URl

---

```ts
type Clock = { nowMs(): number };
type MetricsSink = { emit(event: string, payload: Record<string, unknown>): Promise<void> };

type Deps = {
  clock: Clock;
  sink: MetricsSink;
};

export function createReporter(deps: Deps) {
  return {
    async reportJobSuccess(jobName: string, durationMs: number): Promise<void> {
      if (!jobName) throw new Error("jobName required");
      if (durationMs < 0) throw new Error("durationMs must be >= 0");

      await deps.sink.emit("job.success", {
        jobName,
        durationMs,
        reportedAtMs: deps.clock.nowMs(),
      });
    },
  };
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence: Looks good to me
