# Browser review template

Save to `_working/<topic>/reviews/browser-review.md` during step 8. Do not mark verification complete in `README.md` until this file exists with evidence.

Serve the bundle locally (`python3 -m http.server` in `final/`) — `file://` URLs often block or distort behaviour.

## Header

```markdown
# Browser review — <topic title>

- **Artefact:** `_working/<topic>/final/bundle.html`
- **Audience tested as:** <who>
- **Viewports:** mobile ~375px, desktop ~1280px (record actual widths used)
- **Reviewer:** <agent or human>
- **Date:** <ISO date>
```

## First screen

- **Primary question:** <from README brief>
- **Answered on first screen?** yes / partial / no
- **Notes:**

## Navigation anchors

Click every in-page nav link at **both** viewports. Target: section heading within ~24px of `scroll-padding-top` (sticky header + margin).

| Link label | Target `#id` | Mobile landing OK? | Desktop landing OK? | Notes |
| ---------- | ------------ | ------------------ | ------------------- | ----- |
|            |              | pass / fail        | pass / fail         |       |

If any fail: fix `scroll-padding-top` on `html` and/or `scroll-mt-*` on sections, rebundle, re-test.

## Interactive controls

| Control                       | Mobile | Desktop | Notes     |
| ----------------------------- | ------ | ------- | --------- |
| Accordion / collapsible items |        |         | list each |
| Tabs                          |        |         |           |
| Filters / toggles             |        |         |           |
| Copy / export buttons         |        |         |           |

## Reader checks

- [ ] No critical meaning is colour-only, hover-only, or animation-only
- [ ] Self-contained (no runtime CDN fetches in network tab)
- [ ] Privacy posture matches README (paths, gist visibility)
- [ ] Executive/decision artefacts (if applicable): scope, owner, review gate, kill condition stated

## Audience-fit issues

Separate from bugs — things that work but fail the reader's job:

-

## Implementation bugs

-

## Verdict

- **Ship as-is / ship with noted caveats / do not ship**
- **Blockers:**

```
