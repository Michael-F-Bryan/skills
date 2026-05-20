# Secondary Transcript Cross-Check

Use when a meeting note has both a local `scribe` transcript and an independent transcript source such as Google Meet/Gemini. The secondary transcript is evidence for correction, not a replacement for the note format.

## Pattern

1. Export or copy the secondary transcript to a scratch file under `/tmp/<slug>/`.
2. Split both transcripts into comparable time ranges. For long recordings, use 20–45 minute chunks or natural recording-file boundaries.
3. Compare each range independently and produce conservative corrections:
   - ASR term fixes supported by meeting context (`oil and gas`, `DPIRD`, product names, people, places)
   - speaker attribution fixes where the secondary transcript or conversation flow gives strong evidence
   - punctuation and sentence-boundary fixes only when they improve readability without changing meaning
4. Apply only high-confidence corrections to the polished transcript in the Obsidian note.
5. Re-read the final note and spot-check corrected terms, speaker names, recording embeds, and section order.

## Guardrails

- Do not paste a raw secondary transcript into the note by default.
- Do not wholesale replace the polished transcript with Google Meet/Gemini output; it often has its own speaker and ASR errors.
- Do not treat every difference as a correction. Prefer `leave unchanged` when evidence is weak.
- When a replacement suggestion is close but not exact, manually adjust it rather than applying mechanically.
- Report the correction pass briefly: number of corrections applied, notable classes of fixes, and any uncertainty.
