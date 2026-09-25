# Reading a fixture result

The `fixture-check` job runs `src/fixture_check.py`. Read the GitHub run's
`head_sha`, `status`, `conclusion` and URL before deciding whether that commit
passed. A queued or running check is not successful; a failed or cancelled check
does not permit the test merge.

[Fixture inputs](fixture-usage.md) describe the three supported modes.
