# Click Patterns for Internal Tooling

These patterns keep the CLI maintainable and aligned with a modular-monolith style.

## 1) Single Composition Root

- Keep one CLI entrypoint (`main` group).
- Register subcommands from focused modules.
- Apply global concerns (logging level, telemetry toggles) at the root.

## 2) Shared Option Decorators

When options repeat across commands, create typed bundles and decorators.

```python
from dataclasses import dataclass
import click

@dataclass(frozen=True)
class ApiOptions:
    base_url: str
    token: str

    def client(self) -> ApiClient:
        ...

def api_options(func):
    @click.option("--api-base-url", required=True, type=str)
    @click.option("--api-token", required=True, type=str)
    @click.pass_context
    def wrapper(ctx, base_url: str, token: str, *args, **kwargs):
        options = ApiOptions(base_url=base_url, token=token)
        return ctx.invoke(func, *args, api_options=options, **kwargs)
    return wrapper
```

## 3) Thin Command, Rich Domain Module

Command handlers should orchestrate only:

1. parse options
2. construct dependencies
3. call library function
4. surface user-facing result/errors

Put business logic in domain modules under `<agent_name>/`:

```python
# cli/sync.py
@click.command("sync-users")
@api_options
def sync_users(api_options: ApiOptions):
    run_user_sync(
        base_url=api_options.base_url,
        token=api_options.token,
    )
```

```python
# users/sync.py
def run_user_sync(*, base_url: str, token: str) -> None:
    # business logic and orchestration live here
    ...
```

## 4) Dependency Injection Boundary

- Construct clients in CLI wiring and pass them inward.
- Avoid hidden singleton clients or implicit global setup.
- Avoid reading env vars in domain or infra modules.
- `__main__.py` may load `.env` before calling the CLI entrypoint; domain/infra modules still must not read env directly.

## 5) Error and Logging Discipline

- Fail with actionable, user-readable messages.
- Log metadata (counts, IDs, durations), not sensitive payloads.
- Keep command output stable enough for machine parsing when needed.

## 6) When to Add New Abstractions

Add a new helper/decorator only when:

- two or more commands share identical semantics, or
- a cross-cutting concern is clearly stable.

Otherwise, keep duplication local until the seam is real.

## 7) Testing Strategy

- Behavior tests for domain logic modules.
- Focused CLI wiring tests for argument parsing/injection.
- Avoid tests that only assert trivial framework plumbing.

See [../checklist.md](../checklist.md) for completion checks and verification gates.
