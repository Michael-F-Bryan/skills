# Labelling Sample: Dimension 4 - Error Semantics Explicitness

Dimension reminder: how explicit, typed, and context-rich error handling is versus opaque, generic, or implicit failure paths.

---

```rust
#[derive(Debug)]
pub enum LoadUserError {
    EmptyUserId,
    NotFound(String),
    Db(String),
}

pub fn load_user_name(user_id: &str, db: &dyn UserStore) -> Result<String, LoadUserError> {
    let id = user_id.trim();
    if id.is_empty() {
        return Err(LoadUserError::EmptyUserId);
    }

    let user = db
        .fetch_user(id)
        .map_err(|e| LoadUserError::Db(format!("fetch_user failed for id={id}: {e}")))?;

    match user {
        Some(u) => Ok(u.name),
        None => Err(LoadUserError::NotFound(id.to_string())),
    }
}

pub struct UserRecord {
    pub name: String,
}

pub trait UserStore {
    fn fetch_user(&self, user_id: &str) -> Result<Option<UserRecord>, String>;
}
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence:
  - This is pretty close to what I'd normally write - There are only really two differences
  - The `fetch_user()` method should be returning a proper error type, instead of just a `String`
  - The only difference is that the `LoadUserError::Db` variant would probably be written as `Db { user_id: String, error: DatabaseError }` so we capture both the original cause of the error (our hypothetical `DatabaseError`), plus the user ID that caused it.

---

```go
package uploads

import "errors"

func SaveAvatar(userID string, image []byte) error {
	if userID == "" {
		return errors.New("bad input")
	}
	if len(image) == 0 {
		return errors.New("bad input")
	}

	err := writeFile("/tmp/avatar-"+userID+".png", image)
	if err != nil {
		return errors.New("failed")
	}
	return nil
}

func writeFile(path string, data []byte) error {
	// imagine real implementation
	return nil
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - The errors aren't really actionable and wouldn't help a caller to debug the issue
  - We should be saying what is bad about the input (i.e. "empty user ID" or "empty image"), and the file writing error should wrap the original error with a more descriptive message (i.e. `fmt.Errorf("failed to write file %q: %w", path, err)`).

---

```python
import json
from pathlib import Path


def load_profile(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"profile file does not exist: {path}")
    if not p.is_file():
        raise ValueError(f"profile path is not a file: {path}")

    raw = p.read_text(encoding="utf-8")
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"profile JSON is invalid at {path}: {exc}") from exc

    if not isinstance(payload, dict):
        raise TypeError(f"profile root must be an object, got {type(payload).__name__}")

    return payload
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - There's no point doing all the `p.exists()` and `p.is_file()` checks because `read_text()` will rais the exceptions anyway, plus it opens us up to TOCTOU bugs
  - I'd just let the `json.JSONDecodeError` bubble up - it's useful enough already
  - The `isinstance(payload, dict)` is good, although in a real codebase I'd want to use pydantic to deserialise into a properly typed `Profile` model

---

```ts
export async function fetchWidget(widgetId: string): Promise<any> {
  try {
    const res = await fetch(`https://api.example.com/widgets/${widgetId}`);
    if (!res.ok) {
      throw "request failed";
    }
    return await res.json();
  } catch {
    throw "error";
  }
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - The try-catch is pretty much redundant because we're not actually "handling" the error. In fact, it's harmful because it throws away error details that could be useful for debugging.
  - The `if (!res.ok) { throw }` is a good idea, but we should be throwing a proper error type instead of a string
