# Email signatures and HTML email

Email clients strip `@import`, variables, and web fonts. Inline hex values from [tokens.md](tokens.md#email-safe-values).

## Signature block

**Plain text:**

```text
Michael F. Bryan
Michael-F-Bryan · www.michaelfbryan.com
```

**HTML (inline styles only):**

```html
<div style="font-family: 'Atkinson Hyperlegible', Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.5; color: #17191d;">
  <strong style="color: #17191d; letter-spacing: -0.01em;">Michael F. Bryan</strong><br />
  <span style="color: #586372;">Michael-F-Bryan <span style="color: #164dcc;">/</span> </span>
  <a href="https://www.michaelfbryan.com" style="color: #164dcc; text-decoration: underline;">www.michaelfbryan.com</a>
</div>
```

The accent slash echoes the site mark. Drop it if the client mangles nested spans.

## Colour mapping

| Role | Hex |
|---|---|
| Primary text | `#17191d` |
| Secondary text | `#3f4956` |
| Muted / metadata | `#586372` |
| Link / accent | `#164dcc` |
| Rule | `#c7ccd2` |
| Background (if used) | `#f9fafb` or white |

## HTML email constraints

- Use tables for layout if needed, not CSS grid/flex in critical structure.
- Minimum 14px body; 16px preferred for longer emails.
- Separate sections with a 1px `#c7ccd2` top border, not boxes or background fills.
- Every link gets an underline; do not rely on hover.
- Status colours must include text labels, not colour dots alone.
- Include a plain-text fallback with meaningful link URLs.

## Fonts

Name Atkinson Hyperlegible first so recipients who have it installed see it, with Arial/Helvetica as the real fallback. Do not embed woff2 files in signatures. Monospace labels are not worth the risk in email; use bold sans instead.
