# Implementation Checklist

## HTML file checklist

- [ ] Single `.html` file unless assets are explicitly required.
- [ ] Inline CSS or local asset references only.
- [ ] Semantic headings form a sensible outline.
- [ ] First screen answers the primary reader question.
- [ ] Mobile width around 375px is readable without sideways scrolling.
- [ ] `<details>`/tabs/filters work with keyboard and without hover-only reliance.
- [ ] Nav links land sections cleanly below sticky headers at mobile and desktop widths.
- [ ] Mobile nav links are visible or have an obvious scroll/wrap affordance.
- [ ] No critical meaning is colour-only.
- [ ] Images and diagrams have useful captions or alt text.
- [ ] External dependencies, if any, are pinned and justified.
- [ ] Privacy posture is visible in notes and matches sharing method.

## Browser verification scriptlet

Use the browser tool when available. If only terminal is available, run a local static server and use whatever browser automation exists in that environment.

Minimum reviewer actions:

1. Open the artefact.
2. Resize or emulate mobile width.
3. Click every nav link and disclosure control.
4. Inspect first screen, key visual, risk/evidence section, and next-action block.
5. Report audience-fit failures separately from implementation bugs.
