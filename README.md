# testfordel workflow fixture

Disposable repository for a BontaFlowStack GitHub workflow check.

This repository contains disposable documentation, a standard-library Python
check and a GitHub Actions fixture triggered manually or by a push to `docs-test`. Temporary GitHub Pages
configuration is used only during the authorized deployment tests.

## Verification

Run `git diff --check` and inspect the changed Markdown and local links.
Supplementary documentation belongs in `docs/`.

[Read the workflow smoke-check](docs/workflow-smoke.md).

[Fixture commands and temporary Pages behavior](docs/fixture-usage.md).

[Reading the actual check result](docs/check-results.md).
