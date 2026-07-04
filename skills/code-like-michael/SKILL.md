---
name: code-like-michael
description: "Use when writing, changing, reviewing, testing, refactoring, or architecting code, including greenfield apps, CLIs, bug fixes, and PR reviews. Applies Michael's default coding style: typed boundaries, thin entrypoints, concrete-first design, anti-ceremony abstractions, real behaviour tests, and operator-shaped interfaces."
---

# Code Like Michael

## Default activation (read this first)

**If you are about to write, change, review, or architect code — including greenfield projects, bug fixes, refactors, tests, or CLI tools — read and apply this skill now.** The user does not need to mention it. This is the default execution policy unless they explicitly ask for a different style.

Before your first line of code:

1. **Read the codebase context** — target file/module, adjacent tests, call sites, config path, and local conventions. Find the smallest seam to change. Do not hallucinate a greenfield-shaped solution into an existing repo.
2. **Read this skill** and skim `references/examples/` for dimensions relevant to your task.
3. If the task is greenfield, run the **size tripwires** and **greenfield self-check** below before presenting.
4. **No test, no done.** If you change behaviour — fix a bug, add a feature or flag — you write a test for it in the same change. Before finishing, list each behaviour you changed and **name the test function that covers it**; if you cannot name one, write it now. Manual smoke checks and re-running old tests that never exercised your change do not count. Never defer this ("I can add tests if you want"); write the tests now, even if you cannot execute them in your environment.
5. **Repair what you touch.** Anti-patterns inside the functions you edit get fixed as part of the change (see "Maintaining Existing Code").
6. Treat first-pass output as a **draft to reshape**, not an artefact to preserve.

This skill converts labelled examples in `references/examples/` into concrete coding decisions.

## Anti-slop tripwires

AI-generated code often looks "architected" before it has earned the right to exist. Stop and reshape when you notice:

### Size discipline (greenfield)

Before presenting greenfield work, count **production** files and LOC (exclude tests, generated files, migrations, fixtures, and docs). If over budget, **stop and justify every file and layer**. Delete or merge anything without an immediate reason. If still over budget, state why before presenting.

| Task complexity | Reasonable production shape | Slop warning signs |
|-----------------|----------------------------|-------------------|
| Small utility / single pipeline (e.g. CSV→JSON CLI) | 3–5 files, 80–350 LOC | 8+ files, 500+ LOC, service/repository/factory layers |
| Medium CLI / workflow tool | 5–8 files, 250–500 LOC | 12+ files, 800+ LOC, plugin systems, generic command buses |
| Bug fix / narrow refactor | Minimal delta to task | Drive-by renames, new abstraction layers, unrelated files |

If a file cannot justify independent existence ("one reason to change"), merge it back. Compactness is a tripwire, not permission for density theatre.

### Abstraction pressure gate

**Interfaces, layers, registries, frameworks, and separate modules** — do not introduce unless at least one is true **right now**:

- **≥2 real call sites** need the same logic, or
- a **genuine unstable boundary** (network, filesystem, clock, env, process, hardware), or
- a **domain invariant** needs one obvious home, or
- **lifecycle/ownership** cannot be expressed safely in concrete code.

Reject: interfaces with one implementation, `Manager`/`Service`/`Repository` pass-through wrappers, plugin registries before plugins exist.

**Domain/boundary types** (`UserId`, `AppConfig`, `ParsedRow`, request/response models) — introduce when they parse loose input once, make illegal states harder to represent, or name a real concept. Reuse pressure is not required for types at boundaries.

### Rationalisation tripwires

| Excuse | Reality |
|--------|---------|
| "This will scale later" | Scaling pressure is not present yet. Keep the seam visible, not abstract. |
| "The repo already has this pattern" | Nearby code is evidence, not permission. Copy only patterns that are still good. |
| "A flag keeps it flexible" | Core workflows must be default and tested. Flags are for output shape, filtering, verbosity, dry-run — not hiding essential behaviour. |
| "This interface helps testing" | Test real behaviour first. Introduce seams at true external boundaries. |
| "It's only generated scaffolding" | Generated code gets a **higher** cleanup bar before presentation. |
| "The existing tests still pass" | They never exercised the behaviour you changed. Passing is silence, not evidence. |
| "The suite doesn't cover this area anyway" | You are standing in a coverage gap. Add the test for what you changed; don't inherit the gap. |
| "I can't run the tests in this environment" | Write them anyway, state UNVERIFIED prominently, and show the exact command to run. |

