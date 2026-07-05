# Implementation Notes

## Recommended generation workflow

When producing a new artefact with this skill:

1. Identify the artefact type:
   - briefing
   - decision record
   - technical report
   - incident review
   - system handoff
   - dashboard/tool
2. Write the current read first.
3. Write the recommendation or decision second.
4. Add evidence, trade-offs, risks, and assumptions.
5. Add next actions.
6. Apply the visual system.
7. Check readability and contrast.
8. Remove decorative elements that do not improve comprehension.

## Standalone HTML approach

For portable HTML artefacts, inline the CSS:

```html
<style>
/* paste tokens.css here */
/* paste operator-notes.css here, removing the @import */
</style>
```

Keep the HTML semantic:

- `main` for page content
- `article` for the artefact
- `header` for title and metadata
- `section` for major content blocks
- `nav` for document navigation
- `table` for comparisons
- `ol` for ordered action lists
- `ul` for unordered evidence or risks

## Theme usage

Default light theme:

```html
<body>
```

Dark theme:

```html
<body data-theme="dark">
```

Use dark theme for tools, demos, dashboards, and long-running screen work. Use light theme for reports, briefs, and PDF/printable artefacts.

## Status labels

Use a small vocabulary:

- Draft
- Proposed
- Recommended
- Accepted
- In progress
- Blocked
- Done
- Superseded
- Deprecated

Status should always be labelled in text. Colour can reinforce it, but must not be the only signal.

## Component naming convention

CSS classes use `on-` as a namespace for Operator Notes.

Examples:

- `on-shell`
- `on-header`
- `on-status-strip`
- `on-callout`
- `on-callout--recommendation`
- `on-table-wrap`

Avoid global component class names like `.card`, `.button`, `.warning`, or `.panel` in generated artefacts, because they collide easily when embedded elsewhere.

## Suggested file naming

For artefacts:

```text
YYYY-MM-DD-topic-briefing.html
YYYY-MM-DD-topic-decision-record.html
YYYY-MM-DD-topic-technical-report.html
```

Examples:

```text
2026-07-05-agent-handoff-briefing.html
2026-07-05-prototype-recovery-decision-record.html
```

## Quality checklist

Before considering an artefact done:

- [ ] The current read is visible near the top.
- [ ] The recommendation or decision is not buried.
- [ ] Important text is readable at 100% zoom.
- [ ] Secondary text is readable, not faint.
- [ ] Borders are visible where they carry structure.
- [ ] Colour is not the only status signal.
- [ ] Trade-offs are shown as a table where useful.
- [ ] Risks and assumptions are visually distinct.
- [ ] Next actions are concrete.
- [ ] The artefact prints reasonably if it is document-like.
- [ ] The document does not look like generic SaaS/template output.

## Practical customisation points

Change these first if post-processing:

- `css/tokens.css` colour variables
- font stack in `--on-font-sans`
- page widths
- border contrast
- callout left-border thickness
- status labels
- footer identity

Avoid changing everything at once. The recognisable feel comes from structure and spacing as much as colour.
