"""Figure registry and visual manifest writers for the analysis pipeline."""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path

from textbook_io import write_text_atomic

from biology.pipeline.paths import OUTPUT_DIR, PROJECT_ROOT
from biology.visual_contracts import build_manifest, write_manifest
from biology.visual_contracts_paths import DEFAULT_MANIFEST

logger = logging.getLogger(__name__)

FIGURE_BLOCK_RE = re.compile(r"\\begin\{figure\}.*?\\end\{figure\}", re.DOTALL)
FIGURE_INCLUDE_RE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
FIGURE_LABEL_RE = re.compile(r"\\label\{(fig:[^}]+)\}")


def write_figure_registry() -> Path:
    """Write a validator-compatible registry for figure labels in injected chapters."""
    figures_dir = PROJECT_ROOT / "output" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    registry_path = figures_dir / "figure_registry.json"

    records: list[dict[str, str]] = []
    seen: set[str] = set()
    for md_file in sorted(OUTPUT_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        for block in FIGURE_BLOCK_RE.findall(text):
            includes = FIGURE_INCLUDE_RE.findall(block)
            labels = FIGURE_LABEL_RE.findall(block)
            filename = Path(includes[0]).name if includes else ""
            for label in labels:
                if label in seen:
                    continue
                record: dict[str, str] = {"label": label, "source": md_file.name}
                if filename:
                    record["filename"] = filename
                records.append(record)
                seen.add(label)

    write_text_atomic(registry_path, json.dumps(records, indent=2) + "\n")
    logger.info("Figure registry written to %s (%d labels)", registry_path, len(records))
    return registry_path


def write_visual_manifest() -> Path:
    """Write the full visual contract manifest."""
    manifest_path = write_manifest(build_manifest(), DEFAULT_MANIFEST)
    logger.info("Visual manifest written to %s", manifest_path)
    return manifest_path


__all__ = ["write_figure_registry", "write_visual_manifest"]
