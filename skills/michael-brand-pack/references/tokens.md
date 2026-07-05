# Design tokens

## Table of contents

- [Source of truth](#source-of-truth)
- [Light theme colours](#light-theme-colours)
- [Dark theme colours](#dark-theme-colours)
- [Typography scale](#typography-scale)
- [Spacing](#spacing)
- [Layout widths](#layout-widths)
- [Radius and borders](#radius-and-borders)
- [Email-safe fonts](#email-safe-fonts)
- [Usage](#usage)

## Source of truth

CSS variables live in [assets/css/tokens.css](../assets/css/tokens.css). Import before [assets/css/web-base.css](../assets/css/web-base.css).

## Light theme colours

| Token | Hex | Use |
|---|---|---|
| `--on-bg` | `#f7f4ec` | Page background |
| `--on-surface` | `#fffcf4` | Cards, panels |
| `--on-surface-alt` | `#ece6d8` | Code blocks, alt rows |
| `--on-text` | `#171717` | Primary text |
| `--on-text-secondary` | `#414853` | Secondary text |
| `--on-text-muted` | `#5f6b7a` | Metadata (still readable) |
| `--on-border` | `#b8b0a2` | Structural borders |
| `--on-border-subtle` | `#d6cec0` | Inner dividers |
| `--on-accent` | `#245c7a` | Links, primary accent |
| `--on-accent-strong` | `#007a8a` | Hover, emphasis |
| `--on-warning` | `#9a6700` | Caution |
| `--on-error` | `#a33a2b` | Blockers |
| `--on-success` | `#3f6b46` | Confirmed/done |
| `--on-info-bg` | `#e8f2f5` | Info callouts |
| `--on-warning-bg` | `#fff1ce` | Warning callouts |
| `--on-error-bg` | `#f8dfda` | Error callouts |
| `--on-success-bg` | `#e4f0e4` | Success callouts |

## Dark theme colours

Apply with `data-theme="dark"` on `<body>` or root container. See `tokens.css` `[data-theme="dark"]` block for full values.

Key shifts: background `#111418`, text `#f2efe7`, accent `#62c6d6`.

## Typography scale

| Token | rem | px | Use |
|---|---:|---:|---|
| `--on-text-xs` | 0.875 | 14 | Labels, compact metadata |
| `--on-text-sm` | 0.9375 | 15 | Dense UI minimum |
| `--on-text-md` | 1 | 16 | Compact body |
| `--on-text-body` | 1.0625 | 17 | Long-form default |
| `--on-text-lg` | 1.125 | 18 | Lead paragraphs |
| `--on-text-xl` | 1.3125 | 21 | h3 scale |
| `--on-text-2xl` | 1.625 | 26 | h2 scale |
| `--on-text-3xl` | 2.25 | 36 | Large display |
| `--on-text-4xl` | 2.75 | 44 | h1 cap |

Line heights: `--on-line-tight` 1.25, `--on-line-normal` 1.55, `--on-line-loose` 1.7.

Font stacks:

```css
--on-font-sans: Atkinson Hyperlegible, Inter, IBM Plex Sans, Source Sans 3, system-ui, …;
--on-font-mono: JetBrains Mono, IBM Plex Mono, Cascadia Code, Roboto Mono, …;
```

## Spacing

| Token | rem |
|---|---:|
| `--on-space-1` | 0.25 |
| `--on-space-2` | 0.5 |
| `--on-space-3` | 0.75 |
| `--on-space-4` | 1 |
| `--on-space-5` | 1.5 |
| `--on-space-6` | 2 |
| `--on-space-7` | 3 |
| `--on-space-8` | 4 |

## Layout widths

| Token | px | Use |
|---|---:|---|
| `--on-width-prose` | 820 | Long-form column |
| `--on-width-briefing` | 1120 | Default page shell |
| `--on-width-wide` | 1360 | Explainer / wide layouts |

## Radius and borders

| Token | Value |
|---|---|
| `--on-radius-sm` | 4px |
| `--on-radius-md` | 8px |
| `--on-radius-lg` | 12px |
| `--on-border-width` | 1px |
| `--on-border-width-strong` | 2px |

## Email-safe fonts

For HTML email and signatures, prefer web-safe stacks with brand colours inline:

- Sans: `Arial, Helvetica, sans-serif` (map accent `#245c7a`, text `#171717`, bg `#f7f4ec`)
- Avoid `@import`, custom woff2, and CSS variables — paste hex values directly.

## Usage

**Web:** link `tokens.css` then `web-base.css`.

**Dark UI:** `<body data-theme="dark">`.

**Print:** light theme preferred; see `web-base.css` print block.

**Rich HTML artefacts:** pair with html-rich-communication; see [html.md](html.md).