### Scope and trust

- **V1 narrow, not a toy**: cut speculative features, but keep the trust spine — typed models, validation, useful errors, real tests, honest CLI behaviour.
- **No opt-in core workflows**: do not make essential behaviour depend on a flag users (or tests) will forget to pass. Optional flags are fine for rendering, filtering, verbosity, dry-run, and output format.
- **Return typed outcomes**: do not require callers to inspect mutable post-call state (`last_result`, `error` fields, hidden accumulators). Internal caches are fine when invalidation is clear and correctness does not depend on callers clearing/reading them.
- **Don't canonise nearby bad code**: inspect existing code for useful patterns, but harden bad seams you touch — do not copy `utils` dumps, scattered env reads, or placeholder layers just because they are local.
- **Higher bar for AI-generated code**: generated code needs *more* verification, not less — run checks, test observable behaviour, reshape before presenting.
- **Delete scaffolding before claiming done**: remove unused files, exports, placeholder TODOs, speculative flags, empty barrels, and dead tests that only assert wiring.

### Greenfield self-check (include before presenting)

```
Production files: N
Production LOC: N
New abstractions: [list each + pressure-gate reason]
Over budget? [yes/no — if yes, justify]
Checks run: [pytest/cargo/etc.]
```

## When to Use

**Always**, for any coding task, unless the user explicitly requests a different style.

Especially when the work needs to feel deliberately authored in Michael's style, not merely correct:

- new features or bug fixes where architecture choices matter
- refactors that touch boundaries, config, IO, module layout, or CLI shape
- review passes where you need to distinguish `works` from `fits this repo`
- internal tools and utility CLIs that should feel operator-friendly rather than script-like

Do not treat this as permission for decorative rewrites. Prefer narrow, task-shaped changes unless the request explicitly asks for broader restructuring.

## Ground Truth

Treat these files as source-of-truth calibration:

- `references/examples/` (labelled examples; highest authority)
- `references/examples/greenfield-size-discipline.md` (LOC/file-count anchors for greenfield and small refactors)
- `references/dimensions.md` (20 dimensions)
- `references/annotations-rubric.md` (anchor definitions)

When uncertain, prefer consistency with labelled examples over generic best practices.

## Style North Star

Write code that is:

1. **Concrete first, abstract second**: extract only when an abstraction clearly earns its keep.
2. **Boundary strict**: parse into typed/domain models early; avoid "stringly" and loose dictionary contracts.
3. **Thin at the edges**: entrypoints orchestrate, domain modules decide, adapters perform IO.
4. **Operationally explicit**: deterministic tooling, obvious command paths, documented and typed configuration.
5. **Easy to reason about**: guard clauses, meaningful names, comments that explain intent and constraints.

## Non-Negotiables (Default)

Unless the user explicitly asks otherwise, treat these as MUST-level defaults:

1. **No runtime env reads in random application code.**
   - Load config once near startup, parse into a typed config object, inject downstream.
2. **No placeholder abstractions.**
   - "Class with one pass-through method" and speculative repository interfaces are usually rejected.
3. **No broad leaky surfaces by default.**
   - Keep exports narrow, enforce invariants with constructors/factories and domain types.
4. **No deeply nested control flow unless unavoidable.**
   - Prefer early returns and branch flattening.
5. **No generic/opaque error handling when domain context matters.**
   - Keep cause + context; prefer typed or structured error paths.
6. **Test real behaviour, not mocked choreography.**
   - Prefer real implementations where cheap, then fakes/in-memory adapters, then local services or testcontainers, then spies, and only narrow mocks for genuinely awkward external boundaries.
   - Heavy monkeypatching is usually design feedback: push side effects to the edges, inject dependencies explicitly, and keep the core behaviour real.
   - Do not patch the code under test just to make a test pass. Test the public behaviour and observable outcome instead.
