# Internal CLI Philosophy

This note captures a durable part of Michael's style for internal tools and utility CLIs.

## Core idea

A good internal CLI is not a thin wrapper around functions. It is a serious operator boundary.

Its job is to:

- package repeated work into named commands,
- expose tasks the way an operator thinks about them,
- absorb protocol and integration awkwardness,
- validate hard at the boundary,
- teach through `--help`, and
- work well for humans, agents, and scripts.

Another way to say it: the CLI is where a messy system becomes operable.

## Preferred shape

### 1. Thin top-level entrypoints

Top-level executables should mostly:

1. initialise process-wide concerns,
2. construct shared dependencies,
3. parse and validate arguments,
4. dispatch to the selected command,
5. map failures into operator-visible errors.

Keep command shells boring. Put real behaviour in domain or application modules.

### 2. Task-shaped command trees

Group commands by operator task, not by source tree layout or package names.

Good command paths are guessable from the work someone is trying to do. If a shell snippet keeps getting copied around, that usually means the behaviour wants a first-class subcommand.

### 3. Small reusable CLI seams

Extract repeated boundary concerns into small composition pieces:

- global flags,
- connection options,
- config loading,
- output formatting,
- auth,
- retries,
- telemetry/bootstrap hooks.

Do not invent broad abstractions for domain logic unless they clearly earn their keep.

### 4. Strict boundary parsing

Parse loose inputs early into typed objects:

- file paths,
- URLs,
- request payloads,
- option combinations,
- environment-backed config.

The boundary should do the awkward validation so downstream code can stay simpler.

### 5. Thin command handlers

A command handler should mostly:

1. validate inputs,
2. assemble dependencies,
3. call the real operation,
4. render the result.

If the command file contains the system's main understanding, the boundary is too fat.

## Help text is part of the interface

Treat `--help` as part of the contract.

Non-trivial commands should encode:

- the shape of the task,
- important invariants,
- dangerous or non-obvious constraints,
- examples for easy-to-misunderstand arguments,
- adjacent commands worth trying next.

This is operational guidance, not decorative documentation.

## Truthfulness rules

Internal tooling is allowed to be blunt. It is not allowed to mislead.

- If behaviour is not implemented, do not fake it.
- If a flag is unsupported, reject it.
- If input is ambiguous, say so.
- If a dependency is missing, fail with context.
- If a payload is malformed, reject it before sending nonsense downstream.

## Human and automation modes

Assume each command will be used:

1. by a human at a terminal,
2. by an agent,
3. in a script or pipeline.

Prefer:

- sensible human-readable defaults,
- stable JSON or machine-readable output where automation needs it,
- file-or-stdout choices where useful,
- progress on stderr instead of contaminating structured stdout.

## Design checklist

Before adding or reshaping a command, answer:

1. What repeated operator task does this command name?
2. Why does it deserve a first-class command instead of a note or shell snippet?
3. What invariants or failure modes matter?
4. Which shared seam should it reuse for config, logging, output, auth, or retries?
5. What should stdout look like for a human?
6. What should stdout look like for automation?
7. What belongs in `--help` so a later agent can use it without tribal knowledge?
8. Which parts are domain logic, and which parts are just boundary adaptation?

## Anti-patterns

Reject these by default:

- giant entrypoints that contain the real logic,
- command trees shaped around internal package names,
- hidden environment-variable behaviour with no help text,
- raw protocol or API leakage where the CLI could normalise it,
- fake flags for unimplemented behaviour,
- machine-readable stdout mixed with progress chatter,
- throwaway one-off scripts left as the only way to perform an important recurring task.
