# Visual language

The reference implementation is [tools.michaelfbryan.com](https://tools.michaelfbryan.com) ([source](https://github.com/Michael-F-Bryan/tools.michaelfbryan.com)). When a decision is unclear, check how the site does it.

## Brand concept

Crisp near-white paper, dark ink, a single cool-blue accent, strong readable type, monospace utility labels, fine rules, and useful whitespace.

Internal rule:

> Make the work legible. Make the next move obvious.

Artefacts should feel useful, legible, structured, direct, evidence-aware, decision-oriented, and accessible by default.

## Pillars

1. **Legibility is authority.** If it matters, it must be readable.
2. **Structure before decoration.** Rules, columns, and whitespace show the shape of the work.
3. **Useful beats impressive.** Polish serves comprehension.
4. **Calm technical confidence.** It should read like the work of someone who has actually done it.
5. **Decisions over documentation.** Help the reader act when the job is to decide or operate.
6. **Accessible by default.** Refined does not mean faint.
7. **Annotation over ornament.** Labels, units, and caveats sit near the things they explain.
8. **Share only repeated jobs.** Build the page in front of you; extract a pattern only when the same job appears again.

## Visual mood

A well-set technical reference page: strong headings, a comfortable reading column, fine horizontal rules between items, monospace kickers, and one blue used with intent.

Avoid: SaaS landing page, rounded card grids, gradient heroes, academic PDF, cyberpunk terminal, Notion template, startup pitch deck, corporate strategy report.

## Signature moves

These are what make a page recognisably Michael's:

| Move | How |
|---|---|
| Mono kicker above a heading | 12px JetBrains Mono, bold, uppercase, 0.14em tracking, accent |
| Tight, large, balanced headings | 60px page title at -0.035em; 36px section title at -0.03em |
| Prose in secondary grey at a measure | 18px/32px `--text-secondary`, max 44rem |
| Ruled lists instead of cards | `border-t` on the list, `border-b` on each row, 1px `--rule` |
| Numbered steps | `01`, `02` in mono accent, title bold, body muted |
| Definition rows | Mono accent term in a 12rem column, secondary description beside it |
| Bands, not boxes | Full-width `--surface` or `--panel` block bounded by top and bottom rules |
| Accent left rule for asides | 2px accent `border-left`, 20px padding, 14px secondary text |
| Site mark | `Michael F. Bryan / Tools`: ink, accent slash, muted area name |

## Colour direction

Light is the canonical theme for everything the site publishes, including interactive tools. The dark theme in `tokens.css` is an extension for surfaces that must follow the viewer's system setting. It keeps the same structure.

Use colour for signal only:

- accent: links, kickers, step numbers, selected state, focus, the one highlighted element in a figure;
- error: validation messages and blockers;
- warning / success (extension): risk and confirmation, always with a text label;
- neutral: everything else, including structure and surfaces.

Diagrams use ink, accent, and rule strokes: ink for the reference, accent for the subject, rule or dashed rule for secondary or final states. Do not introduce a categorical palette unless the data genuinely needs several series.

## Visual jobs

Every major visual element should do one of these jobs:

| Job | Meaning |
|---|---|
| orient | show current state, boundary, map, or section location |
| compare | make options/trade-offs visible |
| decide | surface recommendation, owner, gate, or next action |
| warn | expose risk, caveat, validation state, or unknown |
| remember | provide a restrained visual anchor |
| teach | explain relationships or sequence |
| operate | support action, checklist, or status |

Remove visuals with no job.

## Typography direction

Atkinson Hyperlegible, 400 and 700 only. JetBrains Mono for labels, numbers, and code. Headings are bold and tightly tracked; body prose is regular, generously leaded, and set in the secondary grey so headings and bold text carry the hierarchy.

## Accessibility floor

- Running prose 18px; supporting prose 16px; sentences never below 14px.
- 12px is allowed only for uppercase mono labels of a few words.
- Line height about 1.75 for prose.
- Primary and secondary text at 7:1 or better; muted and accent at 4.5:1 or better on every surface.
- Structural rules at 3:1 or better (`--rule`, not `--rule-subtle`, for the outer rules of a block).
- Colour is never the only status signal.
- Visible focus: 2px accent outline, 4px offset.
- 44px touch targets on phones.
- Semantic HTML before ARIA; no horizontal page scroll at phone width.

## Diagram visuals

Diagrams show system shape, not decoration.

- Square boxes, 1px rule or ink strokes, explicit boundaries, directional arrows.
- Label arrows when the relationship is not obvious; labels in mono uppercase or 14px sans.
- Put labels, units, and caveats near the relevant thing; avoid forced eye travel to legends. When a legend is unavoidable, use short inline stroke swatches.
- Show ownership, state, and failure paths where relevant.
- Avoid mystery icons, 3D/isometric decoration, drop shadows, gradients, and tiny text.
- Set figures on `--panel` or `--surface` with a rule border, and a muted 14px caption beneath.
- Must be readable at 100% zoom and export cleanly to PDF.

Preferred types: boundary diagram, sequence, state, data flow, decision tree, timeline, risk map.

## Anti-patterns

**Too generic:** default Tailwind colours, rounded shadowed cards, pill chips everywhere, decorative icons.

**Too corporate:** vague strategy language, consultancy palette, executive-deck gloss.

**Too developer aesthetic:** dark terminal everywhere, monospace body text, fake command prompts.

**Too academic:** abstract-first prose, excessive caveats before the recommendation, completeness over action.

**Too colourful:** a second accent, tinted backgrounds on every callout, colour used to make things "pop".

**Too polished for the thinking:** beautiful styling over unclear audience, missing risk, weak headings, or unverified claims.

## Writing voice

Voice, tone, recommendation patterns, and artefact structure live in `voice-michael`. This skill covers visual look and visual judgement.
