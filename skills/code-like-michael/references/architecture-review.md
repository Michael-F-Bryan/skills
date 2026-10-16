# Architecture review: finding and deepening shallow modules

Use this procedure to investigate architectural friction and propose useful changes. It adapts Matt Pocock's deep-module techniques; [the core skill](../SKILL.md) governs engineering judgement and [testing-without-mock-theatre.md](testing-without-mock-theatre.md) governs testing. See [architecture-sources.md](architecture-sources.md) for attribution and the licence.

## When to use this reference

Use it when the user asks for an architecture review, asks where structure is causing friction, or hands over a refactor whose main question is where complexity should live. Do not run it as a routine step of ordinary coding, and do not run it to justify renovation the task did not ask for.

This is one lens for architecture review, not its complete scope. Establish the system's material risks first, including state ownership, concurrency, failure propagation, dependency cycles and deployment constraints where relevant. Use deepening where caller burden or scattered responsibility contributes to those risks. A worthwhile recommendation need not introduce or deepen a module; adapt the procedure to the actual problem rather than forcing a deepening candidate.

Review alone does not authorise implementation. If the request already authorises implementation within this scope, proceed within that authority once a candidate is chosen; otherwise present the recommendation and wait for a decision. In neither case does a review authorise writing glossaries or decision records, opening tickets, or publishing anything outside the session.

## Vocabulary this reference adds

Use these terms when they sharpen a point, not as a mandatory dialect. Keep the project's domain names and the core skill's existing language, including "boundary".

- **Interface**: everything a caller must know to use a module correctly: signatures, invariants, ordering constraints, error modes, required configuration, and performance characteristics. Wider than a type signature.
- **Seam**: a place where behaviour can be substituted without editing the code at that place. Where the seam sits is a design decision separate from what sits behind it. A seam can be internal to a module (used by its own tests) without being part of the interface.
- **Depth**: the useful complexity a module hides relative to the burden it puts on a caller. A module is **deep** when a lot of behaviour sits behind a small interface and **shallow** when the interface is nearly as complex as the implementation. Depth is leverage at the interface, not a line-count ratio.
- **Locality**: the maintainer's share of depth. Change, bugs, knowledge and verification concentrate in one place instead of spreading across callers. The core skill's warning about edge-case hacks applied too far downstream is a locality failure.

Depth is useful encapsulation, not a reason to merge unrelated responsibilities or optimise a size ratio. A module's external interface need not be its only legitimate test surface.

## Procedure

### 1. Scope before you scan

Deepening pays off by making future change easier, so look first where change actually happens.

- If the user named a module, subsystem or pain point, take that scope and skip the inference below.
- Otherwise, read a good stretch of commit history (for example `git log --oneline --stat` over recent months) and note the files and areas that keep recurring. Let those pull attention first. If change is scattered with no hot spot, widen the net rather than inventing one.
- Read repository instructions, an existing domain glossary if the project has one, and any recorded design decisions that already exist (ADRs, design notes, `AGENTS.md`). Use the project's own names for its concepts when describing candidates. Do not create any of these files. A recorded decision is not re-litigated unless the friction you find is real enough to warrant reopening it, and then say so explicitly in the candidate.

Scoping is read-only. Do not change code while scanning.

### 2. Walk the code and note friction

Explore organically rather than applying a checklist mechanically. Prompts that reliably surface shallow structure:

- Where does understanding one concept require bouncing between several small modules?
- Where is a module's interface nearly as complicated as its implementation?
- Where were pure functions extracted for testability while the real bugs live in how they are called and sequenced?
- Where do tightly coupled modules leak details across their seams, so a change in one forces edits in the other?
- Which parts are untested, or only testable by reaching past their interface?

Apply the **deletion thought experiment** to anything that looks shallow. Imagine removing the module as a wrapper while keeping the behaviour it fronts, then ask two questions: what must each caller now know that it did not before, and where does the responsibility move? If callers need to know nothing new and nothing moves, the module was a pass-through. If every caller would have to absorb the same knowledge, the module was earning its keep. If the knowledge would land in one sensible place that does not yet exist, that place is a deepening candidate. Removing the behaviour itself is a different question (a product change, not a structural one) and is out of scope here.

Two cautions the core skill insists on:

- A forwarding layer may still own a meaningful contract: compatibility for real consumers, a policy decision, or presentation. Judge it by consequences for callers, not by how little code it contains.
- Consumer count is evidence, not a threshold. One real consumer can justify a helper or a seam; a dozen hypothetical consumers justify nothing. Do not import any rule of the form "N adapters make a seam real".

Lower-level control a real consumer needs (streaming, resource limits, device capabilities a wrapper must see) is not shallowness. Do not propose hiding it to make an interface look smaller.

