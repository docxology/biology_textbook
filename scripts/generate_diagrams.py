"""Thin orchestrator: Generate all Mermaid PNG diagrams.

Invokes src/mermaid/biology_diagrams.py to render all 24 biology diagrams.
Default output: <project_root>/output/figures/mermaid/
"""

from __future__ import annotations

import argparse
from pathlib import Path

from _bootstrap import PROJECT as PROJECT_DIR, ensure_project_paths

ensure_project_paths()


def main() -> int:
    from textbook_logging import get_logger
    from mermaid import ALL_BIOLOGY_DIAGRAMS, MermaidRenderer

    logger = get_logger(__name__)
    parser = argparse.ArgumentParser(description="Render all Mermaid biology diagrams to PNG")
    parser.add_argument("--output-dir", type=Path,
                        default=PROJECT_DIR / "output" / "figures" / "mermaid")
    parser.add_argument("--width", type=int, default=1200, help="Mermaid render viewport width in pixels")
    parser.add_argument("--height", type=int, default=1200, help="Mermaid render viewport height in pixels")
    parser.add_argument(
        "--strict-png",
        action="store_true",
        help="Fail instead of accepting .mmd fallbacks; use this in publication build paths.",
    )
    args = parser.parse_args()

    renderer = MermaidRenderer(output_dir=args.output_dir, strict_png=args.strict_png)
    paths = renderer.render_all(ALL_BIOLOGY_DIAGRAMS, width=args.width, height=args.height)
    if args.strict_png:
        non_png = [path for path in paths if path.suffix != ".png"]
        if non_png:
            for path in non_png:
                logger.error("Strict PNG mode rejected non-PNG output: %s", path)
            return 1

    success = sum(1 for p in paths if p.exists())
    logger.info(f"Rendered {success}/{len(ALL_BIOLOGY_DIAGRAMS)} Mermaid diagrams → {args.output_dir}")
    print(f"[generate_diagrams] {success}/{len(ALL_BIOLOGY_DIAGRAMS)} diagrams → {args.output_dir}")

    for path in paths:
        print(f"  {'✓' if path.exists() else '✗'} {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
