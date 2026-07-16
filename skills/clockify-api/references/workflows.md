# Clockify API workflows

Load this reference only for direct API work that is not already implemented by `jake-tools`.

## Authentication and request shape

Retrieve the API key at runtime from 1Password and keep it in process memory only. Send it as `X-Api-Key`; use `Accept: application/json`, and add `Content-Type: application/json` for mutations. Resolve the current user and workspace once per task.

Use `references/openapi.json` for exact paths and schemas. Inspect only the relevant operation instead of loading the full specification into context.

## Project/client association cleanup

Clockify “company” maps to project `clientId`; tasks inherit it from their project.

1. Resolve the workspace and target client.
2. List active and archived projects.
3. Select projects with exact criteria, such as a Jira-key naming pattern and empty `clientId`.
4. Update each project while preserving required fields: name, colour, billable, public, archived, note, and client.
5. Re-list and prove no selected project has the old or empty client.
6. If tasks matter, verify matching tasks sit beneath correctly associated projects.

## Jira-backed naming

- Clockify project names use the Jira parent summary without an `SF-NNN` prefix.
- Keep the Jira key in the project note, such as `Jira: SF-131`, or retain an existing Jira URL.
- Clockify task names keep the key prefix, such as `SF-353 Vehicle Control Logic - Preliminary Architecture`.

Prefer:

```bash
unset PYTHONPATH
cd ~/Documents/jake-tools
uv run jake-tools clockify jira-name SF-353 "Vehicle Control Logic - Preliminary Architecture" --json
```

## Merging duplicate Jira-backed projects

Clockify has no project-merge endpoint. Keep the correctly named project and archive the duplicate only after moving its data.

1. Resolve both projects, active users, tasks, and time entries. Stop if the inventory is partial.
2. Use the unsuffixed, summary-only project as canonical and preserve its Jira note.
3. Copy duplicate tasks, reusing exact-name matches. Record old → new task IDs.
4. Move every duplicate-project entry to the canonical project and mapped task while preserving start, end, billable, description, and tags.
5. Attach previously taskless canonical entries only when the description exactly matches a known task summary.
6. Archive, rather than delete, the duplicate using a full project update.
7. Verify the duplicate is archived, contains no remaining entries, copied tasks exist, and no active duplicate naming remains.

Make reruns idempotent: reuse exact-name tasks, skip migrated entries, and tolerate an already archived duplicate.

## Recent work and time-entry hygiene

Use explicit periods: today, yesterday, this week, or concrete start/end timestamps. Useful checks include:

- running timers;
- entries without a project or task;
- blank descriptions;
- suspiciously short entries;
- exact Jira keys in descriptions.

For updates, enumerate the exact entry IDs and before/after fields first. Never perform fuzzy bulk edits.

## Correlating entries with Jira

Evidence order:

1. exact issue key in the Clockify description;
2. exact key from another trusted task source;
3. an already-established exact description mapping;
4. explicit human instruction.

If evidence is weaker, report candidates and do not mutate.

## Verification receipts

After mutation, fetch the changed object again and compare the relevant fields. For bulk work, also re-run the original selection query and prove the old state no longer matches. Report counts, exact IDs/names, and any skipped conflicts.
