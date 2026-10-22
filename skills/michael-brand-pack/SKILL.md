---
name: michael-brand-pack
description: Style explicitly Michael-branded personal surfaces.
---

# Michael Brand Pack

Michael F. Bryan visual design system. The reference implementation is [tools.michaelfbryan.com](https://github.com/Michael-F-Bryan/tools.michaelfbryan.com) (`src/app/globals.css` and `src/components/`); this skill mirrors its tokens and components. It owns look and visual judgement. It does not replace writing voice or rich-communication workflow. Do not use “Operator Notes” as the conceptual frame for all artefacts; treat it, if used at all, as one possible surface label rather than the governing abstraction.

## Activation boundary

Use only for Michael’s personal sites/tools or explicitly requested Michael branding. Ordinary HTML, company engineering reports, CSU notes, and generic diagrams do not activate this pack. Honour the destination’s existing visual identity.

## Quick start

1. Read `references/tokens.md` for values.
2. Pick one channel below → read the matching reference.
3. Start from a template when useful: `templates/rich-html-document.html`, `templates/tool-workspace.html`, `templates/email-signature.html`, or `templates/style-calibration.md`.
4. For plain web/rich HTML, load Atkinson Hyperlegible and link `assets/css/web-base.css` (it imports `tokens.css`). For Tailwind v4, copy the site's `globals.css` instead.
5. Check that styling makes the work legible and the next move obvious.

## Channel router

| User task | Read | Assets |
|---|---|---|
| Personal site, tools site, app chrome, landing pages | `references/websites.md` | `tokens.css`, `web-base.css`, or the site's `globals.css` |
| Email signature, HTML email | `references/email.md` | Token values inline |
| Word / Google Docs templates, slides | `references/documents.md` | Token values as pt/hex mapping |
| Rich HTML artefact: decision brief, explainer, design review, report, deck | `references/html.md` | Pair with `html-rich-communication`; templates in `templates/` |
| Full visual language, mood, diagrams | `references/visual-language.md` | All CSS assets and `templates/style-calibration.md` |

## Core visual rules

1. Legibility is authority: important text must be readable at 100% zoom.
2. Structure before decoration: rules, columns, and whitespace expose the thinking.
3. One palette: near-white paper `#f9fafb`, ink `#17191d`, secondary-grey prose `#3f4956`, one blue accent `#164dcc`. Light theme for everything, tools included; dark only as the `tokens.css` extension when the host expects it.
4. Styling must not make the wrong artefact look finished. Fix the communication structure first.
5. Type: Atkinson Hyperlegible 400/700. Running prose 18px/32px, supporting 16px, captions and dense UI 14px. Only short uppercase mono labels go down to 12px.
6. Headings are bold, tightly tracked, and balanced; prose sits in secondary grey at a 44rem measure.
7. Mono accent kickers above section titles; muted mono labels for metadata.
8. Ruled rows instead of cards, full-width bands instead of boxes. Surfaces are square; radius only on small badges and third-party controls. No shadows or gradients.
9. Visible structural rules (`--rule`, 3:1+). Use `--rule-subtle` only for inner dividers.
10. The accent is a signal (links, kickers, selected state, focus, the subject of a figure), not decoration. Every status also has a text label.
11. Direct annotation beats legends: labels, units, and caveats sit near the thing they explain.
12. Domain motifs are accents, not the governing system, unless the artefact is a demo/marketing surface.
13. If the user asks for a conflicting mood, run style-conflict calibration: keep brand legibility, honour the requested feel where it serves the job, and show a quick proof before polish.
14. Accessible by default: 2px accent focus ring at 4px offset, 44px touch targets on phones, semantic HTML, no horizontal scroll at phone width, print-friendly where relevant.

## Pairing

- Rich artefact workflow and verification → `html-rich-communication`
- Writing voice and artefact tone → `voice-michael`

## Template index

| File | Use when |
|---|---|
| `templates/rich-html-document.html` | Report, explainer, design review, decision brief (entry layout with right-hand nav) |
| `templates/tool-workspace.html` | Tool, dashboard, sandbox, or long-running screen work (workspace layout) |
| `templates/email-signature.html` | HTML email signature starting point; inline-safe styles |
| `templates/style-calibration.md` | Quick proof before applying a mood that conflicts with brand defaults |

Templates are starting points, not mandatory frames. Replace placeholder content and remove unused sections.

## Reference index

| File | When to read |
|---|---|
| `references/visual-language.md` | Brand mood, signature moves, diagram visuals, anti-patterns |
| `references/tokens.md` | Token tables, type roles, rhythm, widths, dark and signal extensions, Tailwind mapping |
| `references/websites.md` | Site/tool chrome and the component map |
| `references/email.md` | Signatures and HTML email constraints |
| `references/documents.md` | Word/Google Docs and slide style mapping |
| `references/html.md` | Rich HTML artefact channel rules |

## Keeping in sync

When the tools site's `globals.css` or shared components change, update `assets/css/tokens.css`, `assets/css/web-base.css`, and `references/tokens.md` to match. Values marked "extension" are the only ones this skill defines on its own.