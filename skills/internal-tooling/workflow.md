# Internal Tooling Workflow

Use this when turning an automation request into durable internal tooling.

## Lifecycle

### 1) Ideation

- Capture the operator problem in one sentence.
- Identify frequency: one-off, occasional, recurring.
- Identify risk: read-only vs mutating; low-risk vs operationally sensitive.
- Identify audience: just you vs other humans/agents.

### 2) Decision

- Apply [references/decision-gate.md](references/decision-gate.md).
- If CLI is required, continue to design and implementation.
- If one-off shell is acceptable, run it directly and ask whether it should be promoted if repeated.

### 3) Design

- Choose command shape (`uv run <agent-name> <group> <command>`).
- Define typed option bundles and dependency boundaries.
- Decide output/error behavior (human-readable, stable when needed for automation).

### 4) Implementation

- Keep command handlers thin.
- Keep business logic in domain modules.
- Inject dependencies from CLI boundary.
- Follow [references/click-patterns.md](references/click-patterns.md) and [references/project-structure.md](references/project-structure.md).

### 5) Verification

- Run the checklist in [checklist.md](checklist.md).
- Confirm command discoverability (`--help`) and behavior tests.

### 6) Adoption

- Add a short usage example in repo docs or runbooks.
- Ensure command naming and help text support discoverability.

### 7) Maintenance

- Track repeated one-offs and convert to CLI when thresholds are crossed.
- Keep docs aligned with actual command surface.
- Prefer additive command evolution over breaking behavior changes.

### 8) Deprecation

- Mark command/flag as deprecated in help text.
- Provide replacement command and migration note.
- Remove after transition window and doc updates.
