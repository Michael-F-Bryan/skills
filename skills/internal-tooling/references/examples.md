# Prompted Examples (Bad vs Good)

These examples are intended to shape behavior, not just syntax.
Primary decisioning source: [decision-gate.md](decision-gate.md).
Primary implementation workflow: [../workflow.md](../workflow.md).

---

## Example 1: Repeatable Backfill Task

### Prompt

> We need to backfill missing claim statuses for the last 60 days. I will probably run this a few times while validating.

### Bad Example

```python
# scripts/backfill_claim_status.py
import os
import requests

token = os.getenv("API_TOKEN")
base = os.getenv("API_BASE_URL")

for claim_id in open("claim_ids.txt").read().splitlines():
    requests.post(f"{base}/claims/{claim_id}/backfill", headers={"Authorization": token})
```

### Why It's Bad

- Commits reusable automation as a throwaway script.
- Reads env vars directly in script logic.
- No CLI help surface, no standard options, no guardrails.
- No typed options or dependency injection.

### Good Example

```text
Agent plan:
1) Add `uv run jake claims backfill-status` command.
2) Add shared `@api_options` decorator used across claims commands.
3) Put backfill flow in `jake/claims/backfill.py`.
4) Add tests for date-range behavior and dry-run mode.

Tool calls (abbreviated):
- Edit `jake/cli/options.py` (add `ApiOptions`, `api_options` decorator)
- Edit `jake/cli/claims.py` (new `backfill-status` command)
- Add `jake/claims/backfill.py`
- Add tests in `tests/claims/test_backfill.py`
```

### Why It's Good

- Productizes repeatable work in discoverable CLI.
- Reuses shared options and setup.
- Keeps command thin and business logic in library.
- Supports reliable reruns and ongoing maintenance.
- Related: [Click Patterns - Shared Option Decorators](click-patterns.md#2-shared-option-decorators), [Project Structure - What Goes Where](project-structure.md#what-goes-where)

---

## Example 2: One-Off Read-Only Inspection

### Prompt

> Can you quickly check whether there are any orphaned temp files in `/tmp/openclaw-cache` right now?

### Bad Example

```text
Agent adds `uv run jake cache audit-tmp` command immediately, with tests and docs.
```

### Why It's Bad

- Over-engineers a truly one-off, low-risk question.
- Adds long-term code surface for a short-lived inspection.

### Good Example

```text
Agent uses shell/exec directly:
`ls -lah /tmp/openclaw-cache`
`du -sh /tmp/openclaw-cache/*`

Then reports findings and asks whether this should become a recurring check.
```

### Why It's Good

- Uses direct shell for genuinely ad hoc read-only work.
- Preserves CLI surface area for reusable automation.
- Includes follow-up decision point for future CLI conversion.
- Related: [Decision Gate - Scoring Rubric](decision-gate.md#scoring-rubric)

---

## Example 3: Hidden Env Reads in Domain Logic

### Prompt

> Add a command to sync users from the identity provider.

### Bad Example

```python
# jake/users/sync.py
import os
import requests

def run_sync():
    base_url = os.getenv("IDP_URL")
    token = os.getenv("IDP_TOKEN")
    return requests.get(f"{base_url}/users", headers={"Authorization": token}).json()
```

### Why It's Bad

- Core logic depends on process environment.
- Harder to test and reuse.
- Violates boundary: config should enter through CLI wiring.

### Good Example

```python
# jake/users/sync.py
def run_sync(*, idp_client: IdpClient) -> SyncResult:
    users = idp_client.fetch_users()
    return reconcile_users(users)
```

```text
# CLI handler (conceptual)
@idp_options
def sync_users(idp_options: IdpOptions):
    client: IdpClient = idp_options.client()
    result = run_sync(idp_client=client)
    print_summary(result)
```

### Why It's Good

- Keeps environment/config handling at the CLI edge.
- Injects explicit dependencies.
- Enables focused tests on business behavior.
- Related: [Click Patterns - Dependency Injection Boundary](click-patterns.md#4-dependency-injection-boundary), [Project Structure - Dependency and Config Boundaries](project-structure.md#dependency-and-config-boundaries)

---

## Example 4: Agent Dialogue and Tool Choice

### Prompt

> I need a weekly report command for unresolved ingestion failures.

### Bad Example (Dialogue)

```text
User: I need a weekly report command for unresolved ingestion failures.
Agent: I'll just write `scripts/report_failures.py` quickly.
Agent tool call: write script, run script, paste output.
```

### Why It's Bad

- Ignores explicit request for a reusable command.
- Produces unstructured output and non-discoverable workflow.

### Good Example (Dialogue)

```text
User: I need a weekly report command for unresolved ingestion failures.
Agent: I'll add `uv run openclaw reports unresolved-failures --since 7d`.
Agent: I'll keep command wiring in CLI, and report logic in domain modules.
Agent tool calls:
  - update CLI group with new `reports` subcommand
  - add shared datastore options decorator if needed
  - add `openclaw/reports/` module and tests
  - run `uv run openclaw reports unresolved-failures --help`
```

### Why It's Good

- Implements durable operator workflow.
- Keeps command discoverable and self-documenting.
- Follows thin-wrapper CLI architecture and testing discipline.
- Related: [Project Structure - CLI Organization](project-structure.md#cli-organization), [Checklist](../checklist.md)
