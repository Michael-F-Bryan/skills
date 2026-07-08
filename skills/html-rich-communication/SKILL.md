---
name: html-rich-communication
description: >-
  Use when creating rich communication artefacts: HTML pages, visual briefs,
  explainers, decision memos, design reviews, PR/review aids, reports,
  dashboards, prototypes, decks, or custom editing interfaces that help a human
  inspect, understand, compare, decide, review, operate, learn, or export edits.
  Use when a user asks for an HTML artefact, polished page, interactive report,
  visual explanation, or shareable browser document.
---

# HTML Rich Communication

## Core principle

Rich artefacts help a specific reader do a specific cognitive job. HTML is useful because it keeps humans in the loop with dense, visual, shareable, and sometimes two-way communication. It is not a licence to make weak thinking look finished.

Default to Markdown when the answer is short, linear, and easiest to edit. Use HTML or another rich surface when understanding depends on layout, comparison, diagrams, interaction, review focus, progressive disclosure, or export. Treat the first screen as a working surface: it should orient, help choose, demonstrate, or produce output — not duplicate navigation.

## Non-negotiables

1. **No polished build before a communication contract.** If you cannot state the reader, question, action, trust blockers, and boundaries, you are not ready to design the surface.
2. **No final-looking artefact before first feedback** for ambiguous, high-stakes, or audience-sensitive work. Time pressure is not a waiver: “just make it polished”, “don’t overthink it”, “send it today”, and “show the team in 30 minutes” still require a compressed contract and first-feedback unless the user explicitly accepts final-only after you state the risk.
3. **No React by default.** Static single-file HTML is the default rich lane. Use React only when stateful interaction, complex components, charts, reuse, or maintainability justify it.
4. **No mode contamination.** User-guide material does not dominate design reviews; reference tables do not masquerade as explanation; dashboards do not replace decisions.
5. **No prominent number without provenance.** Classify as measured, code default, config default, inferred, requirement, target, forecast, assumption, or promise.
6. **No repeated caveat boxes.** Every important caveat/risk/non-goal has one canonical home; other sections reference it tersely.
7. **No completion claim without verification** appropriate to the lane and reader job.
8. **No stateful interaction without export.** If the reader manipulates state — sorting, tagging, tuning, editing, filtering, or selecting — provide a copy/export path and inspect the exported output during verification.

## Workflow

| Stage | Output | Purpose |
|---|---|---|
| 1. Communication contract | Contract block in working notes or first-feedback file | Lock reader, job, question, action, trust, boundaries |
| 2. Mode routing | Selected artefact mode(s) | Pick shape before writing or building |
| 3. Source slice | Source notes, parked material | Use only material needed for this reader job |
| 4. Critique-first pass | Outline critique / hard questions | Attack framing before polish |
| 5. First-feedback artefact | `first-feedback.md` or rough static HTML | Let human/AI reject structure cheaply |
| 6. Calibration ledger | `feedback-ledger.md` when feedback exists | Map comments to fix/move/cut/reject |
| 7. Content + visual plan | Brief, disposition table, visual plan | Decide visible/disclosed/linked/cut content |
| 8. Implementation lane | Markdown, static HTML, React, deck, or editor | Build only the surface the job needs |
| 9. Verification | Review evidence | Check function and audience fit |
| 10. Share | Local file or secret gist | Deliver with privacy posture intact |

Keep working artefacts under `_working/<topic>/` and confirm `_working/` is gitignored before writing.

## 1. Communication contract

Write this before implementation:

```markdown
## Communication contract

- Reader:
- Reader mode: decide / review / understand / operate / learn / compare / explore / edit-export
- Primary question the first screen must answer:
- Secondary questions:
- Action after reading:
- What must be believed/trusted:
- What must not be implied:
- Boundaries / non-goals likely to matter:
- Content that belongs elsewhere:
- Evidence available:
- Evidence missing:
- Privacy posture:
```

Use `references/communication-contract.md` for the full contract, reader gap model, and critique prompts.

## 2. Mode router

Choose the mode that matches the reader job, not the user's first noun. “Polished HTML” is not a mode; choose the reader job first, then decide whether the first output should be rough or final. If the reader's job is to decide, approve, fund, defer, or stop, do not lead with dashboard language; lead with the decision brief and push dashboard views to appendix only.

| Mode | Use when | Default shape |
|---|---|---|
| Decision brief | Reader must approve, choose, fund, defer, or stop | BLUF → recommendation → options → evidence → risks → decision block |
| Design review | Reader must critique architecture/design | context → goals/non-goals → system shape → contracts → decisions/trade-offs → risks/open questions |
| Technical explainer | Reader must understand how something works | mental model → path/diagram → annotated snippets → gotchas → FAQ |
| User guide/operator doc | Reader must perform a task | prerequisites → steps → expected results → troubleshooting → doc tests |
| Reference/pathfinder | Reader must look up facts or find the right page | indexed tables/cards → labels → links → examples |
| Report/status/incident | Reader must absorb state and next action | headline → status/timeline → evidence → owners → follow-ups |
| Code review/PR aid | Reader must review code safely | change summary → risk map → annotated diffs/modules → tests → focus areas |
| Exploration fan-out | Reader is choosing direction | side-by-side options → trade-offs → selection prompt |
| Prototype/design sandbox | Reader must feel or tune interaction | live example → controls → notes → copy/export selected params |
| Custom editing interface | Reader manipulates data then returns it | purpose-built UI → constraints/warnings → copy/export output |
| Deck | Reader needs meeting narrative | section slides → reader cues → appendix |
| Dashboard/tool | Reader needs ongoing monitoring/exploration | filters/state → key metrics → drilldowns → export |

