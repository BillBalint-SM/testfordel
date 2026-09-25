# Test fixture

Run `python src/fixture_check.py` for the successful check. The optional
`FIXTURE_MODE=failure` deliberately fails; `FIXTURE_MODE=wait` waits 120 seconds.
These are test inputs, not application functionality.

The manually dispatched `fixture.yml` workflow takes `mode` and a unique
`marker`. Its GitHub run ID and commit identify the actual execution.

The temporary GitHub Pages fixture serves `docs/index.html` and `health.json`.
The health document reports `fixture-v1`, allowing a response from a stale build
to be distinguished from the selected revision. Pages is disabled after testing.

[Back to README](../README.md).
