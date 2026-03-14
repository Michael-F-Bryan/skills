---
name: para-custodian
description: Periodically maintain a shallow PARA workspace using specialised sub-agents. The skill surveys the repo, classifies files into PARA containers, distils atomic notes using the CODE method, and safely proposes or applies maintenance actions.
entrypoint: references/workflow.md
---

# PARA Custodian

This skill maintains a repository organised using a strict shallow PARA layout.

The repository uses numbered PARA roots:

- `1-projects/`
- `2-areas/`
- `3-resources/`
- `4-archives/`

Each root may contain **one level of containers only**.

Example:

```
1-projects/mdbook-linkcheck-triage/plan.md
3-resources/para/PARA-summary.md
```

Deeper nesting must not be introduced.

Both skills assume the same PARA layout (four roots, one level of containers); retrieval aids (manifests, indexes, note metadata) are described in knowledge-base-navigator references.

## Core responsibilities

This skill periodically:

1. Surveys repository activity
2. Detects active projects and emerging topics
3. Reviews PARA classification
4. Evaluates container health
5. Distils atomic notes using the CODE system
6. Applies safe changes
7. Proposes large changes via the user's communication channel

Before creating a new atomic note or moving content, use the knowledge-base-navigator skill to check whether equivalent knowledge already exists; avoid duplicates.

The process is designed to run autonomously with minimal intervention.

After each workflow step, persist the step output.

If the step changed tracked repository files, commit and push immediately with a step-scoped commit message.

If the step produced only temporary analysis artifacts, do not commit them unless the workflow is running on a dedicated maintenance branch that preserves intermediate state.

## Change thresholds

Safe auto-apply:

- ≤ 10 files created or moved
- no container splits
- no container merges
- no root-level changes

Proposal required:

- > 10 files moved/created
- container split or merge
- container rename
- new conceptual container

Large changes must be surfaced through the configured communication channel (e.g. Discord).

## Sub-agent architecture

Each maintenance stage is performed by a specialised sub-agent with strict inputs and outputs.

Agents:

- Repo Survey Agent
- Activity Detection Agent
- Classification Review Agent
- Container Health Agent
- Atomic Distillation Agent
- Maintenance Planner Agent

Agents should **adapt rather than fail**.

When uncertain they should:

- produce best-effort output
- annotate uncertainty
- continue the workflow

Agents must not abort the process unless the repository cannot be accessed.

## Progressive disclosure

The skill uses a `references/` directory.

Each reference file describes:

- workflow orchestration
- agent contracts
- evaluation rules
- atomic note standards
- proposal protocols

Agents should load only the references required for their step.

This reduces context usage during long-running autonomous workflows.

## Token Economy

Never re-read the full PARA repository by default.

Default to incremental maintenance based on:
- files changed since the last successful maintenance run
- recently touched containers
- open proposals
- unresolved classification issues

Each sub-agent must operate within a bounded read budget.

Prefer:
1. git metadata
2. container manifests
3. cached summaries
4. full file contents only when necessary

The Atomic Distillation Agent may create at most 3 atomic notes per run.

It should prefer strong, reusable insights over broad coverage.

Container-wide structural review should not run on every heartbeat.

Run broad container-health checks on a slower cadence than delta-based maintenance.
