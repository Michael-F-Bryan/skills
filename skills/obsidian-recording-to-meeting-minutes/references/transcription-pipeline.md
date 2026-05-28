# Transcript Pipeline Trade-offs

This note captures the preferred pipeline for long Obsidian meeting recordings.

## Recommended order

1. **Load vault rules first.** Read the vault's `AGENTS.md` before touching the note.
2. **Preserve the note.** Keep frontmatter, prep notes, and existing recording embeds.
3. **Merge recordings if needed.** If the note links multiple audio files, merge them into one scratch audio stream in note order.
4. **Run `scribe` once on the merged stream.** Treat transcription as the expensive step and avoid parallel fan-out here.
5. **Map speakers before polishing.** Use attendees + existing human notes + transcript anchors to map diarised labels.
6. **Plan chapters from the raw transcript.** Use one specialist to derive chapter boundaries and timestamps.
7. **Fan out chapter polishing.** Give each chapter to its own sub-agent when possible. Require `/transcript-polisher` in strict Obsidian mode.
8. **Merge conservatively.** Keep uncertain labels uncertain. Do not invent speaker confidence.
9. **QA with a dedicated sub-agent gate.** Validate structure and evidence before vault write.
10. **Write and verify manually.** Preserve the original embeds, then re-read at least early and later chapters.

## Why this trade-off

- `scribe` starts slowly and does the expensive model work, so parallel runs waste time and RAM.
- Chapter polishing is mostly cleanup and file handling, so it scales better across sub-agents.
- Small chapter contexts reduce cost and usually improve transcript accuracy.
- One chapter-planning pass keeps the coordinator context from bloating.
- Merged diarisation usually produces more stable speaker IDs than separate per-file transcription.

## Practical rule

**Transcribe once, map speakers, chapter-plan once, polish in parallel, then pass QA.**

If the recording is short enough that chaptering adds no value, skip the fan-out and keep the transcript in one pass.
