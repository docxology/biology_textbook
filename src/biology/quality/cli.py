"""CLI entry point for textbook quality auditing."""

from __future__ import annotations

import argparse

from biology.quality.engine import collect_findings, print_report
from biology.quality.models import Finding
from biology.quality import paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit high-value textbook quality invariants.")
    parser.add_argument("--check", action="store_true", help="Exit nonzero when blocking findings are present.")
    parser.add_argument(
        "--max-advisories",
        type=int,
        default=0,
        help="Number of advisory findings to print and enforce in --check mode.",
    )
    args = parser.parse_args(argv)

    findings = collect_findings()
    if args.check:
        advisory_count = sum(1 for finding in findings if finding.severity == "advisory")
        if advisory_count > args.max_advisories:
            findings.append(
                Finding(
                    "error",
                    "advisory-limit-exceeded",
                    paths.QUALITY_ADVISORIES,
                    1,
                    f"{advisory_count} advisories exceeds --max-advisories={args.max_advisories}",
                )
            )
    print_report(findings, max_advisories=args.max_advisories)
    if args.check and any(finding.severity == "error" for finding in findings):
        return 1
    return 0


__all__ = ["main"]
