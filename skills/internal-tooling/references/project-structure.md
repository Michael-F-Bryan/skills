# Project Structure

This file describes the recommended shape for internal tooling built as part of the repo’s CLI.

Treat this as a **default starting point**, not a rigid filesystem law.
Start compact. Split things by responsibility once the seams are real.

## Goals

We want internal tooling that is:

- easy to discover
- easy to review
- easy to test
- safe to evolve
- explicit about dependencies
- not polluted by hidden config reads or global state

## Baseline Layout

A typical Python internal tooling package might look like this:

```text
your_package/
├── __main__.py
├── cli/
│   ├── __init__.py
│   ├── app.py
│   ├── common_options.py
│   └── commands/
│       ├── __init__.py
│       ├── sync.py
│       ├── report.py
│       └── backfill.py
├── domain/
│   ├── __init__.py
│   ├── sync.py
│   ├── report.py
│   └── backfill.py
├── infra/
│   ├── __init__.py
│   ├── api_client.py
│   ├── db.py
│   └── filesystem.py
├── models/
│   ├── __init__.py
│   └── types.py
└── tests/
    ├── cli/
    ├── domain/
    └── infra/
```

Not every tool needs every directory.

For a smaller tool, this flatter structure is perfectly acceptable:

```text
your_package/
├── __main__.py
├── cli.py
├── sync.py
├── report.py
├── api_client.py
└── tests/
```

Prefer the smaller version until the codebase gives you a real reason to split.

## Responsibilities

### `__main__.py`

Use this as the composition root for local execution.

Good places for:

- process startup
- loading environment variables from `.env` files
- invoking the CLI app
- top-level exception handling
- minimal bootstrapping

Avoid putting real business logic here.

### `cli/`

This layer defines the command-line interface.

Good places for:

- command names
- options and arguments
- help text
- user-facing validation that is specific to CLI usage
- wiring dependencies together
- translating domain results into terminal output

Avoid putting business rules here.

A command handler should mostly do three things:

1. parse CLI input
2. construct dependencies
3. call domain code

### `cli/common_options.py`

Use this for shared Click/Typer option bundles when the reuse is real.

Examples:

- `--base-url`
- `--token`
- `--timeout`
- `--json`
- `--dry-run`

Do not create abstraction soup for one or two commands.
Shared options should exist because they reduce duplication and keep behaviour consistent.

### `cli/commands/`

Use one module per command or per tightly related command group.

This keeps command handlers easy to scan and helps avoid a single giant CLI file.

### `domain/`

This layer contains the actual behaviour.

Good places for:

- orchestration logic
- validation that is independent of the terminal
- transformation logic
- policy decisions
- idempotency behaviour
- domain-specific error types

This is where the code should remain useful even if the CLI disappeared and a REST API or worker process called into the same logic.

### `infra/`

This layer contains adapters to external systems.

Examples:

- API clients
- database access
- file storage access
- queue producers
- clock abstractions
- wrappers around third-party libraries

Keep this boring and explicit.
The job of `infra/` is not to be clever. The job is to isolate side effects.

### `models/`

Only introduce this when shared types genuinely exist.

Examples:

- request/response objects
- value objects
- typed identifiers
- enums
- validated configuration objects

Do not create a `models/` package just because it feels proper.

## Config and Environment Rules

### Allowed places to read environment variables

Environment and process configuration should only be read at the boundary, such as:

- `__main__.py`
- CLI option defaults
- explicit configuration-loading helpers used by the CLI layer

### Disallowed places to read environment variables

Do not read environment variables inside:

- domain modules
- reusable library code
- random helper functions
- deep infra functions called by unrelated contexts

Hidden config reads make code harder to test, harder to reuse, and harder to reason about.

Pass config in explicitly.

## Dependency Passing

Dependencies should be created at the edge and passed inward.

Good:

```python
@click.command()
@click.option("--base-url", required=True)
@click.option("--token", required=True)
def sync(base_url: str, token: str) -> None:
    client = ApiClient(base_url=base_url, token=token)
    result = domain.sync_everything(client)
    render_result(result)
```

Bad:

```python
def sync_everything() -> None:
    token = os.environ["API_TOKEN"]
    client = ApiClient(base_url=os.environ["BASE_URL"], token=token)
    ...
```

Prefer explicit parameters over hidden process state.

## Output Design

For each command, decide whether the output is:

- human-readable
- machine-readable
- both

### Recommended conventions

- Human-oriented logs and progress go to `stderr`
- Structured data goes to `stdout`
- Add a stable `--json` mode when automation is likely
- Do not mix logs into JSON output
- Make exit codes meaningful

### Example exit code expectations

- `0` → success
- non-zero → failure
- distinguish usage errors from operational failures when practical

The exact scheme can vary, but callers should not have to guess.

## Destructive Command Safety

Commands that mutate or delete should usually support one or more of:

- `--dry-run`
- explicit confirmation flags such as `--yes`
- scoped filters that reduce blast radius
- clear summaries of intended actions before execution

If a command is risky to rerun or hard to reverse, design for caution.

## Testing Strategy

### CLI tests

Test:

- argument parsing
- help text for important commands
- wiring and delegation
- output formatting
- exit codes

Do not make CLI tests carry the whole burden of behavioural verification.

### Domain tests

Test:

- happy path behaviour
- edge cases
- invalid inputs
- failure modes
- idempotency and retry semantics where relevant

This is where most meaningful tests should live.

### Infra tests

Test:

- serialisation and deserialisation
- boundary conditions
- integration with external contracts where feasible
- adapter behaviour, not vendor internals

## Growth Rules

Start with the smallest structure that remains clear.

Split modules when:

- files are becoming hard to scan
- concepts are mixing
- unrelated responsibilities are cohabiting
- tests are awkward because concerns are tangled

Do not split solely because “proper architecture” says you should.

## Command Surface Hygiene

Every new command increases the maintenance burden.

Before adding a command, ask:

- Is this distinct enough from existing commands?
- Could this be a subcommand or mode of an existing command?
- Does it have a clear owner and purpose?
- Will somebody understand why it exists six months from now?

Prefer a coherent CLI over a junk drawer of unrelated verbs.

## Example Mapping

### Good fit for this structure

- `tool report generate`
- `tool records backfill`
- `tool files sync`
- `tool users deactivate`

### Probably not worth formalising yet

- a one-off SQL investigation
- a temporary local file inspection
- a short exploratory API call during discovery

## Summary

Use this structure to keep the repo’s operational tooling:

- explicit
- testable
- composable
- stable at the edges
- simple in the middle

Structure is here to support clarity, not ceremony.
