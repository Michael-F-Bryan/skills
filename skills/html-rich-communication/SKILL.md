---
name: html-rich-communication
description: Build readable HTML explanations for human recipients.
---

# HTML Rich Communication

Own explanatory structure, rendering and the recipient’s reading experience. `voice-michael` owns prose voice; a publishing skill/package owns publication mechanics. Use `michael-brand-pack` only for personal sites/tools or explicit Michael branding, not ordinary HTML.

## Shape the explanation

1. Identify the reader, their existing context and the question or decision this page should help with. Ask only if a missing audience, privacy boundary or purpose would materially change the result.
2. Reuse established source material; research again only for missing or stale claims. Choose a spine: a worked scenario for a mechanism, a decision for a brief, a finding for a report. Introduce components when the scenario reaches them rather than opening every explainer with architecture.
3. Put the answer and orientation early. Use headings that expose the argument. Keep useful detail; disclose or link lookup material when it interrupts reading. Word counts, section counts and elapsed time are heuristics, not acceptance gates.
4. Distinguish facts, judgement and uncertainty at the point of use. Label prominent numbers as measured, default, target, estimate or assumption, with source and material caveat. A polished layout must not make an unvalidated default look measured.

## Render the smallest useful surface

Static semantic HTML with inline CSS, SVG and small JavaScript is normally enough. Start from [fast-explainer.html](templates/fast-explainer.html) if useful; remove empty sections. Use native disclosure where it helps, not a dashboard frame for every document.

Label units and caveats near the thing they qualify. Preserve meaningful reading order, contrast, keyboard focus, text alternatives and non-colour status labels. Make phone-width reading deliberate rather than shrinking a desktop table. Respect the destination’s existing identity.

For stateful interfaces, define export fields, selection, ordering and whether material filter/sort/tag state is included. Inspect the actual export against the visible interface. Use [implementation routing](references/implementation-routing.md) only when state or dependencies justify more machinery; [chart routing](references/chart-routing.md) when a visual is useful.

## Verify the deliverable

Serve locally and inspect desktop and phone-width rendering. Check the opening answer, reading order, overflow, links, console errors and controls. Exercise keyboard use and copy/export where present. Inspect emitted HTML when a bundler transforms the source. Verify print if needed. Repair material failures and recheck the affected surface; do not limit repair to an arbitrary pass count.

Recipient accessibility includes access to sources and the delivered page, not only local screenshots. See [review and verification](references/review-and-verification.md) for richer packs. Use [content disposition](references/content-disposition.md) and [design decisions](references/design-decisions.md) only when useful; no mandatory ledgers.

## Publication boundary

Claude Artifacts is Michael’s default sharing destination. Use the current publisher skill/package (for example `claude-artifact-publishing`) and verify the exact published target and recipient access before claiming delivery. Do not copy publishing mechanics here.

A blocked publisher is not permission to create a Gist, Cloudflare deployment or another host. Report the blocker and retain the local artefact; obtain explicit authorisation for another destination. Link-only hosting does not make private material safe.

## Stop

Stop when the reader’s question is answered, the delivered surface is usable, material claims are grounded and requested delivery is verified. Report remaining access/rendering blockers honestly; a local file is not a verified shareable link.
