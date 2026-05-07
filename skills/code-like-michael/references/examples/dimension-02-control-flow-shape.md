# Labelling Sample: Dimension 2 - Control Flow Shape

Dimension reminder: preference for straight-line control flow with guard clauses/early exits versus deep nesting and branch pyramids.

---

```rust
pub fn finalize_order(input: &OrderInput) -> Result<FinalizedOrder, OrderError> {
    if input.items.is_empty() {
        return Err(OrderError::NoItems);
    }
    if input.customer_id.trim().is_empty() {
        return Err(OrderError::MissingCustomer);
    }

    let total_cents = input
        .items
        .iter()
        .map(|item| item.unit_price_cents.saturating_mul(item.quantity as u64))
        .sum();

    if total_cents == 0 {
        return Err(OrderError::InvalidTotal);
    }

    Ok(FinalizedOrder {
        customer_id: input.customer_id.clone(),
        total_cents,
    })
}

pub struct OrderInput {
    pub customer_id: String,
    pub items: Vec<OrderItem>,
}

pub struct OrderItem {
    pub unit_price_cents: u64,
    pub quantity: u32,
}

pub struct FinalizedOrder {
    pub customer_id: String,
    pub total_cents: u64,
}

pub enum OrderError {
    NoItems,
    MissingCustomer,
    InvalidTotal,
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - That's pretty much my ideal control flow shape

---

```go
package pricing

func ComputeDiscount(priceCents int64, tier string, hasCoupon bool, couponCode string) int64 {
	var discount int64 = 0

	if priceCents > 0 {
		if tier == "gold" {
			discount = priceCents / 5
		} else {
			if tier == "silver" {
				discount = priceCents / 10
			} else {
				discount = 0
			}
		}

		if hasCoupon {
			if couponCode != "" {
				if couponCode == "SAVE20" {
					discount += priceCents / 5
				} else {
					if couponCode == "SAVE10" {
						discount += priceCents / 10
					} else {
						discount += 0
					}
				}
			}
		}
	}

	if discount > priceCents {
		discount = priceCents
	}

	return discount
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I've been traumatized by a "senior" developer that would write code that had a dozen levels of indentation and nested if-statements in the past, and this is giving me flashbacks
  - The nesting and computational complexity is just off the charts
  - Mutating the discount variable as you go means it's nigh on impossible to reason about what the final discount is
  - Using a stringly-typed `tier` also doesn't help
  - Why are there separate `hasCoupon` and `couponCode` arguments? If the coupon code is optional, we can just use the empty string to represent "no coupon"

---

```python
def normalize_email(raw: str) -> str:
    value = raw.strip()
    if not value:
        raise ValueError("email is required")
    if "@" not in value:
        raise ValueError("email must contain @")

    local, domain = value.split("@", 1)
    if not local:
        raise ValueError("email local part is empty")
    if "." not in domain:
        raise ValueError("email domain must contain dot")

    return f"{local.lower()}@{domain.lower()}"
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - Email parsing is hard - you should really be using a library like `email-validator` for this, or at least a regex
  - I guess the code itself is okay, though, if it was in a different context

---

```ts
type AccessContext = {
  isAuthenticated: boolean;
  role: "guest" | "member" | "admin";
  ownsResource: boolean;
  featureFlagEnabled: boolean;
};

export function canEditProject(ctx: AccessContext): boolean {
  if (ctx.isAuthenticated) {
    if (ctx.featureFlagEnabled) {
      if (ctx.role === "admin") {
        return true;
      } else {
        if (ctx.role === "member") {
          if (ctx.ownsResource) {
            return true;
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
    } else {
      return false;
    }
  } else {
    return false;
  }
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - Deep nesting is a big code smell - it's so much easier to reason about if you do early returns to get the "easy" conditions out of the way
  - This should also prefer a switch statement over if-else chains because they tend to be more readable
  - All the `return false`'s are just noise
  - The `if condition { return true } else { return false }` pattern is just a verbose way of saying `return condition`

Here is how I'd write it:

```ts
export function canEditProject(ctx: AccessContext): boolean {
 if (!ctx.isAuthenticated || !ctx.featureFlagEnabled) {
  return false;
 }

 switch (ctx.role) {
  case "admin":
   return true;
  case "member":
   return ctx.ownsResource;
  default:
   return false;
 }
```
