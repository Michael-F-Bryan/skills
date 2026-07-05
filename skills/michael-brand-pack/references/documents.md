# Word and Google Docs templates

Map [tokens.md](tokens.md) to document styles. Docs apps do not load CSS variables — apply named styles with these targets.

## Document defaults

| Style | Font | Size | Colour | Notes |
|---|---|---:|---|---|
| Normal / Body | Atkinson Hyperlegible or Arial | 11pt (~17px equivalent) | `#171717` | Line spacing 1.15–1.3 |
| Heading 1 | Same sans | 22–26pt | `#171717` | Bold, tight spacing below |
| Heading 2 | Same sans | 16–18pt | `#171717` | Bold; optional bottom border `#b8b0a2` |
| Heading 3 | Same sans | 13–14pt | `#171717` | Bold |
| Caption / metadata | Same sans | 10–11pt | `#414853` | Must stay readable |
| Hyperlink | Same sans | inherit | `#245c7a` | Underlined |

## Page and margins

- Background white or `#f7f4ec` for cover pages only.
- Margins: 2–2.5 cm standard; wider side margins for briefings if printing.
- Max line length ~80 characters in body styles where the app allows.

## Status and callout blocks

Use paragraph styles with left border (Word: border-left 3–5pt `#245c7a`) and light fill:

| Callout | Left border | Fill |
|---|---|---|
| Info / read | `#245c7a` | `#e8f2f5` |
| Recommendation | `#007a8a` | `#e8f2f5` |
| Warning / risk | `#9a6700` | `#fff1ce` |
| Error | `#a33a2b` | `#f8dfda` |

Always include a text label (e.g. **Recommendation:**) — not colour alone.

## Tables

Header row background `#ece6d8`, text `#171717`, borders `#b8b0a2`. Cell padding equivalent to 8–12px.

## Print / PDF export

Prefer light theme. Ensure heading styles survive PDF export — verify h1/h2 are visually distinct from body at 100% zoom.

## Slides (brief)

- Title: 28–36pt, `#171717` on `#f7f4ec` or white.
- Body: 18–22pt minimum on slides; never below 16pt.
- One accent colour `#245c7a` for links and key highlights; avoid gradient backgrounds.
