# Email signatures and HTML email

Email clients strip `@import`, variables, and many modern CSS features. Inline hex values from [tokens.md](tokens.md).

## Signature block (plain text + minimal HTML)

**Plain text:**

```text
Michael F. Bryan
Michael-F-Bryan · michael-f-bryan.com
```

**HTML (inline styles only):**

```html
<div style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; line-height: 1.5; color: #171717;">
  <strong style="color: #171717;">Michael F. Bryan</strong><br />
  <span style="color: #414853;">Michael-F-Bryan · </span>
  <a href="https://michael-f-bryan.com" style="color: #245c7a; text-decoration: underline;">michael-f-bryan.com</a>
</div>
```

## Colour mapping

| Role | Hex |
|---|---|
| Primary text | `#171717` |
| Secondary | `#414853` |
| Link / accent | `#245c7a` |
| Background (if used) | `#f7f4ec` |

## HTML email constraints

- Use tables for layout if needed — not CSS grid/flex in critical structure.
- Minimum 14px body; 15–16px preferred for readability.
- Every link gets underline or obvious colour — do not rely on hover.
- Status colours must include text labels, not colour dots alone.
- Test in plain-text fallback; include meaningful link URLs.

## Fonts

Stick to Arial, Helvetica, Georgia, or system sans. Do not embed custom woff2 in signatures.
