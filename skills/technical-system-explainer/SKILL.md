---
name: technical-system-explainer
description: Use when an engineering reader needs to understand how a system, protocol, component boundary, or technical method works.
---

# Technical System Explainer

## Default shape

Teach one useful mental model through one concrete path. Do not turn an explainer into a complete reference manual.

1. State the primary question in one sentence.
2. Give the short answer immediately.
3. Walk one representative scenario from start to finish.
4. Introduce boundaries, messages, states, or components at the moment the scenario crosses them.
5. Separate acceptance, internal state, and physical outcome when they prove different things.
6. Close with the few constraints or unresolved questions that materially change interpretation.

For HTML delivery, use `html-rich-communication`; its ten-minute lane owns page structure, verification, and publishing.

## Source discipline

If a grounded explanation already exists in the conversation or working notes, use it. Do not repeat its research phase.

When facts are missing, inspect the smallest authoritative source slice that resolves them—normally one project source and up to two canonical external sources. Expand only when sources disagree or a safety-critical claim remains uncertain.

Use project vocabulary. Distinguish standard protocol behaviour from the chosen implementation and from the current experiment's evidence.

## Bounds

Default to 4–6 sections and 900–1,500 words. Prefer:

- one mental model;
- one worked path or sequence;
- one boundary/contract view where it earns its place;
- one constraints section; and
- a short source trail.

Move catalogues, exhaustive command lists, timing matrices, component maps, roadmaps, and failure analysis to disclosure or a separate reference unless the user explicitly asks for them.

Architecture-first is not the default. Use it only when the reader already understands the workflow and explicitly needs topology, interfaces, or component ownership.

## Failure test

If removing a section would not stop the reader answering the primary question, remove it. Useful material in the wrong document is still wrong.
