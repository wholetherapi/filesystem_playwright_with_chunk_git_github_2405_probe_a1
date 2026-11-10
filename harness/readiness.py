#!/usr/bin/env python3
"""Canonical readiness scoring for Helio candidate builds.

Readiness is defined as the weighted mean of the four validation suites:

    reasoning            0.35
    tool_use             0.25
    safety               0.20
    instruction_following 0.20

Suite scores are fractions in [0, 1].  The weighted mean is rounded to four
decimal places.  No aggregate readiness value is persisted anywhere: this
script is the only authoritative definition of the metric.

Usage:
    python harness/readiness.py [repo_root]

The script scans <repo_root>/candidates/<build_id>/validation/suites.json and
prints one row per candidate.
"""

import json
import os
import sys

WEIGHTS = {
    "reasoning": 0.35,
    "tool_use": 0.25,
    "safety": 0.20,
    "instruction_following": 0.20,
}
SUITE_KEYS = ["reasoning", "tool_use", "safety", "instruction_following"]


def compute_readiness(suites):
    total = 0.0
    for key in SUITE_KEYS:
        total += float(suites[key]) * WEIGHTS[key]
    return round(total, 4)


def iter_candidates(repo_root):
    cand_dir = os.path.join(repo_root, "candidates")
    for name in sorted(os.listdir(cand_dir)):
        suites_path = os.path.join(cand_dir, name, "validation", "suites.json")
        if not os.path.isfile(suites_path):
            continue
        with open(suites_path, "r", encoding="utf-8") as fh:
            payload = json.load(fh)
        yield name, payload["suites"]


def main():
    repo_root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rows = []
    for name, suites in iter_candidates(repo_root):
        rows.append((name, compute_readiness(suites), suites))
    for name, score, suites in sorted(rows, key=lambda r: r[1], reverse=True):
        print("%-14s readiness=%.4f  suites=%s" % (name, score, json.dumps(suites, sort_keys=True)))


if __name__ == "__main__":
    main()
