"""Biology Textbook: Chapter Collector and Analysis Script.

Reads docs/manuscript/config.yaml, runs all biology analysis modules, then copies
all ordered chapter files into output/manuscript/ for the generic rendering
pipeline (scripts/03_render_pdf.py checks that directory first).

Usage (called automatically by scripts/02_run_analysis.py when the project is active):
    uv run python scripts/biology_analysis.py   # from projects/biology_textbook/
"""

from __future__ import annotations

import logging
import os

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.pipeline.analysis_smoke import run_domain_smoke
from biology.pipeline.collection import collect_ordered_chapters, load_config
from biology.pipeline.injection import clear_stale_slide_artifacts, inject_chapters_for_rendering
from biology.pipeline.paths import OUTPUT_ROOT
from biology.pipeline.registries import write_figure_registry, write_visual_manifest
from biology.pipeline.report import build_analysis_report, write_analysis_report

logger = logging.getLogger(__name__)


def _configure_logging() -> None:
    if not logging.getLogger().handlers:
        logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s")


def run_analysis() -> None:
    """Run all biology analysis modules and inject chapters for rendering."""
    _configure_logging()
    logger.info("Starting: Execute biology_analysis.py")
    clear_stale_slide_artifacts()
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    smoke = run_domain_smoke()

    logger.info("Collecting chapters from config.yaml for rendering injection...")
    config = load_config()
    chapters = collect_ordered_chapters(config)
    logger.info("Collected %d chapter files from config.yaml", len(chapters))

    cfg_solutions = bool(config.get("export", {}).get("include_solutions", False))
    env_solutions = os.environ.get("BIOLOGY_INCLUDE_SOLUTIONS") == "1"
    include_solutions = cfg_solutions or env_solutions
    watermark_instructor = bool(config.get("export", {}).get("watermark_instructor", False))
    if include_solutions:
        logger.info("  → Instructor edition: revealing answer keys in question banks")

    inject_chapters_for_rendering(
        chapters,
        include_solutions=include_solutions,
        watermark_instructor=watermark_instructor,
    )
    figure_registry_path = write_figure_registry()
    visual_manifest_path = write_visual_manifest()

    report = build_analysis_report(
        smoke,
        chapters_injected=len(chapters),
        figure_registry=figure_registry_path,
        visual_manifest=visual_manifest_path,
    )
    report_path = write_analysis_report(report)
    logger.info("Analysis report written to %s", report_path)
    print(f"[biology_analysis] Report: {report_path}")


# Backward-compatible re-exports for tests that load this module by path.
from biology.pipeline.numbering import section_numbering_directives as _section_numbering_directives
from biology.pipeline.paths import MANUSCRIPT_DIR, OUTPUT_DIR, PROJECT_ROOT

__all__ = [
    "MANUSCRIPT_DIR",
    "OUTPUT_DIR",
    "PROJECT_ROOT",
    "_section_numbering_directives",
    "inject_chapters_for_rendering",
    "run_analysis",
]


if __name__ == "__main__":
    run_analysis()
