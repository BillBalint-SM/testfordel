"""Deterministic check for the disposable GitHub test repository."""
import os
import time
from pathlib import Path

mode = os.environ.get("FIXTURE_MODE") or Path("ci-mode.txt").read_text().strip()
assert mode in {"success", "failure", "wait"}, "unknown fixture mode"
if mode == "wait":
    time.sleep(120)
assert 2 + 2 == (5 if mode == "failure" else 4), "intentional CI fixture failure"
print("fixture check passed")
