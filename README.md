# Helio Model Release Registry

This repository is the governance workspace for the Helio production release
cycle. It contains:

- `candidates/<build_id>/` - packaged validation artefacts for each candidate
  build (manifest, placeholder weight file, validation suite scores).
- `harness/readiness.py` - the canonical readiness metric definition.
- `policy/release_gate.md` - the production promotion rules.
- `releases/current.json` - the release currently serving production traffic.

The build registry itself is kept as GitHub issues in this repository. Each
issue title is a registry record name; historical records are titled
`EVB-...`, and a closed issue means the record is released while an open issue
means it is still pending.
