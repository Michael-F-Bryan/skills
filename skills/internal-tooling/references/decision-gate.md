# Decision Gate

Use this decision gate when deciding whether a piece of work should become a first-class CLI command or remain a one-off shell action, notebook cell, or short script.

## Goal

Bias towards **named, discoverable, reviewable tooling** for work that matters, without turning every small task into permanent command surface area.

The question is not “can this be a CLI command?”
The question is “**should this become part of the repo’s supported operational interface?**”

## Default Principle

Prefer a CLI command when the work is:

- repeated
- shared
- stateful
- risky
- parameterised
- worth testing
- worth documenting

Prefer a one-off shell command or temporary script when the work is:

- clearly ad hoc
- read-only
- local in scope
- low-risk
- unlikely to be reused
- faster to inspect than to formalise

## Immediate CLI Triggers

Build a CLI command if **any** of the following are true:

- The task **mutates external state**
  Examples: writing to a database, updating remote systems, creating or deleting resources, modifying files in bulk.
- The task is likely to be **reused by you or somebody else**
- The task needs **validation, filtering, retries, batching, paging, or structured error handling**
- The task would benefit from **stable arguments and a documented interface**
- The task is important enough that you would want **tests** around its behaviour
- The task is the sort of thing you would reasonably expect to run again in a month and still understand

## Strong Signals For “Probably CLI”

A task should usually become a CLI command when **two or more** of the following are true:

- It takes input parameters that will vary from run to run
- It touches shared environments or production-like systems
- It needs consistent logging or progress reporting
- It would be annoying or risky to reconstruct from shell history
- It is part of an operational workflow, support workflow, migration, report, or backfill
- A reviewer would benefit from seeing the operation expressed as a named command instead of a blob of ad hoc code

## Strong Signals For “Probably One-Off”

A task should usually stay as a shell action or short-lived script when **all** of the following are true:

- It is read-only
- It is local to the current investigation
- It has no real value once the immediate question is answered
- It does not need a stable interface
- It does not need tests
- It can be expressed clearly in a few lines without inventing abstractions

## Practical Heuristic

Use this quick rubric.

### Build a CLI command

- Mutates state? → **Yes**
- Will be reused? → **Yes**
- Needs validation, retries, batching, filtering, or paging? → **Yes**
- Worth testing or documenting? → **Yes**

If the answer is **yes to any of the first three**, build a CLI command.
If the answer is **yes to two or more overall**, build a CLI command.

### Keep it one-off

- Read-only
- Local investigation only
- No expected reuse
- No need for stable arguments
- No need for tests

If that set describes the task, keep it one-off.

## Escalation Rule

Start with the lightest thing that is still responsible.

A one-off should be promoted into a CLI command when it starts to accumulate any of these smells:

- more flags or parameters than comfortably fit in a one-liner
- repeated copy/paste into shell history
- embedded environment lookups
- retry loops
- parsing or validation logic
- structured logging
- “just tweak this and run it again”
- somebody else needing to run it
- desire to keep it around “for later”

Once that happens, stop pretending it is temporary.

## Boundary Rule

If you decide to build a CLI command:

- expose a **named subcommand**
- keep the command handler thin
- move real behaviour into domain/library code
- read config and environment only at the boundary
- make dependencies explicit
- make the output and failure modes intentional

## Output Contract Rule

When formalising a CLI command, decide these things up front:

- Is the output for humans, automation, or both?
- Do we need a machine-readable mode such as `--json`?
- What exit codes should callers rely on?
- Should logs go to `stderr` and data to `stdout`?
- Is the command safe to retry?
- Do destructive operations need `--dry-run`, explicit confirmation, or both?

A command without an output contract is only half-designed.

## Examples

### Build a CLI command

- Backfill missing metadata for a set of records
- Sync remote resources to a known local layout
- Generate a report people will want again next week
- Bulk update configuration in an external system
- Inspect a remote service with filtering, pagination, and retries

### Keep it one-off

- Grep some logs to answer a one-time question
- Run a small SQL query during an investigation
- Inspect a single local file
- Check how many records match a condition before deciding what to do next
- Try out an API call once while exploring the shape of the data

## Anti-Patterns

Do not formalise work into a CLI command just because:

- it is possible
- it feels more “engineered”
- you want to avoid making a judgement call
- the command name sounds neat
- a tiny local investigation could theoretically happen again someday

Do not keep something as a one-off when:

- it mutates state
- it has already been run twice
- it contains logic you would not want to re-derive under pressure
- somebody else is likely to need it
- it now has enough complexity that correctness matters

## Final Test

Ask this:

> If someone needed to do this again in six weeks, would I rather point them at a named command with help text and tests, or at a shell snippet buried in history?

If the named command is clearly better, build the command.
