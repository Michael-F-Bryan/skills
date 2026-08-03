# Public writing (Michael)

**Scope:** blog posts, public technical prose, and reflective professional writing. Derived from Michael's published blog corpus. The structural rules here — openings, headings, closings, Hugo shortcodes — are for public long-form only; they do not transfer to reviews, PRs, notes, or updates, which have their own references.

## Register

Professional but conversational, roughly 2–2.5 on a 5-point formality scale. Warm peer sharing hard-won understanding, not guru or textbook. Measured and calm; blunt when making a point, then softening. Contractions are the default; full forms appear for emphasis. First person for experience and stance, direct `you` and `we` for the reader.

Humour is light and rare: self-deprecation ("took me embarrassingly long to realise"), dry understatement, occasional wordplay or pop-culture sign-off. Emoji sparingly, in asides only (🤷 after an honest compromise).

Certainty is calibrated: exploratory for opinion ("my take", "I'd like to explore"), definitive for technical fact, explicitly hedged where reality is messy ("9 times out of 10...", "it's complicated"). Comfortable saying "I don't know."

## Openings

Openings set scene and stakes in a short paragraph, not a bold one-line claim or a question. The recurring shapes:

- **Personal context** — why I'm writing, what I learned the hard way: "I thought it might be helpful to write down some of the core principles and values that guide my professional life."
- **Concrete scenario** — "Imagine you are implementing a calculator application and want users to be able to extend the application with their own functionality." The scenario is a specific engineering situation the reader can inhabit; hype framing ("Imagine a world where...") is a different move and does not fit.
- **Prior-art callback** — "A while ago someone posted a question on the Rust User Forums... I'd like to explore my take on things."
- **Received wisdom + trigger** — "One of the first things I learned when programming professionally is that *global variables are bad*... the other day, a 3rd party native library reminded me *why*."

Process and how-to pieces still need a minimal personal stake before the first step — one sentence on why this matters or what it cost to learn.

## Structure and flow

Use H2 for main sections and H3 for subsections whenever the piece has three or more distinct parts; never publish a multi-section piece without headings. Headings are short and scannable, and they carry much of the transition load.

Transitions are signposted locally at pivots: "There's quite a lot going on here, so let's unpack it a bit", "Now that we've covered X...", "Let me show you what this looks like in practice." The boundary: a signpost moves the reader through *this* pivot; an announced itinerary ("In this article we'll cover X, Y, and Z", "First we'll look at X, then move to Y") narrates the whole route and is out. If the structure needs announcing, the headings aren't doing their job.

Paragraph rhythm is deliberately mixed: most body paragraphs run 3–6 sentences; single-sentence paragraphs are saved for emphasis or pivot ("It's also really hard."); longer blocks are fine around code. Repeated one-liners for fake punch flatten the effect — the short sentence lands because it's rare.

Closings wrap up rather than sell: a brief summary, often a callback or soft caveat ("Don't think of these as hard and fast rules..."), and a low-pressure invitation — issue tracker, "let me know", or a thematic sign-off. Short process pieces should still get one reflective or caveat sentence rather than ending on a purely utilitarian summary.

## Teaching moves

- **Show, then unpack.** Present the complete working thing first, acknowledge the density, then break it down: code block → "There's quite a lot going on here, so let's unpack it a bit" → stepwise explanation.
- **Alternatives before committing.** Before any fancy solution, ask "do we actually *need* to come up with a fancy solution here?" and list the options — including "don't" — before choosing. "9 times out of 10 taking the more complicated option will require you to do extra work that wasn't needed in the first place."
- **Concrete-first.** A scenario or working code before the abstract principle, never a jargon-led definition as the hook. "See how the concrete example makes the abstract pattern immediately understandable?"
- **Real artefacts as evidence.** Terminal output, compiler errors, Valgrind/Miri runs, and diagrams are part of the argument, not decoration. Include the failure mode, not just the happy path.
- **Credit and defer.** Link generously; "Ralf Jung does a much better job of explaining the subtleties of provenance so I'll just defer to his articles."

## Sentences

Medium length is the default; long sentences carry technical qualification; short ones mark rhythm breaks and payoff. Frequent "X, but/meaning/so Y" shapes for reasoning. Em dashes and parentheses for asides, colons to introduce lists and "here's how" moments, semicolons rarely. Fragments are allowed for punch and sign-off ("Don't be that guy.", "Success!").

## Vocabulary

Precise domain terms for technical readers (*vtable*, *provenance*, *RAII*) with links or one-line clarification on first mention; deliberately plain language for mixed audiences ("clever algorithms employed in the games industry" instead of naming A*). Jargon is a tool for compression, never for status.

Recurring words and phrases, used naturally rather than sprinkled: *quite*, *unpack*, *gist*, *the happy path*, *under the hood*, *in practice*, *9 times out of 10*, *I'm a big fan of*, *That said*, *Don't get me wrong*, *Feel free to*. "Here's the thing" works for a genuine pivot, not as a tic. Mild intensifiers (*really*, *pretty*, *kinda*) in moderation; no profanity.

## Code and markup

Code is the main vehicle for explanation: full or substantial snippet, then prose that unpacks it. File-path comments at the top of blocks when they orient the reader (`// core/src/lib.rs`). Console blocks preserve prompts and output. Backticks for anything the reader might type, search for, or need to recognise — including inside list items.

In blog prose, comparisons and options use parallel or nested bullet lists rather than markdown tables; lists break up density and structure the argument. (Operator artefacts are the opposite — tables for trade-offs — see [operator-artifacts.md](operator-artifacts.md).)

## Callouts on the blog (Hugo)

A how-to or technical piece for Michael's blog usually earns at least one callout — a tip for the central lesson, or a note for the repo link or a meta aside. Use Hugo shortcodes: `{{% notice tip/note/info/warning %}}` for asides and safety caveats, `{{% expand %}}` for long code or noisy output, `{{< figure >}}` for diagrams. For any destination other than the blog, use that platform's native markup instead.

## Reflective pieces

Warm first person, concrete anecdotes, controlled emotion. Ground reflection in one real experience and own it ("So yeah, it was a hard decision to leave because I loved my teammates and the project, but I'm confident it was the right one."). Observation and preference, not universal life advice; values and expectations, not productivity tips.

## Exemplars

Calibrate against these quoted lines:

- "Motivation is a funny thing."
- "It's also really hard."
- "I mean, haven't we all been there? You're trying to solve a problem, you find what looks like the perfect article, and five minutes later you're somehow more confused than when you started."
- "There's quite a lot going on here, so let's unpack it a bit."
- "Normally you'd just reach for a `Box<dyn std::io::Write>` here, but as we've already mentioned Rust's trait objects aren't FFI-safe, meaning we need to be a little more creative."
- "When you assume confusion indicates explanation failure rather than reader failure, you start thinking about problems differently."
- "In an ideal world all code would be perfect... Unfortunately, this *isn't* an ideal world so we need to develop techniques that allow us to keep working under less than ideal conditions while limiting the negative effects."
- "Yes I know the irony in using a `static` variable to workaround another library's zealous use of `static` variables, but sometimes you've got to break a couple eggs to make an omelette 🤷"
- "Don't think of these as hard and fast rules. Instead, think of them more like factors that may contribute to low motivation or reduced performance."
- "So long, and thanks for all the fish."
