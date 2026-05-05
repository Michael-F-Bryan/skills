# Labeling Sample: Dimension 19 - Build/Tooling Contract

Dimension reminder: reproducibility and explicitness of build/test/lint/dev workflows.

---

```rust
// Makefile
// .PHONY: test lint check
// test: ; cargo test --all-targets --all-features
// lint: ; cargo clippy --all-targets --all-features -- -D warnings
// check: ; cargo fmt --check && cargo clippy -- -D warnings && cargo test
//
// rust-toolchain.toml
// [toolchain]
// channel = "stable"
```

- Score (1-5): 2
- Confidence (`low|medium|high`): high
- Evidence:
  - I wouldn't use `make` for creating shortcuts - just use `cargo test` directly

---

```go
// README excerpt:
// "Run stuff however you want."
//
// no Makefile
// no documented test command
// no pinned tool versions
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - A README should tell newcomers how to get started. At the very least, you could say something like "Use `cargo build` and `cargo test` like a normal Rust project".

---

```python
# pyproject.toml excerpt
# [tool.ruff]
# line-length = 100
#
# [tool.pytest.ini_options]
# addopts = "-q"
#
# scripts:
# uv run ruff check .
# uv run pytest
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - It's obvious that the author has taken time to set up their tools
  - Using `uv` is great, and doing `uv run ruff` indicates that they've pinned their tools to a specific version rather than installing some random version globaly

---

```ts
// package.json excerpt
// {
//   "scripts": {
//     "dev": "tsx src/cli.ts",
//     "typecheck": "tsc --noEmit",
//     "lint": "eslint .",
//     "test": "vitest run",
//     "ci": "pnpm typecheck && pnpm lint && pnpm test"
//   },
//   "packageManager": "pnpm@9.12.0"
// }
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - It's good to see that they've set up scripts for all the common tasks you would do
  - I also like that they've specified the package manager version so you don't accidentally use `yarn`  on a `pnpm` project
