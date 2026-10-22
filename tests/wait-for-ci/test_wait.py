"""Exercise the shipped recipe through a fake executable, without remote writes."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / "skills/wait-for-ci/scripts/wait.py"
SHA = "a" * 40
FAKE = r'''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
a = sys.argv[1:]
with open(os.environ["CALLS"], "a") as f:
    f.write(json.dumps(a) + "\n")
if a == ["run", "watch", "--help"]:
    print("--compact  Show relevant steps" if os.environ["COMPACT"] == "1" else "--interval  seconds")
elif a[:2] == ["run", "view"]:
    p = Path(os.environ["COUNT"])
    n = int(p.read_text()) if p.exists() else 0
    p.write_text(str(n + 1))
    sha = "b" * 40 if os.environ.get("WRONG") == "pre" or (n and os.environ.get("WRONG") == "post") else "a" * 40
    print(json.dumps(dict(headSha=sha, status="completed", conclusion=os.environ.get("CONCLUSION", "success"))))
elif a[:2] == ["run", "watch"]:
    assert "--exit-status" in a and a[a.index("--interval") + 1] == "10"
    assert ("--compact" in a) == (os.environ["COMPACT"] == "1")
    print("poll chatter\n" * 100)
    print("failure detail", file=sys.stderr)
    sys.exit(int(os.environ.get("EXIT", "0")))
else:
    sys.exit(99)
'''


class WaitRecipe(unittest.TestCase):
    def run_recipe(self, compact="1", **env):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            gh = root / "gh"
            gh.write_text(FAKE)
            gh.chmod(0o755)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "123", SHA, "--repo", "owner/repo"],
                env={**os.environ, "PATH": directory + os.pathsep + os.environ["PATH"],
                     "COMPACT": compact, "CALLS": str(root / "calls"),
                     "COUNT": str(root / "count"), **env},
                capture_output=True, text=True,
            )
            calls = [json.loads(line) for line in (root / "calls").read_text().splitlines()]
            return result, calls

    def test_supported(self):
        result, calls = self.run_recipe()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(sum(c[:2] == ["run", "view"] for c in calls), 2)

    def test_unsupported_quiet(self):
        result, _ = self.run_recipe("0")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("poll chatter", result.stdout)
        self.assertNotIn("failure detail", result.stderr)

    def test_watch_failures_preserved(self):
        for compact in ("0", "1"):
            result, _ = self.run_recipe(compact, EXIT="7")
            self.assertEqual(result.returncode, 7)
            self.assertIn("failure detail", result.stderr)
            if compact == "0":
                self.assertLessEqual(len(result.stderr.splitlines()), 30)

    def test_wrong_sha_before_watch(self):
        result, calls = self.run_recipe(WRONG="pre")
        self.assertEqual(result.returncode, 2)
        self.assertFalse(any(c[:2] == ["run", "watch"] for c in calls))

    def test_wrong_sha_after_watch(self):
        result, _ = self.run_recipe(WRONG="post")
        self.assertEqual(result.returncode, 2)

    def test_non_success_despite_zero_watch(self):
        result, _ = self.run_recipe(CONCLUSION="cancelled")
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
