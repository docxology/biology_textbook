#!/usr/bin/env python3
"""Insert ``\\label{sec:...}`` into every chapter and rewrite prose cross-refs.

The textbook renders markdown → LaTeX → PDF via pandoc + pdflatex. Every
chapter needs a stable section label so downstream text can use
``\\cref{sec:unit_III_metabolic_integration}`` instead of hard-coded prose
like "See Chapter 11".

This script is idempotent: running it twice leaves the manuscript unchanged.
It reads ``manuscript/config.yaml`` for chapter ordering, then:

1. Inserts ``\\label{sec:<id>}`` immediately after the first-line title of
   every chapter file (only if the label is not already present).
2. Builds a map ``chapter_number -> canonical_label`` derived from the
   config order.
3. Rewrites prose cross-references of the form "See Chapter N", "--> See
   Chapter N", "see Chapter N" into ``\\cref{sec:<id>}`` form.
4. Reports statistics (files touched, labels inserted, refs rewritten).
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from functools import partial
from pathlib import Path

import yaml

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

from biology.curriculum_sync.sync_blocks import attach_section_identifier

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT_ROOT = Path(__file__).resolve().parent.parent / "manuscript"
CONFIG_PATH = MANUSCRIPT_ROOT / "config.yaml"


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

@dataclass
class ChapterInfo:
    """One chapter's identity."""

    number: int            # sequential 1..N across Units I-X
    unit_id: str           # e.g. "unit_I"
    unit_label: str        # e.g. "I"
    stem: str              # file stem e.g. "atoms_molecules"
    file: Path             # full path
    title: str             # title from config
    label: str             # canonical crossref label "sec:unit_I_atoms_molecules"


@dataclass
class RewriteReport:
    labels_inserted: int = 0
    labels_present: int = 0
    crefs_rewritten: int = 0
    files_touched: list[Path] = field(default_factory=list)

    def summary(self) -> str:
        return (f"labels_inserted={self.labels_inserted} "
                f"labels_already_present={self.labels_present} "
                f"prose_refs_rewritten={self.crefs_rewritten} "
                f"files_touched={len(self.files_touched)}")


# ---------------------------------------------------------------------------
# Config ingestion
# ---------------------------------------------------------------------------

def load_chapters() -> list[ChapterInfo]:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    chapters: list[ChapterInfo] = []
    number = 0
    for unit in cfg["units"]:
        unit_id = unit["id"]
        unit_label = unit["label"]
        unit_dir = MANUSCRIPT_ROOT / unit["directory"]
        for ch in unit.get("chapters", []):
            if ch.get("enabled") is False:
                continue
            # Unit 0 chapters don't count toward the Chapter 1..N sequence
            if unit_id != "unit_0":
                number += 1
            stem = ch["file"].replace(".md", "")
            file_path = unit_dir / ch["file"]
            label = f"sec:{unit_id}_{stem}"
            chapters.append(ChapterInfo(
                number=number if unit_id != "unit_0" else 0,
                unit_id=unit_id, unit_label=unit_label, stem=stem,
                file=file_path, title=ch["title"], label=label,
            ))
    return chapters


def load_labs(chapters: list[ChapterInfo]) -> list[tuple[Path, str, str]]:
    """Return (path, label, title) for every lab file."""
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    labs: list[tuple[Path, str, str]] = []
    for bundle in cfg.get("appendices", {}).get("labs", []):
        unit_id = bundle["unit"]
        for f in bundle.get("files", []):
            path = MANUSCRIPT_ROOT / "labs" / unit_id / f["file"]
            stem = f["file"].replace(".md", "")
            label = f"sec:lab_{unit_id}_{stem.removeprefix('lab_')}"
            labs.append((path, label, ""))
    return labs


def load_questions(chapters: list[ChapterInfo]) -> list[tuple[Path, str, str]]:
    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    qs: list[tuple[Path, str, str]] = []
    for bundle in cfg.get("appendices", {}).get("questions", []):
        unit_id = bundle["unit"]
        for f in bundle.get("files", []):
            path = MANUSCRIPT_ROOT / "questions" / unit_id / f["file"]
            stem = f["file"].replace(".md", "")
            label = f"sec:q_{unit_id}_{stem.removeprefix('questions_')}"
            qs.append((path, label, ""))
    return qs