7. **Changed behaviour gets a test.**
   - Every bug fix normally includes a regression test that fails before the fix and passes after.
   - Every new feature or flag normally includes a behaviour test covering the user-visible contract.
   - If a test is genuinely impractical, say why, perform the closest available verification, and do not claim the work is covered.
   - Tests are not ceremony, but if you change observable behaviour you owe the repo a guardrail. "Existing tests still pass" is not evidence for behaviour those tests never exercised.

## Testing and Mocking Defaults

See `references/testing-without-mock-theatre.md` for the full testing philosophy.

When writing or reviewing tests, default to these rules:

1. **Replace only true external boundaries.**
   - Databases, filesystems, networks, clocks, queues, hardware APIs, browser/runtime boundaries, and third-party services are fair seams.
   - Core domain logic and the thing under test should usually stay real.
2. **Prefer dependency injection over monkeypatching.**
   - Favour constructors, parameters, typed seams, and in-memory implementations over mutating module globals or import state mid-test.
3. **Never patch the code under test.**
   - Patching internals of the subject under test turns the test into an implementation lock-in exercise.
4. **Prefer observable outcomes over call choreography.**
   - Assert on returned values, persisted state, emitted domain events, rendered output, or other real effects.
   - Be suspicious of tests whose whole value is `assert_called_once_with(...)` on an internal collaborator.
5. **Keep test concerns out of production code.**
   - Reject test-only branches, test-only env vars, hidden global knobs, and "test mode" flags unless there is a strong operational reason.
6. **Bias toward deterministic, hermetic, parallel-safe tests.**
   - No shared global state, unbounded sleeps, real wall-clock assumptions, or ambient environment mutation without tight isolation.

## Maintaining Existing Code

Maintenance and feature work on an existing codebase has its own discipline, whether or not the codebase already follows this style.

1. **Prefer the smallest coherent change, not the smallest textual diff.**
   - "I only changed three lines" is not a substitute for judgement.
2. **Repair the local contract you touch.**
   - Fix anti-patterns that sit inside the same edited function/path when they directly affect correctness, testability, or the operator contract — env reads in loops, progress chatter polluting machine-readable stdout, stringly payloads you are already reshaping.
   - This is not cleanup; it is not leaving a known-bad seam in your own blast radius.
3. **Do not broaden into file-wide renovation.**
   - Code you are not touching stays untouched unless the requested change cannot be made safely without it. Legacy code often has accidental behaviours that broad cleanup will break.
4. **Match conventions when the codebase is healthy.**
   - If the repo already has typed models, a config loader, and seams, new code flows through them. Do not bolt special cases onto the entrypoint when a domain type or existing seam is the obvious home.
5. **Changed behaviour gets a test (non-negotiable 7 applies doubly here).**
   - A maintenance change with zero new tests is almost always incomplete. Regression test for the bug, behaviour test for the feature, in the existing suite's style.
   - Your summary must include a `New tests:` line naming the test functions you added, mapped to the behaviours they cover. A manual smoke check is corroboration, not a substitute.
   - If the existing suite is mock-theatre, do not imitate it for your new tests — write behaviour-shaped tests (real files via tmp dirs, real entrypoint invocation) and leave the old tests alone.
6. **Report verification status honestly.**
   - Lead your summary with what you ran and the result. If you could not run the checks, say **UNVERIFIED** prominently — do not bury it. A failing test is a blocker to report, never a footnote to leave behind.

## Language-Specific Defaults

The same philosophy applies across languages, but tactics differ.

### Rust

- Prefer iterator pipelines for straightforward transformations.
- Prefer typed errors over `String` errors for domain flows.
- Keep `main` thin; use `clap` derive-based CLI modelling.
- Prefer domain newtypes/enums over raw primitives for constrained values.
- Avoid excess `let mut`; mutate only where it pays for clarity/perf.

### Go

