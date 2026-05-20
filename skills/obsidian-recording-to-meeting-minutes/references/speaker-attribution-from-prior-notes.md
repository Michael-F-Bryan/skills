# Speaker attribution using prior notes

Use this when a meeting recording has diarised `SPEAKER_XX` labels and the vault contains better-diarised notes with overlapping attendees.

## Pattern

1. Search the relevant area for prior meeting notes with the same attendees or a subset of them.
2. Prefer notes where transcript speaker labels are already human names and the user has indicated the diarisation is good.
3. Extract short “fingerprints” for each person:
   - recurring phrases and hedges (`I reckon`, `I guess`, etc.)
   - topic ownership and domain language
   - thinking style: technical/systemic, commercial/practical, process/alignment, facilitation/advisory
   - turn length and conversational role
4. Compare fingerprints against each raw diarisation cluster *per chunk*. Treat `SPEAKER_01` as local to the recording file, not global across all chunks.
5. Use contextual anchors before text statistics: explicit names, role in the room, “your company”/“our team” framing, anecdotes only one attendee would know, and direct replies like “Morgan, you were one”.
6. If using automated text stats, treat them as weak evidence. Small anchor corpora can overfit badly, especially when several speakers discuss the same topic.
7. Rewrite labels only where the evidence improves confidence. Leave ambiguous labels unchanged or mention uncertainty in the final.

## Confidence notes from the beachhead-market session

- Facilitators are often easiest: long framing turns, agenda control, and unique career anecdotes can identify them more reliably than word choice.
- Michael-style anchors in Sunfish notes often include technical/systemic reasoning, data architecture, product constraints, modelling, and phrases like “I reckon” / “I guess”.
- Morgan-style anchors often include commercial mechanics, strategic trade-offs, customer and budget practicality, relationship/reputation risk, and “what will this unblock?” framing.
- Nikki-style anchors often include process, alignment, decision clarity, where thinking has landed, and how the team should reason together.
- Taylor may need more caution if fewer well-diarised anchors exist; avoid over-confident Taylor assignments from residual matching alone.

## Pitfalls

- Do not treat diarisation IDs as identities across split recordings.
- Do not rely only on a bag-of-words classifier; shared meeting vocabulary can swamp individual style.
- Do not over-fit one prior meeting where the topic was very different.
- Do not silently change many labels without recording the mapping and confidence in your final response.
