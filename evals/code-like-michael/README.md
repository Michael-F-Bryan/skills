# code-like-michael evaluation suite

Probes that proved useful during the 10x improvement loop. Re-run after skill edits to check activation and adherence.

## Prerequisites

- Skill symlinked: `skills/code-like-michael` → global agents folder
- Sub-agents need `available_skills` context to test activation fairly (plain Task sub-agents may not inherit skill discovery)

## Challenges

| Challenge | What it tests | Arms |
|-----------|---------------|------|
| [greenfield-csv-cli](challenges/greenfield-csv-cli/) | Greenfield size, typed boundaries | Unprompted + explicit |
| [greenfield-rss-cli](challenges/greenfield-rss-cli/) | Harder greenfield, moderate complexity | Unprompted + explicit |
| [refactor-utils-dump](challenges/refactor-utils-dump/) | Surgical refactor, abstraction threshold | Unprompted + explicit |
| [test-hardwired-io](challenges/test-hardwired-io/) | Testing without mock theatre | Unprompted + explicit |
| [slop-induction](challenges/slop-induction/) | Vague ambitious spec → architecture slop | Skill-on with available_skills |

## How to run

1. Spawn an agent with the challenge `PROMPT.md` (unprompted or explicit arm).
2. For activation tests, include the skill in `<available_skills>` with current frontmatter description.
3. Grade using [grading/rubric.md](grading/rubric.md).
4. Record results under `_working/code-like-michael-10x/` or a new working folder.

## Grading

See [grading/rubric.md](grading/rubric.md).
