# Reviewing destructive Git cleanup CLIs

Use this checklist when a command discovers and removes worktrees, branches, refs, or other local Git state.

## Safety boundary probes

- **Ignored content:** `git status --porcelain` without `--ignored` can report clean while a forced worktree removal deletes ignored files. Probe tracked, untracked, ignored, and recursively initialised-submodule content separately.
- **Preflight versus execution:** a clean classification can become stale before `--force`. Require a complete preflight before the first deletion, cooperative serialization for same-tool runs, and immediate identity/HEAD/ref/lock/dirtiness revalidation before each destructive command. State the residual arbitrary-editor race honestly.
- **Submodule transactionality:** deinitialising submodules before a fallible worktree removal damages a worktree that may remain after failure. Review the order and demand either direct verified removal or fail-closed retention.
- **Branch identity:** checking “not in use” and then running an unbound delete can race with branch reuse. Bind deletion to the inspected ref OID with compare-and-delete semantics, after rechecking worktree use.
- **Literal porcelain parsing:** use NUL-delimited porcelain and preserve path/reason bytes literally. Newlines and spaces are legal path content; generic `strip()` calls can change identity.
- **Caller and primary protection:** invoke from primary, linked, and nested linked directories. The caller must not delete itself, and the primary must not be treated as an ordinary candidate.
- **Failure semantics:** exercise at least two candidates where a later operation fails. Decide and document all-or-nothing versus best-effort behavior; do not let a one-candidate test imply transactionality.
- **Dry run:** snapshot file bytes, index, status, refs, reflogs, config, `FETCH_HEAD`/`ORIG_HEAD`, worktree metadata, locks, branches, and submodule state. A HEAD-only snapshot does not prove no mutation.

## Review topology

Use real temporary repositories, local bare remotes, linked worktrees, and local submodules. Do not mock subprocess calls for acceptance evidence.

Mutation probes belong in a disposable clone or temporary worktree, never the read-only review target. Check target status before and after the review; transient files created and removed mid-review still violate a no-write brief and can race with coordinator verification.

## Verdict calibration

Treat data-loss paths, stale-force checks, pre-removal submodule mutation, and unbound ref deletion as blocking until reproduced or disproved. Treat parser literalness and duplicated state as blocking only when they can select the wrong target or defeat fail-closed behavior; otherwise classify them separately as hardening or simplification.
