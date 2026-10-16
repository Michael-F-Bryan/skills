---
name: code-like-michael
description: Use when designing, coding, testing, or reviewing code.
---

# Code Like Michael

Use this as a decision aid for code Michael would be willing to own, not a scorecard for making code look like his past projects. Apply it to coding, architecture, tests, verification, and review by default; explicit user instructions and the repository's real constraints take precedence. Start with a working simple design unless a known hard constraint already rules it out. Do not reproduce private interview examples in public code, docs, or this skill.

## Before changing code

Read the relevant implementation, consumers, tests, configuration, and repository instructions. For an existing codebase, find the smallest **coherent** change; nearby conventions are evidence, not permission to copy a bad seam. Identify the behaviour to change, its consumer, and what observation would disprove success. Skim a relevant labelled example only when a specific choice is uncertain; examples illustrate trade-offs rather than dictate structure.

## The decision loop

1. **Make the common path work simply.** Implement the actual task before building a framework for imagined tasks. A well-designed high-level API may hide complexity. Offer lower-level control when a real consumer needs it (for example streaming, resource limits, or missing backend capabilities), not merely because control sounds elegant.
2. **Name the present pressure for structure.** A helper earns its place when it encapsulates a coherent complexity or noticeably simplifies a caller, even with one call site. A module may emerge from mixed responsibilities, coupled test setup, a distinct consumer, or clearer project direction. A boundary type earns its place when it captures a meaningful concept or prevents likely misuse; a one-off internal operation may need only a test. Use the language's affordances rather than mechanically importing Rust patterns into Go or Python. A known hard constraint can justify early structure; otherwise let a working system evolve.
3. **Keep ownership and state understandable.** Prefer explicit inputs, clear lifetimes, early returns that narrow possible states, and local mutation where useful. Watch for globals, implicit timing/ordering, data inconsistencies, and edge-case hacks applied too far downstream. Separate business decisions from CLI setup, input parsing, and result/error presentation when that separation makes the flow easier to reason about. A handler may reasonably own presentation transforms; a domain module need not be artificially free of every adapter.
4. **Shape failures around caller action.** Expected failures are data; preserve useful cause and context, but do not invent fine-grained error types, redundant prechecks, multiple error channels, or recovery paths the caller cannot use. A parser or editor may accumulate diagnostics; a device driver should keep surfacing a real fault rather than silently clearing it. Programming bugs and violated invariants are different from expected domain failures. Prefer predictable, sufficiently diagnostic failure over opaque automatic repair. For persistent-state changes, consider testing migration directions and transactional rollback where supported; not every migration is reversible or transactional.
5. **Choose dependencies and compatibility by consequences.** Compare the effort and bugs of a sound homegrown implementation with a dependency's setup, portability, maintenance, and architectural intrusion. A contained package has a lower bar than a framework that takes over the application. Before changing a public contract, consider actual consumers and migration cost; internal or little-used APIs need not carry ceremonial compatibility layers.
6. **Test the behaviour at a useful boundary.** Keep the subject of the test real; replace awkward external dependencies with in-memory implementations or other honest seams when appropriate. Compiler-like pipelines may be clearest with disk fixtures and end-to-end analysis; data transformations may suit golden snapshots, whose diffs must be checked against expected behaviour. Do not create production hooks solely to satisfy a test, or mistake constructor tests and mock choreography for confidence. Test setup friction can signal coupling, but can also be inherent to the domain.
7. **Reshape the draft before delivery.** Look for patchwork branches, unnecessary files and options, misleading placeholders, duplicated mechanisms, and code that will immediately become someone else's debt. Do not renovate unrelated code for aesthetic consistency. Repair an adjacent bad seam when it affects the changed contract or its likely consequences justify the extra scope; otherwise ship the narrow coherent fix.

## Verification and reporting

Select evidence to match each material claim and its consumer. A focused regression and owning package suite are often useful; a browser, device, protocol peer, renderer, or generated-code consumer may be the real acceptance boundary. Broaden checks for material blast radius or repository gates, not ritual. Reuse valid evidence if the relevant state has not changed. If a test is impractical, give the reason and use the closest direct check; never imply coverage that was not obtained. Report what ran, what passed or failed, and the remaining limitation. A passing existing suite alone does not establish newly changed behaviour.

File/LOC counts and abstraction lists can alert you to sprawling small greenfield work, but are **not budgets, output requirements, or reasons to compress coherent code**. Ask instead whether every part has a present purpose and whether a simpler arrangement would remain understandable. The examples in `references/examples/greenfield-size-discipline.md` are comparative illustrations, not target shapes.

## Audience and documentation

- Put detailed API behaviour and runnable examples near the API; Rust doctests are particularly useful. Keep a README a concise landing page with purpose, installation, and pointers rather than an unchecked manual. Use comments for surprising constraints and trade-offs, not paraphrases of the code. A useful `AGENTS.md` can orient humans and agents to layout and validation commands; do not add one merely as ceremony.
- For a library, minimise setup imposed on every consumer. Avoid ambient mutable state and unsolicited stdout; document concurrency and error semantics honestly. A bottom-of-stack device driver should expose device capabilities and fault conditions needed by wrappers, even when its public surface is broader than a polished application façade.
- For an operator CLI, organise around tasks, make commands discoverable, reject misleading input and unsupported flags, and provide concise actionable diagnostics. Keep structured stdout free of progress chatter. Do not add flags, output formats, or auto-repair because they sound useful without a consumer.

## Review posture

Review concrete risks and observable consequences, assuming competence and good intent. Distinguish a defect from a taste preference; suggest a specific alternative where useful. If a review thread cycles through a couple of unproductive exchanges, prefer a synchronous conversation to prolonged nitpicking. Prioritise correctness, state/ownership, real-consumer evidence, and maintainability over conformity to this document. For an architecture review or a refactor whose main question is where complexity should live, consult [architecture review](references/architecture-review.md) for the deepening lens, without treating it as the whole review. Do not turn it into an extra step for ordinary coding.

## Calibration and limits

Michael's direct interview answers and corrections are stronger evidence of his intent than synthetic labelled snippets; current task requirements and repository constraints still govern the work. The 20 dimensions and scored examples in `references/` are prompts for noticing trade-offs, **not** independent requirements to maximise, weighted scores to optimise, or a mandate to copy an example's topology. A public unfinished repository shows one stage of evolution, not an endorsed greenfield template. When evidence is weak or preferences conflict, explain the consequential trade-off rather than asserting a personal rule.

Further references: `references/testing-without-mock-theatre.md` (testing), `references/architecture-review.md` (architecture review and deepening candidates), `references/internal-cli-philosophy.md` (CLIs), `references/dimensions.md` and `references/annotations-rubric.md` (historical calibration), and `references/examples/` (contextual examples). Consult only what the task needs.
