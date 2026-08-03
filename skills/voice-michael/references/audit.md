# Audit reference (Michael)

**Scope:** load this only when editing or evaluating completed prose — never while drafting. Identify the smallest material correction; `good as-is` is an acceptable verdict.

**Register:** these rules are strict for polished public prose, operator artefacts, decision notes, and docs. Forum/help replies deliberately relax several of them — check the register table in [forum-help.md](forum-help.md) before flagging conversational markers there.

## The Michael Test

Revise if any answer is no:

1. **Substance** — Does it teach, decide, or transfer something real? Signature phrasing without a lesson is seasoning with no dish.
2. **Peer tone** — Skilled colleague to colleague, not guru, textbook, or influencer.
3. **Concrete first** — Working code, scenario, or observation before (or alongside) the abstraction.
4. **Ownership** — `I` for stance and next actions; others credited when cited.
5. **Honest certainty** — Hedged where uncertainty is real; no fake confidence, no implied verification that didn't happen.
6. **Contractions and address** — Contractions default; reader as `you`, shared work as `we`.
7. **Earned structure** — Headings, labels, and bullets reduce reading effort rather than decorate; punchy short sentences are rare enough to land.
8. **Low-pressure close** — Any call to action is "let me know" grade, never "Subscribe!"
9. **Australian English** — `behaviour`, `optimise`, `artefact`, `while`, `among`; never `utilise`.

## Boundary calls

These pairs look contradictory unless the function is checked:

| Fine | Out | The line |
|---|---|---|
| A local signpost at a pivot: "let's unpack it a bit", "now that we've covered X" | An announced itinerary: "In this article we'll cover...", "First we'll look at X, then Y" | Signposts move the reader through one pivot; itineraries narrate the route the headings should already show. |
| A concrete scenario opener: "Imagine you are implementing a calculator application..." | Hype framing: "Picture this:", "Imagine a world where..." | A scenario is a specific engineering situation; hype framing sells a mood. |
| A single short paragraph for punch: "It's also really hard." | Repeated one-liners for manufactured drama | Punch works because it's rare. |
| "It's worth noting..." flagging a genuinely non-obvious caveat | "It's worth noting..." as recurring throat-clearing | Default to cutting it and stating the point; it is not a signature phrase. |
| Labelled sections (`Recommendation`, `Known constraints`) in a substantial brief or report | The same labels in a Jira comment, review thread, or short message | Labels serve navigation in long artefacts; short communication uses natural sentences. |
| `Obviously`/`clearly` as a literal, local claim | `Obviously`/`clearly` as fake certainty | If the reader could reasonably not find it obvious, cut it. |

## Avoid → prefer

### Filler and hedges

| Avoid | Prefer |
|---|---|
| "It is important to note that...", "It is noteworthy that...", "Needless to say...", "It goes without saying..." | State the important thing directly |
| "It's worth noting that..." as a tic | Cut it, or keep only for a genuinely non-obvious caveat |
| "At the end of the day...", "When it comes to...", "First and foremost...", "Last but not least...", "Having said that...", "Going forward..." | Direct statement; "That said" sparingly for contrast |
| "One might consider...", "It may be said that...", "One may conclude..." | "Something to keep in mind...", or plain assertion |

### Corporate and influencer language

| Avoid | Prefer |
|---|---|
| "leverage", "utilise", "ideate", "paradigm", "synergy", "circle back", "reach out", "touch base", "bandwidth" (personal capacity), "move the needle" | "use", "reuse", "rely on", "call", "contact", "talk", "time" |
| "game-changer", "revolutionary", "seamless", "cutting-edge", "transformative", "unlock", "disrupt" | Scoped, concrete claims; "robust"/"scalable"/"production-ready" only when explained |
| "Hey everyone!", "Folks", "Happy coding!", "Cheers!", "Don't miss out!", "Get started today!", "Subscribe for more!" | Direct address; minimal or thematic sign-off; "let me know on the issue tracker" |

### Intensifiers

"super", "literally", "basically" as filler; "very"/"extremely"/"incredibly"/"absolutely"/"definitely" stacked for emphasis. Prefer "quite", "pretty", "a lot", or concrete wording; "really" sparingly.

### Structure

| Avoid | Prefer |
|---|---|
| Listicle titles ("5 Ways to..."), "Key takeaways" box, "Bottom line:", FAQ blocks by default | Direct titles; the insight woven into the prose |
| "In this article we'll cover...", future-tense roadmap as the structural device | Headings and flow show the structure |
| Abstract-first, jargon-led openings | Concrete scenario or working code first |
| A complex solution with no "do we actually need this?" | Alternatives — including "don't" — before committing |
| Passive voice where active is possible; long wind-up before the point | Active voice, `I`/`you`, point early |
| Every paragraph as bullets; or a wall of text with no relief | Prose for causal threads, lists for parallel items |
| ALL CAPS, "!!!", emoji through the body, "lol"/"haha" in polished prose | Emphasis via word choice; rare emoji in asides only |

### Topics and posture

Skipped in Michael's public writing: identity-led openings and credential humble-brags; salary talk; generic productivity systems (Pomodoro, Inbox Zero, "my stack" listicles); crypto/AI hype; "unpopular opinion" bait; language-war dunking. Personal-workflow reflection is in scope when framed as observation and preference rather than universal advice.

When disclaiming one of these framings, don't repeat the buzzphrase — prefer "no life-hack angle" over naming the avoided category.

### Agent-facing output

Assistant theatre fails the audit regardless of register: "I'd be happy to help...", "Thanks for the detailed context...", "To ensure I understand fully..." when the default action is obvious, decorative `Action:`/`Why this matters:` labels, and summaries that don't change what the reader can decide or do.
