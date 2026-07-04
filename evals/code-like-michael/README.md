# code-like-michael evaluation suite

Probes that proved useful during the 10x improvement loop. Re-run after skill edits to check activation and adherence.

## Prerequisites

- Skill symlinked: `skills/code-like-michael` → global agents folder
- Sub-agents need `available_skills` context to test activation fairly (plain Task sub-agents may not inherit skill discovery)

**Verify the deployed skill before every run.** Agents read the skill through `~/.claude/skills/` / `~/.agents/skills/`; if that path holds a stale copy instead of a symlink, every run silently evaluates an old skill. This burned five re-runs on 2026-07-04. Check first:

```bash
readlink ~/.agents/skills/code-like-michael   # must point into this repo
diff -r ~/.claude/skills/code-like-michael/SKILL.md skills/code-like-michael/SKILL.md && echo OK
```

## Challenges

| Challenge | What it tests | Arms |
|-----------|---------------|------|
| [greenfield-csv-cli](challenges/greenfield-csv-cli/) | Greenfield size, typed boundaries | Unprompted + explicit |
| [greenfield-rss-cli](challenges/greenfield-rss-cli/) | Harder greenfield, moderate complexity | Unprompted + explicit |
| [refactor-utils-dump](challenges/refactor-utils-dump/) | Surgical refactor, abstraction threshold | Unprompted + explicit |
| [test-hardwired-io](challenges/test-hardwired-io/) | Testing without mock theatre | Unprompted + explicit |
| [slop-induction](challenges/slop-induction/) | Vague ambitious spec → architecture slop | Skill-on with available_skills |
| [greenfield-larger](challenges/greenfield-larger/) | Medium greenfield (crawler/audit CLI), size + seams under pressure | Cursor CLI, unprompted |
| [maintain-legacy-codebase](challenges/maintain-legacy-codebase/) | Maintenance on messy code: harden-what-you-touch, regression tests | Cursor CLI, unprompted |
| [maintain-styled-codebase](challenges/maintain-styled-codebase/) | Maintenance on skill-styled code: convention matching, seam reuse | Cursor CLI, unprompted |

## How to run

1. Copy the challenge `fixture/` (if any) to a scratch directory so the committed fixture stays pristine.
2. Run the agent. Preferred: Cursor CLI from the scratch directory, which gets real skill discovery —

   ```bash
   cursor-agent -p --output-format stream-json --model composer "<task text from PROMPT.md>" > run.jsonl
   ```

   Check the event log for a read of `code-like-michael/SKILL.md` before the first edit (activation), then grade the diff. Note: in non-interactive mode the CLI may block shell execution, so run the fixture's tests yourself afterwards.
3. Alternative: Task sub-agents, but these lack skill discovery — inject the skill via an `<available_skills>` block for activation tests, or instruct explicitly for adherence-only tests.
4. Grade using [grading/rubric.md](grading/rubric.md).
5. Record results under `_working/code-like-michael-10x/` or a new working folder.

## Grading

See [grading/rubric.md](grading/rubric.md).
