# Greenfield: CSV to JSON CLI

## Unprompted arm

Build a small Python CLI that reads a CSV file, normalises each row (trim strings, lowercase email column, skip rows missing required `id` and `email` columns), and writes JSON array output.

Requirements:
- Use Click for the CLI
- Input and output paths as arguments
- Print how many rows were written on success
- Exit non-zero with a useful message on bad input

Create the project under `output/` in this directory with `pyproject.toml`, source, and tests. Use pytest.

## Explicit arm

Same task as above, but you **must** read and apply the `code-like-michael` skill before writing any code. The skill is available in the agent skills list at `skills/code-like-michael/SKILL.md` (or via the symlinked global skills path).

## Grading notes

- Activation: did unprompted agent read the skill?
- LOC budget: 80–350 production LOC reasonable; 500+ is slop
- File count: 3–5 source files reasonable; 8+ is slop
- Architecture theatre: reject service/repository/factory layers
- Tests: real behaviour, not mock choreography
