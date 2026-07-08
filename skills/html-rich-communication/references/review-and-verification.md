# Review and verification

Verification is not only “does the page load?”. It checks whether the artefact does its communication job.

## Functional checks

For HTML lanes:

- serve over local HTTP, not only `file://`;
- check mobile (~375px) and desktop;
- click every in-page/nav link;
- exercise every details/accordion/tab/filter/control;
- verify copy/export output;
- check no colour-only meaning;
- check no runtime CDN/dependency unless explicitly allowed;
- verify privacy posture.

For React, also build and bundle to `final/bundle.html`.

## Audience-fit / deep-quality checks

- Does the first screen answer the primary question?
- Can a scanning reader follow headings, bullets, and callouts?
- Is the artefact in the right mode?
- Are facts, assumptions, judgement, unknowns, and risks visibly distinct?
- Are labels, units, and annotations near the things they explain?
- Does visual hierarchy reduce effort?
- Does the artefact make the next move obvious?
- Does it feel trustworthy without pretending certainty?

For research-backed evidence or decision artefacts, also check:

- Are source-derived clusters/commonalities visible, or is it only a shuffled summary?
- Is there enough content for the claimed source set, with details on demand rather than a thin executive gloss?
- Does each major cluster link back to source material or source families?
- Is there a blind-spot / unknown-unknown analysis?
- Are UI, intent, transport, authority, telemetry, and human-procedure concepts separated where relevant?
- Are evidence strength, freshness, defaults, assumptions, and judgement visually distinguishable?
- Is the source index at the bottom complete enough for auditability?
- Does the copy avoid correction-history phrases such as “not the philosophy” or “this page intentionally avoids…”?

## Review artefact

For final HTML, write `reviews/browser-review.md` using `references/browser-review-template.md`. Separate implementation bugs from audience-fit issues. Verdicts: ship, ship with caveats, do not ship.
