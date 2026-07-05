# Implementation Checklist

## React source checklist (`app/`)

- [ ] Project scaffolded with `scripts/init-artifact.sh` inside `_working/<topic>/`.
- [ ] Implementation follows `visual-plan.md` and refined brief.
- [ ] Project styling skill from `AGENTS.md` applied when stipulated (overrides shadcn defaults).
- [ ] Semantic heading hierarchy in JSX (h1 → h2 → h3).
- [ ] First screen answers the primary reader question.
- [ ] Mobile width around 375px is readable without sideways scrolling.
- [ ] Disclosure/tabs/filters work with keyboard and without hover-only reliance.
- [ ] Nav links land sections cleanly below sticky headers at mobile and desktop widths.
- [ ] Mobile nav links are visible or have an obvious scroll/wrap affordance.
- [ ] No critical meaning is colour-only.
- [ ] Images and diagrams have useful captions or alt text.
- [ ] Charts/diagrams use bundled npm packages, not runtime CDN loads.
- [ ] Privacy posture is visible in notes and matches sharing method.

## Bundle checklist (`final/bundle.html`)

- [ ] `bundle-artifact.sh` run from `app/` without errors.
- [ ] `final/bundle.html` exists and matches latest source.
- [ ] If shared via gist: secret (not `--public`); GistPreview URL verified and recorded in README.
- [ ] File opens in browser as a self-contained page (no runtime CDN dependencies at load time).
- [ ] Bundle size is reasonable; trim unused shadcn imports if bloated.

## Browser verification scriptlet

Use the browser tool when available. If only terminal is available, run a local static server and use whatever browser automation exists in that environment.

Minimum reviewer actions:

1. Open `final/bundle.html`.
2. Resize or emulate mobile width.
3. Click every nav link and disclosure control.
4. Inspect first screen, key visual, risk/evidence section, and next-action block.
5. Report audience-fit failures separately from implementation bugs.
