# PARA Maintenance Workflow

This document defines the orchestrated maintenance workflow.

The workflow is executed periodically (for example during a heartbeat).

## High-level workflow

1. Repo Survey
2. Activity Detection
3. Classification Review
4. Container Health Evaluation
5. Atomic Note Distillation
6. Maintenance Planning
7. Execution / Proposal

Each step runs in its own specialised sub-agent.

## Sub-agent sequence

## 1 Repo Survey Agent

Inputs

- repository root
- git history
- filesystem tree

Outputs

```
survey-report.json
```

Contains:

- recently changed files
- new files
- files outside PARA roots
- containers touched recently

Reference:

```
references/agents/repo-survey.md
```

## 2 Activity Detection Agent

Inputs

```
survey-report.json
```

Outputs

```
activity-report.json
```

Detects:

- active projects
- dormant projects
- emerging topics
- candidate distillation sources

Reference:

```
references/agents/activity-detection.md
```

## 3 Classification Review Agent

Inputs

```
survey-report.json
activity-report.json
```

Outputs

```
classification-report.json
```

Detects:

- misclassified files
- files outside PARA roots
- candidate relocations

Reference:

```
references/agents/classification-review.md
```

## 4 Container Health Agent

Inputs

```
survey-report.json
activity-report.json
classification-report.json
```

Outputs

```
container-health-report.json
```

Detects:

- overly broad containers
- duplicate topics
- archive candidates

Reference:

```
references/agents/container-health.md
```

## 5 Atomic Distillation Agent

Inputs

```
survey-report.json
activity-report.json
```

Outputs

```
atomic-notes-report.json
```

Creates or proposes atomic notes derived from recent work.

Reference:

```
references/agents/atomic-distillation.md
```

## 6 Maintenance Planner Agent

Inputs

All previous reports.

Outputs

```
maintenance-plan.md
```

Contains:

- safe changes
- proposed structural changes
- extracted atomic notes
- repo health summary

Reference:

```
references/agents/maintenance-planner.md
```

## Execution stage

Small changes are applied automatically.

Large changes generate a proposal message.

The proposal protocol is defined in:

```
references/proposals.md
```

## Resilience rules

Agents must:

- attempt partial success rather than fail
- annotate incomplete data
- degrade gracefully if reports are missing

Workflow orchestration must continue even if intermediate reports contain uncertainty.

## Post-maintenance (optional)

After execution or proposal, optionally ensure retrieval aids stay in sync:

- **Manifests:** For containers that were created, split, merged, or significantly changed, ensure or update `_manifest.md` per `knowledge-base-navigator/references/manifests.md` (Purpose, Includes, Excludes, Likely queries, Related).
- **Topic indexes:** For key topic containers (e.g. under `3-resources/`), ensure an `index.md` exists or is updated when notes are added or moved (structure per `knowledge-base-navigator/references/indexes.md`).
- **kb-index:** If the repo uses `kb-index.json`, refresh it after maintenance (e.g. run the index-generation script in knowledge-base-navigator `scripts/` or equivalent).
