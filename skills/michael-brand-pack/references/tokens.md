# Design tokens

## Table of contents

- [Source of truth](#source-of-truth)
- [Palette](#palette)
- [Signal extensions](#signal-extensions)
- [Dark theme](#dark-theme)
- [Typography](#typography)
- [Type roles](#type-roles)
- [Spacing and rhythm](#spacing-and-rhythm)
- [Widths](#widths)
- [Rules, radius, focus](#rules-radius-focus)
- [Tailwind v4 mapping](#tailwind-v4-mapping)
- [Email-safe values](#email-safe-values)

## Source of truth

The canonical tokens live in `src/app/globals.css` of [tools.michaelfbryan.com](https://github.com/Michael-F-Bryan/tools.michaelfbryan.com). [assets/css/tokens.css](../assets/css/tokens.css) mirrors them with the same names, so markup and CSS port both ways. If the site changes, update `tokens.css` and this file to match; do not drift.

Anything marked **extension** is not on the site yet. Use it only when the surface needs it, and keep it visually quieter than the accent.

## Palette

| Token | Hex | Use |
|---|---|---|
| `--paper` | `#f9fafb` | Page background |
| `--surface` | `#ffffff` | Raised band, hovered row, input field |
| `--panel` | `#f1f3f6` | Recessed block, figure ground, read-only field |
| `--ink` | `#17191d` | Headings, primary text, strong emphasis |
| `--text-secondary` | `#3f4956` | Running prose (the default body colour) |
| `--text-muted` | `#586372` | Captions, metadata, muted labels, step bodies |
| `--rule` | `#848d98` | Structural rules and borders (3:1+ on all surfaces) |
| `--rule-subtle` | `#c7ccd2` | Inner dividers between rows inside a ruled block |
| `--accent` | `#164dcc` | Links, kickers, step numbers, selected state, focus ring, key diagram strokes |
| `--error` | `#b42318` | Validation errors, blockers |

The palette has one accent. Tints come from `color-mix(in srgb, var(--accent) 10%, transparent)` rather than new tokens. Text selection uses the accent at 22%.

Contrast on `--paper`: ink 16.8:1, secondary 8.7:1, muted 5.8:1, accent 6.8:1, error 6.3:1, rule 3.2:1.

## Signal extensions

| Token | Light | Dark | Use |
|---|---|---|---|
| `--warning` | `#8a4b00` | `#f0b35a` | Risk, caution, unverified |
| `--success` | `#16693a` | `#6fcf8f` | Confirmed, done, passing |

Show signals as a coloured left rule or label text plus a written label ("Risk:", "Confirmed"). Do not add tinted callout backgrounds for every status.

## Dark theme

**Extension.** The site is light-only. `tokens.css` switches automatically under `prefers-color-scheme: dark` (unless `<html data-theme="light">`) and on `<html data-theme="dark">`. The structure stays the same: one accent, fine rules, square surfaces.

| Token | Dark |
|---|---|
| `--paper` | `#111317` |
| `--surface` | `#171a1f` |
| `--panel` | `#1f232a` |
| `--ink` | `#eef0f3` |
| `--text-secondary` | `#c3c9d1` |
| `--text-muted` | `#9ba4af` |
| `--rule` | `#6f7884` |
| `--rule-subtle` | `#343a43` |
| `--accent` | `#86a8ff` |
| `--error` | `#ff8a7a` |

## Typography

```css
--font-sans: "Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif;
--font-mono: "JetBrains Mono", "IBM Plex Mono", "Cascadia Code", monospace;
```

Atkinson Hyperlegible at weights 400 and 700 only. There is no medium or semibold, so emphasis is either regular or bold. Monospace is for labels, step numbers, term names in definition rows, numeric fields, and code. Never use it for body text.

Google Fonts: `https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap`

Letter-spacing gets tighter as type gets larger:

| Token | Value | Use |
|---|---|---|
| `--tracking-display` | `-0.035em` | Page title |
| `--tracking-heading` | `-0.03em` | Section title |
| `--tracking-title` | `-0.015em` | Site mark, catalogue titles, h3 |
| `--tracking-label` | `0.14em` | Uppercase mono labels |

## Type roles

The site uses Tailwind's default scale. These are the roles actually in use:

| Role | Size / line-height | Weight | Colour | Notes |
|---|---|---|---|---|
| Page title | 36px → 60px (sm+) / 1.08 | 700 | ink | `text-wrap: balance`; keep words unbroken |
| Workspace page title | 30px → 48px (sm+) / 1.08 | 700 | ink | Tools, so the tool starts on screen one |
| Section title | 30px → 36px (sm+) / 1.25 | 700 | ink | Balanced |
| Item title / h3 | 20px | 700 | ink | `--tracking-title` |
| Standfirst (`prose--xl`) | 20px / 36px | 400 | secondary | Opening or closing passage |
| Running prose (`prose`) | 18px / 32px | 400 | secondary | Default reading size |
| Supporting prose (`prose--base`) | 16px / 28px | 400 | secondary | Caveats, follow-on notes |
| Caption, nav, dense UI, step body | 14px / 24px | 400 | muted or secondary | Floor for sentences |
| Label / kicker | 12px mono, uppercase, 0.14em | 700 | accent or muted | Short labels only, never sentences |

## Spacing and rhythm

Spacing uses the 4px scale (Tailwind defaults). There are no separate spacing tokens; the rhythm lives in the components:

| Gap | Value |
|---|---|
| Kicker → section title | 16px |
| Section title → body | 28px |
| Between paragraphs | 24px |
| Between sections | 64px → 96px (sm+) |
| Body → list, figure, or table inside a section | 40px |
| Figure → caption | 20px |
| Row padding in ruled lists | 16–24px vertical |
| Page padding (entry) | 48px → 64px (sm+) top and bottom |
| Page padding (workspace) | 32px → 40px (sm+) |
| Side gutter | 20px → 32px (sm+) |

## Widths

| Token | Value | Use |
|---|---|---|
| `--container-page` | 70rem (1120px) | Page frame |
| `--container-article` | 52rem (832px) | Article column |
| `--container-measure` | 44rem (704px) | Running prose, captions, descriptions |

The on-this-page rail is 14rem with a 4rem gap, to the right of the article from 1024px.

## Rules, radius, focus

- Rules are 1px `--rule`. Inner dividers use `--rule-subtle`. Emphasis rules are 2px accent (aside note) or a solid accent bar (catalogue marker).
- Surfaces are square: bands, panels, figures, tables, inputs, and segmented controls have no radius. `--radius-sm` (4px) is for small badges; `--radius-md` (8px) is only for third-party controls that expect `--radius`.
- No shadows.
- Focus: `outline: 2px solid var(--accent); outline-offset: 4px`.
- Touch targets: 44px minimum height below 640px; compact from 640px up.

## Tailwind v4 mapping

In a Tailwind v4 or shadcn project, copy the `@theme inline` block and `:root` values from the site's `globals.css` rather than `tokens.css`. Utility names: `bg-paper`, `bg-surface`, `bg-panel`, `text-ink`, `text-secondary`, `text-muted`, `border-rule`, `border-rule-subtle`, `text-accent`, `text-error`, `tracking-display|heading|title|label`, `leading-display`, `max-w-page|article|measure`. shadcn aliases map onto the same palette (`primary` = accent, `border` = rule, `destructive` = error).

## Email-safe values

Email clients strip variables and web fonts. Paste hex values:

| Role | Hex |
|---|---|
| Text | `#17191d` |
| Secondary | `#3f4956` |
| Muted | `#586372` |
| Link / accent | `#164dcc` |
| Rule | `#c7ccd2` |

Font stack: `"Atkinson Hyperlegible", Arial, Helvetica, sans-serif`.
