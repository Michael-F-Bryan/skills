# Labelling Sample: Dimension 7 - Local Abstraction Threshold

Dimension reminder: tendency to extract helpers deliberately versus keeping too much logic inline (or over-extracting prematurely).

---

```rust
pub fn render_account_badge(first: &str, last: &str, plan: &str, is_active: bool) -> String {
    let display_name = format!("{} {}", capitalise(first), capitalise(last));
    let plan_label = plan.trim().to_uppercase();
    let status_label = if is_active { "ACTIVE" } else { "PAUSED" };
    format!("{display_name} [{plan_label}] {status_label}")
}

fn capitalise(input: &str) -> String {
    let mut chars = input.chars();
    match chars.next() {
        Some(first) => first.to_uppercase().collect::<String>() + chars.as_str(),
        None => String::new(),
    }
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - I feel like this is a good threshold for extracting the `capitalise()` helper

---

```go
package alerts

import "strings"

func Build(msg string, level string, team string, region string, ts string, id string) string {
	msg = strings.TrimSpace(msg)
	level = strings.ToUpper(strings.TrimSpace(level))
	team = strings.ToLower(strings.TrimSpace(team))
	region = strings.ToLower(strings.TrimSpace(region))
	if msg == "" {
		msg = "unknown"
	}
	return "[" + level + "] " + team + "/" + region + " " + ts + " #" + id + " " + msg
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): high
- Evidence:
  - The duplicated `strings.ToUpper()` and `strings.TrimSpace()` is just infuriating. I'd probably write it as...

```go
trim := strings.TrimSpace
upper := func(s string) string { return strings.ToUpper(trim(s)) }
lower := func(s string) string { return strings.ToLower(trim(s)) }
return fmt.Sprintf(
  "[%s] %s/%s %s #%s %s",
  upper(level),
  lower(team),
  lower(region),
  ts,
  id,
  trim(msg),
  )
```

---

```python
def serialize_user(user: dict) -> dict:
    return {
        "id": str(user["id"]).strip(),
        "email": str(user["email"]).strip().lower(),
        "name": str(user["name"]).strip(),
        "is_active": bool(user.get("is_active", True)),
    }
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - This is on the verge of getting too long for me. If it were any more complex, I'd probably extract a helper.lex,

---

```ts
function normalise(input: string): string {
  return input.trim().toLowerCase();
}

function buildKey(namespace: string, id: string): string {
  return `${normalise(namespace)}:${normalise(id)}`;
}

export function upsertCacheRecord(namespace: string, id: string, value: string): { key: string; value: string } {
  return { key: buildKey(namespace, id), value: value.trim() };
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - It really depends. If I came across this in the wild I'd probably just leave it be, but if I was writing it myself I'd probably drop the `buildKey()` helper
