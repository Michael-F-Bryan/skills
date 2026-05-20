# Coordinator workflow

Use this as the coordinator’s playbook. The coordinator owns orchestration, not transcript cognition.

## Purpose

Convert a sparse Obsidian note plus recordings into a verified meeting note while keeping the main context small. The coordinator should pass paths, manifests, and narrow chunks to specialists rather than loading entire transcripts.

## Values

- Source-grounded over plausible.
- Thin coordinator over heroic single-session editing.
- Scratch files over huge prompts.
- Conservative merge over silent invention.
- Preserve vault conventions, frontmatter, and recording embeds.

## Inputs

- Target note path or title.
- Vault path and `AGENTS.md` rules.
- Recording embeds and resolved audio paths.
- Attendee frontmatter and any user hints.
- Optional secondary transcripts.

## Required outputs

Write these under `/tmp/<slug>/`:

- `manifest.json` with note path, attendees, recording paths, durations, chunk windows, offsets, and output paths.
- `scribe/*.json` diarised transcript files.
- `agent-outputs/speaker-attribution.md`
- `agent-outputs/polished-chunk-NN.md`
- `agent-outputs/minutes.md`
- optional `agent-outputs/secondary-corrections-NN.json`
- `agent-outputs/qa-audit.md`
- `final-note.md` before touching the vault.

## Steps

1. Read vault rules and target note.
2. Parse every audio embed; resolve every file. If any recording is ambiguous, stop and ask.
3. Run `scribe --format json` for each recording into `/tmp/<slug>/scribe/`.
4. Compute durations and chunk windows. Prefer file boundaries; split long files into 20–45 minute windows.
5. Build `manifest.json`. Include enough metadata for specialists to work without full coordinator context.
6. Dispatch speaker attribution first.
7. Dispatch transcript-polishing subagents per chunk with `delegate_task` (or the platform’s equivalent). Give each only the relevant JSON/text excerpt path, speaker-attribution output, style requirements, and output path.
8. Dispatch secondary transcript cross-checkers when secondary evidence exists; apply high-confidence corrections to chunk outputs.
9. Dispatch minutes extraction from corrected chunk summaries and timestamp evidence.
10. Merge outputs into `final-note.md` using `references/final-note-template.md`; apply only high-confidence corrections.
11. Dispatch QA/audit on the final draft and evidence manifest.
12. Fix audit blockers, write the vault note, re-read, run structure checks, and manually skim.

## Single-session mode (no subagents)

When the platform cannot spawn subagents, keep the **same phase boundaries and files**; only the executor changes. The coordinator must not load entire transcripts into prompts—always read/write paths under `/tmp/<slug>/`.

1. Complete steps 1–5 as usual (vault rules, embeds, `scribe`, manifest, chunk excerpts on disk).
2. **Speaker attribution:** Open `references/speaker-attribution-agent.md`, follow it in a fresh context window *or* complete the task in the coordinator while passing only manifest paths + small JSON excerpts (never the full meeting JSON inline if it exceeds a comfortable read size—read from `chunks/chunk-NN.json` on disk).
3. **Polishing:** For each chunk, follow `references/transcript-polishing-agent.md` with inputs limited to that chunk’s excerpt files + speaker output; write `agent-outputs/polished-chunk-NN.md`.
4. **Secondary checks:** If applicable, follow `references/secondary-transcript-agent.md` per chunk; write JSON corrections only.
5. **Minutes:** Follow `references/minutes-extraction-agent.md`; write `agent-outputs/minutes.md`.
6. **Merge** into `final-note.md` using `references/final-note-template.md`.
7. **QA:** Follow `references/qa-audit-agent.md` on `final-note.md`; apply fixes, then write to the vault.

If a single step would require pasting more than ~30–50 KB of transcript text into chat, stop and split the work (smaller chunk files, another read pass from disk) instead of pasting.

## Good coordinator behaviour

- “Single-session mode: finished speaker map from disk excerpts, polished chunk 02 to `agent-outputs/polished-chunk-02.md` without pasting the full JSON.”
- “This decision has no timestamp evidence, so I moved it to open questions.”
- “Speaker mapping is uncertain for Taylor in chunk 02; the final note preserves that caveat.”

## Bad coordinator behaviour

- Pasting a 200 KB transcript into the main context.
- Writing the vault note before speaker attribution and polish review.
- Treating `SPEAKER_01` as globally stable.
- Summarising decisions without timestamp evidence.