Details and mode-specific checks: `references/artefact-modes.md`. First-screen and hero patterns: `references/html-effectiveness-patterns.md`.

## 3. Source slice and content disposition

Do not pour all source material into the artefact. For each major content block, assign one fate: core, supporting evidence, visible caveat, disclosure, appendix, linked separate artefact, or cut.

A useful section in the wrong artefact is still wrong. See `references/content-disposition.md`.

## 4. First-feedback loop

For ambiguous or high-stakes artefacts, create a rough first-feedback artefact before polished HTML. It should be easy to disagree with.

Minimum contents: BLUF, reader model, assumptions ledger, anticipated hard questions, outline critique, proposed section order, content disposition, design-decision skeleton, metric provenance, evidence gaps, and reviewer prompts.

Use `templates/first-feedback.md`; details in `references/first-feedback-loop.md`.

## 5. Design decisions, risks, and metrics

Use design decisions instead of defensive “why it is built this way” sections:

```markdown
### Decision: <plain name>

- Selected direction:
- Why:
- Alternatives considered:
- What this buys us:
- Accepted risk / trade-off:
- Validation state:
- Revisit trigger:
```

Prominent numbers need provenance: type, source, validation state, implication, and visual treatment allowed. See `references/design-decisions.md`.

## 6. Multi-artefact workflows

For exploration, planning, implementation handoff, and review, prefer a small linked set of HTML artefacts when one page would blur jobs: exploration board → selected direction → implementation plan → verification/review aid → handoff index. See `references/html-effectiveness-patterns.md`.

## 7. Implementation router

| Lane | Use when | Required output |
|---|---|---|
| Markdown | Short, linear, editable, or first-feedback draft | `.md` file and read-through check |
| Static HTML | Shareable, visual, mostly read-only, light inline JS/SVG | self-contained `.html` served and browser-checked |
| React app | Complex state, shadcn components, charts, reuse, heavy interaction | `app/` source plus bundled `final/bundle.html` |
| Deck HTML | Meeting/sequential presentation | keyboard-nav HTML, first-slide answer, appendix |
| Custom editor | Human edits/sorts/tunes and exports result | export contract, controls exercised, export copied and inspected |

Static HTML is allowed and often preferred. The old React pipeline remains available for the React lane: `scripts/init-artifact.sh`, then `scripts/bundle-artifact.sh`. See `references/implementation-routing.md`.

## Brand and voice

- If a visual brand/design skill is attached, read it and its rich-HTML/channel reference before choosing colours, typography, or motifs.
- If `michael-brand-pack` applies, use warm light document defaults for reports/review docs unless the artefact is a tool/dashboard/demo or the user explicitly accepts the trade-off.
- If a voice/author-style skill is attached, use it for tone and content structure.
- Do not invent brand tokens or voice rules when those skills exist.

## Verification

Verification has two layers:

1. **Functional delivery:** links, anchors, controls, build/bundle, export buttons, no external runtime dependencies, responsive layout, accessibility basics.
2. **Audience fit / deep quality:** first screen answers the primary question; headings have scent; uncertainty is visible without being paralysing; content is in the right artefact; the next move is obvious.

For final HTML, serve over local HTTP and write `reviews/browser-review.md`. For custom editors, copy/export the output and inspect it. For React, bundle to `final/bundle.html`. See `references/review-and-verification.md` and `references/browser-review-template.md`.

## Sharing

Default: local path. When a browser link is needed, publish a **secret** gist and verify raw + GistPreview URLs before reporting. See `references/secret-gist-publishing.md`.

## Common failures

| Failure | Correction |
|---|---|
| Beautiful but wrong audience | Re-lock the communication contract; regenerate first-feedback before polishing |
| User asked for dashboard but needs decision | Route by reader action, not requested surface |
| React used because “HTML artefact” | Use static HTML unless interaction/maintainability justifies React |
| UI guide material inside design review | Move to appendix or separate user guide via content disposition |
| Caveat repeated everywhere | Give it one canonical home and reference it tersely |
| Number looks validated but is a default | Add metric provenance and visual treatment consistent with evidence |
| Custom editor has no export | Add copy/export; inspect exported result during verification |
| Brand polish masks weak structure | Fix contract, headings, hierarchy, and evidence before visual polish |

## Reference index

- Contract: `references/communication-contract.md`
- Modes: `references/artefact-modes.md`
- First feedback: `references/first-feedback-loop.md`, `templates/first-feedback.md`
- Content disposition: `references/content-disposition.md`
- Design decisions and metric provenance: `references/design-decisions.md`
- Implementation routing: `references/implementation-routing.md`
- Review: `references/review-and-verification.md`, `references/browser-review-template.md`
- Components: `references/document-component-patterns.md`, `assets/css/document-components.css`
- Visual element palette: `references/visual-elements.md`
- HTML effectiveness patterns: `references/html-effectiveness-patterns.md`
- Secret gist publishing: `references/secret-gist-publishing.md`