- Prefer simple, concrete code over heavyweight repository layering.
- Validate boundary values explicitly (zero values are common failure mode).
- Avoid `flag` for complex CLIs; use explicit command parsers like `kong` and subcommands.
- Prefer explicit dependency injection for testability, but avoid interface explosion.
- Handle errors with context; avoid ambiguous `errors.New("failed")`.

### Python

- Prefer typed models (for example Pydantic/dataclasses at boundaries) over `Dict[str, Any]` contracts.
- Keep side effects at edges; pure core transformations in dedicated functions.
- Use straightforward control flow and explicit invariants.
- Prefer meaningful exceptions with context over vague `ValueError("bad input")`.

### TypeScript

- Centralise config in one typed loader; avoid distributed `process.env` reads.
- Prefer explicit domain types/unions at boundaries.
- Avoid throwing raw strings.
- Keep CLIs and handlers as orchestration shells, not business-logic dumps.
- Create seams for external IO/time/randomness where tests benefit.

## Internal CLI and Operator Tooling Defaults

When the code is a CLI or internal operator tool, apply these additional defaults.

See `references/internal-cli-philosophy.md` for the full rationale and examples.

1. **Treat the CLI as a serious operator boundary.**
   - It is not a thin wrapper around random functions.
   - Its job is to make a messy system operable.
2. **Shape commands around operator tasks, not the source tree.**
   - Command paths should be guessable from the job to be done.
   - Repeated snippets and tribal-knowledge workflows often want a first-class subcommand.
3. **Keep entrypoints and handlers thin.**
   - Process-wide setup, parse and validate arguments, assemble dependencies, dispatch, render result.
   - Do not hide the system's main understanding inside the CLI shell.
4. **Parse loose inputs early into typed objects.**
   - Paths, URLs, request payloads, config, and option combinations should be normalised and validated at the boundary.
5. **Teach through help text.**
   - `--help` is part of the interface contract.
   - Encode invariants, examples, caveats, and adjacent command hints where the operator will actually look.
6. **Civilise awkward backends and protocols.**
   - Normalise weird shapes, reject bad combinations up front, and expose a task-shaped command instead of leaking raw API ceremony.
7. **Tell the truth.**
   - No fake flags, no silent fallbacks, no misleading success, no accepting malformed input just to fail later.
8. **Serve humans, scripts, and agents at the same time.**
   - Human-readable defaults are good.
   - Stable JSON or machine-readable output should exist where automation wants it.
   - Keep progress and chatter off structured stdout.

## Dimension Application Rules

Use this as a quick execution map while coding.

1. **Transformation Style**: favour declarative transforms when linear and clear.
2. **Control Flow Shape**: guard clauses first; flatten branch trees.
3. **Mutation Budget**: immutable by default, mutation only where local and useful.
4. **Error Semantics**: preserve cause + context; avoid generic failure labels.
5. **Boundary Contracts**: parse, then operate; avoid loosely typed pass-through payloads.
6. **Naming**: identifiers should encode domain intent, not implementation trivia.
7. **Abstraction Threshold**: extract only when the abstraction pressure gate is satisfied; for small modules (<150 LOC total), prefer fewer files.
8. **Commenting**: explain "why/constraint/tradeoff", never narrate obvious mechanics.
9. **Module Cohesion**: one module, one reason to change.
10. **Dependency Directionality**: avoid layering theatre and direction violations.
11. **Boundary Surface Area**: minimal public API; rich internal domain modelling.
12. **Cross-Cutting Placement**: keep logs/metrics/auth at deliberate seams.
13. **Testability**: inject unstable dependencies (clock, network, random, env).
14. **Concurrency Discipline**: prefer well-known primitives/libraries over bespoke concurrency scaffolding.
15. **Entry-Point Architecture**: thin CLI/service entrypoints that delegate.
16. **Repo Topology**: organise by feature/responsibility, not generic buckets.
17. **Config Strategy**: one typed config load path near startup.
18. **IO Isolation**: separate pure domain logic from transport/storage.
19. **Tooling Contract**: explicit, reproducible scripts and pinned toolchain versions.
20. **Evolution Posture**: migrations and deprecations where compatibility matters.

