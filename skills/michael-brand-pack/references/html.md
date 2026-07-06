# Rich HTML channel

Rich HTML artefacts need two concerns kept separate:

| Concern | Owner |
|---|---|
| Communication workflow, artefact mode, implementation lane, verification | `html-rich-communication` |
| Operator Notes visual judgement, colours, typography, density, motif handling | `michael-brand-pack` |
| Writing voice and phrasing | `voice-michael` when attached |

This reference adds Operator Notes rules for rich artefacts. It does not replace the html-rich workflow.

## Operator Notes promise

Field notes refined into decision briefs.

The page should make the work legible and the next move obvious. Styling is evidence architecture: it exposes decisions, risks, owners, labels, units, and relationships.

## Defaults

- Use warm light document styling for reports, decision briefs, design reviews, explainers, and print-friendly artefacts.
- Use dark styling for tools, dashboards, demos, prototypes, long-running screen work, or when the user explicitly accepts the trade-off.
- Domain motifs are accents, not the governing system, unless the artefact is a demo/marketing surface.

For Sunfish/ocean/robotics work, avoid defaulting to dark glowing cyberpunk. Use marine cues sparingly: boundary lines, muted blues/greens, small map/field-note motifs, or diagrams. Keep review documents readable at 100% zoom.

## Style-conflict calibration

When the user asks for an aesthetic that conflicts with Operator Notes defaults, resolve it explicitly before polishing:

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

- `assets/css/tokens.css`
- `assets/css/web-base.css`

Use html-rich component CSS/patterns for document structure.
