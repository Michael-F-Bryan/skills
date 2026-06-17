# Testing without mock theatre

Use this reference when writing or reviewing tests in Michael's style.

## North star

Test real behaviour, not mocked choreography.

The thing under test should mostly stay real. Replace only true external boundaries, and prefer replacements that still behave honestly.

## Preferred replacement hierarchy

1. Real implementation when cheap and deterministic.
2. In-memory fake when replacing an external boundary.
3. Local service or testcontainer when behaviour matters.
4. Spy when you need to observe that a boundary was used.
5. Mock only when the dependency is genuinely awkward, slow, nondeterministic, or external.

Mocks are a narrow tool, not a design style.

## Seam preference

Prefer dependency injection over monkeypatching.

Good seam shape:

```python
service = Service(repo=InMemoryRepo(), clock=FakeClock(...))
```

Smell:

```python
monkeypatch.setattr(module, "repo", fake_repo)
```

Heavy monkeypatching usually means the production code was not designed with honest seams. The normal fix is better design: push side effects to the edges, pass dependencies explicitly, and keep the core logic pure or close to pure.

## Hard rules

### Never patch the code under test

Do not patch internals of the subject under test. That turns the test into an implementation lock-in exercise.

### Test outcomes, not choreography

Good tests prove:

- given this input or state,
- when this public behaviour runs,
- the observable outcome is correct.

Weak tests mostly prove:

- a private method was called,
- internal steps happened in a specific order,
- a mock saw a specific argument list,
- the implementation still matches the author's imagined choreography.

### Keep test concerns out of production code

Avoid:

- test-only branches
- test-only env vars
- production flags added purely to make testing easier
- special-casing test mode
- hidden global knobs
- patching imports halfway through a test

If testing needs these, treat that as design feedback.

## Determinism rules

Prefer tests that are hermetic and parallel-safe:

- no shared global state
- no real wall-clock assumptions
- no shared temp paths, ports, or schemas
- no dependency on test ordering
- no unbounded sleeps
- no ambient environment mutation unless tightly isolated

Rule of thumb: if two test runs would conflict, parallel execution probably will too.

## Architecture reading

When a test needs heavy mocking or monkeypatching, read it as evidence of one or more of these problems:

- hidden dependency
- global state
- hard-coded singleton, client, or session
- side effects buried too deep
- poor module boundary
- implementation coupled to runtime or environment
- design optimised for convenience rather than maintainability

The ideal test gives real confidence, is boring to read, and would still pass after a sensible refactor.
