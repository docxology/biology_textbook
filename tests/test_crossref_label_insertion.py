"""Tests for ``biology.crossref.label_insertion``."""

from __future__ import annotations

from pathlib import Path

import yaml

from biology.crossref.label_insertion import (
    ChapterInfo,
    RewriteReport,
    apply_crossref_labels,
    build_ref_map,
    insert_label,
    insert_unnumbered_label,
    load_chapters,
    load_labs,
    load_questions,
    rewrite_prose,
)


def _write_minimal_config(tmp_path: Path) -> tuple[Path, Path]:
    manuscript = tmp_path / "manuscript"
    (manuscript / "unit_I").mkdir(parents=True)
    (manuscript / "labs" / "unit_I").mkdir(parents=True)
    (manuscript / "questions" / "unit_I").mkdir(parents=True)
    (manuscript / "unit_I" / "atoms.md").write_text("# Atoms\n\nSee Chapter 2 for context.\n", encoding="utf-8")
    (manuscript / "unit_I" / "water.md").write_text("# Water\n", encoding="utf-8")
    (manuscript / "labs" / "unit_I" / "lab_atoms.md").write_text("# Lab Atoms\n\nBody.\n", encoding="utf-8")
    (manuscript / "questions" / "unit_I" / "questions_atoms.md").write_text(
        "# Questions Atoms\n\nBody.\n", encoding="utf-8"
    )
    config = manuscript / "config.yaml"
    config.write_text(
        yaml.safe_dump(
            {
                "units": [
                    {
                        "id": "unit_I",
                        "label": "I",
                        "directory": "unit_I",
                        "chapters": [
                            {"file": "atoms.md", "title": "Atoms"},
                            {"file": "water.md", "title": "Water"},
                        ],
                    }
                ],
                "appendices": {
                    "labs": [{"unit": "unit_I", "files": [{"file": "lab_atoms.md"}]}],
                    "questions": [{"unit": "unit_I", "files": [{"file": "questions_atoms.md"}]}],
                },
            }
        ),
        encoding="utf-8",
    )
    return manuscript, config


def test_load_chapters_assigns_sequential_numbers(tmp_path: Path) -> None:
    manuscript, config = _write_minimal_config(tmp_path)
    chapters = load_chapters(config, manuscript)
    assert [c.number for c in chapters] == [1, 2]
    assert chapters[0].label == "sec:unit_I_atoms"
    assert chapters[1].title == "Water"


def test_load_labs_and_questions_produce_canonical_labels(tmp_path: Path) -> None:
    manuscript, config = _write_minimal_config(tmp_path)
    labs = load_labs(config, manuscript)
    questions = load_questions(config, manuscript)
    assert labs[0][1] == "sec:lab_unit_I_atoms"
    assert questions[0][1] == "sec:q_unit_I_atoms"


def test_insert_label_is_idempotent(tmp_path: Path) -> None:
    path = tmp_path / "ch.md"
    path.write_text("# Title\n\nbody\n", encoding="utf-8")
    report = RewriteReport()
    insert_label(path, "sec:demo", report)
    first = path.read_text(encoding="utf-8")
    assert "\\label{sec:demo}" in first
    assert report.labels_inserted == 1
    insert_label(path, "sec:demo", report)
    assert path.read_text(encoding="utf-8") == first
    assert report.labels_present == 1


def test_insert_unnumbered_label_uses_pandoc_identifier(tmp_path: Path) -> None:
    path = tmp_path / "lab.md"
    path.write_text("# Lab Title\n\nbody\n", encoding="utf-8")
    report = RewriteReport()
    insert_unnumbered_label(path, "sec:lab_demo", report)
    assert "{#sec:lab_demo .unnumbered}" in path.read_text(encoding="utf-8")


def test_rewrite_prose_replaces_chapter_n_with_cref(tmp_path: Path) -> None:
    path = tmp_path / "prose.md"
    path.write_text("As shown, see Chapter 2 for details.\n", encoding="utf-8")
    ref_map = {2: "sec:unit_I_water"}
    report = RewriteReport()
    rewrite_prose(path, ref_map, report)
    assert "\\cref{sec:unit_I_water}" in path.read_text(encoding="utf-8")
    assert report.crefs_rewritten == 1


def test_build_ref_map_skips_unit_zero_chapters() -> None:
    chapters = [
        ChapterInfo(0, "unit_0", "0", "intro", Path("intro.md"), "Intro", "sec:unit_0_intro"),
        ChapterInfo(1, "unit_I", "I", "atoms", Path("atoms.md"), "Atoms", "sec:unit_I_atoms"),
    ]
    assert build_ref_map(chapters) == {1: "sec:unit_I_atoms"}


def test_apply_crossref_labels_dry_run_does_not_write(tmp_path: Path) -> None:
    manuscript, config = _write_minimal_config(tmp_path)
    captured: list[tuple[Path, str]] = []
    report = apply_crossref_labels(
        dry_run=True,
        manuscript_root=manuscript,
        config_path=config,
        write_fn=lambda p, t: captured.append((p, t)),
    )
    assert report.labels_inserted >= 2
    assert captured == []
    assert "\\label{sec:unit_I_atoms}" not in (manuscript / "unit_I" / "atoms.md").read_text(encoding="utf-8")
