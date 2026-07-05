# Implementation Checklist

Use at the end of step 6 (plan fidelity) and step 8 (verification). Nothing in `README.md` should be checked complete until the corresponding items pass.

## Plan fidelity (`visual-plan.md` → built)

Before bundling, compare the visual plan to the React source:

- [ ] Every planned section exists with the intended reader job (not just a heading).
- [ ] Navigation matches the plan (pattern, labels, mobile behaviour).
- [ ] Evidence badges/types from the plan are implemented where specified (**source fact**, **assumption**, **judgement**, **unknown**, **hard rule**, **anti-pattern**, **example**).
- [ ] Typography/colours match the plan or a named project styling skill — not accidental shadcn defaults.
- [ ] Fonts named in the plan are bundled under `app/public/` (woff2) with `@font-face` — not runtime CDN links, not “close enough” system stacks unless the plan was updated.
- [ ] Charts/diagrams use the libraries named in the plan (npm, bundled).
- [ ] Deliberate deviations are recorded in `README.md` under **Plan fidelity** with a one-line reason each.

## React source (`app/`)

- [ ] Project scaffolded with `scripts/init-artifact.sh` inside `_working/<topic>/` (no hand-authored standalone HTML).
- [ ] `html { scroll-padding-top: … }` matches sticky header height; sections use matching `scroll-mt-*`.
- [ ] Semantic heading hierarchy (h1 → h2 → h3).
- [ ] First screen answers the primary reader question from the brief.
- [ ] Mobile width ~375px readable without horizontal scroll.
- [ ] Disclosure/tabs/filters work with keyboard; no hover-only reveals.
- [ ] Mobile nav links are all visible or obviously scrollable/wrapped.
- [ ] No critical meaning is colour-only.
- [ ] Images/diagrams have captions or alt text.
- [ ] No runtime CDN dependencies in source or bundle.

## Bundle (`final/bundle.html`)

- [ ] `bundle-artifact.sh` run from `app/` without manual workaround.
- [ ] `cp app/bundle.html final/bundle.html` done after latest source edit.
- [ ] File opens in browser as a self-contained page.
- [ ] Bundle size reasonable; trim unused shadcn imports if bloated.
- [ ] If shared via gist: secret (not `--public`); GistPreview URL verified and recorded in README.

## Browser verification (required artefact)

- [ ] `reviews/browser-review.md` written using `references/browser-review-template.md`.
- [ ] Tested at mobile (~375px) and desktop widths via browser (local HTTP server, not source inspection alone).
- [ ] Every nav link clicked; anchor landing recorded in the review table.
- [ ] Every accordion/tab/filter exercised at both widths.
- [ ] Audience-fit issues separated from implementation bugs.
- [ ] `README.md` status checkboxes updated **only after** the review file exists.

See `references/browser-review-template.md` for the review file shape.
