"""Configured manuscript surface audit."""

from __future__ import annotations

from pathlib import Path

from biology.maintenance.manuscript_walker import configured_manuscript_surfaces
from biology.quality import paths
from biology.quality.models import Finding
from biology.quality.patterns import EXPECTED_CONFIGURED_SURFACE_COUNTS


def audit_configured_surfaces(findings: list[Finding]) -> None:
    surfaces = configured_manuscript_surfaces()
    counts: dict[str, int] = {}
    seen: set[Path] = set()
    for surface in surfaces:
        counts[surface.category] = counts.get(surface.category, 0) + 1
        if surface.path in seen:
            findings.append(
                Finding("error", "duplicate-configured-surface", surface.path, 1, surface.category)
            )
        seen.add(surface.path)
        if not surface.path.is_file():
            findings.append(
                Finding("error", "missing-configured-surface", surface.path, 1, surface.category)
            )
    for category, expected in EXPECTED_CONFIGURED_SURFACE_COUNTS.items():
        actual = counts.get(category, 0)
        if actual != expected:
            findings.append(
                Finding(
                    "error",
                    "configured-surface-count-drift",
                    paths.MANUSCRIPT / "config.yaml",
                    1,
                    f"{category} expected {expected}, found {actual}",
                )
            )
