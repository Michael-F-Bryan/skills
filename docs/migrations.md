# Ownership and migration

Tool guidance for `jake-tools` and Clockify belongs with the jake-tools package, its live CLI/MCP interfaces and package tests—not independently installed skills that drift. Before removal, the complete `clockify-api` source was copied and byte-compared for the separate package worker. The local scratch handoff is ephemeral, not a runtime dependency; this repository does not certify that package migration.

The obsolete transcript executor skill and unvalidated heavy coding-fingerprint wizard were deleted. Useful [transcript fidelity lessons](transcript-fidelity.md) remain as a concise non-skill reference; old transcript evals are explicitly inactive. There is no archival skill tier.

Summary-callout and wikilinks became [opt-in note conventions](note-conventions.md). All retained skills live in `skills/`; specialist relevance is controlled by narrow activation scope, not installation tiers. Existing installed copies do not disappear automatically. Review the actual profile/project inventory and remove retired copies deliberately. These repository changes do not modify profiles, vault/project instructions or other repositories.
