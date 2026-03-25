# Decision Gate: Build CLI or Not

Use this gate before creating any script or automation.

## Fast Rule

If reusable automation is needed, implement a CLI command under `uv run <agent-name> ...`.

## Scoring Rubric

Score each item as `yes` or `no`.

1. Will this be run more than once?
2. Could another person or agent benefit from reusing it?
3. Does it mutate data, external state, or production-like systems?
4. Does it need validation, retries, paging, filtering, or parameterization?
5. Would future debugging benefit from standard logging and help text?
6. Is it long enough that a one-off script would be harder to review safely?

Decision:

- Any `yes` on (1)-(6): build CLI command.
- One-off shell usage is acceptable only when all six are `no` and the throwaway guardrail from `SKILL.md` is satisfied.

When uncertain, build the CLI command.

## Escalation Guidance

- Started as one-off but gained options/statefulness -> stop and convert to CLI.
- Repeated command copy-paste in chat history -> convert to CLI.
- Script committed to repo for "temporary use" -> replace with CLI command.

Implementation follow-through:
- after deciding CLI, use [../workflow.md](../workflow.md) and [../checklist.md](../checklist.md)
- for command shape and injection patterns, open [click-patterns.md](click-patterns.md)
- for placement and boundaries, open [project-structure.md](project-structure.md)

## Naming Guidance

- Use intent-driven names: `sync`, `backfill`, `validate`, `repair`, `report`.
- Keep top-level grouped by responsibility.
- Avoid ambiguous names like `run`, `do`, `misc`, `helper`.
