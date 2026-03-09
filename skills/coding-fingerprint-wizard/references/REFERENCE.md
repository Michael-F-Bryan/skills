# Coding Fingerprint Wizard References

Read supporting files only when the current phase needs them.

## Choose a file

- Read [analysis-worksheet.md](analysis-worksheet.md) before creating or checking any `_working/coding-fingerprint/` artefact. It is the source of truth for required files, required sections, handoff rules, and the default sub-agent prompt skeleton.
- Read [fingerprint-template.md](fingerprint-template.md) only in Phase 4 when generating the final `coding-fingerprint-[name]/SKILL.md`.
- Read [example-coding-fingerprint.md](example-coding-fingerprint.md) only when the output shape is unclear or when calibrating the finished fingerprint against a worked example.

## Default order

1. Start with `SKILL.md`.
2. Read `analysis-worksheet.md` before Phase 1 and again whenever you need the exact contract for a phase output.
3. Read `fingerprint-template.md` only when Phase 4 begins.
4. Read `example-coding-fingerprint.md` only if the template still leaves the target shape ambiguous or you are doing a final quality check.

## Phase routing

- Coordinator setup: `SKILL.md`, then `analysis-worksheet.md`
- Discovery workers: `analysis-worksheet.md`
- Synthesis workers: `analysis-worksheet.md`
- Challenge workers: `analysis-worksheet.md`
- Delivery worker: `fingerprint-template.md`
- Calibration or QA: `example-coding-fingerprint.md`
