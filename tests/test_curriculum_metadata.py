"""Tests for the textbook-wide curriculum metadata layer."""

from __future__ import annotations

import importlib
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "docs" / "manuscript"
SRC = PROJECT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from textbook_paths import discover_template_root  # noqa: E402

TEMPLATE_ROOT = discover_template_root(PROJECT)

from biology.crossref.helpers import section_reference  # noqa: E402


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _chapter_path(chapter_id: str) -> Path:
    prefix, unit, stem = chapter_id.split("_", 2)
    return MANUSCRIPT / f"{prefix}_{unit}" / f"{stem}.md"


def _lab_path(chapter_id: str) -> Path:
    prefix, unit, stem = chapter_id.split("_", 2)
    return MANUSCRIPT / "labs" / f"{prefix}_{unit}" / f"lab_{stem}.md"


def _question_path(chapter_id: str) -> Path:
    prefix, unit, stem = chapter_id.split("_", 2)
    return MANUSCRIPT / "questions" / f"{prefix}_{unit}" / f"questions_{stem}.md"


def _curriculum():
    return importlib.import_module("biology.curriculum")


def _chapter_metadata():
    return _load_module("chapter_metadata_for_curriculum", PROJECT / "src" / "biology" / "chapter_metadata.py")


def _alignment():
    for path in (SRC, TEMPLATE_ROOT):
        if path is None:
            continue
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
    return importlib.import_module("biology.alignment")


def _sync_blocks():
    return importlib.import_module("biology.curriculum_sync.sync_blocks")


def test_sync_blocks_replaces_duplicate_marker_blocks() -> None:
    sync_blocks = _sync_blocks()
    block = "\n".join(
        [
            sync_blocks.CHAPTER_MARKER[0],
            "### Study Blueprint",
            sync_blocks.CHAPTER_MARKER[1],
        ]
    )
    text = f"Lead\n\n{block}\n\n{block}\n\nTail\n"

    updated, changed = sync_blocks._replace_block(
        text,
        sync_blocks.CHAPTER_MARKER,
        "replacement",
    )

    assert changed is True
    assert updated.count("replacement") == 1
    assert sync_blocks.CHAPTER_MARKER[0] not in updated


def test_sync_blocks_normalizes_heading_titles_and_attrs() -> None:
    sync_blocks = _sync_blocks()

    assert (
        sync_blocks._toc_safe_heading_title(
            "12. Further Reading {.unnumbered}",
            chapter_title="Cell Theory",
        )
        == "Further Reading and Source Notes: Cell Theory {.unnumbered}"
    )
    assert sync_blocks._format_heading(
        "Evidence",
        {"#anchor", ".unnumbered"},
    ) == "Evidence {.unnumbered #anchor}"


def test_sync_blocks_normalize_headings_preserves_fenced_code(tmp_path: Path) -> None:
    sync_blocks = _sync_blocks()
    path = tmp_path / "chapter.md"
    path.write_text(
        "\n".join(
            [
                "# Demo",
                "",
                "```markdown",
                "## Procedure",
                "```",
                "",
                "## 2. Procedure",
                "",
            ]
        ),
        encoding="utf-8",
    )

    changed = sync_blocks.normalize_headings(path, unnumbered=True, dry_run=False)

    assert changed is True
    text = path.read_text(encoding="utf-8")
    assert "```markdown\n## Procedure\n```" in text
    assert "## Experimental Procedure {.unnumbered}" in text


def test_every_config_chapter_has_curriculum_record() -> None:
    config = yaml.safe_load((MANUSCRIPT / "config.yaml").read_text(encoding="utf-8"))
    expected: set[str] = set()
    for unit in config["units"]:
        for chapter in unit["chapters"]:
            expected.add(f"{unit['id']}_{chapter['file'].removesuffix('.md')}")

    curriculum = _curriculum()
    actual = {record.chapter_id for record in curriculum.CURRICULUM}
    assert actual == expected


def test_curriculum_records_are_instructionally_complete() -> None:
    curriculum = _curriculum()
    for record in curriculum.CURRICULUM:
        assert len(record.core_concepts) >= 3
        for field in (
            record.big_idea,
            record.quantitative_model,
            record.data_skill,
            record.lab_focus,
            record.common_misconception,
            record.assessment_focus,
            record.transfer_task,
            record.bridge_api,
        ):
            assert field.strip(), record.chapter_id


def test_curriculum_bridge_apis_resolve() -> None:
    for path in (SRC, TEMPLATE_ROOT):
        if path is None:
            continue
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))

    curriculum = _curriculum()
    missing: list[str] = []
    for record in curriculum.CURRICULUM:
        module_name, attr = record.bridge_api.rsplit(".", 1)
        module = importlib.import_module(module_name)
        if not hasattr(module, attr):
            missing.append(f"{record.chapter_id}: {record.bridge_api}")
    assert not missing


def _has_section_label(text: str, label: str) -> bool:
    """Accept LaTeX ``\\label{}`` or Pandoc H1 ``{#label}`` identifiers."""
    return f"\\label{{{label}}}" in text or f"{{#{label}" in text


