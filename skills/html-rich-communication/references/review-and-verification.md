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

## Review artefact

For final HTML, write `reviews/browser-review.md` using `references/browser-review-template.md`. Separate implementation bugs from audience-fit issues. Verdicts: ship, ship with caveats, do not ship.
