---
name: internal-tooling
description: Build reusable automation as first-class CLI subcommands instead of throwaway scripts. Use when an agent considers writing a script, automating repeated tasks, adding operational tooling, or wiring commands that run as `uv run <agent-name> ...`.
---

# Internal Tooling

Build automation as productized CLI commands, not one-off scripts.

## Core Rule (Summary)

If a task is likely to be repeated, shared, or non-trivial, implement it in the agent's CLI:

- Agent `Jake` runs tools via `uv run jake ...`
- Agent `OpenClaw` runs tools via `uv run openclaw ...`

The agent may still use shell/exec for command execution. The rule is about where reusable automation logic lives.

Canonical decisioning lives in [references/decision-gate.md](references/decision-gate.md). Use this file as the source of truth for CLI-vs-one-off decisions.

## Progressive Disclosure

Read only what you need:

- **Minimum**: this file (`SKILL.md`) for intent and boundaries.
- **Standard**: add [references/decision-gate.md](references/decision-gate.md) for a concrete CLI-vs-one-off decision.
- **Deep**: add one targeted reference for implementation details (patterns, structure, examples, lifecycle).

Stop reading once you can name the next concrete file/command change.

## Routing Table

| Task intent                     | Primary doc                                                        | Section to open                                                                            |
| ------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Decide CLI vs one-off           | [references/decision-gate.md](references/decision-gate.md)         | `## Scoring Rubric`                                                                        |
| Name command surface            | [references/decision-gate.md](references/decision-gate.md)         | `## Naming Guidance`                                                                       |
| Implement command wiring        | [references/click-patterns.md](references/click-patterns.md)       | `## 2) Shared Option Decorators`, `## 3) Thin Command, Rich Domain Module`                 |
| Place files and boundary logic  | [references/project-structure.md](references/project-structure.md) | `## What Goes Where`, `## Dependency and Config Boundaries`                                |
| Verify command quality          | [checklist.md](checklist.md)                                       | `## Verification`                                                                          |
| Resolve ambiguity with examples | [references/examples.md](references/examples.md)                   | `## Example 1: Repeatable Backfill Task` to `## Example 4: Agent Dialogue and Tool Choice` |
| Follow full lifecycle           | [workflow.md](workflow.md)                                         | `## Lifecycle`                                                                             |

## Non-Negotiable Boundaries

- Monolithic CLI surface: one executable (`uv run <agent-name>`) with subcommands.
- Keep the CLI thin: parse inputs, construct dependencies, call library logic.
- Keep business logic in domain modules under `<agent_name>/`, not inside click handlers.
- Use dependency injection at the command boundary.
- No environment-variable reads in domain/infra modules; env parsing/loading stays in `__main__.py`, CLI wiring, or option helper layers.
- No global mutable state for runtime dependencies.

## Throwaway Guardrail

One-off shell usage is acceptable only when all are true:

- Truly single-use.
- Read-only and low-risk.
- No meaningful reuse expected.

This guardrail is necessary but not sufficient: one-off shell is allowed only if the scoring rubric in [references/decision-gate.md](references/decision-gate.md) is all `no`.

If uncertain, build the CLI command.

## Canonical Ownership

- Decisioning and escalation: [references/decision-gate.md](references/decision-gate.md)
- Click wiring patterns: [references/click-patterns.md](references/click-patterns.md)
- Project layout and boundaries: [references/project-structure.md](references/project-structure.md)
- Calibration examples: [references/examples.md](references/examples.md)
- End-to-end execution path: [workflow.md](workflow.md)
- Execution and verification checklist: [checklist.md](checklist.md)

## Quality Bar

- Clear command names that match domain intent.
- Strongly typed boundaries.
- Explicit failure messages with useful context.
- No hidden side effects at import time.
- Small, reviewable diffs over broad refactors.

## Anti-Patterns

- Adding `scripts/*.py` for reusable operational workflows.
- Putting business logic directly in click command functions.
- Reading env vars inside deep library code.
- Creating extra executables when subcommands on the main CLI would suffice.
- Introducing abstractions before a real seam exists.

## Additional Resources

- Workflow by phase (ideation -> deprecation): [workflow.md](workflow.md)
- Implementation and verification checklist: [checklist.md](checklist.md)
- Decision flow and command-selection rubric: [references/decision-gate.md](references/decision-gate.md)
- Click implementation patterns and dependency wiring: [references/click-patterns.md](references/click-patterns.md)
- Prompt + bad/good examples with explanations: [references/examples.md](references/examples.md)
- Project layout, placement rules, and `uv` setup: [references/project-structure.md](references/project-structure.md)
