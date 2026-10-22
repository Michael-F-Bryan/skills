#!/usr/bin/env python3
"""Wait for one exact-revision Actions run; never mutate GitHub."""
import argparse
from collections import deque
import json
import re
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_id")
    parser.add_argument("expected_sha")
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    if not args.run_id.isdigit() or not re.fullmatch(r"[0-9a-fA-F]{40}", args.expected_sha):
        parser.error("require a numeric run ID and exact full 40-character SHA")
    target = [args.run_id, "--repo", args.repo]

    def view():
        result = subprocess.run(
            ["gh", "run", "view", *target, "--json", "headSha,status,conclusion"],
            capture_output=True, text=True, check=True,
        )
        state = json.loads(result.stdout)
        if state["headSha"] != args.expected_sha:
            raise ValueError("run headSha does not match the expected exact SHA")
        return state

    view()
    help_result = subprocess.run(["gh", "run", "watch", "--help"],
                                 capture_output=True, text=True, check=True)
    compact = bool(re.search(r"(?<![\w-])--compact(?![\w-])", help_result.stdout))
    command = ["gh", "run", "watch", *target, "--exit-status", "--interval", "10"]
    if compact:
        command.append("--compact")
        code = subprocess.run(command).returncode
    else:
        # Disk-backed capture avoids poll spam and unbounded in-memory buffering.
        with tempfile.TemporaryFile(mode="w+t") as log, tempfile.TemporaryFile(mode="w+t") as errors:
            code = subprocess.run(command, stdout=log, stderr=errors).returncode
            if code:
                # Keep stderr distinct: buffered stdout can otherwise bury its diagnostics.
                for stream in (log, errors):
                    stream.seek(0)
                    print("".join(deque(stream, maxlen=15)), file=sys.stderr, end="")
    if code:
        return code if code > 0 else 128 - code
    state = view()
    if state["status"] != "completed" or state["conclusion"] != "success":
        print("Watch exited zero but run is not completed/success: " + json.dumps(state),
              file=sys.stderr)
        return 1
    print(f"Run {args.run_id}: success at {args.expected_sha}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr, file=sys.stderr, end="")
        sys.exit(error.returncode if isinstance(error, subprocess.CalledProcessError)
                 and error.returncode > 0 else 2)
