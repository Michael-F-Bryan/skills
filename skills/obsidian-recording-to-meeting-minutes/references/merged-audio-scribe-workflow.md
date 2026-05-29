# Merged audio + `scribe` workflow for Obsidian meeting notes

Use this when a note has multiple audio embeds and you want one polished chapterised transcript.

## What worked

- Resolve every embedded audio file first, then concatenate them in note order.
- Run `scribe` **once** on the merged audio.
- Use the diarised JSON output as the source of truth for chapter breaks and speaker runs.
- Use the human-written prep notes as speaker hints, not as hard facts.

## Command pattern

```bash
cat > /tmp/<slug>/concat.txt <<'EOF'
file '/path/to/Recording 1.m4a'
file '/path/to/Recording 2.m4a'
file '/path/to/Recording 3.m4a'
EOF

ffmpeg -y -f concat -safe 0 -i /tmp/<slug>/concat.txt -ar 16000 -ac 1 /tmp/<slug>/audio/merged.wav
scribe --format json -o /tmp/<slug>/scribe/merged.json /tmp/<slug>/audio/merged.wav
```

## `scribe` JSON shape

The JSON produced in this session had:

- `speakers`: a list of speaker IDs
- `segments`: a list of `{speaker, text, start, end}` objects

## Speaker mapping notes

- Map speakers with the meeting note’s diarisation hints first.
- If a speaker only appears in a few obvious lines, keep the label uncertain rather than forcing it.
- If the note already names a person in prep bullets, treat that as a clue, not proof.

## Chaptering notes

- Build chapters from topic shifts, not from fixed time slices alone.
- Titles work better when they name the topic and the decision pressure, not just the company or person.
- Keep the original audio embeds in the final note unless the user asks to remove them.

## Pitfalls

- Do not transcribe each embed separately when the note has several recordings from one meeting.
- Do not replace the prep notes with the transcript.
- Do not invent clean speaker names when the diarisation is weak.
- Do not leave duplicated `## Transcript` headers in the final note.