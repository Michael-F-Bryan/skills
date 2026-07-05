# Visual language

## Table of contents

- [Brand concept](#brand-concept)
- [Pillars](#pillars)
- [Visual mood](#visual-mood)
- [Colour direction](#colour-direction)
- [Typography direction](#typography-direction)
- [Accessibility floor](#accessibility-floor)
- [Diagram visuals](#diagram-visuals)
- [Anti-patterns](#anti-patterns)
- [Writing voice](#writing-voice)

## Brand concept

**Operator-grade communication:** field notes refined into decision briefs.

Internal rule:

> Make the work legible. Make the next move obvious.

Artefacts should feel useful, legible, structured, direct, evidence-aware, decision-oriented, and accessible by default.

## Pillars

1. **Legibility is authority** — if it matters, it must be readable.
2. **Structure before decoration** — make the shape of the work visible.
3. **Useful beats impressive** — polish serves comprehension.
4. **Calm technical confidence** — sound like someone who has done the work.
5. **Decisions over documentation** — help the reader act when the job is decide/operate.
6. **Accessible by default** — refined does not mean faint.

## Visual mood

Readable technical document + field manual + clean software interface.

Avoid: SaaS landing page, academic PDF, cyberpunk terminal, Notion template, startup pitch deck, corporate strategy report.

## Colour direction

Light theme is canonical for reports and documents. Dark theme is secondary for tools, dashboards, demos, and long-running screen work.

Use colour for signal:

- accent: links, selected states, key highlights
- warning: risk/caution
- error: blocker/failure
- success: confirmed/done
- neutral: structure and surfaces

Do not spray colour around to make things “pop”. See [tokens.md](tokens.md) for hex values.

## Typography direction

Recommended body/UI fonts: Atkinson Hyperlegible, Inter, IBM Plex Sans, Source Sans 3, system-ui fallback.

Recommended monospace: JetBrains Mono, IBM Plex Mono, Cascadia Code, Roboto Mono.

Do not use monospace as body text.

## Accessibility floor

- Body text generally 17–18px for long-form; dense UI not below 15px.
- Line height 1.45–1.65 for prose.
- Primary text targets AAA-like contrast; secondary text minimum 4.5:1 where practical.
- Borders visible when they carry structure.
- Colour is never the only status signal.
- Interactive elements need visible focus states.
- Semantic HTML before ARIA; documents usable at 100% zoom.

| Element | Target |
|---|---|
| Body text | Prefer 7:1+ contrast |
| Secondary text | Minimum 4.5:1 where practical |
| Large headings | Minimum 4.5:1 |
| Meaningful borders | Minimum 3:1 against adjacent colours |

## Diagram visuals

Diagrams show system shape, not decoration.

- Labelled boxes, explicit boundaries, directional arrows.
- Label arrows when the relationship is not obvious.
- Show ownership, state, and failure paths where relevant.
- Avoid mystery icons, 3D/isometric decoration, unlabelled arrows, tiny text.
- Prefer rectangular boxes, solid borders, low colour count.
- Readable at 100% zoom; export cleanly to PDF.

Preferred types: boundary diagram, system boundary, sequence, state, data flow, decision tree, timeline, risk map.

For HTML artefact diagram patterns and Mermaid routing, use html-rich-communication with an attached brand skill for colours.

## Anti-patterns

**Too corporate:** vague strategy language, consultancy palette, executive-deck gloss.

**Too casual:** jokes in structural headings, meme energy, unsupported assertions.

**Too developer aesthetic:** dark terminal everywhere, monospace body, fake command prompts.

**Too academic:** abstract-first prose, excessive caveats before recommendation, completeness over action.

**Too generic:** default Tailwind palette, AI dashboard card grids, decorative icons, no visible decision structure.

## Writing voice

Voice, tone, recommendation patterns, and artefact structure live in [voice-michael](../voice-michael/SKILL.md) — especially [references/operator-artifacts.md](../voice-michael/references/operator-artifacts.md). This skill covers visual look only.
