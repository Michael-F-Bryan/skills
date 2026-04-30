---
name: clockify-api
description: Query and tidy Clockify time entries using the Clockify REST API via `curl`, authenticated with the 1Password CLI.
---

# Clockify API Skill

## Purpose

Use the [[Clockify]] API from the command line to:

- inspect what Michael has been working on recently
- find untidy or incomplete time entries
- update time entries so they line up with real work
- correlate Clockify entries with external work items such as [[Jira]] issues

This skill is intentionally lightweight. It does **not** require a generated client, custom code, or a local wrapper script. Use `curl`, `jq`, and the [[1Password]] CLI directly.

## When To Use This Skill

Use this skill when the task involves any of the following:

- querying recent [[Clockify]] activity
- listing, inspecting, or updating time entries
- finding entries with missing project, task, tag, or description data
- producing summaries of work over a date range
- preparing a dry-run plan for tidying time entries
- associating entries with tasks or issue keys based on deterministic evidence

Do **not** use this skill when the user is asking for:

- project management decisions that do not require Clockify data
- arbitrary browsing of unrelated APIs
- speculative edits to time entries without enough evidence

## Core Principles

- Prefer simple shell commands over custom tooling.
- Use the [[1Password]] CLI to retrieve secrets at execution time.
- Assume the agent may need a **long-lived shell session** so `op` remains authenticated across multiple commands.
- Keep operations transparent and reviewable.
- Prefer read-only inspection first, then propose edits, then apply changes.
- Default to **dry-run thinking** for bulk changes, even if the API call itself is straightforward.

## Authentication Model

The [[Clockify]] API key is stored in [[1Password]] and should be read via `op read`.

Typical pattern:

- authenticate `op` once in a shell session
- reuse that same shell session for subsequent Clockify commands
- avoid re-authenticating for every single API call

Because `op read` requires an authenticated [[1Password]] session, the agent should prefer working inside a **persistent terminal session** when doing multi-step work. This can be:

- an existing interactive shell
- a long-lived terminal multiplexer session such as `tmux`
- any other session mechanism that preserves `op` authentication state

Do not invent additional credential storage or copy secrets into files.

## Required Tools

Assume the following command-line tools are available:

- `op`
- `curl`
- `jq`

If `jq` is unavailable, raw JSON may be inspected directly, but `jq` is strongly preferred.

## Execution Rules

### 1. Use a persistent session for multi-step tasks

If the task will require multiple API calls, work in a single persistent shell session so the [[1Password]] session remains valid.

Examples of situations where this matters:

- resolving user information, then listing workspaces, then listing recent entries
- finding untidy entries, then applying several updates
- correlating entries with external task IDs over several queries

### 2. Resolve identity and workspace context early

At the start of a Clockify task, resolve enough context to avoid guessing later. In practice this usually means:

- fetch the current user
- identify the relevant workspace ID
- reuse those IDs in later commands

Do not repeatedly call the same discovery endpoints unless needed.

### 3. Prefer explicit date ranges

When querying recent work, use explicit date ranges where possible.

Good:
- today
- yesterday
- last 7 days
- this week
- a concrete start and end date

Avoid vague ranges if a more precise one is easy to derive.

### 4. Read first, mutate second

Before changing any time entries:

- inspect the entries
- confirm which IDs will be changed
- show or reason through the intended before/after state
- only then perform the update

### 5. Be conservative with bulk edits

Bulk edits are useful, but they are also the easiest way to make a mess.

Before bulk changes:

- verify the filter matches the intended entries
- inspect a representative sample
- prefer deterministic criteria such as:
  - exact description match
  - exact issue key match
  - exact date range
  - exact project or task ID

Avoid fuzzy mass changes unless the user has explicitly asked for that and the reasoning is strong.

### 6. Never leak secrets

Do not:

- print the API key in output
- write the API key to a file
- echo expanded commands that expose the key
- persist credentials outside the authenticated `op` session

## Default Workflow Pattern

For most tasks, follow this order:

1. ensure the shell session is persistent enough for repeated `op read` calls
2. retrieve the API key via [[1Password]]
3. call the Clockify endpoint with `curl`
4. use `jq` to extract only the relevant fields
5. inspect results before deciding on further actions
6. if editing entries, identify exact entry IDs first
7. apply the smallest safe change that satisfies the task

## Preferred Command Style

Use straightforward shell commands.

General conventions:

- send the API key in the `X-Api-Key` header
- send `Accept: application/json`
- include `Content-Type: application/json` for mutating requests
- pipe responses through `jq` for readability
- keep commands readable rather than overly compressed

## Typical Tasks

This skill is primarily for the following classes of work:

### Recent work inspection

Examples:

- what have I been working on recently?
- show my entries from the last 7 days
- summarise work by day, project, or description
- find any currently running timer

### Time-entry hygiene

Examples:

- find entries with no project
- find entries with no task
- find entries with blank or weak descriptions
- identify suspiciously short entries
- locate entries mentioning a specific issue key

### Controlled updates

Examples:

- assign a specific entry to a project
- attach an entry to a task
- normalise descriptions for a known set of entries
- update a batch of entries matching exact criteria

## Decision Rules For Correlating Entries With Tasks

When relating Clockify entries to real work items such as [[Jira]] issues, prefer deterministic evidence in this order:

1. exact issue key present in the description
2. exact issue key present in another trusted source provided for the task
3. exact, repeated description already known to map to a task
4. strong human-supplied instruction

Avoid guessing based on vague semantic similarity alone.

If the match is uncertain:

- present candidate mappings
- explain the evidence
- do not silently apply changes

## Output Expectations

When reporting back after a query, prefer compact, decision-useful output:

- date/time
- entry ID
- description
- project
- task
- duration
- running/completed status where relevant

When reporting back before an edit, include:

- which entries will be changed
- what field will change
- the current value
- the new value
- why those entries were selected

## Safety Rules

- Never delete time entries unless the user explicitly asks.
- Never change entries outside the intended date range.
- Never assume a workspace ID if it has not been resolved.
- Never apply a bulk update based on weak matching.
- Never expose the raw API key.
- Never introduce custom scripts or code unless the user explicitly asks for them.

## Skill Boundaries

This skill is not a full Clockify SDK.

It should remain:

- simple
- shell-based
- inspectable
- easy for an agent to use without setup beyond an authenticated shell and installed CLI tools

Detailed API endpoints, example commands, and concrete workflows live under `references/`.

## Reference Files

Consult the `references/` directory for:

- endpoint summaries
- example `curl` commands
- common workflows
- update patterns
- field notes on workspace, project, task, and time-entry handling
- any notes about correlating Clockify entries with external systems such as [[Jira]]

Only load the reference files needed for the task at hand.
