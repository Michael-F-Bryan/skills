---
name: code-like-michael
description: Write, refactor, review, and shape repositories in Michael's style. Use when the user wants code or repo structure that feels like Michael wrote it, with explicit boundaries, thin composition roots, typed contracts, pragmatic framework use at hard edges, late handwritten abstraction, early code generation for mechanical repetition, and strong drift-aware verification.
---

# Code Like Michael

Treat this skill as binding unless the repository already has stronger local conventions.

The goal is not "clean code" in the abstract. The goal is to produce code and repo shape that make ownership, execution order, contracts, and operational behaviour obvious.

## Non-Negotiables

Always prefer:
- visible composition roots
- responsibility-shaped modules, crates, or packages
- typed contracts at important boundaries
- local wrappers only where semantics begin
- handwritten abstraction only after the seam is stable
- generation and drift checks for mechanical repetition
- realistic seam tests over mock theatre

Do not optimise for:
- abstract symmetry
- service/repository scaffolding by default
- purity facades over real platform boundaries
- deduplication before semantic sameness is proven
- hiding unfinished work behind generic abstractions

## Agent Default

If you are unsure what Michael would do, choose the option that:

1. keeps the top-level flow easier to read
2. makes the boundary contract more explicit
3. avoids introducing a new abstraction layer
4. tests the real seam that can fail
5. makes docs, schemas, diagnostics, or generated output harder to drift

## Repo-Shaping Rules

Use these defaults when creating or restructuring a repository:

- Start compact, but split early when there are distinct execution modes, ownership boundaries, or tooling surfaces.
- Keep one obvious composition root per executable surface: `main`, `run`, `serve`, CLI command, worker bootstrap, or router setup.
- Separate reusable core from shells early.
- Add a dedicated repo-tooling surface once generation, release, docs, or compatibility workflows exist. In Rust this often means `xtask`; in app repos it may mean `tools/`, `scripts/`, or a dedicated package.
- Keep apps, libs, infra, generated contracts, and docs legible as separate concerns inside one repo when they belong to one delivery unit.

Avoid:
- one giant package mixing runtime, release, codegen, tests, and infra concerns
- microservice-style fragmentation before there are real responsibility boundaries
- repo shapes named after patterns instead of responsibilities

For repo-level guidance, read [references/repo-shaping.md](references/repo-shaping.md).

## Boundary Rule

Choose strictness by boundary type, not by slogan.

- Fail early at integrity boundaries: config, auth, IDs, request shape, transport status, schema input, unsafe defaults.
- Continue with structure when downstream diagnostics are the product: parsers, compilers, analysis pipelines, validation/reporting flows.

Any tolerance should be explicit in types, policy, or API shape. Do not rely on silent best effort.

## Code-Shaping Rules

Prefer:
- thin orchestration at the top
- medium-sized flow functions when they make execution order obvious
- smaller helpers for detailed rules
- stage-shaped or boundary-shaped modules
- explicit structs, enums, and named boundary types
- stable, contextual, lowercase errors at meaningful boundaries

Avoid:
- deep constructor chains that hide startup order
- generic `utils`, `common`, `manager`, or `processor` modules
- reflection-heavy or magical conversion code
- framework or protocol types leaking inward once local semantics begin

## Abstraction Threshold

Do not introduce a handwritten abstraction until one of these is true:

- the repeated shape is semantically identical
- the concern is globally cross-cutting
- the boundary genuinely varies
- lifecycle or concurrency ownership needs a seam

Do introduce generation early when repetition is mechanical:

- grammar-driven syntax trees
- schema-driven models
- generated diagnostics or code tables
- API contracts and clients

Default rule:
- tolerate the first duplication
- inspect the second
- abstract on the third only if the behaviour is truly the same

## Framework, Dependencies, And DI

Michael is not anti-framework. He is anti-fake-boundary.

Use frameworks, code generators, and managed platforms directly when they are the honest outer boundary:
- routers
- GraphQL
- SQL/query generation
- OpenAPI
- Temporal/workflow engines
- Terraform
- managed auth/storage platforms

Wrap them only where local policy or semantics begin.

Prefer:
- explicit parameter passing
- builders
- tiny interfaces at IO seams
- focused dependencies with a clear job

Avoid:
- DI containers
- deep trait graphs
- repository/service layers with no real second implementation
- dependency sprawl that adds complexity without leverage

## Contracts, Docs, And CI

Treat these as product surfaces:
- generated code
- schemas
- diagnostics catalogues
- user-facing docs
- release metadata
- DB policies and migrations

Default moves:
- commit important contract artefacts when the repo expects them
- add drift checks for anything humans would otherwise forget to regenerate
- keep README concise and practical
- add architecture/ADR/spec docs when decisions are durable or externally significant
- build CI around fast feedback: build, tests, lint/format, and regeneration/drift checks first
- add docs publishing, release automation, or deploy steps when the repo has real consumers or a live service

## Testing Rule

Bias toward strong verification, not ritualised TDD.

Prefer:
- request-path tests
- fixture tests
- parser or snapshot tests
- DB/container/integration tests
- corpus tests
- generated-artefact drift checks

Use mocks or tiny fakes only when the seam is already real and the full boundary is too expensive.

Do not invent an interface just so a unit test can exist.

## Review Triggers

The result is off-style if:

- the repo shape hides clear ownership boundaries
- the main flow is hard to recover without tracing multiple abstractions
- a boundary contract is implicit when it should be typed, schematised, generated, or policy-backed
- validation is buried deep in domain logic
- a shared helper deduplicates code that is still semantically different
- a framework facade exists only for stylistic purity
- generated or documented output can drift silently
- tests mostly prove mocked choreography instead of real behaviour

## Delivery Checklist

Before returning code, check:

- [ ] Is the repo or module shape aligned to real responsibilities?
- [ ] Is execution order obvious from one composition root per executable surface?
- [ ] Are important boundaries expressed in types, schemas, generated artefacts, or policy?
- [ ] Is validation happening at the correct edge for this boundary type?
- [ ] If bad input is tolerated, is that because richer downstream diagnostics are the product?
- [ ] Did I avoid introducing a new abstraction layer unless the seam is stable?
- [ ] Did I keep frameworks visible at the edge and stop them from defining the core?
- [ ] Do the tests exercise a real seam, corpus, fixture, or drift surface?
- [ ] Can docs, diagnostics, schemas, or generated code drift without a failing check?

## Additional Resources

- For concrete "write this instead of that" examples, read [references/write-this-not-that.md](references/write-this-not-that.md)
- For boundary and abstraction choices, read [references/boundary-playbook.md](references/boundary-playbook.md)
- For repo topology, docs, CI, dependencies, and rollout defaults, read [references/repo-shaping.md](references/repo-shaping.md)
