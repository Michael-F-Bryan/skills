# Rich HTML channel

Rich HTML artefacts need two concerns kept separate:

| Concern | Owner |
|---|---|
| Communication workflow, artefact mode, implementation lane, verification | `html-rich-communication` |
| Visual judgement, colours, typography, density, templates, motif handling | `michael-brand-pack` |
| Writing voice and phrasing | `voice-michael` when attached |

This reference adds Michael Brand Pack rules for rich artefacts. It does not replace the html-rich workflow.

## Promise

Make the work legible. Make the next move obvious.

The page should expose decisions, risks, owners, labels, units, relationships, and confidence without making weak thinking look finished.

`Operator Notes` is optional identity copy. Do not use it as the conceptual wrapper unless the user asks for that surface or it is clearly the artefact's intended label.

## Defaults

- Use warm light document styling for reports, decision briefs, design reviews, explainers, and print-friendly artefacts.
- Use dark styling for tools, dashboards, demos, prototypes, long-running screen work, or when the user explicitly accepts the trade-off.
- Domain motifs are accents, not the governing system, unless the artefact is a demo/marketing surface.

For Sunfish/ocean/robotics work, avoid defaulting to dark glowing cyberpunk. Use marine cues sparingly: boundary lines, muted blues/greens, small map/field-note motifs, or diagrams. Keep review documents readable at 100% zoom.

## Templates

| Template | Use when | Notes |
|---|---|---|
| `../templates/rich-html-document.html` | Warm light document, report, explainer, review artefact | Pair with `html-rich-communication`; remove unused sections |
| `../templates/dark-tool.html` | Tool, dashboard, sandbox, demo, long-running screen work | Must include labels, focus states, export if stateful |
| `../templates/style-calibration.md` | Requested mood conflicts with defaults | Use before polish; produce a quick proof/tile |

## Style-conflict calibration

When the user asks for an aesthetic that conflicts with brand defaults, resolve it explicitly before polishing:

```markdown
## Style calibration

- Brand defaults to preserve:
- Requested mood to honour:
- Audience / reading context:
- Chosen direction:
- What is rejected and why:
- Quick visual proof to show first:
```

Do not silently override the user's requested mood. Do not silently obey it either. State the trade-off, then produce a small first-feedback mock or style tile when mood is part of the job. Success is both: the artefact reads as the requested domain/mood **and** remains legible, structured, and review-appropriate.

## Long-form artefact layout

For dense reports, decision artefacts, evidence packs, and design reviews:

- Put document navigation to the left of the body on desktop when the page has more than a few sections.
- Include a rough reading-progress indicator in that rail when the artefact is long enough to skim over multiple sittings.
- Collapse navigation behind a hamburger/details control on phone-sized viewports.
- Keep the hero for orientation and the first reader question; do not duplicate the table of contents there when a persistent nav exists.
- Put the source index at the bottom so auditability is available without interrupting the argument.
- Use evidence-strength, provenance, freshness, risk, and confidence labels as quiet structural aids, not decorative badges.

## Correction-proof phrasing

A revised artefact must stand alone. Do not surface internal correction history in the design or copy: avoid labels such as “not the philosophy”, “not the recommendation”, “this page intentionally avoids…”, or “I should have…”. Use positive reader-job labels instead: “Evidence pack”, “Decision material”, “Review brief”, “Source map”, or “Open questions”.

## Visual jobs

Every major visual element should do one of these jobs:

| Job | Examples |
|---|---|
| orient | system boundary, current state, section map |
| compare | options grid, before/after, trade-off table |
| decide | recommendation, decision gate, owner/review block |
| warn | risk, caveat, validation state |
| remember | restrained visual anchor, memorable motif |
| teach | annotated diagram, progressive explanation |
| operate | checklist, status, next action |

Remove visuals with no job.

## Direct annotation

Put labels, units, explanations, and caveats beside the thing they explain. Avoid legends and captions that force eye travel when inline labels would be clearer.

## Anti-polish rule

Do not use the brand system to make a weak artefact look done. If the communication contract is unclear, fix hierarchy, headings, evidence typing, and next action before adding visual finish.

## Density rule

High density is welcome when grouping, spacing, and hierarchy preserve scanability. Dense does not mean tiny or faint. Body text generally stays 17–18px for long-form and not below 15px for dense UI.

## Decoration rule

Ban harmful decoration, not all memorability. A visual anchor is allowed when it improves orientation or recall. Remove it when it competes with the decision, weakens contrast, or adds domain cosplay.

## Assets

When implementing branded web surfaces, copy or import:

- `../assets/css/tokens.css`
- `../assets/css/web-base.css`

Use html-rich component CSS/patterns for document structure.
