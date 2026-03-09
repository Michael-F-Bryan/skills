# Boundary Playbook

Use this playbook when deciding module splits, validation placement, abstraction level, and test shape.

## 1. Classify The Boundary

Pick the closest match first.

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
- do not push this deeper into domain code

### Diagnostic Boundary

Examples:
- parser
- compiler
- linter
- static analysis pass
- document or content validation pipeline

Default move:
- preserve enough structure to continue
- accumulate diagnostics
- stop only when continuing would destroy diagnostic value

### Hard Framework Boundary

Examples:
- router
- GraphQL resolver
- SQL/query generator
- OpenAPI generator
- Terraform
- managed auth platform

Default move:
- use the framework directly at the edge
- add a local wrapper only when semantics or policy diverge
- avoid purity facades that just rename the tool

## 2. Choose The Module Split

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
- orchestration is hidden in constructors and interfaces

## 3. Decide Whether To Wrap

Wrap the boundary when:
- third-party types would leak awkward semantics inward
- you need stable serialisation, hashing, or equality rules
- the boundary needs local policy, error mapping, or validation
- the seam is small and meaningful enough to name directly

Do not wrap when:
- the wrapper only renames the framework
- the platform already is the boundary
- the wrapped API is simpler than the facade you are about to invent

### Rule Of Thumb

Write this:
- `decodeCreateUserRequest()`
- `RequestID`
- `HashedRegex`
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
- the repetition is mechanical enough for generation

### Shortcut

If two functions only look similar because both happen to decode JSON, do not unify them yet.

If three packages all need the same request ID propagation or shutdown wiring, centralise it.

## 5. Pick The Test Shape

Choose the cheapest real seam that proves behaviour.

### Prefer

- fixture tests for file/content-driven workflows
- request-path tests for handlers
- snapshot tests for structured output or diagnostics
- DB/container tests for query or migration boundaries
- drift tests for generated code, docs, schemas, and diagnostics catalogues

### Avoid

- mocks for boundaries that are already cheap to exercise
- tests that only prove call order
- interfaces invented just so a unit test can exist

## 6. Comment Only For Meaning

Good comment targets:
- invariants
- trade-offs
- unusual failure policy
- why a wrapper exists
- why this path fails fast or keeps going

Bad comment targets:
- line-by-line narration
- restating types or control flow

## 7. Pre-Return Questions

Ask before returning code:

- Is the flow obvious from one composition root?
- Did I validate at the right boundary for this kind of problem?
- Did I keep third-party types out of local logic once local semantics started?
- Did I avoid introducing an abstraction whose only job is deduplication?
- Did I test a real seam instead of a fabricated one?
- Can generated or derived output drift without a failing check?