### 3. Note each candidate's dependencies

For each candidate, note what the deepened module would depend on. The category is descriptive: it tells you which verification options are likely to be available, not which architecture to build. Choose the replacement by the claim the test must prove, as described under "Choosing a replacement" and "Architecture reading" in [testing-without-mock-theatre.md](testing-without-mock-theatre.md).

| Category | Examples | Possible verification approach |
| --- | --- | --- |
| In-process | pure computation, in-memory state, clocks or schedulers | test real behaviour directly where deterministic; substitute nondeterministic inputs or scheduling where the claim requires control |
| Local-substitutable | database with a local stand-in, in-memory filesystem, local service or container | the real thing where cheap and deterministic, otherwise an honest stand-in inside the test suite |
| Remote but owned | your own service across a network | a port with an in-memory implementation may suit behaviour tests; keep a check at the real transport for compatibility claims |
| True external | third-party services you do not control | an injected dependency with a narrow fake or mock may suit the subject's logic; keep the subject real and a provider-boundary check where the contract matters |

An in-memory implementation does not establish protocol or provider compatibility; when that is the claim, verify at the real boundary. Whether to introduce a port is a design judgement about ownership, lifetime control and meaningful encapsulation, not a count of implementations. Injecting a genuine dependency so tests can substitute it is legitimate; it is not the same as adding a test-mode branch, runtime flag or production method that exists only for a test.

### 4. Present candidates

Present candidates in the conversation or as plain text by default. Add a diagram or a written artefact when it genuinely helps the reader or the user asked for one, and keep it within the requested scope; no tickets, no files outside what was asked. For each candidate give:

- **Files or modules involved.**
- **Friction**: the observable consequence of the current shape (bouncing, duplicated fixes, untestable paths, leaked details), not an aesthetic complaint.
- **What would change**: a concrete plain-language description of the deepened module and what moves behind it. An illustrative sketch of the interface is welcome; present it as a sketch, and defer committing to a final interface until step 5 so the shape is not fixed before constraints are known.
- **Benefit**: stated as locality (where change would concentrate), leverage (what callers stop needing to know), and how tests would improve.
- **Cost and risk**: affected consumers, migration effort, blast radius, and anything a recorded decision already says.
- **Strength**: `Strong`, `Worth exploring`, or `Speculative`.

End with a **top recommendation**: the one candidate to tackle first and why. An honest review may find **no worthwhile candidate**; say so rather than manufacturing one. If implementation is not already authorised, ask which candidate, if any, the user wants to pursue, and wait. If it is, continue to step 5 with the top recommendation unless the user has said otherwise.

### 5. Design the chosen candidate

Resolve these questions before implementation. Surface consequential choices or unresolved constraints in the conversation; for a small, obvious change within existing authority, proceed and report the relevant reasoning with the result:

- the constraints any new interface must satisfy, including repository conventions that are genuine constraints;
- the dependencies and their categories from step 3;
- the shape of the deepened module and what sits behind the seam;
- which existing tests still describe real behaviour and which would become redundant.

**Design it twice when it matters.** For a consequential or uncertain interface choice, sketch materially different alternatives before committing to a design. Useful lenses: minimise what the common caller must learn without hiding needed capabilities; make the most common call trivial; accommodate genuinely different existing callers; or shape it around an injected cross-seam dependency. For each alternative show a caller example, what complexity it hides, and how dependencies, state, failures and lifetimes are handled. Compare depth, locality, seam placement and migration cost, then give a recommendation; a hybrid is allowed. Work in-session, or delegate independent alternatives when that adds value, without a fixed agent count. For a small or obvious change, one careful design is enough.

Two testability prompts from upstream, both consistent with the core skill when read as prompts: accept dependencies rather than constructing them inside the module, and prefer returning results over hidden side effects. Local mutation inside a module remains fine where it is the clearer implementation.

### 6. Tests across a deepening

Write new tests at the deepened module's interface, asserting observable outcomes. A good test here would still pass after a sensible internal refactor. A test that must change whenever the implementation changes may indicate implementation coupling; check whether it protects meaningful behaviour, pins an internal algorithm on purpose, or guards a necessary boundary before concluding it is testing past the interface.

Old tests on the shallow modules are not deleted automatically. Retire one only when the new interface tests demonstrably cover the behaviour it protected, and record the retirement as a visible, deliberate part of the change. Keep an old test that pins a specific past bug or a boundary the new tests do not reach. Full-pipeline disk fixtures and golden snapshots remain valid where the testing reference says they are.

### 7. Deliver as a normal change

Implementation follows the core skill unchanged: the smallest coherent change, adjacent repairs only where they affect the changed contract, verification matched to each material claim, and an honest report of what ran and what remains unverified.
