# Multi-chunk Obsidian recordings

Use this when one meeting note embeds several audio files, usually because recording paused during breaks.

## Reusable pattern

1. Extract all `![[...m4a]]`, `![[...mp3]]`, or `![[...wav]]` embeds from the target note.
2. Resolve each file under the vault, normally `Attachments/`.
3. Sort chunks by timestamp in the filename when present, e.g. `Recording 20260520105435.m4a`, `Recording 20260520111705.m4a`, `Recording 20260520124103.m4a`.
4. Transcribe each chunk separately to `/tmp/<slug>/<recording>.json` with `scribe --format json`.
5. Compute durations from JSON segment end times and/or `ffprobe`.
6. Compare filename timestamps, durations, and transcript boundary text to detect gaps/overlap. Do not silently make overlapping files continuous; document the chosen offset rule in the manifest.
7. Split long files into 20–45 minute chunk windows for transcript-polishing subagents. Natural topic/file boundaries are better than perfectly equal sizes.
8. When drafting `## Key details`, preserve every recording embed and state that chunks are ordered by filename timestamps.
9. In `## Transcript`, use continuous timestamps from the agreed start of the first chunk, not per-file timestamps that restart at `00:00`.
10. Treat speaker labels as chunk-local. Diarisation IDs can change between files, so map speakers independently per chunk using attendees, content, and speaking patterns. If the vault has better-diarised notes with overlapping attendees, use `references/speaker-attribution-agent.md` and `references/speaker-attribution-from-prior-notes.md` before assigning final names.

## Pitfalls

- Do not transcribe only the first embed.
- Do not assume `SPEAKER_01` is the same person in every chunk.
- Do not leave the middle chunks out of the note body just because they were short.
- Do not create a raw transcript section; keep scratch JSON/transcript artefacts in `/tmp` unless the user asks to store them.
- If another processed note for the same meeting already exists, read it as context, but still ground the final note in the target recordings and preserve the target note’s frontmatter unless deliberately merging notes.
