# Document component patterns

HTML layout patterns for rich artefacts. Class prefix: `doc-*`. Styles in [assets/css/document-components.css](../assets/css/document-components.css).

## Table of contents

- [Reader job × components](#reader-job--components)
- [Decision-oriented blocks](#decision-oriented-blocks)
- [Explainer layouts](#explainer-layouts)
- [Progressive disclosure](#progressive-disclosure)
- [Example ownership](#example-ownership)

## Reader job × components

| Component | decide | learn | operate | verify |
|---|---|---|---|---|
| Status strip | ✓ | — | ✓ | optional |
| Current read | ✓ | — | optional | optional |
| Recommendation | ✓ | — | optional | if verdict |
| Trade-off table | ✓ | optional | optional | ✓ |
| Risk block | ✓ | optional | ✓ | ✓ |
| Next move / CTA | ✓ | — | ✓ | — |
| Section panel | optional | ✓ | ✓ | ✓ |
| Boundary diagram | optional | ✓ | ✓ | optional |
| Compare pair | optional | ✓ | optional | optional |
| Sidebar nav | optional | ✓ | optional | ✓ |
| Evidence badges | ✓ | ✓ | ✓ | ✓ |

Route by html-rich artefact brief **Reader job**. Do not apply decision-brief chrome to teaching explainers.

Templates: [assets/templates/document/](../assets/templates/document/).

## Decision-oriented blocks

### Status strip (`.doc-status-strip`)

Near top of decide/operate artefacts. Fields: Status, Owner, Updated, Confidence, Scope.

### Current read (`.doc-callout--read`)

Interpretation first — when the artefact needs judgement, not just information.

### Recommendation (`.doc-callout--recommendation`)

Pattern:

```text
Recommendation: Do X.
Why: Y.
Trade-off: Z.
Next move: A.
```

### Trade-off table

Columns: Option | Upside | Downside | Read

### Risk block (`.doc-callout--warning`)

Fields: risk, impact, likelihood, severity, mitigation. Severity: Low / Medium / High / Blocker.

### Next move

Concrete actions — not “improve robustness” or “align stakeholders”.

## Explainer layouts

Use with [assets/templates/document/mentoring-explainer.html](../assets/templates/document/mentoring-explainer.html).

### Section panel (`.doc-section`)

Section boundaries obvious in long explainers. 4+ major topics.

```html
<section id="topic" class="doc-section">
  <h2>Topic title</h2>
  <p>Content…</p>
</section>
```

### Sidebar nav (`.doc-layout-with-nav`, `.doc-side-nav`)

Sticky section links for 4+ sections. Stacks above content on mobile.

```html
<div class="doc-layout-with-nav">
  <nav class="doc-side-nav" aria-label="On this page">
    <strong>On this page</strong>
    <a href="#section-id">Section title</a>
  </nav>
  <div><!-- sections --></div>
</div>
```

### Boundary diagram (`.doc-boundary-diagram`)

Core vs replaceable external edges — testing, architecture teaching.

```html
<div class="doc-boundary-diagram" role="img" aria-label="Describe the diagram">
  <div class="doc-boundary-diagram__core">Core — keep real</div>
  <div class="doc-boundary-diagram__edges">
    <div class="doc-boundary-diagram__edge">External API</div>
  </div>
</div>
```

### Compare pair (`.doc-compare`)

Side-by-side bad/good code — **one canonical home** per example.

```html
<div class="doc-compare__pair">
  <p class="doc-compare__pair-label">Pair 1 — short label</p>
  <div class="doc-compare__bad"><h3>✕ Bad</h3><pre><code>…</code></pre></div>
  <div class="doc-compare__good"><h3>✓ Better</h3><pre><code>…</code></pre></div>
</div>
```

### Centred hero (`.doc-hero--centered`)

Thesis-first explainer header. Minimal metadata (e.g. Updated date). Omit status strip and recommendation CTA for learn job.

### Glossary (`.doc-glossary`)

Define jargon once near the hero.

## Progressive disclosure

Use `<details>` / accordion only when the panel earns hiding:

| Minimum | Requirement |
|---|---|
| Context | 2+ sentences explaining why this matters |
| Substance | 3+ bullets **or** a bad/good code pair |
| Action | At least one “what to do instead” item |

Do not accordion a single sentence — use an open bullet list.

## Example ownership

Each code example has one **canonical section**. Other sections link or deepen — do not repeat the same snippet in tabs, accordions, and compare blocks.

Before adding a tab, accordion, or new section, ask: is this the canonical home, a link, or genuinely new value?

Voice and tone for content: use an attached voice / author-style skill when present.
