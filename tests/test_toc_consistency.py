"""Canonical table-of-contents consistency checks."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any, cast

import yaml
import pytest

from biology.toc import BookToc, load_toc


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"


def _load_script_module(name: str):
    path = PROJECT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, module)
    spec.loader.exec_module(module)
    return module


_metadata_script = _load_script_module("insert_chapter_metadata")
_sync_script = _load_script_module("sync_curriculum_materials")
_GRID_END = _metadata_script._GRID_END
_GRID_START = _metadata_script._GRID_START
build_grid = _metadata_script.build_grid
CONCEPT_MAP_MARKER = _sync_script.CONCEPT_MAP_MARKER
NAV_MARKER = _sync_script.NAV_MARKER
PREFACE_SCOPE_MARKER = _sync_script.PREFACE_SCOPE_MARKER
READING_PATHS_MARKER = _sync_script.READING_PATHS_MARKER
build_front_matter_navigation = _sync_script.build_front_matter_navigation
build_preface_scope_table = _sync_script.build_preface_scope_table
build_suggested_reading_paths = _sync_script.build_suggested_reading_paths
build_textbook_concept_map = _sync_script.build_textbook_concept_map
from biology.pipeline.numbering import section_numbering_directives as _section_numbering_directives


def _first_h1(path: Path) -> str:
    match = re.search(r"^#\s+(.+)$", path.read_text(encoding="utf-8"), flags=re.MULTILINE)
    if match is None:
        raise AssertionError(f"Missing H1 in {path.relative_to(PROJECT)}")
    return _heading_display(match.group(1))


def _heading_display(raw: str) -> str:
    return re.sub(r"\s+\{[^}]*\}\s*$", "", raw).strip()


def _config() -> dict[str, Any]:
    return dict(yaml.safe_load((MANUSCRIPT / "config.yaml").read_text(encoding="utf-8")))


def _navigation_block() -> str:
    return _marked_block((MANUSCRIPT / "front_matter.md").read_text(encoding="utf-8"), NAV_MARKER)


def _marked_block(text: str, marker: tuple[str, str]) -> str:
    start, end = marker
    pattern = re.compile(f"{re.escape(start)}.*?{re.escape(end)}", flags=re.DOTALL)
    match = pattern.search(text)
    if match is None:
        raise AssertionError(f"Missing generated block {start}")
    return match.group(0)


def _course_grid_block() -> str:
    text = (MANUSCRIPT / "front_matter.md").read_text(encoding="utf-8")
    return _marked_block(text, (_GRID_START, _GRID_END))


def test_renderable_h1s_match_canonical_toc() -> None:
    book_toc = load_toc(PROJECT)
    mismatches: list[str] = []

    for unit in book_toc.units:
        if _first_h1(unit.intro_path) != unit.intro_title:
            mismatches.append(str(unit.intro_path.relative_to(PROJECT)))
        for chapter in unit.chapters:
            if _first_h1(chapter.path) != chapter.title:
                mismatches.append(str(chapter.path.relative_to(PROJECT)))

    for companion in (*book_toc.labs, *book_toc.questions):
        if _first_h1(companion.path) != companion.title:
            mismatches.append(str(companion.path.relative_to(PROJECT)))

    for reference in book_toc.references:
        if _first_h1(reference.path) != reference.title:
            mismatches.append(str(reference.path.relative_to(PROJECT)))

    assert not mismatches


def test_lab_and_question_config_entries_do_not_duplicate_titles() -> None:
    appendices = _config()["appendices"]
    offenders: list[str] = []
    for section in ("labs", "questions"):
        for bundle in appendices[section]:
            for entry in bundle["files"]:
                if "title" in entry:
                    offenders.append(f"{section}/{bundle['unit']}/{entry['file']}")
    assert not offenders


def test_course_planning_grid_uses_exact_config_chapter_titles() -> None:
    book_toc = load_toc(PROJECT)
    front = _course_grid_block()
    expected_grid = f"{_GRID_START}\n{build_grid(book_toc)}\n{_GRID_END}"
    assert front == expected_grid
    for chapter in book_toc.chapters:
        unit = book_toc.units_by_id[chapter.unit_id]
        assert chapter.name_ref in front
        assert unit.name_ref in front
        assert chapter.title not in front
    assert "Water — The Molecule of Life" not in front
    assert "Water And Life" not in front


def test_front_matter_navigation_lists_every_unit_and_reference_once() -> None:
    book_toc: BookToc = load_toc(PROJECT)
    block = _navigation_block()
    for unit in book_toc.units:
        assert block.count(unit.name_ref) == 1, unit.display_title
    for reference in book_toc.references:
        assert block.count(reference.name_ref) == 1, reference.title


def test_front_matter_generated_blocks_match_toc_builders() -> None:
    book_toc = load_toc(PROJECT)
    text = (MANUSCRIPT / "front_matter.md").read_text(encoding="utf-8")
    assert _marked_block(text, NAV_MARKER) == build_front_matter_navigation(book_toc)
    assert _marked_block(text, READING_PATHS_MARKER) == build_suggested_reading_paths(book_toc)
    assert _marked_block(text, CONCEPT_MAP_MARKER) == build_textbook_concept_map(book_toc)


def test_preface_scope_table_matches_toc_builder() -> None:
    book_toc = load_toc(PROJECT)
    text = (MANUSCRIPT / "preface.md").read_text(encoding="utf-8")
    assert _marked_block(text, PREFACE_SCOPE_MARKER) == build_preface_scope_table(book_toc)


def test_unit_intro_section_labels_present() -> None:
    book_toc = load_toc(PROJECT)
    standalone = re.compile(r"^\\label\{sec:[^}]+\}\s*$", re.MULTILINE)
    for unit in book_toc.units:
        text = unit.intro_path.read_text(encoding="utf-8")
        first_h1 = next((line for line in text.splitlines() if line.startswith("# ")), "")
        assert f"{{#{unit.section_label}" in first_h1, unit.intro_path
        assert standalone.search(text) is None, unit.intro_path


def test_pandoc_binds_unnumbered_h1_identifier_to_section_label() -> None:
    """Guard ``\\nameref`` support: Pandoc must emit ``\\section*{{…}}\\label{{sec:…}}``."""
    import shutil
    import subprocess

    pandoc = shutil.which("pandoc")
    if pandoc is None:
        pytest.skip("pandoc not installed")
    sample = (
        "# Unit I — Chemistry of Life: Introduction {#sec:unit_I_unit_intro .unnumbered}\n\n"
        "## Why This Unit Matters {.unnumbered}\n"
    )
    result = subprocess.run(
        [pandoc, "-f", "markdown", "-t", "latex"],
        input=sample,
        capture_output=True,
        text=True,
        check=True,
    )
    latex = result.stdout.replace("\n", " ")
    assert "\\section*{Unit I --- Chemistry of Life: Introduction}\\label{sec:unit_I_unit_intro}" in latex
    assert "\\subsection*{Why This Unit Matters}" in latex


def test_generated_appendix_headings_match_reference_config_titles() -> None:
    book_toc = load_toc(PROJECT)
    references = book_toc.references_by_file
    assert _first_h1(references["appendix_curriculum_map.md"].path) == references[
        "appendix_curriculum_map.md"
    ].title
    assert _first_h1(references["appendix_instructor_orchestration.md"].path) == references[
        "appendix_instructor_orchestration.md"
    ].title


def test_generated_appendix_subheadings_do_not_hard_code_chapter_numbers() -> None:
    """Generated appendix headings should use canonical titles, not Chapter N prefixes."""
    for filename in ("appendix_curriculum_map.md", "appendix_instructor_orchestration.md"):
        text = (MANUSCRIPT / "appendices" / filename).read_text(encoding="utf-8")
        offenders = re.findall(r"^#{3,4}\s+Chapter\s+\d+:", text, flags=re.MULTILINE)
        assert not offenders, filename


def test_toc_exposes_canonical_chapter_labels_by_number() -> None:
    book_toc = load_toc(PROJECT)
    assert book_toc.chapters_by_number[2].title == "Water — The Molecule of Life"
    assert book_toc.chapters_by_number[2].section_label == "sec:unit_I_water_and_life"
    assert book_toc.chapters_by_companion_number["0.1"].section_label == "sec:unit_0_systems_science"
    assert book_toc.chapters_by_companion_number["0.4"].section_label == "sec:unit_0_history_philosophy_biology"
    assert set(book_toc.chapters_by_companion_number).issuperset({"0.1", "0.2", "0.3", "0.4"})


def test_unit_zero_display_numbers_do_not_shift_main_chapters() -> None:
    book_toc = load_toc(PROJECT)
    display_numbers = {chapter.chapter_id: chapter.display_number for chapter in book_toc.chapters}
    assert display_numbers["unit_0_systems_science"] == "0.1"
    assert display_numbers["unit_0_complex_adaptive_systems"] == "0.2"
    assert display_numbers["unit_0_active_inference"] == "0.3"
    assert display_numbers["unit_0_history_philosophy_biology"] == "0.4"
    assert display_numbers["unit_I_atoms_molecules"] == "1"


def test_render_injection_resets_section_numbering_after_unit_zero() -> None:
    book_toc = load_toc(PROJECT)
    ordered = [
        MANUSCRIPT / "front_matter.md",
        MANUSCRIPT / "preface.md",
        book_toc.units_by_id["unit_0"].intro_path,
        *book_toc.units_by_id["unit_0"].chapters,
        book_toc.units_by_id["unit_I"].intro_path,
        book_toc.chapters_by_id["unit_I_atoms_molecules"].path,
    ]
    ordered_paths = cast(list[Path], [item.path if hasattr(item, "path") else item for item in ordered])
    directives = _section_numbering_directives(ordered_paths)
    assert r"\renewcommand{\thesection}{0.\arabic{section}}" in directives[
        book_toc.chapters_by_id["unit_0_systems_science"].path.resolve()
    ]
    assert r"\renewcommand{\thesection}{\arabic{section}}" in directives[
        book_toc.units_by_id["unit_I"].intro_path.resolve()
    ]


def test_chapter_badges_match_canonical_format() -> None:
    """Metadata badges must match insert_chapter_metadata output (no stale ordinals)."""
    book_toc = load_toc(PROJECT)
    chapter_map = book_toc.chapters_by_id
    mismatches: list[str] = []
    badge_pattern = re.compile(
        re.escape(_metadata_script._BADGE_MARKER) + r"\n> .*(?=\n|$)",
        flags=re.MULTILINE,
    )
    for chapter in book_toc.chapters:
        expected = _metadata_script._format_badge(chapter, chapter_map)
        text = chapter.path.read_text(encoding="utf-8")
        match = badge_pattern.search(text)
        if match is None:
            mismatches.append(f"{chapter.path.relative_to(PROJECT)}: missing badge")
            continue
        if match.group(0) != expected:
            mismatches.append(str(chapter.path.relative_to(PROJECT)))
    assert not mismatches, f"Stale chapter badges: {mismatches[:5]}"


def test_companion_h1s_do_not_embed_chapter_ordinals() -> None:
    """Lab and question H1s must not bake in Ch N / Lab N ordinals."""
    offenders: list[str] = []
    for companion in (*load_toc(PROJECT).labs, *load_toc(PROJECT).questions):
        h1 = _first_h1(companion.path)
        if re.search(r"\bCh\s+\d", h1):
            offenders.append(f"{companion.path.relative_to(PROJECT)}: {h1}")
        if re.match(r"^Lab\s+\d", h1):
            offenders.append(f"{companion.path.relative_to(PROJECT)}: {h1}")
    assert not offenders, offenders[:5]


def test_markdown_headings_are_toc_safe() -> None:
    """No source heading should create blank or double-numbered ToC entries."""
    manual_prefix = re.compile(r"^\d+(?:\.\d+)*\.?\s+\S")
    offenders: list[str] = []
    for path in sorted(MANUSCRIPT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        in_fence = False
        for line_no, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not line.startswith("#"):
                continue
            match = re.match(r"^(#{1,6})\s*(?P<title>.*)$", line)
            if match is None:
                continue
            title = _heading_display(match.group("title"))
            if not title or manual_prefix.match(title):
                offenders.append(f"{path.relative_to(PROJECT)}:{line_no}:{line}")
    assert not offenders


def test_alt_comments_do_not_become_blank_setext_headings() -> None:
    offenders: list[str] = []
    pattern = re.compile(r"<!--\s*alt:\s*.*?\s*-->\n---", flags=re.DOTALL)
    for path in sorted(MANUSCRIPT.rglob("*.md")):
        if pattern.search(path.read_text(encoding="utf-8")):
            offenders.append(str(path.relative_to(PROJECT)))
    assert not offenders
