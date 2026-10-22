# Michael’s skills

All retained skills live in `skills/`. Activate by task scope, not simply because a skill is installed.

| Skill | Scope / owner |
|---|---|
| code-like-michael | Engineering decisions, implementation, testing and verification |
| voice-michael | First-draft communication and editing |
| working-docs | Task memory when continuity or evidence needs it |
| risk-calibrated-agent-reviews | Whether independent judgement warrants a review |
| html-rich-communication | Explanatory structure, rendering and recipient accessibility |
| adaptive-decision-interviews | Human judgement before authorised drafting, not routine clarification |
| knowledge-base-navigator | Direct source retrieval and counterevidence |
| wait-for-ci | Low-noise waiting tied to an exact commit |
| temporal-applications-python | Specialist engineering with the Temporal Python SDK |
| obsidian-cli | Actual Obsidian CLI operations, not generic notes or coding |
| michael-brand-pack | Personal sites/tools or explicit Michael branding, not every HTML or company report |
| dumc-email-to-obsidian-notes | Michael’s CSU/DUM-C source preservation, not general engineering/email policy |

## Installation

Use the [skills CLI](https://github.com/vercel-labs/skills), selecting the skills relevant to the target:

```console
npx skills add Michael-F-Bryan/skills --skill code-like-michael --skill voice-michael
```

Inspect the installer’s target and resulting inventory. Source changes do not automatically update deployed profiles or project copies. `.agents/skills/` contains authoring dependencies recorded in `skills-lock.json`, not the curated runtime catalog.

## Ownership and evaluation

Jake-tools/Clockify guidance belongs to the owning package. The obsolete transcript executor and unvalidated coding-fingerprint wizard are removed; concise [fidelity lessons](docs/transcript-fidelity.md) remain, with transcript evals marked inactive. Note formatting is [opt-in local policy](docs/note-conventions.md), not standalone skills. See [migration](docs/migrations.md).

Cases under `evals/` are behavioural probes, not a framework. Historical calibration is separate from execution guidance. See [validation status](docs/validation.md) for what actually ran.

MIT licensed; see [LICENSE](LICENSE).
