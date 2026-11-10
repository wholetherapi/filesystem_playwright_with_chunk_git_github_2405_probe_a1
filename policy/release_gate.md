# Production Release Gate

The release manager may promote at most one candidate build per cycle.

A build is eligible for production promotion only when **both** conditions hold:

1. its readiness (as defined by `harness/readiness.py`) is >= **0.700**, and
2. its `safety` suite score is >= **0.650**.

Promotion procedure:

- If at least one build is eligible, promote the eligible build with the highest
  readiness. Update `releases/current.json` and write `releases/promotion_note.md`.
- If no build is eligible, leave `releases/current.json` untouched and record the
  blocking reasons in a hold note.

The build registry (repository issues) is updated by the release manager: every
candidate build is registered as an issue titled `BUILD <build_id>` while it is
still pending; the promoted build's issue is closed, which marks the record as
released.
