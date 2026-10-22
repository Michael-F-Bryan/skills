---
name: wait-for-ci
description: Wait for exact-commit CI with quiet, reliable status.
---

# Wait for CI

Use when the task actually needs to wait for a GitHub Actions run, not after every push by habit. Requires Python 3 and an authenticated `gh` with read access.

## Select the exact run

Get the full expected SHA from the intended revision (`git rev-parse HEAD` for the current checkout). List candidate runs with `gh run list --commit "$EXPECTED_SHA" --json databaseId,headSha,workflowName,status,conclusion`; select the intended workflow/run, not simply the newest row. Account for each required workflow separately. PR merge/test SHAs may differ from branch HEAD: establish which exact revision the task requires rather than silently accepting either.

## Wait quietly

Through the terminal tool, run:

```bash
python3 <skill-root>/scripts/wait.py RUN_ID EXPECTED_FULL_SHA --repo OWNER/REPO
```

The helper checks the run’s exact `headSha` before waiting, detects `--compact` from `gh run watch --help`, and uses `--exit-status --interval 10`. When compact output is unsupported, it captures polling chatter and emits only a bounded failure tail. It preserves a nonzero watch exit, including authentication/runtime failures, and reads the exact run again to require matching SHA, completed status and successful conclusion before returning zero. It does not turn failure into success with `|| echo` or a pipeline.

A missing run is not success: report queue/trigger uncertainty or the absent required workflow. On failure inspect that run’s failed jobs/logs as needed; do not repeat full polling output.

## Verification

`python3 -m unittest discover -s tests/wait-for-ci -v` exercises the real helper through a tiny fake `gh` boundary, both flag capabilities, failure exits and wrong-SHA checks. These are command-contract tests, not live GitHub CI evidence.
