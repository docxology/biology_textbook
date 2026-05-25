#!/usr/bin/env python3
"""Run the biology textbook publication-readiness gate.

Thin CLI for :mod:`biology.quality.publication_gate`. Default ``--check`` runs
the practical project-local gate; ``--full`` adds expensive root orchestration
(root setup, project-root pytest with the 90% ``src/`` gate, root render, root
output validation, and the root PDF log gate).
"""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths()

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
        help="Include expensive root setup/test/render/validation and coverage.",
    )
    args = parser.parse_args(argv)

    with tempfile.TemporaryDirectory(prefix="biology_textbook_readiness_") as tmpdir:
        failures = run_publication_gate(full=args.full, artifact_dir=Path(tmpdir))

    status = "PASS" if failures == 0 else "FAIL"
    depth = "full" if args.full else "default"
    print(f"\naudit_publication_readiness: {status} ({depth}, failures={failures})")
    if args.check and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
