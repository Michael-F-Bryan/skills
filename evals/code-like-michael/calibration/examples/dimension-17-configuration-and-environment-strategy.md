# Labelling Sample: Dimension 17 - Configuration and Environment Strategy

Dimension reminder: how explicit, typed, centralised, and validated configuration handling is versus ad hoc environment/config reads spread across the codebase.

---

```rust
use std::env;

#[derive(Debug)]
pub struct AppConfig {
    pub database_url: String,
    pub port: u16,
    pub log_level: String,
}

pub fn load_config() -> Result<AppConfig, String> {
    let database_url = env::var("DATABASE_URL").map_err(|_| "DATABASE_URL missing".to_string())?;
    let port = env::var("PORT")
        .unwrap_or_else(|_| "8080".to_string())
        .parse::<u16>()
        .map_err(|_| "PORT must be a valid u16".to_string())?;
    let log_level = env::var("LOG_LEVEL").unwrap_or_else(|_| "info".to_string());

    Ok(AppConfig {
        database_url,
        port,
        log_level,
    })
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This is so bad
  - First, your app configuration should be done immediately after startup (i.e. `main()`)
  - Second, this code is loading environment variables, which are essentially global state, with no way of configuring them
  - It's also completely undocumented - the only way to know what the configuration keys are is to read the code
  - I almost missed that the `PORT` variable is optional and defaults to `8080` - it just got lost in the wall of parsing and mapping and unwrapping and `to_string()` calls.
  - Just use `clap`. It's so much less code, less error-prone, the environment variables are mentioned in your `--help` text, and you can infer everything you need from the types
  - The `LOG_LEVEL` variable is also a bit of a smell. Most of the Rust ecosystem has standardised around `$RUST_LOG`, so even if you aren't using Rust's `env_logger` or `tracing` libraries, by using a different environment name you are making this program a special snowflake that people need to know how to configure separately

---

```go
package api

import (
	"net/http"
	"os"
)

func HandleHealth(w http.ResponseWriter, r *http.Request) {
	region := os.Getenv("REGION")
	if region == "" {
		region = "unknown"
	}
	w.WriteHeader(http.StatusOK)
	_, _ = w.Write([]byte("ok:" + region))
}

func ConnectDB() string {
	// Read from env at call site.
	return os.Getenv("DATABASE_URL")
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I feel very strongly that application code should never read environment variables. Instead, it should be loaded into domain-specific types on startup and the dependency should be passed into the code that needs it
  - The `HandleHealth()` function should probably become a `func HandleHealth(region string) http.Handler` and close over the `region` value
  - Throwing the write error away is also a bit of a smell. At the very least, I'd want to log that error as a warning
  - The `ConnectDB()` function is doubly bad because it accesses environment variables at runtime, which is a big no-no, plus it is also poorly named because we don't even get a database handle out of it.

---

```python
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    redis_url: str
    port: int = Field(default=8000, ge=1, le=65535)
    debug: bool = False


def load_settings() -> AppSettings:
    try:
        return AppSettings()
    except ValidationError as exc:
        raise RuntimeError(f"invalid settings: {exc}") from exc
```

- Score (1-5): 4
- Confidence (`low|medium|high`): high
- Evidence:
  - I like that this explicitly defines a class with strong type hints for the configuration
  - I also like how it's quite obvious that we default to port 8000, and the value must be between 1 and 65535
  - The `SettingsConfigDict(env_file=".env")` is a nice touch - I didn't know you could do that with Pydantic
  - Overall, I'm pretty happy with how this app's settings are configured. I'd normally prefer all configuration to be visible with the `--help` text, but if this is the standard way to do configuration in this codebase then I'm happy to follow along with it.

---

```ts
// config.ts
export function getDatabaseUrl(): string {
  const url = process.env.DATABASE_URL;
  if (!url) throw new Error("DATABASE_URL missing");
  return url;
}

export function isDebugEnabled(): boolean {
  return process.env.DEBUG === "true";
}

// elsewhere in handlers and jobs:
// const region = process.env.REGION || "us-east-1";
// const timeoutMs = Number(process.env.TIMEOUT_MS || "5000");
```

- Score (1-5): 2
- Confidence (`low|medium|high`): high
- Evidence:
  - I'm not a fan of this - normal code outside the setup path shouldn't be touching environment variables. It becomes super hard to reason about what the environment variables are expected (e.g. when setting up infra), and the defaults are documented nowhere except the source code
  - It's okay to have a separate `config.ts` file, I would just expect it to have a single exported `loadConfig()` function that returns a typed configuration object so all the config is loaded in one place
