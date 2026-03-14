# Structural Change Proposals

Large repository changes must not be executed automatically.

Instead they should be proposed.

## Big change threshold

A change is considered structural when:

- more than **10 files** are moved or created
- a container split is required
- containers must merge
- a container must be renamed

These require a proposal.

## Proposal format

```
🧠 PARA Maintenance Proposal

ID
para-<id>

Problem
Explain what is wrong.

Evidence
What repo activity suggests the change?

Proposal
Describe the structural change.

Impact
Number of files moved/created.

Planned actions
List file operations.

Reply with

approve para-<id>
reject para-<id>
revise para-<id>
```

## Proposal storage

Proposals should also be written to the repository.

Example location:

```
1-projects/openclaw-maintenance/proposal-para-42.md
```

## Safety rules

Never propose:

- deletion of user-authored knowledge
- moving files modified in the last few hours
- restructuring containers with active edits

Prefer incremental changes.
