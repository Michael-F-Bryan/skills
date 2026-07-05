---
name: michael-brand-pack
description: >-
  Applies Michael F. Bryan's Operator Notes visual design system — warm
  high-contrast palette, typography scale, spacing tokens, light/dark themes —
  across websites, email signatures, Word/Google Doc templates, slides, and
  any branded surface. Use whenever the user mentions Operator Notes styling,
  Michael F. Bryan brand colours, personal site theming, email signatures,
  document templates, or "make it look like Michael" — even without naming this
  skill. For rich HTML documents, the user may also attach html-rich-communication.
  For writing voice, the user may also attach a voice or author-style skill.
---

# Michael Brand Pack

Visual design system for Operator Notes — warm high-contrast palette, typography, spacing, and channel-specific application. This skill owns **look**, not workflow or writing voice.

## Quick start

1. Read [references/tokens.md](references/tokens.md) for values.
2. Pick one channel below → read **one** reference file.
3. Apply [assets/css/tokens.css](assets/css/tokens.css) plus [assets/css/web-base.css](assets/css/web-base.css) for web surfaces.

## Channel router

| User task | Read | Assets |
|---|---|---|
| Personal site, app chrome, landing pages | [references/websites.md](references/websites.md) | `assets/css/tokens.css`, `web-base.css` |
| Email signature, HTML email | [references/email.md](references/email.md) | Token values inline (email-safe fonts) |
| Word / Google Docs templates | [references/documents.md](references/documents.md) | Token values as pt/hex mapping |
| Rich HTML artefact (decision brief, explainer) | [references/html.md](references/html.md) | Pair with html-rich-communication |
| Full visual language, mood, diagrams | [references/visual-language.md](references/visual-language.md) | All CSS assets |

## Core visual rules

1. Legibility is authority — important text must be readable at 100% zoom.
2. Use the warm light theme for documents, reports, and print; dark theme for tools and dashboards.
3. Body text: 17–18px long-form; dense UI not below 15px.
4. Primary text targets AAA-like contrast; secondary text stays readable, not faint.
5. Borders visible when they carry structure — no `rgba(0,0,0,0.05)` dividers.
6. Colour signals meaning; every status also has a text label.
7. Headings read as headings — size and weight steps, not bold body text.
8. No SaaS gradient card grids, startup chrome, or decorative branding.
9. Structure before decoration — layout exposes the thinking.
10. Accessible by default — focus states, semantic HTML, print-friendly where relevant.

## Pairing (do not duplicate their content)

- **Rich HTML artefacts** (workflow, React scaffold, templates, component patterns) → [html-rich-communication](../html-rich-communication/SKILL.md)
- **Writing voice and artefact tone** → [voice-michael](../voice-michael/SKILL.md)

## Reference index

| File | When to read |
|---|---|
| [references/visual-language.md](references/visual-language.md) | Brand mood, pillars, diagram visuals, anti-patterns |
| [references/tokens.md](references/tokens.md) | Full token tables, light/dark values, font stacks |
| [references/websites.md](references/websites.md) | Personal site and app chrome |
| [references/email.md](references/email.md) | Signatures and HTML email constraints |
| [references/documents.md](references/documents.md) | Word/Google Docs style mapping |
| [references/html.md](references/html.md) | Pointer to html-rich for HTML channel |
