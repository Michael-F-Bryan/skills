# Labeling Sample: Dimension 12 - Cross-Cutting Concern Placement

Dimension reminder: whether logging/metrics/auth/retries are handled consistently at boundaries or scattered through core logic.

---

```rust
pub fn calculate_shipping_cents(weight_grams: u64, zone: u8) -> u64 {
    // Pure domain calculation; cross-cutting handled by caller/application layer.
    let base = 500 + (weight_grams / 100) * 20;
    base + (zone as u64 * 50)
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - Looks good? I don't quite know what I'm looking for here

---

```go
package pricing

import "log"

func Quote(amount int64, tier string) int64 {
	log.Println("quote.start", amount, tier)
	if amount <= 0 {
		log.Println("quote.error.invalid_amount")
		return 0
	}
	if tier == "gold" {
		log.Println("quote.metric.gold_hit")
		return amount - amount/5
	}
	log.Println("quote.done")
	return amount
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - I might write code like this while debugging, but the log statements would all get deleted before it is merged
  - If the start `quote.start` and `quote.done` were replaced with an otel span that gets `defer span.End()` that's another story, though

---

```python
class CheckoutService:
    def __init__(self, payments, audit_logger):
        self.payments = payments
        self.audit_logger = audit_logger

    def charge(self, customer_id: str, amount_cents: int) -> str:
        self.audit_logger.info("checkout.charge.start", customer_id=customer_id)
        charge_id = self.payments.charge(customer_id, amount_cents)
        self.audit_logger.info("checkout.charge.success", charge_id=charge_id)
        return charge_id
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - It's good to see that they're using structured logging and have stable message IDs
  - Knowing when a charge has started and succeeded is valuable business information, rather than just being a debug log

---

```ts
export async function createInvoice(customerId: string, amountCents: number): Promise<string> {
  if (!customerId) throw new Error("customerId required");
  if (amountCents <= 0) throw new Error("amount must be positive");

  // auth, retry, and metrics are all mixed inline here
  if (!process.env.API_TOKEN) throw new Error("not authorized");
  let attempts = 0;
  while (attempts < 3) {
    attempts++;
    try {
      const res = await fetch("https://api.example.com/invoices", {
        method: "POST",
        headers: { Authorization: `Bearer ${process.env.API_TOKEN}` },
        body: JSON.stringify({ customerId, amountCents }),
      });
      if (!res.ok) continue;
      console.log("metric.invoice_created", attempts);
      return (await res.json()).id;
    } catch {
      // ignore
    }
  }
  throw new Error("invoice create failed");
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - I'd want to log when we do a retry
  - We are also dropping the exception message when it should probably be logged
  - I'd probably also want to log some metadata about the invoice being created
