# Michael Brand Pack

Visual design system for Michael F. Bryan / Michael-F-Bryan branded surfaces: websites, tools, email, documents, slides, and rich HTML artefacts.

Tokens and components mirror [tools.michaelfbryan.com](https://github.com/Michael-F-Bryan/tools.michaelfbryan.com) (`src/app/globals.css`, `src/components/`). Crisp near-white paper, dark ink, one cool-blue accent, Atkinson Hyperlegible, monospace labels, fine rules.

Operator Notes is an optional surface label, not the governing abstraction for every artefact.

## Quick start

1. Read [SKILL.md](SKILL.md) channel router.
2. Load [references/tokens.md](references/tokens.md) for values.
3. Start from a template when useful:
   - [templates/rich-html-document.html](templates/rich-html-document.html)
   - [templates/tool-workspace.html](templates/tool-workspace.html)
   - [templates/email-signature.html](templates/email-signature.html)
   - [templates/style-calibration.md](templates/style-calibration.md)
4. For web, link [assets/css/web-base.css](assets/css/web-base.css), which imports [assets/css/tokens.css](assets/css/tokens.css). For Tailwind v4, copy the site's `globals.css`.

## Pairing

| This skill | Companion |
|---|---|
| Visual tokens, CSS, channel guides, templates | [html-rich-communication](../html-rich-communication/SKILL.md) — HTML workflow and templates |
| — | [voice-michael](../voice-michael/SKILL.md) — writing voice |

## Layout

```text
michael-brand-pack/
├── SKILL.md
├── README.md
├── references/
│   ├── visual-language.md
│   ├── tokens.md
│   ├── websites.md
│   ├── email.md
│   ├── documents.md
│   └── html.md
├── templates/
│   ├── rich-html-document.html
│   ├── tool-workspace.html
│   ├── email-signature.html
│   └── style-calibration.md
└── assets/
    └── css/
        ├── tokens.css
        └── web-base.css
```

## Default identity

```text
Michael F. Bryan · Michael-F-Bryan
www.michaelfbryan.com
tools.michaelfbryan.com
```

Use `Operator Notes` only when the user or surface explicitly calls for that label.
