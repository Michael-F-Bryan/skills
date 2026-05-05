# Labeling Sample: Dimension 20 - Evolution Posture

Dimension reminder: bias toward stable contracts with explicit migration/deprecation strategy versus unmanaged breaking churn.

---

```rust
#[derive(Debug)]
pub struct UserV2 {
    pub id: String,
    pub email: String,
}

#[deprecated(note = "use UserV2")]
pub type User = UserV2;

pub fn parse_user_v2(raw: &str) -> Result<UserV2, String> {
    let parts: Vec<&str> = raw.split(',').collect();
    if parts.len() != 2 {
        return Err("expected format: id,email".to_string());
    }
    Ok(UserV2 { id: parts[0].to_string(), email: parts[1].to_string() })
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): high
- Evidence:
  - I normally don't worry about creating `xxxV2` types. Most of the stuff I work on is internal or doesn't have many users, so I'm happy to make a breaking change and bump semver if necessary

---

```go
package api

// Breaking change, no migration plan.
type UserResponse struct {
	UID   string `json:"uid"`
	Mail  string `json:"mail"`
	Flags []int  `json:"flags"`
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): low
- Evidence:
  - I've got no idea what this "breaking change" is, so I can't really say anything about it

---

```python
from dataclasses import dataclass
import warnings


@dataclass
class InvoiceV2:
    invoice_id: str
    total_cents: int


def parse_invoice(raw: dict) -> InvoiceV2:
    if "id" in raw and "invoice_id" not in raw:
        warnings.warn("`id` is deprecated; use `invoice_id`", DeprecationWarning, stacklevel=2)
        raw = {**raw, "invoice_id": raw["id"]}
    return InvoiceV2(invoice_id=raw["invoice_id"], total_cents=int(raw["total_cents"]))
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - It feels like backwards compatibility is important for this code, so I appreciate the deprecation warning and adapting the input to the new format
  - I probably wouldn't worry about something like this for internal code, though, unless there was an obvious business reason to support old invoices

---

```ts
// Changelog: none
// Migration guide: none

export type Task = {
  id: string;
  // renamed from `title` to `headline` with no compatibility layer
  headline: string;
};

export function createTask(input: { headline: string }): Task {
  return { id: crypto.randomUUID(), headline: input.headline };
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): high
- Evidence:
  - Renaming public APIs without a deprecation notice or adapter code is just opening your users up to a world of pain
