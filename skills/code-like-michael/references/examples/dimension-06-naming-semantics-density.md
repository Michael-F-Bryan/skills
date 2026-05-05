# Labeling Sample: Dimension 6 - Naming Semantics Density

Dimension reminder: how strongly names encode domain intent and role versus generic/ambiguous identifiers.

---

```rust
pub struct RetryPolicy {
    pub max_attempts: u8,
    pub backoff_millis: u64,
}

pub fn should_retry_http_request(attempt_index: u8, status_code: u16, policy: &RetryPolicy) -> bool {
    attempt_index < policy.max_attempts && matches!(status_code, 408 | 429 | 500..=599)
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - Says what it does on the tin

---

```go
package p

func Do(a int, b int, c bool) int {
	x := a + b
	if c {
		x = x * 2
	}
	return x
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This function is completely useless - the only way to know what it does is by reading the body
  - Even then, you still have no idea what `a`, `b`, and `c` even *mean*

---

```python
def compute_invoice_total_cents(line_item_amounts_cents: list[int], tax_rate_percent: float) -> int:
    subtotal_cents = sum(line_item_amounts_cents)
    tax_cents = round(subtotal_cents * (tax_rate_percent / 100))
    return subtotal_cents + tax_cents
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - The unit suffixes are useful as a once-off, but I feel like it's bloating the function
  - It'd be better to use strongly-typed units (e.g. using the `pint` library)

---

```ts
export function f(a: string, b: string, c: number): string {
  const x = a.trim();
  const y = b.trim();
  const z = `${x}-${y}-${c}`;
  return z.toLowerCase();
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - You could at least try to give the function and parameters more descriptive names
