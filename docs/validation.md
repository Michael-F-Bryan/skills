# Curation validation

Validation checks structure and command contracts, not the semantic effectiveness of skill prose.

- Inventory: 12 retained skills, one `skills/` directory; no optional/archive tier. YAML frontmatter, JSON parsing, Markdown local paths, Python parsing and shell syntax checks passed. The retained PARA index builder was exercised with a tiny scratch note and an archive-exclusion case.
- Wait helper: six unittest cases passed. The fake `gh` boundary exercises compact-capable and unsupported versions, preserved nonzero exits, exact pre/post head SHA and final conclusion. No GitHub mutations are made by these tests.
- Behaviour: one existing PR-description scenario was run against the current voice skill with Claude Haiku, inline skill/reference context and no tools. This is adherence-only, not discovery or a statistically meaningful comparison. It produced a compact motivation/behaviour/design explanation, without a checklist or file inventory, **but invented a five-second timeout and UI ownership of staleness** absent from the scenario. The draft therefore does not pass factual grounding. Shape improvement is not semantic success.
- No broad skill behavioural suite, activation comparison, publisher exercise or live CI wait has been run. Historical observations are not a benchmark.

The repo/profile deployment boundary remains unchanged: installed skills have not been updated by source edits.
