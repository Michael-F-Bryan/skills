# Project Structure for Internal Tooling

This guide defines the default layout for an agent-owned internal tooling project.

## Setup (Always `uv`)

Use `uv` for environment, dependency, and execution workflow.

Recommended commands:

```bash
uv sync
uv run <agent-name> --help
uv run pytest -q
```

Rules:

- Do not introduce alternate package managers unless explicitly required.
- Run tools through `uv run ...` to keep execution consistent.
- Keep dependencies minimal and task-driven.

## Default Repository Layout

```text
<repo>/
  pyproject.toml
  README.md
  <agent_name>/
    __init__.py
    __main__.py
    cli/
      __init__.py
      main.py
      options.py
      <domain_a>.py
      <domain_b>.py
    <domain_a>/
      __init__.py
      service.py
    <domain_b>/
      __init__.py
      service.py
    infra/
      __init__.py
      clients.py
      storage.py
    models/
      __init__.py
      options.py
      results.py
  tests/
    cli/
    domains/
    fixtures/
```

## Entrypoint Convention

Use `<repo>/<agent_name>/__main__.py` as the runtime entrypoint.

Responsibilities:

1. Walk up the filesystem tree from current working directory to root.
2. Load each `.env` file found during the walk.
3. Call `main()` from `<agent_name>.cli.main`.

Conceptual implementation:

```python
from pathlib import Path
from dotenv import load_dotenv

from myagent.cli.main import main as cli_main


def _load_env_files_recursively() -> None:
    current = Path.cwd().resolve()
    for directory in [current, *current.parents]:
        env_file = directory / ".env"
        if env_file.exists():
            load_dotenv(env_file, override=False)


def run() -> None:
    _load_env_files_recursively()
    cli_main()


def main() -> None:
    run()


if __name__ == "__main__":
    main()
```

## Script Entry in `pyproject.toml`

Expose the CLI via `<agent_name>.__main__:main`:

```toml
[project.scripts]
<agent-name> = "<agent_name>.__main__:main"
```

## What Goes Where

- `cli/`: click groups/commands, argument parsing, option decorators, boundary wiring.
- `<domain_*>/`: business logic and use-case flows grouped by domain.
- `infra/`: external integrations (APIs, DB, filesystem, queues).
- `models/`: typed contracts used at boundaries (options/result payloads).
- `tests/cli/`: command parsing/wiring behavior.
- `tests/domains/`: business rules and workflows.

Avoid:

- placing business logic in `cli/`
- raw environment reads outside `__main__.py`, CLI option wiring, or option helper layer
- `scripts/` for reusable operational tasks that should be CLI commands
  - see calibration example: [Example 1: Repeatable Backfill Task](examples.md#example-1-repeatable-backfill-task)

## CLI Organization

Use one monolithic executable surface:

- `uv run <agent-name> ...`

Pattern:

- `cli/main.py` defines top-level `click.group`.
- Each domain command module registers with the main group.
- Shared flags and option bundles live in `cli/options.py`.

Example command shape:

```text
uv run jake users sync
uv run jake reports unresolved-failures --since 7d
uv run jake db migrate
```

## Dependency and Config Boundaries

- Parse/load env only in `__main__.py`, CLI wiring, or option helper layer.
- Convert flags/env to typed option objects once at the boundary.
- Construct clients in CLI or dedicated wiring helpers.
- Pass concrete dependencies into domain functions explicitly.

This keeps domain code deterministic and testable.

Do not read env vars in domain/infra modules.

## How to Decide File Placement

Use this decision order:

1. Is this parsing/wiring/entrypoint? -> `cli/`
2. Is this domain behavior/rules? -> `<domain_*>/`
3. Is this third-party IO or side effects? -> `infra/`
4. Is this shared typed payload/option/result object? -> `models/`
5. Is this only test data/helpers? -> `tests/fixtures/`

If a file spans multiple categories, split it at the seam.

## Growth Rules

- Start compact, then split by responsibility as commands grow.
- Introduce shared abstractions only after repeated semantic sameness.
- Keep one obvious composition root per executable surface.
- Prefer additive subcommands over new executables.

## Testing and Verification

Minimum expectations for each new command:

1. Domain behavior test for business logic path.
2. CLI wiring test for option parsing/injection.
3. Help discoverability check:
   - `uv run <agent-name> --help`
   - `uv run <agent-name> <command> --help`

For substantial changes, also run repo-standard lint/type/test checks through `uv run`.

For implementation sequence and lifecycle usage, see [../workflow.md](../workflow.md).
For the completion gate, use [../checklist.md](../checklist.md).
