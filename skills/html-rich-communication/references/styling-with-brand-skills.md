# Styling with attached brand and voice skills

## Table of contents

- [Detect attached skills](#detect-attached-skills)
- [Division of labour](#division-of-labour)
- [CSS integration pattern](#css-integration-pattern)
- [Tailwind preflight and headings](#tailwind-preflight-and-headings)
- [shadcn token mapping](#shadcn-token-mapping)
- [Fallback without brand skill](#fallback-without-brand-skill)
- [Visual plan notes](#visual-plan-notes)
- [Common failures](#common-failures)

## Detect attached skills

Before building, check what the user attached:

- **@-mention** in the prompt (e.g. user @-tags a brand or voice skill)
- **Manually attached skills** in the agent session
- **Project instructions** (`AGENTS.md`) naming a default styling or voice skill

If a visual brand or design-system skill is attached, read it and apply its tokens, CSS, and visual rules. Do not invent a parallel palette.

If a voice or author-style skill is attached, read it for tone and content-structure rules.

## Division of labour

| Concern | Owner |
|---|---|
| Artefact brief, workflow, React scaffold, bundle, browser review | html-rich-communication (this skill) |
| HTML layout components, templates, progressive disclosure patterns | html-rich-communication |
| Colours, typography tokens, web-base CSS | Attached brand / design-system skill |
| Writing voice, recommendation patterns, artefact tone | Attached voice / author-style skill |

## CSS integration pattern

After `init-artifact.sh` creates `app/`:

```bash
mkdir -p app/src/styles
cp <html-rich-skill>/assets/css/document-components.css app/src/styles/
```

If a brand skill is attached (or `BRAND_SKILL_DIR` is set):

```bash
# Example only — use the actual attached skill path
cp "$BRAND_SKILL_DIR/assets/css/tokens.css" app/src/styles/
cp "$BRAND_SKILL_DIR/assets/css/web-base.css" app/src/styles/
```

Import order in `app/src/index.css`:

```css
@import './styles/tokens.css';        /* when brand attached */
@import './styles/web-base.css';      /* when brand attached */
@import './styles/document-components.css';

@tailwind base;
@tailwind components;
@tailwind utilities;
```

Brand skill owns colours and typography; html-rich owns artefact layout patterns (`doc-*` classes).

## Tailwind preflight and headings

Tailwind resets headings to `font-size: inherit` and `font-weight: inherit`. Without overrides, h1–h3 match body text.

Add scoped heading rules after Tailwind (in web-base.css from the brand skill, or a local override):

```css
.doc-page h1 {
  font-size: clamp(2.15rem, 4vw, 2.75rem);
  font-weight: 820;
  letter-spacing: -0.02em;
}

.doc-page h2 {
  font-size: clamp(1.65rem, 3vw, 2.25rem);
  font-weight: 780;
  letter-spacing: -0.018em;
  border-bottom: 1px solid var(--doc-border, #ccc);
  padding-bottom: 0.5rem;
}

.doc-page h3 {
  font-size: 1.3125rem;
  font-weight: 740;
}

section[id] > h2:first-child {
  margin-top: 0;
}
```

Wrap page content in `<main class="doc-page">`. Verify at 100% zoom in browser.

## shadcn token mapping

When using shadcn/ui with an attached brand skill, map shadcn CSS variables to that skill's tokens in `@layer base :root` so interactive components match the brand theme. Prefer brand callout/panel classes for content blocks; use shadcn for interaction primitives (Accordion, Tabs, Checkbox).

## Fallback without brand skill

html-rich ships neutral defaults in `assets/css/document-components.css` (`--doc-*` variables). Use accessible neutrals from [visual-elements.md](visual-elements.md). Do not invent a branded palette when no brand skill is present.

## Visual plan notes

In `visual-plan.md`, record:

- Whether a brand skill and voice skill are attached
- Reader job (decide, learn, operate, verify, etc.)
- Which html-rich templates apply (`assets/templates/document/`)
- Components to include or omit by reader job — see [document-component-patterns.md](document-component-patterns.md)

## Common failures

| Symptom | Fix |
|---|---|
| Headings look like body text | Scoped `.doc-page h1–h3` after Tailwind; wrap in `.doc-page` |
| Decision-brief chrome on explainer | Re-check reader job; use mentoring template; omit status strip |
| Duplicate code across sections | One canonical example per pattern; link elsewhere |
| Thin accordion panels | Meet progressive disclosure minimum in document-component-patterns |
| init-artifact wrong directory | Run from working folder with relative `app` name |
