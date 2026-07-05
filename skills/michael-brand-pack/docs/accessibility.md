# Accessibility and Legibility Rules

Operator Notes should be accessible by default. The goal is not compliance theatre. The goal is readable, usable, low-friction communication.

## Accessibility floor

- Body text should generally be 17–18px for long-form artefacts.
- Dense technical UI text should not go below 15px.
- Line height should generally sit between 1.45 and 1.65.
- Primary text should target AAA-like contrast where practical.
- Secondary text must still be readable.
- Borders must be visible when they carry structure.
- Colour must not be the only signal.
- Interactive elements must have visible focus states.
- Links should be visually distinguishable.
- Tables should have readable headers, sufficient spacing, and visible row structure.
- Documents should be usable at 100% zoom.
- HTML should use semantic elements before ARIA.

## Contrast rules

| Element | Target |
|---|---:|
| Body text | Prefer 7:1+ contrast |
| Secondary text | Minimum 4.5:1 where practical |
| Large headings | Minimum 4.5:1 |
| Meaningful borders/icons | Minimum 3:1 against adjacent colours |
| Decorative dividers | May be lower, but must not carry meaning |

## Typography rules

| Element | Size | Notes |
|---|---:|---|
| Long-form body | 17–18px | Default for reports and briefs |
| Dense UI body | 15–16px | Do not go smaller without strong reason |
| Metadata | 14–15px | Still readable |
| Code | 14.5–16px | Depends on density |
| Captions | 14–15px | Avoid tiny captions |

## Layout rules

- Use clear heading levels.
- Keep prose line length controlled.
- Use lists for grouped facts.
- Use tables for comparisons.
- Use callouts to distinguish recommendations, evidence, risks, and assumptions.
- Avoid relying on subtle grey-on-grey separation.
- Use visible focus states for links and controls.

## Colour rules

Colour may indicate status, but every status must also have a label.

Good:

```html
<span class="status status--blocked">Blocked</span>
```

Bad:

```html
<span class="dot red"></span>
```

## Print/export rules

For print-oriented artefacts:

- prefer the light theme
- avoid hidden navigation-only content
- avoid fixed-position UI that prints poorly
- keep links visible and descriptive
- make tables fit where possible
- avoid very dark backgrounds

## Common failures to avoid

- 13px body text
- pale grey metadata that carries meaning
- borders with `rgba(0,0,0,0.05)`
- status conveyed only by colour
- hover-only controls
- tables without visible row separation
- cards that rely only on shadow for boundaries
- icons without labels
- headings that do not describe the section
