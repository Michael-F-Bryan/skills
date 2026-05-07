# Examples

These examples show how to apply the internal-tooling guidance in practice.

They are intentionally concrete.
The goal is to make the desired judgement calls easy to imitate.

## Example 1: Repeated Backfill Task → Build A CLI Command

### Scenario

You need to backfill missing metadata for records in a remote system.

The task:

- queries many records
- filters them by conditions
- updates external state
- needs retries
- will probably be run again
- benefits from a dry run and a stable interface

### Bad approach

Create an ad hoc script in `scripts/fix_stuff.py` that:

- reads env vars internally
- contains query logic, retry logic, and mutation logic in one file
- has no dry-run mode
- is not wired into the repo’s main CLI
- is copied around when someone needs it again

### Better approach

Add a named command such as:

```bash
tool records backfill-metadata --source legacy --limit 500 --dry-run
tool records backfill-metadata --source legacy --limit 500 --yes
```

### Why this should be a command

Because the task:

- mutates external state
- has enough complexity that correctness matters
- benefits from validation and safety controls
- is likely to be reused
- is worth documenting and testing

### Good structure

```text
your_package/
├── cli/commands/backfill.py
├── domain/backfill.py
└── infra/api_client.py
```

The command handler:

- parses options
- constructs the client
- calls `domain.backfill_metadata(...)`
- renders a plan or result

The domain code:

- computes what needs to change
- applies the changes
- handles retries or per-record failure policies
- returns structured results

## Example 2: One-Off Read-Only Investigation → Keep It One-Off

### Scenario

You are investigating an incident and want to know how many rows in a local database match a condition.

This is:

- read-only
- local to the investigation
- unlikely to be reused
- not worth adding help text or tests for

### Good approach

Run the SQL query directly, or put it in a short temporary notebook or shell snippet.

Example:

```bash
psql "$DATABASE_URL" -c "
  select count(*)
  from jobs
  where status = 'stalled'
"
```

### Why this should stay one-off

Because it is:

- read-only
- low-risk
- ephemeral
- faster to inspect than to formalise

Do **not** create a permanent CLI command just because a command is possible.

## Example 3: Temporary Exploration That Graduates Into Tooling

### Scenario

You are exploring a third-party API to understand its pagination model.

At first, this is discovery work.

### Good first step

Use a shell command or scratch script:

```bash
curl -H "Authorisation: Bearer $TOKEN" \
  "https://api.example.com/v1/items?page=1"
```

### When to promote it

Promote it into a CLI command once the task starts to include:

- pagination
- filtering
- stable output requirements
- repeated use
- retries
- sharing with others

### Example promoted command

```bash
tool items list --status active --page-size 100 --json
```

### Lesson

Exploration is not a failure.
Premature formalisation is also not a virtue.

Start light, then formalise once the seam is real.

## Example 4: Hidden Env Reads → Bad

### Bad code

```python
def sync_users() -> None:
    token = os.environ["API_TOKEN"]
    base_url = os.environ["API_BASE_URL"]
    client = ApiClient(base_url=base_url, token=token)
    ...
```

### Why this is bad

The function:

- cannot be reused cleanly
- is awkward to test
- hides its dependencies
- ties domain behaviour to process state

### Better code

```python
def sync_users(client: ApiClient) -> SyncResult:
    ...
```

And in the CLI layer:

```python
@click.command()
@click.option("--base-url", required=True)
@click.option("--token", required=True, envvar="API_TOKEN")
def sync(base_url: str, token: str) -> None:
    client = ApiClient(base_url=base_url, token=token)
    result = sync_users(client)
    render_result(result)
```

### Lesson

Read config at the boundary.
Pass dependencies inward.

## Example 5: Reporting Command With Stable Output

### Scenario

A support workflow needs a report that people will read interactively, but automation may also consume it later.

### Good command design

```bash
tool report stale-jobs
tool report stale-jobs --json
```

### Why this is good

Because the command has:

- a clear name
- stable arguments
- an obvious human mode
- an obvious machine mode
- a reusable interface for future workflows

### Implementation shape

The command handler should:

- parse CLI flags
- call the report generator
- emit formatted text or JSON

The report logic should:

- query the required sources
- compute the results
- return structured data

The formatting layer should decide how to present that data.

## Example 6: Destructive Operation With Safety Controls

### Scenario

You need to deactivate a set of users in an external system.

This is risky because it mutates shared external state.

### Bad approach

```bash
python scripts/deactivate_users.py users.csv
```

No dry run. No confirmation. No stable interface. No clear behaviour contract.

### Better approach

```bash
tool users deactivate --input users.csv --dry-run
tool users deactivate --input users.csv --yes
```

### Why this is better

Because the command makes it clear:

- what the operation is
- what data it acts on
- how to preview changes
- how to explicitly approve execution

### Expected behaviour

- `--dry-run` prints what would happen and exits successfully without mutation
- `--yes` is required for actual execution
- logs and warnings go to `stderr`
- machine-readable results should be available if automation is likely

## Example 7: Command That Should Stay A Library Function

### Scenario

You need a reusable parser or transformation function that multiple commands might call.

Example: parse a vendor-specific export file into a normalised internal representation.

### Good approach

Create a library or domain function:

```python
def parse_vendor_export(src: str) -> ParsedExport:
    ...
```

Then let commands call it as needed.

### Why this should not automatically become a command

Because not every reusable function needs terminal surface area.

A function should become a command only when there is a meaningful operational task to expose.

### Lesson

“Reusable” and “user-facing CLI” are not the same thing.

## Summary

Use these examples to keep the judgement call straight:

- repeated, risky, shared, stateful work → usually a CLI command
- ad hoc, read-only, local investigation → usually one-off
- discovery can start light and grow into tooling
- config belongs at the boundary
- library functions do not need to become commands unless there is a real operational interface to expose
