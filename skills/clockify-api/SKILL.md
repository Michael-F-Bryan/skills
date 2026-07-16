---
name: clockify-api
description: Use when querying or changing Clockify projects, tasks, clients, or time entries, including Jira-backed reconciliation and deterministic cleanup.
---

# Clockify API

## Core rule

Use the shortest existing path, then verify the resulting Clockify state. Prefer `jake-tools` when it already implements the operation; use direct API calls only for unsupported work.

## Fast path

1. Check the installed interface before designing a workflow:
   ```bash
   unset PYTHONPATH
   cd ~/Documents/jake-tools
   uv run jake-tools clockify --help
   ```
   Run the relevant subcommand's `--help`. For Jira reconciliation, use `clockify jira-sync`; for naming, use `clockify jira-name`.
2. If no matching command exists, retrieve the API key at runtime from `op://Smart-Home/Clockify API Key for Cursor/API Key`. Never print or persist it.
3. Resolve the user and workspace once, then reuse their IDs. Use explicit date ranges and exact IDs/keys.
4. Read before mutation. For bulk work, produce a dry-run and select records by deterministic criteria.
5. Apply the smallest change that satisfies the request.
6. Re-read the affected project, task, or time entry from Clockify before reporting completion.

## Routing

| Request | Default path |
|---|---|
| Jira tickets ↔ Clockify tasks/projects | `jake-tools clockify jira-sync --help` |
| Jira-backed names | `jake-tools clockify jira-name --help` |
| Recent entries or timer state | Direct API read |
| One unsupported create/update | Direct API mutation plus re-read |
| Bulk cleanup or duplicate merge | Load `references/workflows.md`; dry-run first |
| Endpoint/field detail | Load only the needed part of `references/openapi.json` |

## Safety contract

- Never delete time entries unless Michael explicitly asks.
- Never change records outside the requested range or exact selection.
- Never infer Jira mappings from vague semantic similarity; prefer exact issue keys and trusted IDs.
- Do not repeatedly rediscover workspace, user, client, or project IDs in one task.
- Do not download or inspect the full OpenAPI document for a routine operation with a known path.
- Preserve existing fields required by Clockify update endpoints.

## Reporting

Keep the result compact: affected IDs/names, before → after, dry-run or applied state, and the authoritative re-read that proved it. Do not narrate authentication or endpoint discovery unless it blocked the task.
