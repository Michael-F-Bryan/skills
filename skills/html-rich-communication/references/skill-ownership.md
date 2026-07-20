# Rich HTML skill ownership

`html-rich-communication` is the single owner of the normal design → build → verify → publish lane.

The former Hermes-curated skills are retained as narrow overlays so their trigger names remain useful without multiplying work:

| Skill | Narrow responsibility | Legacy curated copy to reconcile |
|---|---|---|
| `rich-communication-artifact-design` | Resolve a genuinely ambiguous reader job | `~/.hermes/skills/communication/rich-communication-artifact-design` |
| `technical-system-explainer` | Shape technical content around one worked path | `~/.hermes/skills/communication/technical-system-explainer` |
| `rich-html-artifact-delivery` | Publish an already verified file | `~/.hermes/skills/communication/rich-html-artifact-delivery` |
| `html-artifact-publishing` | Debug a failed hosted preview only | `~/.hermes/skills/productivity/html-artifact-publishing` |
| `rendered-artifact-verification` | Verify generated configuration/runtime outputs, not ordinary static HTML | `~/.hermes/skills/software-development/rendered-artifact-verification` |
| `michael-brand-pack` | Visual identity | existing shared installation |
| `voice-michael` | Writing voice | existing shared installation |

These source-controlled versions replace same-named automatically curated copies. After this branch is merged and installed, remove the old `~/.hermes/skills/...` copies or replace them with symlinks to the shared `~/.agents/skills/<name>` installation. Verify each bare `skill_view(<name>)` resolves unambiguously to the source-controlled copy. Do not leave duplicate names active.

The heavy references under `html-rich-communication` remain available for observable extended-lane conditions. They are not a default checklist.
