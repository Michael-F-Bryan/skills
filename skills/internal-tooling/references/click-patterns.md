# Click Patterns

This file captures recommended patterns for building CLI commands with Click.

The aim is not “more abstraction”.
The aim is **clear command handlers, explicit dependency wiring, and domain logic that survives outside the terminal**.

## Core Rule

Keep the command thin.

A Click command should mostly:

1. parse arguments and options
2. construct dependencies
3. call domain code
4. render output
5. choose an exit code

If the command contains most of the real logic, the boundary is in the wrong place.

## Composition Root

Prefer one clear place where the CLI app is assembled.

Typical responsibilities:

- registering command groups
- wiring shared options
- centralising common behaviour
- top-level exception handling
- common output mode handling where appropriate

This reduces drift across commands.

## Shared Options

Use shared decorators or helpers for options that truly recur across commands.

Good candidates:

- authentication options
- API endpoint options
- timeout / retry controls
- output mode options such as `--json`
- safety flags such as `--dry-run`

Example:

```python
import click

def api_options(fn):
    fn = click.option("--base-url", required=True)(fn)
    fn = click.option("--token", required=True, envvar="API_TOKEN")(fn)
    return fn
```

Use this to reduce duplication, not to hide behaviour.

If callers cannot tell where an option came from or what it does, the abstraction has gone too far.

## Domain Delegation

Prefer this shape:

```python
@click.command()
@click.option("--user-id", required=True)
@api_options
def deactivate_user(user_id: str, base_url: str, token: str) -> None:
    client = ApiClient(base_url=base_url, token=token)
    result = users.deactivate(client=client, user_id=user_id)
    render_result(result)
```

Avoid this shape:

```python
@click.command()
@click.option("--user-id", required=True)
def deactivate_user(user_id: str) -> None:
    token = os.environ["API_TOKEN"]
    client = ApiClient(os.environ["BASE_URL"], token)
    response = client.post(...)
    if response.status_code == 200:
        ...
```

The first version makes the seam obvious.
The second version traps behaviour inside the command.

## Config Handling

Read config at the boundary.

Allowed:

- Click options
- envvar-backed Click options
- explicit config-loading helpers called by the command layer

Avoid:

- `os.environ[...]` inside domain code
- config reads buried in helpers
- module import side effects that load config

A command should be able to construct its dependencies explicitly and pass them in.

## Output Patterns

Decide whether a command is for humans, automation, or both.

### Human-oriented output

Use plain, readable terminal output for interactive use.

Example:

```python
click.echo(f"Deactivated {result.count} users")
```

### Machine-oriented output

When a command is likely to be scripted, add a stable `--json` mode.

Example:

```python
@click.option("--json", "as_json", is_flag=True, help="Emit machine-readable JSON")
def report(as_json: bool) -> None:
    result = reports.generate()
    if as_json:
        click.echo(result.model_dump_json())
    else:
        click.echo(format_human_report(result))
```

### Logging discipline

Prefer:

- logs, warnings, and progress → `stderr`
- structured result data → `stdout`

This matters once commands start feeding other tools.

## Dry Run Pattern

Commands that mutate state should often support `--dry-run`.

Example:

```python
@click.command()
@click.option("--dry-run", is_flag=True, help="Show what would change without applying it")
def sync(dry_run: bool) -> None:
    plan = sync_domain.plan(...)
    if dry_run:
        click.echo(format_plan(plan))
        return

    result = sync_domain.apply(plan=plan, ...)
    click.echo(format_result(result))
```

A good dry run should reflect actual intent, not just print a vague message.

## Error Handling

Use exceptions and error types intentionally.

### Good practice

- wrap low-level failures with context
- raise domain-specific errors when callers need to branch
- present concise, actionable terminal errors
- choose non-zero exit codes on failure

Example:

```python
try:
    result = users.deactivate(client=client, user_id=user_id)
except UserNotFound as exc:
    raise click.ClickException(f"User {exc.user_id} was not found")
except ApiError as exc:
    raise click.ClickException(f"Failed to deactivate user: {exc}")
```

### Avoid

- swallowing errors
- printing raw tracebacks for expected failures
- returning magic booleans instead of meaningful failure states
- encoding all behaviour in Click exceptions instead of domain logic

## Adding Abstractions

Only add helpers once the seam is real.

Good reasons:

- three or more commands share the same option bundle
- repeated output logic is drifting
- dependency construction is duplicated and consistent
- common safety behaviour needs to be enforced

Bad reasons:

- the file feels too short
- the abstraction name sounds clever
- maybe another command will need it someday

## Testing Pattern

### Test command handlers for:

- argument parsing
- delegation to domain code
- output formatting
- exit code behaviour
- important help text

### Test domain code for:

- real behaviour
- edge cases
- invalid inputs
- failure modes
- retry or idempotency semantics where relevant

Do not force every behavioural test through the terminal.

## Recommended Shape For A Command

A well-structured command tends to look like this:

1. define options and arguments
2. validate CLI-specific constraints
3. create clients / repositories / adapters
4. call domain function
5. render result in human or JSON form
6. map errors to terminal-friendly messages

That is enough structure for most internal tooling without becoming heavy.

## Summary

Use Click as a thin transport layer.

- parse at the edge
- inject dependencies explicitly
- keep business logic out of handlers
- support stable output when automation needs it
- design mutation commands to be safe
- let abstractions emerge from repetition, not aspiration
