"""Insert ``\\label{sec:...}`` after chapter H1s and rewrite legacy chapter prose.

The textbook renders markdown → LaTeX → PDF via pandoc + pdflatex. Every
chapter needs a stable section label so downstream text can use
``\\cref{sec:unit_III_metabolic_integration}`` instead of hard-coded prose
like "See Chapter 11". This module is the tested business logic behind
``scripts/insert_crossref_labels.py``; the script is a thin CLI orchestrator.

Idempotent: running ``apply_crossref_labels`` twice leaves the manuscript
unchanged.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path
from typing import Protocol

import yaml

from biology.curriculum_sync.sync_blocks import attach_section_identifier
from biology.maintenance.models import PROJECT

MANUSCRIPT_ROOT = PROJECT / "manuscript"
CONFIG_PATH = MANUSCRIPT_ROOT / "config.yaml"


class _WriteFn(Protocol):
    def __call__(self, path: Path, text: str) -> None: ...


def _default_writer() -> _WriteFn:
    from textbook_io import write_text_atomic

    return write_text_atomic


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------


@dataclass
class ChapterInfo:
    """One chapter's identity for label insertion."""

    number: int
    unit_id: str
    unit_label: str
    stem: str
    file: Path
    title: str
    label: str


@dataclass
class RewriteReport:
    """Aggregated counters for a label/prose rewrite pass."""

    labels_inserted: int = 0
    labels_present: int = 0
    crefs_rewritten: int = 0
    files_touched: list[Path] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"labels_inserted={self.labels_inserted} "
            f"labels_already_present={self.labels_present} "
            f"prose_refs_rewritten={self.crefs_rewritten} "
            f"files_touched={len(self.files_touched)}"
        )


# ---------------------------------------------------------------------------
# Config ingestion
# ---------------------------------------------------------------------------


def load_chapters(config_path: Path = CONFIG_PATH, manuscript_root: Path = MANUSCRIPT_ROOT) -> list[ChapterInfo]:
    """Return ``ChapterInfo`` records for every enabled chapter in config order."""
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    chapters: list[ChapterInfo] = []
    number = 0
    for unit in cfg["units"]:
        unit_id = unit["id"]
        unit_label = unit["label"]
        unit_dir = manuscript_root / unit["directory"]
        for ch in unit.get("chapters", []):
            if ch.get("enabled") is False:
                continue
            if unit_id != "unit_0":
                number += 1
            stem = ch["file"].replace(".md", "")
            chapters.append(
                ChapterInfo(
                    number=number if unit_id != "unit_0" else 0,
                    unit_id=unit_id,
                    unit_label=unit_label,
                    stem=stem,
                    file=unit_dir / ch["file"],
                    title=ch["title"],
                    label=f"sec:{unit_id}_{stem}",
                )
            )
    return chapters


def load_labs(config_path: Path = CONFIG_PATH, manuscript_root: Path = MANUSCRIPT_ROOT) -> list[tuple[Path, str, str]]:
    """Return ``(path, label, title)`` for every appendix lab file."""
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    labs: list[tuple[Path, str, str]] = []
    for bundle in cfg.get("appendices", {}).get("labs", []):
        unit_id = bundle["unit"]
        for f in bundle.get("files", []):
            path = manuscript_root / "labs" / unit_id / f["file"]
            stem = f["file"].replace(".md", "")
            label = f"sec:lab_{unit_id}_{stem.removeprefix('lab_')}"
            labs.append((path, label, ""))
    return labs


def load_questions(config_path: Path = CONFIG_PATH, manuscript_root: Path = MANUSCRIPT_ROOT) -> list[tuple[Path, str, str]]:
    """Return ``(path, label, title)`` for every appendix question bank."""
    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    qs: list[tuple[Path, str, str]] = []
    for bundle in cfg.get("appendices", {}).get("questions", []):
        unit_id = bundle["unit"]
        for f in bundle.get("files", []):
            path = manuscript_root / "questions" / unit_id / f["file"]
            stem = f["file"].replace(".md", "")
            label = f"sec:q_{unit_id}_{stem.removeprefix('questions_')}"
            qs.append((path, label, ""))
    return qs


# ---------------------------------------------------------------------------
# Label insertion
# ---------------------------------------------------------------------------

_TITLE_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$")


