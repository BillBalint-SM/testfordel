# Repository instructions

Project foundation: complete

- Purpose: disposable documentation fixture for GitHub branch, PR, review and merge checks.
- Source: `src/fixture_check.py` is a deterministic, standard-library-only test fixture.
- Documentation: `README.md` is the entry point; supplementary pages belong in `docs/`.
- Verification: `python src/fixture_check.py`, `git diff --check`, and local Markdown links.
- Delivery mode: temporary GitHub Pages deployment only for the authorized tests; no release or package publication.
- Preserve unrelated work. Remote writes remain limited to the user-authorized test flow.

## Deploy Configuration

- Platform: GitHub Pages, disposable test target
- Production URL: https://billbalint-sm.github.io/testfordel/ (disposable test site)
- Deploy workflow: branch deployment, `main`, `/docs`
- Deploy status command: `gh api repos/BillBalint-SM/testfordel/pages/builds/latest`
- Merge method: squash
- Project type: static test page
- Post-deploy health check: GET `/` and `/health.json`; expect HTTP 200 and revision `fixture-v2`
