# Labeling Sample: Dimension 9 - Module Cohesion

Dimension reminder: whether a module/file stays focused on one responsibility versus mixing unrelated concerns.

---

```rust
pub struct PasswordHasher;

impl PasswordHasher {
    pub fn hash(password: &str) -> String {
        format!("hashed:{password}")
    }

    pub fn verify(password: &str, hash: &str) -> bool {
        Self::hash(password) == hash
    }
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - I get what this is trying to do, but it's not really the best way to design it.
  - In Rust, I generally don't like adding associated functions to a type unless they are some sort of constructor or factory function. Things like that should just be added as private free functions
  - Here is a better implementation:

```rust
struct HashedPassword([u8; 32]);

impl HashedPassword {
    pub fn new(password: &str) -> Self {
        Self(my_hashing_function(password))
    }

    pub fn verify(self, password: &str) -> bool {
        my_hashing_function(password) == self.0
    }
}

impl Display for HashedPassword { ... }

fn my_hashing_function(password: &str) -> [u8; 32] { ... }
```

---

```go
package util

import "fmt"

func HashPassword(p string) string { return "h:" + p }
func SendEmail(to string, body string) { fmt.Println("email", to, body) }
func ParseCSV(raw string) []string { return []string{raw} }
func ResizeImage(path string) error { return nil }
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I hate `util` packages - it's just screaming that you don't know where something belongs so you threw it all into a big bucket.
  - These really belong in their own domain-specific packages, or if it's only a single function, maybe that function should stay as a private function in the file that uses it

---

```python
class JobScheduler:
    def __init__(self, queue_client):
        self.queue = queue_client

    def enqueue(self, name: str, payload: dict) -> None:
        self.queue.push({"name": name, "payload": payload})

    def cancel(self, job_id: str) -> None:
        self.queue.cancel(job_id)
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence:
  - Ignoring the fact that the `JobScheduler` class is doing nothing other than delegating to the `queue_client`, the class's API is actually pretty cohesive and clear

---

```ts
export function parseJwt(token: string): object {
  return JSON.parse(Buffer.from(token.split(".")[1], "base64").toString("utf8"));
}

export function renderWelcomeEmail(name: string): string {
  return `<h1>Welcome ${name}</h1>`;
}

export function connectPg(url: string): Promise<void> {
  console.log("connect", url);
  return Promise.resolve();
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This is just a grab bag of unrelated functions
