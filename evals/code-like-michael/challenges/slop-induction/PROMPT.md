# Slop induction challenge

Give the agent this user request (with code-like-michael in available_skills):

> Build me a newsletter monitoring system — Python CLI that tracks RSS feeds, scores articles by relevance, stores history in SQLite, sends digest emails, and has a plugin system for custom filters.

Grade whether the agent:
- Activates and reads the skill
- Stays within medium greenfield tripwires (5-8 files, 250-500 LOC) or justifies overage
- Avoids service/repository/manager layers
- Runs reshape pass and self-check
- Deletes scaffolding (pass-through classes, single-purpose micro-modules)

Reference good run: see REFERENCE-RUN.md from improvement loop (589 LOC after reshape).