def test_curriculum_companion_paths_and_labels_exist() -> None:
    curriculum = _curriculum()
    missing: list[str] = []
    for record in curriculum.CURRICULUM:
        for path, label in (
            (_chapter_path(record.chapter_id), f"\\label{{sec:{record.chapter_id}}}"),
            (_lab_path(record.chapter_id), record.lab_label),
            (_question_path(record.chapter_id), record.question_label),
        ):
            if not path.exists():
                missing.append(f"missing file: {path.relative_to(PROJECT)}")
                continue
            text = path.read_text(encoding="utf-8")
            if path == _chapter_path(record.chapter_id):
                if f"\\label{{sec:{record.chapter_id}}}" not in text:
                    missing.append(f"missing label: {path.relative_to(PROJECT)} -> \\label{{sec:{record.chapter_id}}}")
            elif not _has_section_label(text, label):
                missing.append(f"missing label: {path.relative_to(PROJECT)} -> {label}")
    assert not missing


def test_generated_curriculum_blocks_are_present_once() -> None:
    curriculum = _curriculum()
    offenders: list[str] = []
    for record in curriculum.CURRICULUM:
        checks = (
            (_chapter_path(record.chapter_id), "<!-- curriculum-scaffold-start -->"),
            (_lab_path(record.chapter_id), "<!-- lab-evidence-checklist-start -->"),
            (_question_path(record.chapter_id), "<!-- question-coverage-start -->"),
        )
        for path, marker in checks:
            count = path.read_text(encoding="utf-8").count(marker)
            if count != 1:
                offenders.append(f"{path.relative_to(PROJECT)} has {count} copies of {marker}")
    assert not offenders


def test_curriculum_appendix_references_every_chapter_lab_and_question_bank() -> None:
    appendix = (MANUSCRIPT / "appendices" / "appendix_curriculum_map.md").read_text(encoding="utf-8")
    curriculum = _curriculum()
    for record in curriculum.CURRICULUM:
        assert section_reference(record.chapter_id) in appendix
        assert section_reference(record.lab_label) in appendix
        assert section_reference(record.question_label) in appendix


def test_chapter_metadata_and_curriculum_share_the_same_ids() -> None:
    curriculum = _curriculum()
    chapter_metadata = _chapter_metadata()
    curriculum_ids = {record.chapter_id for record in curriculum.CURRICULUM}
    metadata_ids = {record.chapter_id for record in chapter_metadata.CHAPTERS}
    assert curriculum_ids == metadata_ids


def test_alignment_records_cover_curriculum_records() -> None:
    curriculum = _curriculum()
    alignment = _alignment()
    curriculum_ids = {record.chapter_id for record in curriculum.CURRICULUM}
    alignment_ids = {record.chapter_id for record in alignment.ALIGNMENTS}
    assert alignment_ids == curriculum_ids


def test_alignment_records_use_known_framework_labels() -> None:
    alignment = _alignment()
    for record in alignment.ALIGNMENTS:
        assert set(record.vision_change_concepts) <= set(alignment.VISION_CHANGE_CONCEPTS)
        assert set(record.vision_change_competencies) <= set(alignment.VISION_CHANGE_COMPETENCIES)
        assert set(record.ap_big_ideas) <= set(alignment.AP_BIOLOGY_BIG_IDEAS)
        assert set(record.ap_science_practices) <= set(alignment.AP_BIOLOGY_PRACTICES)
        assert set(record.ngss_topics) <= set(alignment.NGSS_HS_LS_TOPICS)
        assert set(record.bioskills) <= set(alignment.BIOSKILLS_CATEGORIES)


def test_alignment_records_are_instructionally_complete() -> None:
    alignment = _alignment()
    for record in alignment.ALIGNMENTS:
        assert record.vision_change_concepts
        assert record.vision_change_competencies
        assert record.ap_big_ideas
        assert record.ap_science_practices
        assert record.ngss_topics
        assert record.bioskills
        assert record.spiral_thread.strip()
        assert record.instructor_move.strip()
        assert record.formative_check.strip()
        assert record.summative_product.strip()


def test_curriculum_appendices_include_alignment_and_instructor_orchestration() -> None:
    curriculum_appendix = (
        MANUSCRIPT / "appendices" / "appendix_curriculum_map.md"
    ).read_text(encoding="utf-8")
    instructor_appendix = (
        MANUSCRIPT / "appendices" / "appendix_instructor_orchestration.md"
    ).read_text(encoding="utf-8")
    curriculum = _curriculum()
    alignment = _alignment()
    for record in curriculum.CURRICULUM:
        framework = alignment.require(record.chapter_id)
        assert section_reference(record.chapter_id) in curriculum_appendix
        assert section_reference(record.lab_label) in instructor_appendix
        assert section_reference(record.question_label) in instructor_appendix
        assert framework.spiral_thread in instructor_appendix
        assert "Framework alignment" in curriculum_appendix


def test_alignment_lookup_helpers_and_counts() -> None:
    alignment = _alignment()
    first = alignment.ALIGNMENTS[0]
    assert alignment.by_id(first.chapter_id) == first
    assert alignment.require(first.chapter_id) == first
    with pytest.raises(KeyError):
        alignment.require("missing_chapter")

    counts = alignment.framework_counts()
    for framework_name in (
        "vision_change_concepts",
        "ap_big_ideas",
        "ap_science_practices",
        "ngss_topics",
        "bioskills",
    ):
        assert counts[framework_name]
