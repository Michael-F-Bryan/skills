# Implementation routing

Pick the smallest surface that serves the communication contract.

## Markdown

Use for short answers, editable drafts, first-feedback, or when rich layout would add friction.

Verify by reading against the contract and checking links/claims.

## Static single-file HTML

Default rich lane. Use for shareable visual documents, reports, explainers, PR aids, simple decks, and light custom editors.

Allowed: inline CSS, inline SVG, small inline JavaScript, native `<details>`, tables, forms, buttons, local assets inlined or colocated when privacy allows.

Verify in a browser over local HTTP. Check responsive layout, no accidental external runtime dependencies, links, controls, and print if relevant.

## React app

Use only when one or more are true:

- complex state or many coordinated controls;
- shadcn/Radix components materially reduce risk;
- bundled charts/diagrams need npm packages;
- artefact is likely to be maintained or extended;
- interaction is too complex for small inline JS.

From `_working/<topic>/`:

```bash
bash <skill-root>/scripts/init-artifact.sh app
cd app
# implement
bash <skill-root>/scripts/bundle-artifact.sh
cp bundle.html ../final/bundle.html
```

Do not use React just because the output is HTML.

## Custom editor

The export is part of the product. For throwaway triage/sorting boards, prefer a single static HTML file with inline JS and a visible export/copy control. Do not scaffold React unless state or coordination is genuinely complex.

Before building, write the export contract: format, ordering, fields, and one sample exported item. For throwaway editors, a three-line contract is enough: task, visible buckets/fields, export format.

Required checks:

- every control exercised;
- validation/warnings visible;
- copy/export button works;
- exported Markdown/JSON/diff/prompt inspected and matched against the visible state.

## Deck HTML

Use when the artefact will be presented sequentially. Required checks: first slide answers the meeting question, keyboard navigation works, and appendix/detail does not dominate the main path.
