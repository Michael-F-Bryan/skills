# Labeling Sample: Dimension 3 - Mutation Budget

Dimension reminder: tolerance for mutable state and reassignment in local scope versus immutable-by-default style with narrow mutation windows.

---

```rust
pub fn summarize_scores(scores: &[u32]) -> ScoreSummary {
    if scores.is_empty() {
        return ScoreSummary {
            min: None,
            max: None,
            average: None,
        };
    }

    let min = scores.iter().copied().min();
    let max = scores.iter().copied().max();
    let sum: u64 = scores.iter().map(|v| *v as u64).sum();
    let average = Some(sum as f64 / scores.len() as f64);

    ScoreSummary { min, max, average }
}

pub struct ScoreSummary {
    pub min: Option<u32>,
    pub max: Option<u32>,
    pub average: Option<f64>,
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - This is okay, but iterating three times feels kinda wasteful.
  - I also don't like that each of the fields is an `Option` because you would need to handle "impossible" states like `min` being `Some` while `max` is `None`. It'd be better for them all to be required and the function just returns an `Option<ScoreSummary>`

Originally, I was thinking it would be nicer to write something like this:

```rust
pub fn summarize_scores(scores: &[u32]) -> Option<ScoreSummary> {
    let (&first, rest) = scores.split_first()?;

    let summary = rest
        .iter()
        .copied()
        .fold(ScoreSummaryBuilder::new(first), ScoreSummaryBuilder::merge);

    Some(ScoreSummary {
        min: summary.min,
        max: summary.max,
        average: summary.sum as f64 / scores.len() as f64,
    })
}

#[derive(Copy, Clone)]
struct ScoreSummaryBuilder {
    min: u32,
    max: u32,
    sum: u32,
}

impl ScoreSummaryBuilder {
    fn new(value: u32) -> Self {
        Self {
            min: value,
            max: value,
            sum: value,
        }
    }

    fn merge(self, value: u32) -> Self {
        Self {
            min: self.min.min(value),
            max: self.max.max(value),
            sum: self.sum + value,
        }
    }
}

pub struct ScoreSummary {
    pub min: u32,
    pub max: u32,
    pub average: f64,
}
```

But then I thought about it a bit more and realised I was writing a bunch of code to shoe-horn some fancy functional programming concepts in when it's cleaner to just write the loop.

```rust
pub fn summarize_scores(scores: &[u32]) -> Option<ScoreSummary> {
    let (&first, rest) = scores.split_first()?;

    let mut min = first;
    let mut max = first;
    let mut sum = first as u64;

    for score in rest.iter().copied() {
        min = min.min(score);
        max = max.max(score);
        sum += score as u64;
    }

    Some(ScoreSummary {
        min,
        max,
        average: sum as f64 / scores.len() as f64,
    })
}
```

---

```go
package inventory

func Reconcile(stock map[string]int, deliveries map[string]int, returns map[string]int) map[string]int {
	result := stock

	for sku, qty := range deliveries {
		if _, ok := result[sku]; ok {
			result[sku] = result[sku] + qty
		} else {
			result[sku] = qty
		}
	}

	for sku, qty := range returns {
		if _, ok := result[sku]; ok {
			result[sku] = result[sku] + qty
		} else {
			result[sku] = qty
		}
	}

	for sku, qty := range result {
		if qty < 0 {
			result[sku] = 0
		}
	}

	return result
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): medium
- Evidence:
  - I'm actually not sure what this code is doing. It'd be so much more readable if it was written in terms of set operations or some other higher-level abstraction.

---

```python
def format_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    for raw in lines:
        value = raw.strip()
        if not value:
            continue
        normalized = value.lower().replace(" ", "_")
        out.append(normalized)
    return out
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - This is pretty reasonable.
  - You could probably use a small `normalizee_line()` helper with a list comprehension, but it's not a big deal.

---

```ts
type LedgerEntry = { id: string; amountCents: number };

export function buildLedger(entries: LedgerEntry[]): {
  ids: string[];
  totalCents: number;
  hasNegative: boolean;
} {
  let ids: string[] = [];
  let totalCents = 0;
  let hasNegative = false;

  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    ids.push(entry.id);
    totalCents = totalCents + entry.amountCents;
    if (entry.amountCents < 0) {
      hasNegative = true;
    }
  }

  ids = ids.sort();

  return { ids, totalCents, hasNegative };
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - This seems like a pretty good place to use mutations. Forcing functional programming onto the code would probably make it more bloated with marginal benefits.
