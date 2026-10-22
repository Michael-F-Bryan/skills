# Labelling Sample: Dimension 18 - Data Boundary and IO Isolation

Dimension reminder: separation of pure/domain logic from IO/persistence/transport concerns.

---

```rust
pub struct TaxRule {
    pub basis_points: u32,
}

pub fn compute_tax_cents(subtotal_cents: u64, rule: TaxRule) -> u64 {
    subtotal_cents * rule.basis_points as u64 / 10_000
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - I feel like there's something missing here because I don't see any IO. It looks fine.

---

```go
package checkout

import (
	"database/sql"
	"encoding/json"
	"net/http"
)

func HandleCheckout(w http.ResponseWriter, r *http.Request, db *sql.DB) {
	var req struct {
		UserID string `json:"user_id"`
		Amount int64  `json:"amount"`
	}
	_ = json.NewDecoder(r.Body).Decode(&req)
	final := req.Amount + req.Amount/10
	_, _ = db.Exec("insert into orders(user_id, total) values (?, ?)", req.UserID, final)
	_ = json.NewEncoder(w).Encode(map[string]any{"total": final})
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - Ignoring the lack of error handling, I'm probably going to write this for a simple, low-complexity CRUD endpoint
  - I like that the `req` struct is declared exactly where it is used
  - I'd want to break the code out if into proper functions and model types if it got any more complex than this, though

---

```python
class InvoiceCalculator:
    def __init__(self, tax_rate_percent: float) -> None:
        self.tax_rate_percent = tax_rate_percent

    def total_cents(self, subtotal_cents: int) -> int:
        return subtotal_cents + round(subtotal_cents * (self.tax_rate_percent / 100))
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - The `InvoiceCalculator` class doesn't add any value here - I'd just make a simple function that takes the subtotal and the tax rate and returns the total

---

```ts
import fs from "node:fs/promises";

export async function loadAndRankUsers(path: string): Promise<string[]> {
  const raw = await fs.readFile(path, "utf8");
  const users = JSON.parse(raw) as Array<{ id: string; score: number }>;
  users.sort((a, b) => b.score - a.score);
  return users.map((u) => u.id);
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I'm not a fan of how the function hides the IO inside its implementation.
  - The code for ranking users should be separate from the code for loading them
