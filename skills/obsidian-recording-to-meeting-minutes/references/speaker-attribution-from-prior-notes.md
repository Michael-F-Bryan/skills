# Speaker attribution using prior notes

Use this when a meeting recording has diarised `SPEAKER_XX` labels and the vault contains better-diarised notes with overlapping attendees.

## Pattern

1. Search the relevant area for prior meeting notes with the same attendees or a subset of them.
2. Prefer notes where transcript speaker labels are already human names and the user has indicated the diarisation is good.
3. Start with the current note first: attendee frontmatter and human-written notes in the note body are higher-priority evidence than style matching.
4. Because transcription came from one merged audio stream, treat diarised IDs as globally stable by default.
5. Extract short “fingerprints” for each person:
   - recurring phrases and hedges (`I reckon`, `I guess`, etc.)
   - topic ownership and domain language
   - thinking style: technical/systemic, commercial/practical, process/alignment, facilitation/advisory
   - turn length and conversational role
6. Compare fingerprints against diarisation clusters across the meeting; only downgrade to chunk-local caveats when the evidence conflicts.
7. Use contextual anchors before text statistics: explicit names, role in the room, “your company”/“our team” framing, anecdotes only one attendee would know, and direct replies.
8. If using automated text stats, treat them as weak evidence. Small anchor corpora can overfit badly, especially when several speakers discuss the same topic.
9. Rewrite labels only where the evidence improves confidence. Leave ambiguous labels unchanged or mention uncertainty in the final.

## Confidence cues (general)

- Facilitators are often easiest: long framing turns, agenda control, and process handoffs can identify them more reliably than word frequency.
- Technical owners often cluster around implementation constraints, architecture details, and systems language.
- Commercial owners often cluster around customer impact, budgets, risk, and execution trade-offs.
- Process/alignment voices often focus on decision clarity, next-step framing, and team coordination.
- Treat these as weak-to-medium cues unless anchored by explicit evidence.

## Pitfalls

- Do not ignore attendee/frontmatter evidence in favour of pure style matching.
- Do not rely only on a bag-of-words classifier; shared meeting vocabulary can swamp individual style.
- Do not over-fit one prior meeting where the topic was very different.
- Do not silently change many labels without recording the mapping and confidence in your final response.
