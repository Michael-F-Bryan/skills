# Labelling Sample: Dimension 16 - Repository Topology Style

Dimension reminder: coherence and intentionality of repo structure (modular monolith/service split/package conventions) versus ad hoc layout.

---

```rust
// repo layout (excerpt)
// src/bin/app.rs
// src/app/commands/sync_users.rs
// src/app/commands/rebuild_index.rs
// src/domain/users/mod.rs
// src/domain/index/mod.rs
// src/adapters/postgres/users_repo.rs
// src/adapters/http/remote_client.rs
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - I think this is the wrong way to break your code up. Instead of grouping by the "kind" of thing (domains, adapters, etc.), components should be grouped by the responsibility/feature/domain
  - This also feels a bit over-engineered

---

```go
// repo layout (excerpt)
// main.go
// helpers.go
// util2.go
// stuff.go
// api_new.go
// old_handlers.go
// db2.go
// temp_migration_copy_final.go
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - This shows evidence that you've just been throwing crap together and experimenting, and not cleaning up after yourself
  - There is no obvious structure to the codebase
  - Seeing `xxx2.go` and `xxx_copy_final.go` just reminds me of the bad old days where you would have a `Chemistry Assignment final draft - actually final (2).docx` file

---

```python
# repo layout (excerpt)
# app/
#   cli.py
#   commands/
#     sync_users.py
#     rebuild_index.py
#   domain/
#     users.py
#     indexing.py
#   infra/
#     postgres.py
#     remote_api.py
# tests/
#   domain/
#   commands/
```

- Score (1-5): 3
- Confidence (`low|medium|high`): high
- Evidence:
  - I'd probably break this down so each feature gets its own module, then there is a `commands` package with all the command-line parsing and sub-commands that just exists to provide the CLI API, do some setup, and call into the main domain logic

---

```ts
// repo layout (excerpt)
// src/index.ts
// src/lib.ts
// src/new/
// src/new2/
// src/shared/
// src/shared2/
// scripts/tmp/
// scripts/tmp2/
// misc/
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - The presence of the `xxx2` folders gives me no confidence in the state of the code, and what is dead code versus the final version
