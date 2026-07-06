---
name: michael-brand-pack
description: >-
  Applies Michael F. Bryan's Operator Notes visual design system — warm
  high-contrast palette, typography scale, spacing tokens, light/dark themes —
  across websites, email signatures, Word/Google Doc templates, slides, rich HTML
  artefacts, and any branded surface. Use whenever the user mentions Operator
  Notes styling, Michael F. Bryan brand colours, personal site theming, email
  signatures, document templates, rich artefact styling, or "make it look like
  Michael" — even without naming this skill.
---

# Michael Brand Pack

Visual design system for Operator Notes: **field notes refined into decision briefs**. This skill owns look and visual judgement. It does not replace writing voice or rich-communication workflow.

## Quick start

1. Read `references/tokens.md` for values.
2. Pick one channel below → read the matching reference.
3. For web/rich HTML, apply `assets/css/tokens.css` plus `assets/css/web-base.css`.
4. Check that styling makes the work legible and the next move obvious.

## Channel router

| User task | Read | Assets |
|---|---|---|
| Personal site, app chrome, landing pages | `references/websites.md` | `tokens.css`, `web-base.css` |
| Email signature, HTML email | `references/email.md` | Token values inline |
| Word / Google Docs templates | `references/documents.md` | Token values as pt/hex mapping |
| Rich HTML artefact: decision brief, explainer, design review, report, deck | `references/html.md` | Pair with `html-rich-communication` |
| Full visual language, mood, diagrams | `references/visual-language.md` | All CSS assets |

## Core visual rules

1. Legibility is authority — important text must be readable at 100% zoom.
2. Structure before decoration — layout exposes the thinking.
3. Use warm light theme for documents, reports, explainers, and review artefacts; dark theme for tools, dashboards, demos, and long-running screen work.
4. Styling must not make the wrong artefact look finished. Fix the communication structure first.
5. Body text: 17–18px long-form; dense UI not below 15px.
6. Primary text targets AAA-like contrast; secondary text stays readable, not faint.
7. Borders visible when they carry structure — no `rgba(0,0,0,0.05)` dividers.
8. Colour signals meaning; every status also has a text label.
9. Direct annotation beats legends: labels, units, and caveats sit near the thing they explain.
10. Domain motifs are accents, not the governing system, unless the artefact is a demo/marketing surface.
11. If the user asks for a conflicting mood, run style-conflict calibration: preserve brand legibility, honour the requested feel where it serves the job, and show a quick proof before polish.
12. No SaaS gradient card grids, startup chrome, cyberpunk terminal cosplay, or decorative branding.
13. Accessible by default — focus states, semantic HTML, print-friendly where relevant.

## Pairing

- Rich artefact workflow and verification → `html-rich-communication`
- Writing voice and artefact tone → `voice-michael`

## Reference index

| File | When to read |
|---|---|
| `references/visual-language.md` | Brand mood, pillars, diagram visuals, anti-patterns |
| `references/tokens.md` | Full token tables, light/dark values, font stacks |
| `references/websites.md` | Personal site and app chrome |
| `references/email.md` | Signatures and HTML email constraints |
| `references/documents.md` | Word/Google Docs style mapping |
| `references/html.md` | Rich HTML artefact channel rules |