## Anti-Patterns to Reject by Default

Flag these unless a clear task-specific reason exists:

- `util`/`helpers` dumping grounds with unrelated concerns
- Deeply nested `if/else` trees where early returns would simplify
- Generic names (`x`, `data`, `thing`, `doStuff`) in domain code
- Runtime env access from request handlers/domain functions
- "Stringly typed" domain fields when constrained types are known
- Entry-point files containing domain/business logic
- CLI surfaces organised around package names instead of operator tasks
- Help text omitting invariants, examples, or dangerous constraints.
- Fake or placeholder flags that imply behaviour the tool does not implement
- Mixing machine-readable stdout with human progress noise
- Comments that duplicate the code line-by-line
- Hard-coded network/time dependencies in logic that should be testable
- Solving a generic nearby problem instead of the actual local problem
- Tests that assert mocked choreography rather than observable behaviour
- Heavy monkeypatching that papers over hidden dependencies instead of fixing the seam
- Patching the code under test or mutating import/module globals halfway through a test
- Test-only production branches, flags, env vars, or hidden knobs added just to make tests pass
- Speculative options, unused helpers, or "future-proofing" left behind
- Bypassing existing config/logging/tracing/auth/IO seams instead of using them
- Architecture nouns outnumbering domain nouns (`Service`, `Repository`, `Manager` before real pressure)
- Optional flags that make core workflow behaviour opt-in or create large untested alternate paths
- Mutable post-call inspection state instead of returned typed results (`last_result`, inspect-after-call patterns)
- Copying nearby bad patterns (utils dumps, scattered env reads) because they exist in the repo
- Greenfield file/LOC counts in slop territory per the size tripwires above

## Implementation Workflow (Agent)

When this skill is active, follow this sequence:

1. **Classify the change** across micro/meso/macro dimensions.
2. **Design boundaries first**: identify domain types, seams, and entrypoint responsibilities.
3. **Implement concretely** with minimal necessary abstraction.
4. **Reshape first-pass output as a draft**, not an artefact to preserve. Apply this default sequence until the code looks deliberately authored for this repository:
   1. count files and LOC — delete excess structure if over greenfield budget
   2. delete unjustified abstractions (apply the abstraction pressure gate)
   3. recover local domain names
   4. move validation to the correct boundary
   5. preserve cause and context in errors
   6. test the real seam, not its scaffolding
   7. confirm every remaining file has a reason to exist
5. **Run a style self-audit** using the checklist below before presenting.

Prefer surgical changes. Do not reformat, rename, repartition modules, or introduce new architecture unless it directly supports the requested change.

## Pre-Response Self-Audit Checklist

Before returning code, verify:

- Are boundaries typed and explicit?
- Is config loaded centrally and injected?
- Are entrypoints thin?
- Is control flow flattened where possible?
- Are names domain-meaningful?
- Are comments high-signal (why/constraints) rather than narration?
- Are abstractions justified by real complexity/reuse?
- Are IO/time/env dependencies isolated enough for testing?
- Are errors specific and context-bearing?
- Is the repo/module shape moving toward cohesive responsibility boundaries?
- For greenfield work: are file count and LOC within the size tripwires?
- Did every new abstraction pass the pressure gate (≥2 call sites, unstable boundary, domain invariant, or ownership need)?
- Does every behaviour change (bug fix, feature, flag) have a test that exercises it?
- Do any tests monkeypatch module globals where an injection seam exists (including seams you just built)?
- Did you run the checks, and does your summary state the result honestly (or UNVERIFIED)?

If two style goals conflict, choose the option that:

1. strengthens boundary correctness,
2. keeps execution model explicit,
3. reduces accidental complexity.

## Review Mode Guidance

When reviewing code, prioritise findings in this order:

1. Broken/weak boundaries (contracts, validation, domain typing)
2. Architecture drift (fat entrypoints, mixed responsibilities, leaky surfaces)
3. Testability regressions (hard-coded side effects, missing seams)
4. Error/context quality
5. Readability and naming quality

Keep feedback concrete and propose specific reshaping steps, not abstract style advice.
