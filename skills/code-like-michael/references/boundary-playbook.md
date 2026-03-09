# Boundary Playbook

Use this when deciding module splits, validation placement, abstraction level, and test shape.

## 1. Classify The Boundary First

Do not write code until you know which boundary you are dealing with.

### Integrity Boundary

Examples:
- config file
- CLI args
- auth claims
- request JSON
- path params
- IDs
- transport status
- schema input

Default move:
- validate immediately
- return a specific boundary error
- reject dangerous or ambiguous defaults early
- do not push this deeper into domain logic

### Diagnostic Boundary

Examples:
- parser
- compiler
- linter
- static analysis pass
- document validation pipeline

Default move:
- preserve enough structure to continue
- accumulate diagnostics
- stop only when continued execution would destroy diagnostic value

### Hard Framework Boundary

Examples:
- router
- GraphQL resolver
- SQL/query generator
- OpenAPI generator
- Temporal workflow
- Terraform
- managed auth or storage platform

Default move:
- use the tool directly at the edge
- add a local wrapper only when semantics or policy diverge
- do not build a purity facade that only renames the tool

## 2. Shape The Module Around The Boundary

Prefer this shape:

```text
main/run/serve
-> boundary decoding and setup
-> focused domain or analysis functions
-> boundary rendering / persistence / transport mapping
```

Good signs:
- the happy path is visible from one file
- each package owns one boundary or one stage
- helper functions make rules clearer, not more abstract

Bad signs:
- you need to jump across five files to understand execution order
- packages are named after patterns instead of responsibilities
- orchestration is hidden in constructors, registries, or interfaces

## 3. Decide Whether To Wrap

Wrap the boundary when:
- third-party types would leak awkward semantics inward
- you need stable serialisation, hashing, equality, or policy
- you need contextual error mapping or validation
- the seam is small and meaningful enough to name

Do not wrap when:
- the wrapper only renames the framework
- the platform already is the honest boundary
- the wrapped API is simpler than the facade you are about to invent

Write this:
- `decodeCreateUserRequest()`
- `RequestID`
- `HashedRegex`
- `Strictness`
- `writeServiceError()`

Not this:
- `PlatformAdapterFactory`
- `FrameworkBridge`
- `GenericTransportService`

## 4. Decide Whether To Abstract

Keep paths separate when:
- the policies differ
- the names differ because the meaning differs
- one path is likely to evolve differently
- the only benefit is saving a few lines

Centralise when:
- the repeated logic is semantically identical
- the concern is globally cross-cutting
- lifecycle ownership is shared
- the repetition is mechanical enough for generation

Shortcut:
- if two functions only look similar because both decode JSON, do not unify them yet
- if three commands all need the same request ID, shutdown, or tracing wiring, centralise it
- if the repeated shape comes from a grammar, schema, or protocol, generate it

## 5. Decide How Strict To Be

Use this rule:
- strict at ingress
- contextual in the core

Meaning:
- reject malformed config/auth/request state early
- keep going in analysis-heavy code when better diagnostics are the product
- make any leniency explicit in API shape, policy, or type names

Avoid:
- silent best-effort parsing at important machine boundaries
- applying one error strategy everywhere in the repo

## 6. Pick The Test Shape

Choose the cheapest real seam that proves behaviour.

Prefer:
- fixture tests for file/content-driven workflows
- request-path tests for handlers
- snapshot tests for structured output or diagnostics
- DB/container tests for persistence and migration boundaries
- workflow harnesses when the framework is the real orchestration seam
- drift tests for generated code, docs, schemas, and diagnostics catalogues

Avoid:
- mocks for boundaries that are already cheap to exercise
- tests that only prove call order
- interfaces invented just so a unit test can exist

## 7. Comment Only For Meaning

Good comment targets:
- invariants
- trade-offs
- unusual failure policy
- why a wrapper exists
- why this path fails fast or keeps going

Bad comment targets:
- line-by-line narration
- restating types or control flow

## 8. Pre-Return Questions

Ask before returning code:

- Is the flow obvious from one composition root?
- Did I shape modules around real boundaries rather than patterns?
- Did I validate at the right boundary for this kind of problem?
- Did I keep third-party types out of local logic once local semantics started?
- Did I avoid introducing an abstraction whose only job is deduplication?
- Did I test a real seam instead of a fabricated one?
- Can generated or derived output drift without a failing check?
