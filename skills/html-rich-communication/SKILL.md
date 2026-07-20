---
name: html-rich-communication
description: >-
  Use when creating a shareable HTML explainer, brief, report, review aid, evidence pack, or other rich communication artefact for a human reader.
---

# HTML Rich Communication

## Default: the ten-minute lane

The usual job is **conversion, not rediscovery**. If the answer, notes, or source material already exists, preserve its claims and turn it into a clearer reading experience. Do not reopen research unless a required claim is missing or stale.

Use this lane for a read-only artefact with one audience and one cognitive job. Target **5–10 minutes from request to verified link**.

1. **Lock the job in one sentence.** `Reader needs to <understand/decide/compare/review/operate> <thing> so they can <action>.` Keep this in working memory; do not create a contract file.
2. **Choose one spine.** For explainers, default to one worked scenario. Introduce concepts only when the scenario needs them. For briefs, lead with the decision. For reports, lead with the finding.
3. **Cut before building.** Default bounds: 900–1,500 words, 4–6 sections, 0–2 useful visuals, at most one main table, and optional source links at the bottom. Put lookup material in `<details>` or link it; do not mix explainer, reference, risk register, and implementation review.
4. **Build once.** Start from `templates/fast-explainer.html` or an equally small static page. Write one self-contained `index.html`; use semantic HTML and inline CSS. No build system is required.
5. **Verify once, repair once.** Serve locally, inspect desktop and 375 px mobile, check first-screen answer, horizontal overflow, links, and console errors. Exercise controls only if controls exist. Make one bounded correction pass, then publish or report the remaining blocker.
6. **Publish if requested.** Create a secret Gist, verify `public: false`, and return the GistPreview URL. Fresh local rendering is sufficient; do not re-review the hosted copy unless delivery itself is failing.

## Effectiveness contract

A good artefact:

- answers the primary question on the first screen;
- reveals its argument through headings alone;
- uses one concrete example or worked path when explaining a mechanism;
- distinguishes fact, judgement, and uncertainty at the point of use;
- labels prominent numbers as measured, default, target, estimate, or assumption, and gives each material caveat one canonical home;
- uses visuals only when they make a relationship faster to grasp; and
- treats mobile as a deliberate single-column reading surface.

## Fast-lane prohibitions

Do not add broad rediscovery, working documents, subagents, React, package installation, bespoke audit scripts, runtime Mermaid, screenshot matrices, or repeated review loops to an ordinary artefact run.

Prefer HTML/CSS or inline SVG. Use Mermaid only when `mmdc` is already available, then render static SVG.

## Extended lane

Load heavier references only when an observable condition requires them:

- a missing reader, decision, or safety/privacy boundary would materially change the answer and cannot be inferred → ask at most one focused question; use `references/first-feedback-loop.md` only if the answer creates genuinely different artefact shapes;
- large evidence corpus or decision pack → preserve a source-contribution map, trace clusters back to source families or notes, label freshness when time matters, expose decision tensions and blind spots, and include a source index; recommend only when requested; use `references/content-disposition.md`, `references/design-decisions.md`, and `references/review-and-verification.md` only where those checks apply;
- stateful editor/dashboard/export → define the export shape first, including whether active filter/sort/tag state is serialised or deliberately omitted; then use `references/implementation-routing.md` and `references/review-and-verification.md`; verify that exported data and material view state match the visible interface;
- justified React → use the React lane in `references/implementation-routing.md` and its bundled scripts;
- publishing failure → use `references/secret-gist-publishing.md`.

High stakes alone is not an extended-lane trigger. Polish, brand treatment, and an inferable audience are not extended-lane triggers either.

## Stop rule

Once the artefact answers the reader's question, works at desktop and phone width, has no material rendering error, and the requested link exists, stop. Extra process is not extra quality.
