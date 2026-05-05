# Labeling Sample: Dimension 5 - Contract Strictness at Boundaries

Dimension reminder: how explicit and strict a file is about validating inputs/outputs and enforcing invariants at boundaries.

---

```rust
#[derive(Debug)]
pub enum ParseError {
    MissingField(&'static str),
    InvalidAge(String),
}

#[derive(Debug)]
pub struct UserInput {
    pub name: String,
    pub age: u8,
}

pub fn parse_user(name: &str, age_raw: &str) -> Result<UserInput, ParseError> {
    let trimmed = name.trim();
    if trimmed.is_empty() {
        return Err(ParseError::MissingField("name"));
    }

    let age_num: u8 = age_raw
        .trim()
        .parse()
        .map_err(|_| ParseError::InvalidAge(age_raw.to_string()))?;

    if age_num < 13 {
        return Err(ParseError::InvalidAge("must be >= 13".to_string()));
    }

    Ok(UserInput {
        name: trimmed.to_string(),
        age: age_num,
    })
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence: That's roughly how I would have written the code, however I would have structured the errors differently. For example, I would have made the `ParseError` enum more specific:

```rust
#[derive(Debug)]
pub enum ParseError {
    EmptyName,
    ParseAge(std::num::ParseIntError),
    Underage(u8),
}
```

---

```go
package billing

type Invoice struct {
	ID       string
	Amount   int64
	Currency string
}

func BuildInvoice(id string, amount int64, currency string) Invoice {
	// Trust caller to pass valid values.
	return Invoice{
		ID:       id,
		Amount:   amount,
		Currency: currency,
	}
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`):
- Evidence:
  - This abstraction doesn't really carry its own weight.
  - If we care about enforcing constraints like the amount being non-negative, then the invoice fields should be private and exposed via getters.
  - Similarly, we should have a better representation for currency than a string. I'd probably create a `Currency` enum for all supported currencies, or if we are getting really fancy I would create a `Currency` struct that has things like a currency code and a currency symbol, then use named constants for known currencies.

---

```python
from datetime import datetime
from typing import Any, Dict


def parse_event(payload: Dict[str, Any]) -> Dict[str, Any]:
    ts_raw = payload.get("timestamp")
    if not isinstance(ts_raw, str):
        raise ValueError("timestamp must be an ISO string")

    event_type = payload.get("type")
    if event_type not in {"click", "view", "purchase"}:
        raise ValueError("unsupported type")

    user_id = payload.get("user_id")
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive int")

    parsed_ts = datetime.fromisoformat(ts_raw)

    return {
        "timestamp": parsed_ts,
        "type": event_type,
        "user_id": user_id,
    }
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This is wrong on so many levels
  - First, it goes against the whole "parse, don't validate" mentality. There's nothing in the type system that tells you any validation was ever performed, so downstream code can't make any assumptions about it.
  - Second, there are implicit assumptions about which keys are in the input dictionary and their types, and same with the outputs. If you got the `Dict[str, Any]` later on down the track, the only way you could know how to use it is by reading the code again
  - Third... just use Pydantic. It's made for exactly this kind of thing, and having a declarative class with type hints makes the entire thing self-documenting.

---

```ts
type CreateTaskInput = {
  title?: string;
  priority?: "low" | "medium" | "high";
  dueDate?: string;
};

type Task = {
  title: string;
  priority: "low" | "medium" | "high";
  dueDate?: Date;
};

export function createTask(input: CreateTaskInput): Task {
  return {
    title: input.title || "untitled",
    priority: input.priority || "low",
    dueDate: input.dueDate ? new Date(input.dueDate) : undefined,
  };
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence:
  - I'm okay with this
  - Defaulting to `"untitled"` is a bit of a smell because a task without something saying what is required isn't really useful, so I'd normally make the `title` field required, but other than that it's pretty nice code
  - Depending on how much the priority is used by other code, you might also want to hoist that out into its own type definition.
