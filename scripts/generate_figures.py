"""Thin orchestrator: Generate all matplotlib scientific figures.

Invokes all generators from src/visualization/plots.py.
Default output: <project_root>/output/figures/
"""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from _bootstrap import PROJECT as PROJECT_DIR, ensure_project_paths

ensure_project_paths()

CONFIG_FILE = PROJECT_DIR / "docs" / "manuscript" / "config.yaml"


def main() -> int:
    from textbook_logging import get_logger
    from visualization import ALL_FIGURE_GENERATORS

    logger = get_logger(__name__)
    parser = argparse.ArgumentParser(description="Generate all biology textbook matplotlib figures")
    parser.add_argument("--output-dir", type=Path,
                        default=PROJECT_DIR / "output" / "figures")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    if CONFIG_FILE.exists():
        cfg = yaml.safe_load(CONFIG_FILE.read_text(encoding="utf-8")) or {}
        a11y = cfg.get("accessibility") or {}
        if a11y.get("color_blindness_safe", True):
            logger.info(
                "Figures use src/visualization/cvd.py (colour-vision–friendly defaults); "
                "see docs/accessibility.md"
            )
    success = 0
    total = len(ALL_FIGURE_GENERATORS)
    failures: list[str] = []

    for name, fn in ALL_FIGURE_GENERATORS:
        try:
            path = fn(args.output_dir)
            logger.info(f"Generated: {path}")
            print(f"  ✓ {path.name}")
            success += 1
        except (ImportError, OSError, RuntimeError, ValueError) as e:
            logger.error(f"Failed to generate '{name}': {e}")
            print(f"  ✗ {name}: {e}")
            failures.append(name)

    logger.info(f"Generated {success}/{total} figures → {args.output_dir}")
    print(f"[generate_figures] {success}/{total} figures → {args.output_dir}")
    if failures:
        failed = ", ".join(failures)
        logger.error(f"Figure generation failed for: {failed}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
