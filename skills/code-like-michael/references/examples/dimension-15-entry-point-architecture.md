# Labeling Sample: Dimension 15 - Entry-Point Architecture

Dimension reminder: how execution is organized through entrypoints (CLI/service/worker), and whether entrypoints stay thin by delegating business logic to domain/application modules.

---

```rust
// src/bin/app.rs
use clap::{Parser, Subcommand};

#[derive(Parser)]
struct Cli {
    #[command(subcommand)]
    cmd: Commands,
}

#[derive(Subcommand)]
enum Commands {
    SyncUsers { source: String },
    RebuildIndex { tenant: String },
}

fn main() -> Result<(), String> {
    let cli = Cli::parse();
    match cli.cmd {
        Commands::SyncUsers { source } => app::commands::sync_users::run(&source),
        Commands::RebuildIndex { tenant } => app::commands::rebuild_index::run(&tenant),
    }
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - I like that the `main()` function is deliberately thin and just delegates to the command implementation
  - Using `clap` with the derive macro is definitely the right choice here. It means your CLI's structure and flags are immediately obvious just by looking at the types, and the enum means your code will naturally follow the CLI structure. It also means that the user can only set the flags that are relevant to the sub-command being executed - "make invalid states unrepresentable" and all that.

---

```go
// cmd/tool/main.go
package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {
	cmd := flag.String("cmd", "", "command: sync|index")
	source := flag.String("source", "", "source name")
	tenant := flag.String("tenant", "", "tenant id")
	flag.Parse()

	if *cmd == "sync" {
		// business logic in entrypoint
		if *source == "" {
			fmt.Fprintln(os.Stderr, "source required")
			os.Exit(1)
		}
		fmt.Println("syncing users from", *source)
		// imagine db + api calls here
		return
	}

	if *cmd == "index" {
		if *tenant == "" {
			fmt.Fprintln(os.Stderr, "tenant required")
			os.Exit(1)
		}
		fmt.Println("rebuilding index for", *tenant)
		// imagine index logic here
		return
	}

	fmt.Fprintln(os.Stderr, "unknown command")
	os.Exit(1)
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I generally hate the `flag` package in Go. First off, flags are global variables that can be registered from anywhere, so you don't have full control of your command-line. The command-line arguments are a key part of your CLI's public interface, so they are something that should be deliberately designed and curated.
  - I also don't like that the code is doing big switches on magic strings (the sub-commands) then manually validating whether certain flags have been set correctly (i.e. `if *tenant == ""`). That's just error-prone and adds low-value noise to the code.
  - Doing a print to stderr and directly calling `os.Exit(1)` is also a code smell. It means your command-line argument parser only did half its job and left a bunch of the validation to the programmer

---

```python
# cli.py
import argparse
from app.commands.sync_users import run_sync_users
from app.commands.rebuild_index import run_rebuild_index


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    sync = sub.add_parser("sync-users")
    sync.add_argument("--source", required=True)

    rebuild = sub.add_parser("rebuild-index")
    rebuild.add_argument("--tenant", required=True)

    args = parser.parse_args()

    if args.command == "sync-users":
        return run_sync_users(source=args.source)
    if args.command == "rebuild-index":
        return run_rebuild_index(tenant=args.tenant)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence:
  - If this was a bigger tool, I'd probably hoist the command-line argument parsing out into its own `parse_args()` function that returns a dataclass and uses unions to represent mutually exclusive sub-commands.
  - I prefer `clap`, but the use of `argparse` is pretty decent here and if that's what the rest of the project uses, then I'm okay with it.
  - It also feels weird to be returning an exit code from `main()` and getting the caller to raise `SystemExit`. Normally, if things went wrong I'd raise an exception inside `run_sync_users()` or `run_rebuild_index()` and let it bubble up until the program eventually crashes. That's immediately more debuggable (you get a stack trace) and means the business logic functions don't need to worry themselves about exit codes.

---

```ts
// src/cli.ts
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { db } from "./infra/db";
import { fetchUsersFromRemote } from "./infra/remote";
import { rebuildSearchIndex } from "./infra/search";

void yargs(hideBin(process.argv))
  .command(
    "sync-users",
    "Sync users",
    (cmd) => cmd.option("source", { type: "string", demandOption: true }),
    async (args) => {
      const users = await fetchUsersFromRemote(String(args.source));
      for (const user of users) {
        await db.query("insert into users(id, email) values ($1, $2)", [user.id, user.email]);
      }
      await rebuildSearchIndex();
    },
  )
  .demandCommand(1)
  .strict()
  .parse();
```

- Score (1-5): 3
- Confidence (`low|medium|high`): low
- Evidence:
  - I haven't actually had to write command-line programs in TypeScript before, but the code looks pretty decent. Can't say more than that.
