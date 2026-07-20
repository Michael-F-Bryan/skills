# Websites and app chrome

Apply [tokens.md](tokens.md) via [assets/css/tokens.css](../assets/css/tokens.css) and [assets/css/web-base.css](../assets/css/web-base.css).

## Page structure

```html
<body>
  <main class="on-page">
    <article class="on-shell">
      <!-- content -->
    </article>
  </main>
</body>
```

Use `.on-shell--wide` for explainer-width layouts. Use `.on-prose` to cap line length on long text columns.

## Theme

Default light theme on `<body>`. Dark theme for tools and dashboards:

```html
<body data-theme="dark">
```

## Typography on web

Import both CSS files in order. Headings in `web-base.css` use token scale — verify at 100% zoom after any CSS reset (Tailwind preflight, etc.).

When using React or Tailwind, ensure the brand token and web-base layers win over framework resets; reassert heading sizes after preflight if necessary. Do not add a separate visual-plan workflow.

## Identity

- Formal/public: **Michael F. Bryan**
- GitHub-adjacent: **Michael-F-Bryan**
- Mark: **MFB** sparingly

Do not overuse initials, fake terminal motifs, or logo-heavy styling. Recognition comes from structure and palette, not decoration.

## Mood

See [visual-language.md](visual-language.md). Personal sites should feel like readable technical documents, not SaaS landing pages.
