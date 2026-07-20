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

Start with static HTML and small inline JavaScript. Promote to React only when one or more are true:

- the same mutable state drives three or more independent views or control groups;
- accessible drag/drop, keyboard interaction, undo/redo, or similarly stateful behaviour needs mature primitives;
- shadcn/Radix components materially reduce risk;
- bundled charts/diagrams need npm packages;
- artefact is likely to be maintained or extended;
- a concrete failure in the static approach shows that small inline JavaScript is becoming brittle.

Control count alone is not a reason to promote.

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

Before building, write the export contract: format, ordering, fields, active selection, and whether filter/sort/tag state that affects the visible result is included or intentionally omitted. Include one sample exported item. For throwaway editors, a compact contract is enough: task, visible buckets/fields, material view state, export format.

Required checks:

- every control exercised;
- validation/warnings visible;
- copy/export button works;
- exported Markdown/JSON/diff/prompt inspected and matched against the visible selection and material filter/sort/tag state.

## Deck HTML

Use when the artefact will be presented sequentially. Required checks: first slide answers the meeting question, keyboard navigation works, and appendix/detail does not dominate the main path.
