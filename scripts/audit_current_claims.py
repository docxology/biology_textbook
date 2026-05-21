#!/usr/bin/env python3
"""Audit current-science claim metadata for fast-moving textbook facts."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


PROJECT = Path(__file__).resolve().parent.parent
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent
for path in (TEMPLATE_ROOT, SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from biology.current_claims import load_current_claims, validate_current_claims  # noqa: E402


STALE_OR_UNQUALIFIED_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("casgevy-scd-transfusion-endpoint", re.compile(r"In SCD, ~94% of patients achieved transfusion independence")),
    ("old-un-2100-population", re.compile(r"UN median projection ~10\.4 billion by 2100")),
    (
        "oneill-as-current-burden",
        re.compile(r"AMR is projected to cause 10 million deaths per year by 2050 \(O'Neill Report, 2016\)"),
    ),
    ("unqualified-high-co2-2100", re.compile(r"Atmospheric CO₂ levels are projected to reach 800-1000 ppm by 2100")),
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit non-zero if any issue is found")
    args = parser.parse_args()

    claims = load_current_claims(project_root=PROJECT)
    issues = [issue.format() for issue in validate_current_claims(claims)]
    issues.extend(_scan_stale_phrases())
    for issue in issues:
        print(issue)
    print(f"current_claims: claims={len(claims)} issues={len(issues)}")
    if args.check and issues:
        return 1
    return 0


def _scan_stale_phrases() -> list[str]:
    issues: list[str] = []
    manuscript = PROJECT / "manuscript"
    for path in sorted(manuscript.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for code, pattern in STALE_OR_UNQUALIFIED_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                rel = path.relative_to(PROJECT)
                issues.append(f"{code} {rel}:{line}: stale or unqualified fast-moving claim")
    return issues


if __name__ == "__main__":
    raise SystemExit(main())
