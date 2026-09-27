# Testing without mock theatre

Use this reference when writing or reviewing tests in Michael's style.

## North star

Test real behaviour, not mocked choreography.

The thing under test should mostly stay real. Replace only true external boundaries, and prefer replacements that still behave honestly.

## Choosing a replacement

Use the real implementation when cheap and deterministic. For an external boundary, an in-memory implementation, local service, or testcontainer can make the relevant behaviour observable; a narrow mock or spy can be useful where the real dependency is awkward. Choose by the claim the test needs to prove, not by a fixed hierarchy.

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

Heavy monkeypatching can reveal a hidden dependency, but not every instance justifies a production refactor. Keep the change proportional to the consumer risk and the scope of the task.

## Testing traps

### Avoid patching the behaviour under test

Patching the behaviour being asserted makes a test circular. Patching a narrow external call reached by the subject may be appropriate when it leaves the actual logic under test intact; prefer an honest seam when one is useful outside the test.

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

If testing needs these, ask whether the production contract needs a better seam; do not add test-only hooks just to satisfy a test.

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

The ideal test gives real confidence and would still pass after a sensible refactor. Compiler pipelines can warrant full-pipeline disk fixtures; functional transformations can warrant golden snapshots. Review a changed snapshot against the expected behaviour rather than accepting it mechanically. Test setup cost can be intrinsic to a complex domain, not necessarily a design defect.
