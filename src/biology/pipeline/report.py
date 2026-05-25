"""Analysis report assembly for the pipeline stage."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from textbook_io import write_text_atomic

from biology.pipeline.analysis_smoke import SmokeReport
from biology.pipeline.paths import OUTPUT_ROOT, PROJECT_ROOT


def build_analysis_report(
    smoke: SmokeReport,
    *,
    chapters_injected: int,
    figure_registry: Path,
    visual_manifest: Path,
) -> dict[str, Any]:
    """Merge domain smoke metrics with injection artifact paths."""
    report = dict(smoke.as_dict())
    report["chapters_injected"] = chapters_injected
    report["figure_registry"] = str(figure_registry.relative_to(PROJECT_ROOT))
    report["visual_manifest"] = str(visual_manifest.relative_to(PROJECT_ROOT))
    return report


def write_analysis_report(report: dict[str, Any], path: Path | None = None) -> Path:
    """Write analysis_report.json under output/."""
    report_path = path or (OUTPUT_ROOT / "analysis_report.json")
    write_text_atomic(report_path, json.dumps(report, indent=2) + "\n")
    return report_path


__all__ = ["build_analysis_report", "write_analysis_report"]
