# Labeling Sample: Dimension 10 - Dependency Directionality Discipline

Dimension reminder: consistency of dependency flow (for example, core/domain inward and adapters outward) with minimal layering violations.

---

```rust
// src/domain/order.rs
pub struct Order {
    pub id: String,
    pub total_cents: u64,
}

pub trait OrderRepository {
    fn save(&self, order: &Order) -> Result<(), String>;
}

pub fn place_order(repo: &dyn OrderRepository, order: Order) -> Result<(), String> {
    if order.total_cents == 0 {
        return Err("order total must be > 0".to_string());
    }
    repo.save(&order)
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - It's hard to explain exactly why I would score this as a 2, but it just doesn't feel right.
  - For one, the `if order.total_cents == 0` check is redundant - it should have been validated when the `Order` was created
  - I probably also wouldn't use the repository pattern unless it was used in a bunch of places and the abstraction carried its own weight. I'd generally prefer to use the database connection directly, or maybe add a thin interface with one method per SQL query used in my codebase (kinda like what `sqlc` does in Go)

---

```go
// internal/domain/user.go
package domain

import (
	"database/sql"
	"fmt"
)

type User struct {
	ID    string
	Email string
}

func SaveUser(db *sql.DB, u User) error {
	if u.Email == "" {
		return fmt.Errorf("email required")
	}
	_, err := db.Exec("insert into users(id, email) values (?, ?)", u.ID, u.Email)
	return err
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - This is definitely what I'd do in Go
  - You'll usually want to validate fields like `if u.Email == ""` because it's common to use the zero value in Go, so an empty string could easily sneak in
  - `*sql.DB` is also a pretty nice abstraction and used all over the place in Go, so the code will be immediately obvious to most developers

---

```python
# app/services/payment_service.py
from app.domain.payment import Payment
from app.adapters.stripe_gateway import StripeGateway


class PaymentService:
    def __init__(self, gateway: StripeGateway) -> None:
        self.gateway = gateway

    def charge(self, payment: Payment) -> str:
        if payment.amount_cents <= 0:
            raise ValueError("amount must be positive")
        return self.gateway.charge(
            amount_cents=payment.amount_cents,
            currency=payment.currency,
            customer_id=payment.customer_id,
        )
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - Without any further context on the domain or expected interfaces, this feels like a useless abstraction. The `charge()` method doesn't really do anything valuable except forward to `self.gateway`
  - I remember watching a talk years ago where the speaker said something valuable - "If a class is just a constructor and one method, then it shouldn't be a class at all. It should be a function."


---

```ts
// src/domain/report.ts
import { fetch } from "undici";
import { readFileSync } from "node:fs";

export async function buildReport(reportId: string): Promise<string> {
  const template = readFileSync("./templates/report.md", "utf-8");
  const res = await fetch(`https://api.example.com/reports/${reportId}`);
  const data = await res.json();
  return template.replace("{{title}}", data.title);
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - I would normally separate the code that fetches the report data from the code that renders it. That way they can be tested independently, which is especially important when one of the functions is making a HTTP call to a hard-coded URL.
  - It also feels like you want to reach for a templating engine here

