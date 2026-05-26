"""Canonical table-of-contents model for the biology textbook.

The manuscript configuration owns book, unit, chapter, and reference appendix
titles. This module derives all companion section titles from that single
source of truth so labs, question banks, generated appendices, front matter,
and planning grids cannot drift independently.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .chapter_metadata import CHAPTERS, ChapterMeta


@dataclass(frozen=True)
class ChapterTocItem:
    """Canonical table-of-contents entry for one configured chapter."""

    chapter_id: str
    unit_id: str
    unit_label: str
    unit_title: str
    file: str
    title: str
    path: Path
    meta: ChapterMeta
    ordinal_in_unit: int

    @property
    def display_number(self) -> str:
        """Return the rendered chapter/section number display.

        Unit 0 chapters use a prelude namespace (0.1, 0.2, ...). Numbered
        Units I-X keep their canonical chapter numbers from ``ChapterMeta``.
        """
        return self.companion_number

    @property
    def grid_number(self) -> str:
        """Return the course-planning-grid number display."""
        return self.display_number

    @property
    def companion_number(self) -> str:
        """Return the lab/question chapter number display."""
        if self.meta.number > 0:
            return str(self.meta.number)
        return f"0.{self.ordinal_in_unit}"

    @property
    def section_label(self) -> str:
        """Return the canonical ``cleveref`` section label for this chapter."""
        return f"sec:{self.chapter_id}"

    @property
    def name_ref(self) -> str:
        """Return a LaTeX reference that renders the current chapter title."""
        return f"\\nameref{{{self.section_label}}}"

    @property
    def plain_ref(self) -> str:
        """Return the chapter title for forward references in early front matter."""
        return self.title

    @property
    def hyperlink_ref(self) -> str:
        """Return a clickable PDF link to this chapter."""
        from biology.crossref.helpers import section_hyperlink

        return section_hyperlink(self.section_label, self.title)

    @property
    def lab_prefix(self) -> str:
        """Return the lab prefix for Unit 0 prelude labs (alpha-indexed)."""
        if self.meta.number > 0:
            return "Lab"
        return f"Lab {_alpha_index(self.ordinal_in_unit)}"

    @property
    def lab_title(self) -> str:
        """Return the companion lab H1 title (no chapter ordinal — use \\cref)."""
        return f"{self.lab_prefix} — {self.title}"

    @property
    def question_title(self) -> str:
        """Return the companion question-bank H1 title (no chapter ordinal)."""
        return f"Questions — {self.title}"


@dataclass(frozen=True)
class UnitTocItem:
    """Canonical table-of-contents entry for one configured unit."""

    unit_id: str
    label: str
    title: str
    directory: str
    intro_path: Path
    intro_title: str
    chapters: tuple[ChapterTocItem, ...]

    @property
    def display_title(self) -> str:
        """Return the unit display title used in front-matter navigation."""
        return f"Unit {self.label} — {self.title}"

    @property
    def section_label(self) -> str:
        """Return the canonical section label for this unit introduction."""
        return f"sec:{self.unit_id}_unit_intro"

    @property
    def name_ref(self) -> str:
        """Return a LaTeX reference that renders the current unit title."""
        return f"\\nameref{{{self.section_label}}}"

    @property
    def plain_ref(self) -> str:
        """Return the unit introduction title for forward references in early front matter."""
        return self.intro_title

    @property
    def hyperlink_ref(self) -> str:
        """Return a clickable PDF link to this unit introduction."""
        from biology.crossref.helpers import section_hyperlink

        return section_hyperlink(self.section_label, self.plain_ref)

    @property
    def hyperlink_display_title(self) -> str:
        """Return a clickable PDF link using the unit display title."""
        from biology.crossref.helpers import section_hyperlink

        return section_hyperlink(self.section_label, self.display_title)


@dataclass(frozen=True)
class CompanionTocItem:
    """Canonical entry for a lab or question-bank companion section."""

    kind: str
    unit_id: str
    file: str
    path: Path
    chapter: ChapterTocItem
    title: str


@dataclass(frozen=True)
class ReferenceTocItem:
    """Canonical entry for a reference appendix."""

    file: str
    title: str
    path: Path

    @property
    def section_label(self) -> str:
        """Return the canonical section label for this reference appendix."""
        if self.file == "glossary.md":
            return "sec:glossary"
        return f"sec:{Path(self.file).stem}"

    @property
    def name_ref(self) -> str:
        """Return a LaTeX reference that renders the current appendix title."""
        return f"\\nameref{{{self.section_label}}}"

    @property
    def plain_ref(self) -> str:
        """Return the appendix title for forward references in early front matter."""
        return self.title

    @property
    def hyperlink_ref(self) -> str:
        """Return a clickable PDF link to this reference appendix."""
        from biology.crossref.helpers import section_hyperlink

        return section_hyperlink(self.section_label, self.title)


@dataclass(frozen=True)
class BookToc:
    """Complete table-of-contents view derived from manuscript configuration."""

    project_root: Path
    config_path: Path
    units: tuple[UnitTocItem, ...]
    chapters: tuple[ChapterTocItem, ...]
    labs: tuple[CompanionTocItem, ...]
    questions: tuple[CompanionTocItem, ...]
    references: tuple[ReferenceTocItem, ...]

    @property
    def chapters_by_id(self) -> dict[str, ChapterTocItem]:
        """Return chapters keyed by stable ``chapter_id``."""
        return {chapter.chapter_id: chapter for chapter in self.chapters}

    @property
    def chapters_by_number(self) -> dict[int, ChapterTocItem]:
        """Return main textbook chapters keyed by rendered chapter number."""
        return {chapter.meta.number: chapter for chapter in self.chapters if chapter.meta.number > 0}

    @property
    def chapters_by_companion_number(self) -> dict[str, ChapterTocItem]:
        """Return chapters keyed by lab/question display number, including Unit 0."""
        return {chapter.companion_number: chapter for chapter in self.chapters}

    @property
    def labs_by_path(self) -> dict[Path, CompanionTocItem]:
        """Return lab entries keyed by source path."""
        return {lab.path: lab for lab in self.labs}

    @property
    def questions_by_path(self) -> dict[Path, CompanionTocItem]:
        """Return question-bank entries keyed by source path."""
        return {question.path: question for question in self.questions}

    @property
    def references_by_file(self) -> dict[str, ReferenceTocItem]:
        """Return reference appendices keyed by configured file name."""
        return {reference.file: reference for reference in self.references}

    @property
    def units_by_id(self) -> dict[str, UnitTocItem]:
        """Return units keyed by stable ``unit_id``."""
        return {unit.unit_id: unit for unit in self.units}


def load_toc(project_root: str | Path | None = None) -> BookToc:
    """Load the canonical table of contents for the project.

    Args:
        project_root: Optional project root. Defaults to the repository project
            containing this module.

    Returns:
        A :class:`BookToc` containing units, chapters, companion materials, and
        reference appendices in render order.
    """
    root = Path(project_root).resolve() if project_root is not None else Path(__file__).resolve().parents[2]
    manuscript = root / "manuscript"
    config_path = manuscript / "config.yaml"
    config = _load_config(config_path)
    metadata = {record.chapter_id: record for record in CHAPTERS}

    units: list[UnitTocItem] = []
    chapters: list[ChapterTocItem] = []
    chapters_by_unit_stem: dict[tuple[str, str], ChapterTocItem] = {}

    for unit in config.get("units", []):
        unit_id = str(unit["id"])
        unit_label = str(unit.get("label", unit_id))
        unit_title = str(unit.get("title", unit_id))
        unit_dir = str(unit["directory"])
        unit_chapters: list[ChapterTocItem] = []
        for ordinal, chapter in enumerate(unit.get("chapters", []), start=1):
            file_name = str(chapter["file"])
            stem = Path(file_name).stem
            chapter_id = f"{unit_id}_{stem}"
            try:
                meta = metadata[chapter_id]
            except KeyError as exc:
                raise KeyError(f"Missing ChapterMeta for configured chapter {chapter_id}") from exc
            item = ChapterTocItem(
                chapter_id=chapter_id,
                unit_id=unit_id,
                unit_label=unit_label,
                unit_title=unit_title,
                file=file_name,
                title=str(chapter["title"]),
                path=manuscript / unit_dir / file_name,
                meta=meta,
                ordinal_in_unit=ordinal,
            )
            unit_chapters.append(item)
            chapters.append(item)
            chapters_by_unit_stem[(unit_id, stem)] = item
        units.append(
            UnitTocItem(
                unit_id=unit_id,
                label=unit_label,
                title=unit_title,
                directory=unit_dir,
                intro_path=manuscript / unit_dir / "unit_intro.md",
                intro_title=f"Unit {unit_label} — {unit_title}: Introduction",
                chapters=tuple(unit_chapters),
            )
        )

    appendices = config.get("appendices", {}) or {}
    labs = _companions(
        kind="lab",
        manuscript=manuscript,
        bundles=appendices.get("labs", []),
        chapters_by_unit_stem=chapters_by_unit_stem,
    )
    questions = _companions(
        kind="question",
        manuscript=manuscript,
        bundles=appendices.get("questions", []),
        chapters_by_unit_stem=chapters_by_unit_stem,
    )
    references = tuple(
        ReferenceTocItem(
            file=str(entry["file"]),
            title=str(entry["title"]),
            path=_reference_path(manuscript, str(entry["file"])),
        )
        for entry in appendices.get("reference", [])
    )

    return BookToc(
        project_root=root,
        config_path=config_path,
        units=tuple(units),
        chapters=tuple(chapters),
        labs=labs,
        questions=questions,
        references=references,
    )


def _load_config(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return dict(yaml.safe_load(handle) or {})


def _companions(
    *,
    kind: str,
    manuscript: Path,
    bundles: list[dict[str, Any]],
    chapters_by_unit_stem: dict[tuple[str, str], ChapterTocItem],
) -> tuple[CompanionTocItem, ...]:
    items: list[CompanionTocItem] = []
    prefix = "lab_" if kind == "lab" else "questions_"
    base_dir = "labs" if kind == "lab" else "questions"
    for bundle in bundles:
        unit_id = str(bundle.get("unit", ""))
        for entry in bundle.get("files", []):
            file_name = str(entry["file"])
            stem = Path(file_name).stem.removeprefix(prefix)
            try:
                chapter = chapters_by_unit_stem[(unit_id, stem)]
            except KeyError as exc:
                raise KeyError(f"{kind} companion has no configured chapter: {unit_id}/{file_name}") from exc
            title = chapter.lab_title if kind == "lab" else chapter.question_title
            items.append(
                CompanionTocItem(
                    kind=kind,
                    unit_id=unit_id,
                    file=file_name,
                    path=manuscript / base_dir / unit_id / file_name,
                    chapter=chapter,
                    title=title,
                )
            )
    return tuple(items)


def _reference_path(manuscript: Path, file_name: str) -> Path:
    path = manuscript / "appendices" / file_name
    if not path.exists() and file_name == "glossary.md":
        return manuscript / "glossary.md"
    return path


def _alpha_index(number: int) -> str:
    if number < 1:
        raise ValueError("alpha index is 1-based")
    value = number
    letters = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        letters = chr(ord("A") + remainder) + letters
    return letters


__all__ = [
    "BookToc",
    "ChapterTocItem",
    "CompanionTocItem",
    "ReferenceTocItem",
    "UnitTocItem",
    "load_toc",
]