def insert_label(
    path: Path,
    label: str,
    report: RewriteReport,
    *,
    dry_run: bool = False,
    write_fn: _WriteFn | None = None,
) -> None:
    """Ensure a numbered chapter file carries ``\\label{label}`` after its H1."""
    if not path.exists():
        print(f"WARN: missing file {path}", file=sys.stderr)
        return
    text = path.read_text(encoding="utf-8")
    if f"\\label{{{label}}}" in text:
        report.labels_present += 1
        return
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if _TITLE_RE.match(line):
            window = "\n".join(lines[i + 1 : i + 4])
            if f"\\label{{{label}}}" in window:
                report.labels_present += 1
                return
            insertion = ["", f"\\label{{{label}}}"]
            new_lines = lines[: i + 1] + insertion + lines[i + 1 :]
            if not dry_run:
                writer = write_fn or _default_writer()
                writer(path, "\n".join(new_lines) + "\n")
                report.files_touched.append(path)
            report.labels_inserted += 1
            return
    print(f"WARN: no H1 title in {path}", file=sys.stderr)


def insert_unnumbered_label(
    path: Path,
    label: str,
    report: RewriteReport,
    *,
    dry_run: bool = False,
    write_fn: _WriteFn | None = None,
) -> None:
    """Ensure an unnumbered surface uses a Pandoc H1 identifier ``{#label .unnumbered}``."""
    if not path.exists():
        print(f"WARN: missing file {path}", file=sys.stderr)
        return
    text = path.read_text(encoding="utf-8")
    updated, changed = attach_section_identifier(text, label, unnumbered=True)
    if not changed:
        report.labels_present += 1
        return
    if not dry_run:
        writer = write_fn or _default_writer()
        writer(path, updated)
        report.files_touched.append(path)
    report.labels_inserted += 1


# ---------------------------------------------------------------------------
# Prose-cross-ref rewriting
# ---------------------------------------------------------------------------


def build_ref_map(chapters: list[ChapterInfo]) -> dict[int, str]:
    """Map a chapter number (1..N) to its canonical section label."""
    return {c.number: c.label for c in chapters if c.number > 0}


_PROSE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"(?:-->|→)\s*See\s+Chapter\s+(?P<n>\d+)(?=[\s.,;:)])", re.IGNORECASE),
        r"see \cref{{{label}}}",
    ),
    (
        re.compile(r"(?<![A-Za-z])see\s+Chapter\s+(?P<n>\d+)(?=[\s.,;:)])"),
        r"see \cref{{{label}}}",
    ),
]

_BAD_DOUBLE_CREF = re.compile(r"\\\\cref\{")


def _replace_chapter_ref(
    match: re.Match[str],
    *,
    ref_map: dict[int, str],
    template: str,
) -> str:
    n = int(match.group("n"))
    label = ref_map.get(n)
    if not label:
        return str(match.group(0))
    return template.format(label=label)


def rewrite_prose(
    path: Path,
    ref_map: dict[int, str],
    report: RewriteReport,
    *,
    dry_run: bool = False,
    write_fn: _WriteFn | None = None,
) -> None:
    """Rewrite prose chapter references inside ``path`` to ``\\cref{...}`` form."""
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    original = text
    text = _BAD_DOUBLE_CREF.sub(r"\\cref{", text)
    for pattern, template in _PROSE_PATTERNS:
        replacer = partial(_replace_chapter_ref, ref_map=ref_map, template=template)
        text, n_sub = pattern.subn(replacer, text)
        report.crefs_rewritten += n_sub
    if text != original and not dry_run:
        writer = write_fn or _default_writer()
        writer(path, text)
        if path not in report.files_touched:
            report.files_touched.append(path)


# ---------------------------------------------------------------------------
# Orchestration entry point
# ---------------------------------------------------------------------------


def apply_crossref_labels(
    *,
    dry_run: bool = False,
    manuscript_root: Path = MANUSCRIPT_ROOT,
    config_path: Path = CONFIG_PATH,
    write_fn: _WriteFn | None = None,
) -> RewriteReport:
    """Run the full label-insertion + prose-rewrite pipeline."""
    chapters = load_chapters(config_path, manuscript_root)
    labs = load_labs(config_path, manuscript_root)
    questions = load_questions(config_path, manuscript_root)
    ref_map = build_ref_map(chapters)
    report = RewriteReport()

    for ch in chapters:
        insert_label(ch.file, ch.label, report, dry_run=dry_run, write_fn=write_fn)
    for path, label, _title in labs + questions:
        insert_unnumbered_label(path, label, report, dry_run=dry_run, write_fn=write_fn)
    for path in list(manuscript_root.rglob("*.md")):
        if path.name in {"README.md", "AGENTS.md"}:
            continue
        rewrite_prose(path, ref_map, report, dry_run=dry_run, write_fn=write_fn)
    return report


__all__ = [
    "CONFIG_PATH",
    "ChapterInfo",
    "MANUSCRIPT_ROOT",
    "RewriteReport",
    "apply_crossref_labels",
    "build_ref_map",
    "insert_label",
    "insert_unnumbered_label",
    "load_chapters",
    "load_labs",
    "load_questions",
    "rewrite_prose",
]
