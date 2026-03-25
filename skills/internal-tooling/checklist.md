# Internal Tooling Checklist

Use this checklist before claiming an internal tooling change is complete.

## Implementation

- Command is added under existing monolithic CLI (`uv run <agent-name> ...`).
- Command name is intent-driven and discoverable.
- Handler is thin (parse, wire, invoke, surface result).
- Business logic is in domain modules, not in click handlers.
- Shared concerns use typed options/decorators where semantics are repeated.
- Dependencies are injected at boundary; no hidden globals/singletons.

## Boundaries

- No env reads in domain/infra modules.
- Env parsing/loading is only in `__main__.py`, CLI wiring, or option helper layer.
- No reusable operational workflow is implemented as `scripts/*.py`.

## Verification

- Domain behavior tests added/updated.
- CLI wiring tests added/updated.
- Help discoverability checked:
  - `uv run <agent-name> --help`
  - `uv run <agent-name> <command> --help`
- Project-standard quality checks run (lint/type/tests) when required by host repo.

## Operations and Maintenance

- Logging outputs metadata, not sensitive payloads.
- Failure messages are explicit and actionable.
- If changes are breaking, deprecation/migration note is included.
- Documentation/runbook snippet is updated when this command is for shared use.
