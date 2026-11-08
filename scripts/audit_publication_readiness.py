#!/usr/bin/env python3
"""Run the biology textbook publication-readiness gate.

Thin CLI for :mod:`biology.quality.publication_gate`. Default ``--check`` runs
the project-local gate; ``--full`` also runs coverage, live-source analysis,
strict PNG/PDF rendering and output validation. Artifacts remain under this
repository's ``output/`` tree; external template code is read-only.
"""

from __future__ import annotations

import argparse

from _bootstrap import ensure_project_paths

ensure_project_paths(include_template=False)

from biology.quality.publication_gate import (
    build_command_steps,
    build_python_steps,
    run_publication_gate,
)

__all__ = ["build_command_steps", "build_python_steps", "main"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit non-zero if any readiness step fails.")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Include coverage, analysis, strict PNG/PDF rendering and output validation.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Parallel audit workers for independent gate steps (default: 1).",
    )
    args = parser.parse_args(argv)

    failures = run_publication_gate(
        full=args.full,
        max_workers=max(1, args.workers),
    )

    status = "PASS" if failures == 0 else "FAIL"
    depth = "full" if args.full else "default"
    print(f"\naudit_publication_readiness: {status} ({depth}, failures={failures})")
    if args.check and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
