#!/usr/bin/env python3
"""Audit current-science claim metadata for fast-moving textbook facts."""

from __future__ import annotations

import argparse

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.current_claims import (
    load_current_claims,
    scan_stale_manuscript_phrases,
    validate_current_claims,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit non-zero if any issue is found")
    args = parser.parse_args()

    claims = load_current_claims(project_root=PROJECT)
    issues = [
        issue.format()
        for issue in validate_current_claims(claims, references_path=PROJECT / "docs" / "manuscript" / "references.bib")
    ]
    issues.extend(scan_stale_manuscript_phrases(PROJECT / "docs" / "manuscript", project_root=PROJECT))
    for issue in issues:
        print(issue)
    print(f"current_claims: claims={len(claims)} issues={len(issues)}")
    if args.check and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
