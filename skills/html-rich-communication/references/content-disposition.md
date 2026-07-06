# Content disposition

Every major content block needs a fate. This prevents polished artefacts from becoming mixed-mode dumping grounds.

## Disposition values

| Fate | Meaning |
|---|---|
| core | Needed to answer the primary question |
| supporting evidence | Needed for trust, but not first-screen material |
| visible caveat | Must be seen early to avoid misleading the reader |
| disclosure | Useful detail hidden behind details/tabs/accordion |
| appendix | Reference/detail at the end |
| linked separate artefact | Belongs in a user guide, reference, dashboard, or explainer elsewhere |
| cut | Does not serve this reader job |

For approval/funding decisions, logs, charts, site-by-site notes, code snippets, and broad dashboard views default to disclosure or appendix unless they change the recommended decision. An appendix is not a dashboard in disguise; keep the decision path dominant.

## Canonical caveat home

Each caveat, warning, risk, or non-goal gets one canonical home. Elsewhere, use a terse reference.

Bad: repeat “no feedback loop” in hero, boundaries, implementation, and risks.

Good: put it under `Accepted risk / out of scope`, then reference “see accepted risk: open-loop control” where relevant.

## Information scent pass

Headings and nav labels are promises. Before building, check whether a scanning reader can tell where their question is answered.

- Prefer question or takeaway headings over vague labels.
- Keep sections on one level.
- Link or disclose adjacent modes instead of blending them.
