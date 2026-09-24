# Word and Google Docs templates

Map [tokens.md](tokens.md) to document styles. Docs apps do not load CSS variables, so apply named styles with these targets. Atkinson Hyperlegible is on Google Fonts and free to install; fall back to Arial.

## Document defaults

| Style | Font | Size | Colour | Notes |
|---|---|---:|---|---|
| Normal / Body | Atkinson Hyperlegible | 11pt | `#3f4956` | Line spacing 1.5; 12pt after paragraphs |
| Title | Atkinson Hyperlegible Bold | 30–36pt | `#17191d` | Line spacing 1.0; tight character spacing (-0.5pt) if the app allows |
| Heading 1 | Atkinson Hyperlegible Bold | 22pt | `#17191d` | 24pt before, 12pt after |
| Heading 2 | Atkinson Hyperlegible Bold | 15pt | `#17191d` | |
| Kicker / Label | JetBrains Mono Bold (or Consolas) | 8pt, all caps, expanded 1.5pt | `#164dcc` | Paragraph above a heading; keep with next |
| Caption / metadata | Atkinson Hyperlegible | 9–10pt | `#586372` | Must stay readable |
| Hyperlink | inherit | inherit | `#164dcc` | Underlined |
| Code | JetBrains Mono (or Consolas) | 9.5pt | `#17191d` | Shading `#f1f3f6` |

Headings in ink, body in the secondary grey: the contrast between them carries the hierarchy.

## Page and margins

- White background. No page colour or cover gradients.
- Margins: 2–2.5 cm; body text column around 16 cm or less.
- Header: `Michael F. Bryan / <area>` at 9pt, with the slash in `#164dcc` and a 0.5pt `#848d98` bottom border.

## Callouts and status

Use a paragraph style with a 1.5pt left border and no fill:

| Callout | Left border | Label |
|---|---|---|
| Note / recommendation | `#164dcc` | **Recommendation:** / **Note:** |
| Risk / warning | `#8a4b00` | **Risk:** |
| Error / blocker | `#b42318` | **Blocker:** |
| Confirmed | `#16693a` | **Confirmed:** |

Always include the text label, never colour alone.

## Tables

- No vertical borders and no zebra fills.
- Top border 0.5pt `#848d98`; header row bottom border 0.5pt `#848d98`; body row borders 0.5pt `#c7ccd2`.
- Header cells: 8pt mono (or bold sans) all caps, `#586372`.
- Numbers right-aligned in mono.

## Print / PDF export

Keep the light palette. Check that heading styles survive export and that the title, headings, and body are visually distinct at 100% zoom.

## Slides

- White or `#f9fafb` background; no gradients or photos behind text.
- Mono accent kicker above each slide title.
- Title 32–40pt bold ink with tight tracking; body 18–24pt in `#3f4956`, never below 16pt.
- Separate items with thin `#848d98` rules instead of boxes.
- One accent `#164dcc`, used for the kicker and the one thing to look at on each slide.
