# Labeling Sample: Dimension 8 - Commenting Philosophy

Dimension reminder: preference for comments that explain intent/constraints/tradeoffs versus comments that restate obvious mechanics.

---

```rust
// We intentionally cap retries to avoid duplicate side effects on upstream payment capture.
pub fn clamp_retry_attempts(requested: u8) -> u8 {
    requested.min(3)
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
    - This is a good example of a comment that explains the *why* of the code, not just what it does

---

```go
package metrics

// This function returns sum.
func Sum(vals []int) int {
	// initialize result
	result := 0
	// loop over values
	for _, v := range vals {
		// add v to result
		result = result + v
	}
	// return result
	return result
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
   - This is a waste of time. The comments aren't telling me anything that the code doesn't already say.
   - It's actually got negative value because if I came along later and updated the `result = result + v` to `result -= v`, the comments would be wrong.

---

```python
def parse_timeout_ms(raw: str) -> int:
    # Keep timeout parsing strict because this feeds circuit-breaker tuning.
    value = int(raw)
    if value <= 0:
        raise ValueError("timeout must be positive")
    return value
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - This is probably a bad comment because it's not immediately obvious why being "strict" with the parsing is needed by the circuit breaker.

---

```ts
// TODO: maybe this does the thing???
export function buildDisplayName(first: string, last: string): string {
  // trim first
  const a = first.trim();
  // trim last
  const b = last.trim();
  // combine
  return `${a} ${b}`;
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
    - Useless doc-comment - if the author doesn't know what it does why how should I? Doc-comments should make it obvious why the function exists and where it fits into the wider system
    - The code comments are just repeating the code and add no value