# ---------------------------------------------------------------------------
# Label insertion
# ---------------------------------------------------------------------------

_LABEL_LINE_RE = re.compile(r"^\\label\{sec:[A-Za-z0-9_\-]+\}\s*$")
_TITLE_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$")


def insert_label(path: Path, label: str, report: RewriteReport, dry_run: bool = False) -> None:
    """Ensure numbered chapter files keep ``\\label{label}`` on the line after H1."""
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
            # Look ahead for an existing sec: label on the next few lines
            window = "\n".join(lines[i + 1: i + 4])
            if f"\\label{{{label}}}" in window:
                report.labels_present += 1
                return
            # Insert label immediately after the title with one blank-line
            insertion = ["", f"\\label{{{label}}}"]
            new_lines = lines[: i + 1] + insertion + lines[i + 1:]
            if not dry_run:
                write_text_atomic(path, "\n".join(new_lines) + "\n")
                report.files_touched.append(path)
            report.labels_inserted += 1
            return
    # No H1 found — skip
    print(f"WARN: no H1 title in {path}", file=sys.stderr)


def insert_unnumbered_label(
    path: Path,
    label: str,
    report: RewriteReport,
    dry_run: bool = False,
) -> None:
    """Ensure unnumbered surfaces use a Pandoc H1 identifier ``{#label .unnumbered}``."""
    if not path.exists():
        print(f"WARN: missing file {path}", file=sys.stderr)
        return
    text = path.read_text(encoding="utf-8")
    updated, changed = attach_section_identifier(text, label, unnumbered=True)
    if not changed:
        report.labels_present += 1
        return
    if not dry_run:
        write_text_atomic(path, updated)
        report.files_touched.append(path)
    report.labels_inserted += 1


# ---------------------------------------------------------------------------
# Prose-cross-ref rewriting
# ---------------------------------------------------------------------------

def build_ref_map(chapters: list[ChapterInfo]) -> dict[int, str]:
    """Map a chapter number (1..N) to its canonical section label."""
    return {c.number: c.label for c in chapters if c.number > 0}


_PROSE_PATTERNS = [
    # "--> See Chapter 11" / "→ See Chapter 11"
    (re.compile(r"(?:-->|→)\s*See\s+Chapter\s+(?P<n>\d+)(?=[\s.,;:)])", re.IGNORECASE),
     r"see \cref{{{label}}}"),
    # "(see Chapter 20)" / "see Chapter 20"
    (re.compile(r"(?<![A-Za-z])see\s+Chapter\s+(?P<n>\d+)(?=[\s.,;:)])"),
     r"see \cref{{{label}}}"),
    # "(see Section 19.5)" — leave as-is when we don't have a section map
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


def rewrite_prose(path: Path, ref_map: dict[int, str], report: RewriteReport, dry_run: bool = False) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    original = text
    # Heal any previous-run artefact of double-backslash cref.
    text = _BAD_DOUBLE_CREF.sub(r"\\cref{", text)
    for pattern, template in _PROSE_PATTERNS:
        replacer = partial(_replace_chapter_ref, ref_map=ref_map, template=template)
        text, n_sub = pattern.subn(replacer, text)
        report.crefs_rewritten += n_sub
    if text != original and not dry_run:
        write_text_atomic(path, text)
        if path not in report.files_touched:
            report.files_touched.append(path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    chapters = load_chapters()
    labs = load_labs(chapters)
    questions = load_questions(chapters)
    ref_map = build_ref_map(chapters)

    report = RewriteReport()

    # 1. Insert chapter labels
    for ch in chapters:
        insert_label(ch.file, ch.label, report, dry_run=dry_run)
    # 2. Insert lab and question labels with Pandoc H1 identifiers
    for path, label, _title in labs + questions:
        insert_unnumbered_label(path, label, report, dry_run=dry_run)

    # 3. Rewrite prose cross-refs in every content file
    for path in list(MANUSCRIPT_ROOT.rglob("*.md")):
        if path.name in {"README.md", "AGENTS.md"}:
            continue
        rewrite_prose(path, ref_map, report, dry_run=dry_run)

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] {report.summary()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
