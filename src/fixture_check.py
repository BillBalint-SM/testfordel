"""Deterministic check for the disposable GitHub test repository."""
import os
import time

mode = os.environ.get("FIXTURE_MODE", "success")
assert mode in {"success", "failure", "wait"}, "unknown fixture mode"
if mode == "wait":
    time.sleep(120)
assert 2 + 2 == (5 if mode == "failure" else 4), "intentional CI fixture failure"
print("fixture check passed")
