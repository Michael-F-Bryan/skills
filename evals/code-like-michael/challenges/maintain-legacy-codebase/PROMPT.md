# Maintenance: legacy codebase (not skill-styled)

## Task given to agent

The `project/` directory contains a small inventory reporting tool used by the ops team. Two changes are needed:

1. Add a `--warehouse <name>` filter: inventory items now have an optional `warehouse` field, and the report should only include items from the given warehouse when the flag is passed.
2. Ops reports that items with quantity exactly equal to the threshold are treated as OK but should be LOW (`qty <= threshold`, not `qty < threshold`).

Keep the tool working for existing users. Run the tests.

## What this probes

The fixture is deliberately messy: scattered `os.environ` reads inside loops, a `utils.py` dump with an unused helper, stringly dicts, a fat `main()` with a nested if-pyramid, mock-theatre tests patching `urllib`, alerts hidden behind an `ALERTS_ENABLED` opt-in flag.

Grading questions:

- **Surgical vs drive-by:** does the agent scope the rewrite to the seams it touches, or rewrite everything / change nothing?
- **Don't canonise bad code:** does it copy the env-read-in-loop and dict-passing patterns for the new feature, or harden the seams it touches?
- **Boundary bug fix:** is the threshold fix tested with a real behaviour test (not another urlopen mock)?
- **Dead code:** does it notice/remove `chunk_list` if it touches utils, or leave unrelated code alone (either is defensible — look at reasoning)?
- **Tests:** are new tests behaviour-shaped (run the report on a temp file), or more mock choreography?
