"""Consumer-visible selection, preservation and fresh-hydration regressions."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

from biology.pipeline.collection import collect_ordered_chapters
from biology.pipeline.injection import inject_chapters_for_rendering
from biology.toc import load_toc


def selected_book(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, dict[str, Any]]:
    manuscript = tmp_path / "docs" / "manuscript"
    manuscript.mkdir(parents=True)
    for name in ("front_matter.md", "preface.md", "unit_I/water_and_life.md",
                 "labs/unit_I/lab_water_and_life.md", "questions/unit_I/questions_water_and_life.md"):
        path = manuscript / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Supplied source\n", encoding="utf-8")
    monkeypatch.setattr("biology.pipeline.collection.PROJECT_ROOT", tmp_path)
    monkeypatch.setattr("biology.pipeline.collection.MANUSCRIPT_DIR", manuscript)
    config = {
        "front_matter": {"include_front_matter": True, "include_preface": False,
                         "files": [{"file": "front_matter.md"}, {"file": "preface.md"}]},
        "units": [{"id": "unit_I", "label": "I", "title": "Foundations", "directory": "unit_I",
                   "chapters": [{"file": "atoms_molecules.md", "title": "Atoms", "enabled": False},
                                {"file": "water_and_life.md", "title": "Water"}]}],
        "appendices": {
            "include_labs": True, "include_questions": True,
            "labs": [{"unit": "unit_I", "files": [{"file": "lab_atoms_molecules.md"}, {"file": "lab_water_and_life.md"}]}],
            "questions": [{"unit": "unit_I", "files": [{"file": "questions_atoms_molecules.md"}, {"file": "questions_water_and_life.md"}]}],
        },
    }
    return manuscript, config


def test_selection_uses_snapshot_and_honors_disabled_chapter_and_preface(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript, config = selected_book(tmp_path, monkeypatch)
    assert collect_ordered_chapters(config) == [
        manuscript / "front_matter.md", manuscript / "unit_I/water_and_life.md",
        manuscript / "labs/unit_I/lab_water_and_life.md",
        manuscript / "questions/unit_I/questions_water_and_life.md",
    ]
    toc = load_toc(tmp_path, config=config)
    assert toc.chapters[0].display_number == "1"
    assert [lab.chapter.chapter_id for lab in toc.labs] == ["unit_I_water_and_life"]


def test_missing_selected_input_is_not_silently_omitted(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript, config = selected_book(tmp_path, monkeypatch)
    (manuscript / "unit_I/water_and_life.md").unlink()
    with pytest.raises(FileNotFoundError, match="water_and_life"):
        collect_ordered_chapters(config)


def test_configured_input_cannot_escape_manuscript(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript, config = selected_book(tmp_path, monkeypatch)
    (manuscript.parent / "outside.md").write_text("Not book content", encoding="utf-8")
    config["front_matter"]["files"] = [{"file": "../outside.md"}]
    with pytest.raises(ValueError, match="escapes"):
        collect_ordered_chapters(config)


def injection_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    manuscript = tmp_path / "source"
    manuscript.mkdir()
    output = tmp_path / "output" / "manuscript"
    output.mkdir(parents=True)
    (output / "old.md").write_text("previous complete manuscript", encoding="utf-8")
    (output / "references.bib").write_text("old bibliography", encoding="utf-8")
    monkeypatch.setattr("biology.pipeline.injection.OUTPUT_DIR", output)
    monkeypatch.setattr("biology.pipeline.injection.MANUSCRIPT_DIR", manuscript)
    monkeypatch.setattr("biology.pipeline.injection.PROJECT_ROOT", tmp_path)
    return manuscript, output


def test_read_failure_preserves_complete_previous_injection(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript, output = injection_tree(tmp_path, monkeypatch)
    good = manuscript / "good.md"
    good.write_text("new first chapter", encoding="utf-8")
    invalid = manuscript / "invalid.md"
    invalid.write_bytes(b"\xff")
    before = {path.name: path.read_bytes() for path in output.iterdir()}
    with pytest.raises(UnicodeDecodeError):
        inject_chapters_for_rendering([good, invalid])
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before
    assert not list(output.parent.glob(".manuscript-stage-*"))


def test_fresh_injection_cannot_reuse_stale_auxiliary_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript, output = injection_tree(tmp_path, monkeypatch)
    source = manuscript / "fresh.md"
    source.write_text("# Fresh source\n", encoding="utf-8")
    inject_chapters_for_rendering([source])
    assert not (output / "old.md").exists()
    assert not (output / "references.bib").exists()
    assert "# Fresh source" in (output / "01_fresh.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("answer_template", [
    "{code}", "Before ≤ 2.\n\n{code}", "{code}\n\nAfter ≤ 2.",
    "Before ≤ 2.\n\n{code}\n\nAfter ≤ 2.",
])
def test_instructor_hydration_preserves_code_and_math_in_every_answer_position(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, answer_template: str,
) -> None:
    manuscript, output = injection_tree(tmp_path, monkeypatch)
    source = manuscript / "fresh.md"
    outside_code = 'print("outside ≤")'
    answer_code = 'print("answer ≤")'
    answer = answer_template.format(code=f"```python\n{answer_code}\n```")
    source.write_text(
        f'Threshold ≤ 1.\n\n$x ≤ 1$\n\n```python\n{outside_code}\n```\n'
        f'<!-- SOLUTION\n{answer}\nSOLUTION -->\n', encoding="utf-8",
    )
    inject_chapters_for_rendering([source], include_solutions=True)
    parsed = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars", "--to=json", str(output / "01_fresh.md")],
        capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL,
    )
    blocks = json.loads(parsed.stdout)["blocks"]
    assert [block["c"][1] for block in blocks if block["t"] == "CodeBlock"] == [outside_code]
    quotes = [block["c"] for block in blocks if block["t"] == "BlockQuote"]
    assert len(quotes) == 1
    assert [block["c"][1] for block in quotes[0] if block["t"] == "CodeBlock"] == [answer_code]
    math = [inline["c"][1] for block in blocks if block["t"] == "Para"
            for inline in block["c"] if inline["t"] == "Math"]
    assert r"\leq" in math
    assert "x ≤ 1" in math
