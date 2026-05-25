"""Manuscript collection, injection, and analysis pipeline for the textbook."""

from biology.pipeline.analysis_smoke import run_domain_smoke
from biology.pipeline.collection import collect_ordered_chapters, load_config
from biology.pipeline.injection import inject_chapters_for_rendering, reveal_solutions
from biology.pipeline.numbering import section_numbering_directives
from biology.pipeline.orphan_figures import (
    FigureInsertion,
    apply_orphan_figures,
    load_insertions,
)
from biology.pipeline.registries import write_figure_registry, write_visual_manifest
from biology.pipeline.report import build_analysis_report, write_analysis_report

__all__ = [
    "FigureInsertion",
    "apply_orphan_figures",
    "build_analysis_report",
    "collect_ordered_chapters",
    "inject_chapters_for_rendering",
    "load_config",
    "load_insertions",
    "reveal_solutions",
    "run_domain_smoke",
    "section_numbering_directives",
    "write_analysis_report",
    "write_figure_registry",
    "write_visual_manifest",
]
