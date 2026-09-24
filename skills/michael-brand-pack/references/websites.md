# Websites and app chrome

The reference site is [tools.michaelfbryan.com](https://github.com/Michael-F-Bryan/tools.michaelfbryan.com): Next.js, Tailwind v4, tokens in `src/app/globals.css`, shared components in `src/components/`.

## Choosing an implementation

| Project | Use |
|---|---|
| Tailwind v4 / shadcn | Copy the site's `globals.css` (`@theme inline` + `:root`) and reuse its component class lists: `Container`, `PageTitle`, `Label`, `Section`, `SectionTitle`, `Prose`, `Steps`, `Figure` |
| Plain HTML/CSS | Link [tokens.css](../assets/css/tokens.css) and [web-base.css](../assets/css/web-base.css); use the matching classes below |
| Inline-only (artifact hosts, email) | Paste values from [tokens.md](tokens.md) |

Load Atkinson Hyperlegible (400, 700) through `next/font/google` or Google Fonts. Without it the page falls back to system sans and loses much of its character.

## Component map

| Site component | Plain-CSS class | Job |
|---|---|---|
| Header in `layout.tsx` | `.site-header` + `.site-mark` | `Michael F. Bryan <span class="slash">/</span> <span class="area">Tools</span>` over a bottom rule |
| `Container` | `.container` | 70rem frame, 20px → 32px gutters |
| `PageTitle` | `.page-title` | Display heading |
| `Label` | `.label`, `.label--muted` | Accent kicker; muted for metadata such as an entry's kind |
| `Section` | `.section` > `.label` + `.section-title` + `.section-body` | Titled section |
| `SectionTitle` | `.section-title` | Heading for custom section layouts |
| `Prose` | `.prose`, `.prose--xl`, `.prose--base` | Reading measure in secondary grey |
| `Steps` / `Step` | `ol.steps` > `li` > `.step-title` + `.step-body` | Numbered sequence |
| `Figure` | `figure.figure` > `figcaption` | Caption beneath; the figure picks its own frame |
| Catalogue list | `ol.catalogue` | Accent bar, title, description, kind label |
| Entry page | `.entry`, `.entry--workspace`, `.entry-grid`, `.toc` | Explainer with right-hand nav, or tool workspace |

## Page structure

```html
<header class="site-header">
  <div class="container">
    <a class="site-mark" href="/">Michael F. Bryan <span class="slash">/</span> <span class="area">Tools</span></a>
  </div>
</header>
<main class="entry">
  <div class="container entry-grid">
    <header class="entry-header">
      <span class="label label--muted">Explainer</span>
      <h1 class="page-title">Title that states the subject</h1>
      <div class="prose prose--xl"><p>One-paragraph description.</p></div>
    </header>
    <nav class="toc" aria-label="On this page">…</nav>
    <article class="entry-article stack">
      <section class="section" aria-labelledby="s1">
        <span class="label">Kicker</span>
        <h2 class="section-title" id="s1">Section title</h2>
        <div class="section-body prose"><p>…</p></div>
      </section>
    </article>
  </div>
</main>
```

Interactive tools use `.entry--workspace`: a short intro, no on-this-page rail, and the tool spanning the full page width, so it starts within the first screen on phones.

## Layout habits

- Lists of things are ruled rows, not cards: a top rule on the list and a bottom rule on each row.
- Emphasised blocks are full-width bands (`.band--surface` or `.band--panel`) bounded by top and bottom rules.
- Side notes use `.note`: a 2px accent left rule.
- Hover on a row raises it to `--surface`; hover on a link turns it accent and underlines it at a 4px offset.
- Keep subject-specific layouts and illustrations local to the page. Promote a pattern to a shared component only when the same job appears on more than one page.

## Controls

Use native elements styled with tokens: `.field` (square, 1px rule, surface fill, mono and right-aligned for numbers), read-only fields on `--panel` with `--rule-subtle`, `.segmented` toggle groups with `aria-pressed` (selected = accent fill, paper text), `.link-button` for secondary actions, and `accent-color` on range inputs. Errors are `role="alert"` text in `--error` at 14px. Reach for a component library only when native HTML cannot provide the interaction.

## Theme

Light by default, matching the site. `tokens.css` follows `prefers-color-scheme` unless `<html data-theme="light">` is set; force dark with `<html data-theme="dark">`.

## Identity

- Formal/public: **Michael F. Bryan**
- GitHub-adjacent: **Michael-F-Bryan**
- Area names after the accent slash: **Tools**, or whatever the site section is
- Locale: `lang="en-AU"`, Australian spelling

Recognition comes from type, rules, and the single blue, not from logos or initials.
