# Repo Shaping

Use this when creating a new repo, splitting an existing one, or deciding where new code belongs.

## Default Stance: Modular Monolith

Prefer one delivery unit with clear internal boundaries. Split into separate services or repos only when execution mode, ownership, lifecycle, or operational boundary makes it necessary. Do not over-split into many packages/crates/apps just because boundaries are visible—keep them visible inside one unit until the split is justified.

## Default Topology

Choose the smallest repo shape that still makes real boundaries obvious.

### Small Utility

Prefer:

```text
src/ or crates/core/
cli/ or src/bin/
tests/
xtask/ or tools/
```

Use this when:
- there is one delivery surface
- the core logic is reusable
- release, docs, or generation workflow already exists

Avoid:
- putting release/codegen/doc tooling into the same module as product logic

### Workspace

Prefer:

```text
crates/
  core/
  cli/
  codegen/
  testing/
  xtask/
integration-tests/
```

Use this when:
- there are multiple execution modes
- there is code generation
- CLI/editor/server/test harnesses have different dependencies
- contributor workflows differ by area

Avoid:
- one giant core crate plus miscellaneous modules for everything else

### App Monorepo

Prefer:

```text
apps/
libs/
infra/
docs/ or generated-contracts/
```

Use this when:
- backend, worker, frontend, infra, and generated contracts are one delivery unit
- shared libraries are real and local
- operational tooling belongs with the product

Avoid:
- flattening all code into `internal/`
- splitting into many repos before boundaries are stable

## Composition Roots

Every executable surface should have one obvious entrypoint:
- `main`
- `run`
- `serve`
- CLI command `Run()`
- worker bootstrap

That file should:
- load config
- assemble dependencies
- start lifecycle and telemetry wiring
- hand off quickly

That file should not:
- hide startup inside a container
- bury lifecycle order in constructors
- implement business rules inline

## Docs Default

Always provide:
- a concise `README.md`
- enough setup or usage detail for a new contributor or operator

Add architecture or ADR docs when:
- the repo has durable structural choices
- there are multiple plausible designs
- the project exposes public contracts
- the repo is likely to have more than one contributor over time

Do not chase markdown volume.
Do document:
- boundaries
- workflows
- dangerous defaults
- sources of truth
- regeneration steps if they are not automated

## CI Default

The base pipeline should usually prove:
- build
- tests
- lint/format
- regeneration or drift checks

Add when justified:
- docs publishing
- release automation
- deploy pipelines
- compatibility or corpus runs
- cross-platform jobs

Optimise for fast feedback.
Avoid CI that only proves compilation while contracts can still drift.

## Dependency Posture

Prefer dependencies that do one clear job:
- CLI parsing
- tracing/logging
- schema generation
- query/code generation
- parser infrastructure
- HTTP clients

Be suspicious of:
- dependency stacks that force broad app architecture
- feature-flag complexity that leaks everywhere
- native-link churn with weak payoff

Michael is willing to take on heavier dependencies when they buy obvious leverage at a real boundary.

## DI And Wiring

Prefer:
- constructors
- plain config structs
- builders
- tiny interfaces at IO seams

Avoid:
- service locators
- DI containers
- trait/interface graphs created before a real second implementation exists

## Codegen And Sources Of Truth

If a shape is mechanical, promote its source of truth:
- grammar file
- schema
- YAML table
- SQL policy
- API contract

Then:
- generate the derived files
- check them in if the repo expects it
- add a drift check

Do not hand-maintain repeated mechanical code across packages.

## Production-Leaning Defaults

Even early-stage repos should usually have:
- explicit boundaries
- basic CI
- typed contracts
- visible incomplete areas

It is acceptable to leave:
- TODOs
- ignored tests
- manual steps

But only when:
- the boundary shape is already clear
- the incompleteness is visible
- the repo does not pretend the feature is finished

## Smell Test

The repo shape is probably wrong if:
- one package owns runtime, release, docs, codegen, and test harness concerns
- startup order is only recoverable by reading constructors
- generated artefacts have no reproducible source of truth
- CI cannot catch stale docs, schemas, or generated code
- there is a service/repository layer without real variation pressure
