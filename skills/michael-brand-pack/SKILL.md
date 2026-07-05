---
name: michael-brand-pack
summary: |
    Create operator-grade technical artefacts using Michael F. Bryan's brand system: legible, structured, decision-oriented, accessible-by-default HTML documents, reports, briefings, and technical communication.
---

# Michael Brand Pack

Use this skill when creating rich HTML artefacts, technical reports, decision briefs, project write-ups, architecture notes, incident reviews, system handoffs, or other rich communication outputs that should feel recognisably Michael F. Bryan / Michael-F-Bryan.

The brand concept is **operator-grade communication**: field notes refined into decision briefs.

Core rule:

> Make the work legible. Make the next move obvious.

## Default outcome

The output should feel:

- readable and visually clear
- technically competent
- practical and grounded
- structured enough to survive being forwarded
- direct enough to support decisions
- accessible by default
- personal-professional, not corporate-generic

Avoid:

- faint low-contrast UI
- tiny typography
- generic SaaS card grids
- startup gradient styling
- academic throat-clearing
- consultancy sludge
- cyberpunk terminal cosplay
- decorative branding that does not help comprehension

## Brand pillars

1. **Legibility is authority** — if it matters, it must be readable.
2. **Structure before decoration** — make the shape of the work visible.
3. **Useful beats impressive** — polish should serve comprehension.
4. **Calm technical confidence** — sound like someone who has done the work.
5. **Decisions over documentation** — help the reader act, not just understand.
6. **Accessible by default** — refined does not mean faint.

## Standard artefact structure

For most serious artefacts, use this order:

1. Title
2. Purpose / context
3. Status strip
4. Current read
5. Recommendation
6. Why it matters
7. Evidence / observations
8. Options / trade-offs
9. Risks / failure modes
10. Open questions
11. Next move / next actions
12. Appendix / details

For short artefacts:

1. Title
2. Current read
3. Recommendation
4. Reasoning
5. Next move

For decision records:

1. Decision
2. Context
3. Options considered
4. Recommendation
5. Trade-offs
6. Risks
7. Follow-up actions

## Voice rules

- Lead with the read.
- Separate facts, judgement, assumptions, and uncertainty.
- Be blunt about systems, not people.
- Prefer specific nouns and direct recommendations.
- Use tables for trade-offs.
- Use diagrams for relationships and system shape.
- Use labelled uncertainty instead of fake certainty.

Good:

> The current design hides the important state. That is acceptable for the prototype, but it will make failures hard to diagnose once multiple people depend on it.

Avoid:

> There are several possible considerations which may be relevant to future robustness.

## Visual rules

- Use the warm high-contrast light theme as the default for documents, reports, and exportable artefacts.
- Use the dark theme for tools, dashboards, demos, and long-running screen work.
- Body text should generally be 17–18px for long-form content.
- Dense technical UI text should not go below 15px.
- Primary text should target AAA-like contrast where practical.
- Secondary text must remain readable.
- Borders should be visible when they carry structure.
- Colour should signal meaning, not decorate.
- Do not use colour as the only status signal.

## Required components for rich artefacts

Prefer these reusable components:

- Status strip
- Current read
- Recommendation
- Decision block
- Evidence block
- Trade-off table
- Risk block
- Assumption block
- Open questions
- Next actions / next move
- System diagram
- Appendix

## File map

- `README.md` — overview and usage.
- `docs/brand-guide.md` — full brand guide.
- `docs/voice-and-tone.md` — writing rules and examples.
- `docs/accessibility.md` — accessibility floor and visual legibility rules.
- `docs/component-patterns.md` — reusable artefact components.
- `css/tokens.css` — design tokens.
- `css/operator-notes.css` — complete stylesheet.
- `templates/briefing.html` — standard briefing template.
- `templates/decision-record.html` — decision record template.
- `templates/technical-report.html` — deeper report template.
- `examples/system-handoff.html` — sample finished artefact.
- `examples/decision-brief.html` — sample decision brief.
- `components/*.html` — snippet library.
- `diagrams/diagram-style.md` — diagram rules and examples.

## Implementation note

When generating a standalone HTML artefact, inline or link `css/operator-notes.css`. Keep semantic HTML. Use headings, labelled regions, tables, and ARIA labels where appropriate. Make the document printable unless the user explicitly wants an app-like interface.
