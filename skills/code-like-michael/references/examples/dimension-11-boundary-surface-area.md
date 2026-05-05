# Labeling Sample: Dimension 11 - Boundary Surface Area

Dimension reminder: preference for narrow, intentional interfaces/contracts versus broad exposed APIs and leaky internals.

---

```rust
pub mod billing {
    pub use crate::billing_impl::*;
}

pub mod billing_impl {
    pub struct Invoice {
        pub id: String,
        pub amount_cents: u64,
    }

    pub fn new_invoice(id: String, amount_cents: u64) -> Invoice {
        Invoice { id, amount_cents }
    }

    pub fn parse_currency(s: &str) -> String {
        s.trim().to_uppercase()
    }

    pub fn compute_tax(amount_cents: u64) -> u64 {
        amount_cents / 10
    }

    pub fn write_invoice_row(id: &str, amount_cents: u64, tax_cents: u64) {
        println!("{id},{amount_cents},{tax_cents}");
    }
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This code is terrible
  - First, if we are going to re-export the functions under a facade, why is `billing_impl` made public
  - Second, the separate module is useless - just put everything in the `billing` module
  - There is no reason to have a `new_invoice()` constructor when all of `Invoice`'s fields are public
  - Constructors should also be associated with the type they are constructing, so `new_invoice()` should be `Invoice::new()`
  - Using `u64` for money is also a bit of a smell. I'd probably introduce a `Money` type which is a newtype wrapper around `u64` and essentially acts as a fixed-point decimal with 2 decimal places.
  - The `write_invoice_row()` function is also terrible. The caller has no way to specify where the invoice is written (what if they wanted to write it to a socket or a file?), plus you need to pass in each of the `Invoice` fields separately, which violates encapsulation and makes the `Invoice` redundant
  - Parsing currency is also terrible. First, parsing usually implies that the text being parsed can be invalid, so I would have expected to see a `Result` return type here. I would also expect it to be parsed into a separate type - strings are kinda useless. I'd also expect to leverage the `std::str::FromStr` trait rather than having this as a free function. That helps discoverability because you can look at the API docs for your `Currency` type and see that it can be parsed from a string.

---

```go
package orders

type Store interface {
	InsertOrder(Order) error
}

type Order struct {
	id         string
	totalCents uint64
}

func NewOrder(id string, totalCents uint64) (Order, error) {
	if id == "" {
		return Order{}, ErrInvalidOrderID
	}
	if totalCents == 0 {
		return Order{}, ErrInvalidOrderTotal
	}
	return Order{id: id, totalCents: totalCents}, nil
}

func (o Order) ID() string { return o.id }

func Save(s Store, o Order) error {
	return s.InsertOrder(o)
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - I like that the `NewOrder()` function is validating its inputs and encapsulation enforces that people can't accidentally modify a `Order` that is already valid
  - Using known errors instead of `fmt.Errorf()` is also nice because it means the caller can handle the error specifically rather than having to handle all errors generically
  - I would probably give the `Store.InsertOrder()` method a `context.Context` argument so we get support for cancellation and timeouts
  - That `Save()` function is a waste of time - just call `s.InsertOrder()` directly

---

```python
from dataclasses import dataclass


@dataclass
class Session:
    user_id: int
    roles: list[str]
    expires_at_epoch: int


def is_expired(session: Session, now_epoch: int) -> bool:
    return now_epoch >= session.expires_at_epoch


def can_publish(session: Session) -> bool:
    return "publisher" in session.roles


def update_roles(session: Session, roles: list[str]) -> Session:
    return Session(user_id=session.user_id, roles=roles, expires_at_epoch=session.expires_at_epoch)
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - All of these functions should be methods on the `Session` type
  - The name `update_roles()` makes me think that we'll be mutating the `Session` object. I'd probably call it `Session.with_roles("first", "second", "third")` instead and create a new `Session` which merges the new roles into the existing ones
  - Having a `Session.can_publish()` method is kinda nice because it means the caller doesn't need to know the magic `"publisher"` string, although probably a better way to do it would be to make the roles an enum and then have a `Session.has_role(Role.PUBLISHER)` method

---

```ts
type Token = {
  readonly value: string;
  readonly issuedAtMs: number;
  readonly expiresAtMs: number;
};

export type TokenService = {
  issue(userId: string, nowMs: number): Token;
  verify(token: string, nowMs: number): "valid" | "expired" | "invalid";
};

export function createTokenService(secret: string): TokenService {
  function issue(userId: string, nowMs: number): Token {
    const value = `${userId}:${secret}:${nowMs}`;
    return { value, issuedAtMs: nowMs, expiresAtMs: nowMs + 3600_000 };
  }

  function verify(token: string, nowMs: number): "valid" | "expired" | "invalid" {
    const parts = token.split(":");
    if (parts.length !== 3) return "invalid";
    const issuedAt = Number(parts[2]);
    if (!Number.isFinite(issuedAt)) return "invalid";
    if (nowMs >= issuedAt + 3600_000) return "expired";
    return "valid";
  }

  return { issue, verify };
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): medium
- Evidence:
  - I like the `createTokenService()` abstraction which gives you a default `TokenService` implementation that does the right thing
  - I also like that we've introduced a `TokenService` interface, which means we can swap it out during testing
  - The `Token` type is pretty nice, too
  - I like that `verify()` gives us more than a binary "is valid" - it also tells us whether the token has expired
  - Accepting `nowMs` instead of hard-coding `Date.now()` is also a nice touch
