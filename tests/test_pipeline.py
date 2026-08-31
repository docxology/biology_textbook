"""Tests for biology.pipeline manuscript injection and numbering."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from biology.pipeline.analysis_smoke import run_domain_smoke
from biology.pipeline.collection import collect_ordered_chapters, load_config
from biology.pipeline.injection import (
    clear_stale_slide_artifacts,
    inject_chapters_for_rendering,
    instructor_preamble_text,
    reveal_solutions,
)
from biology.pipeline.numbering import (
    MAIN_NUMBERING_DIRECTIVE,
    UNIT_ZERO_NUMBERING_DIRECTIVE,
    section_numbering_directives,
)
from biology.pipeline.paths import MANUSCRIPT_DIR, OUTPUT_DIR, PROJECT_ROOT
from biology.pipeline.registries import write_figure_registry, write_visual_manifest
from biology.pipeline.report import build_analysis_report, write_analysis_report


def test_reveal_solutions_blockquotes_answer() -> None:
    text = "<!-- SOLUTION\nThe answer is 42.\nSOLUTION -->"
    result = reveal_solutions(text)
    assert "> The answer is 42." in result
    assert "<!-- SOLUTION" not in result


def test_reveal_solutions_normalizes_unicode_math_symbols() -> None:
    text = "<!-- SOLUTION\nATP ⇌ ADP + Pi and 𝜑 ≤ 1.\nSOLUTION -->"
    result = reveal_solutions(text)
    assert r"$\rightleftharpoons$" in result
    assert r"$\leq$" in result
    assert r"$\varphi$" in result
    assert "⇌" not in result
    assert "𝜑" not in result


def test_section_numbering_directives_for_unit_zero_and_main() -> None:
    unit_zero_chapter = MANUSCRIPT_DIR / "unit_0" / "systems_science.md"
    unit_one_intro = MANUSCRIPT_DIR / "unit_I" / "unit_intro.md"
    unit_one_chapter = MANUSCRIPT_DIR / "unit_I" / "atoms_molecules.md"
    if not unit_zero_chapter.exists():
        pytest.skip("manuscript not present in this checkout")

    ordered = [unit_zero_chapter, unit_one_intro, unit_one_chapter]
    directives = section_numbering_directives(ordered)
    assert directives[unit_zero_chapter.resolve()] == UNIT_ZERO_NUMBERING_DIRECTIVE
    assert directives[unit_one_intro.resolve()] == MAIN_NUMBERING_DIRECTIVE


def test_pipeline_paths_resolve_to_project_root() -> None:
    assert PROJECT_ROOT.name == "biology_textbook" or PROJECT_ROOT.is_dir()
    assert MANUSCRIPT_DIR == PROJECT_ROOT / "docs" / "manuscript"
    assert OUTPUT_DIR == PROJECT_ROOT / "output" / "manuscript"


def test_load_config_and_collect_ordered_chapters() -> None:
    config = load_config()
    chapters = collect_ordered_chapters(config)
    assert chapters
    assert all(path.suffix == ".md" for path in chapters)
    assert MANUSCRIPT_DIR / "unit_I" / "atoms_molecules.md" in chapters


def test_collect_ordered_chapters_includes_appendices_when_enabled() -> None:
    config = load_config()
    appendices = dict(config.get("appendices", {}) or {})
    appendices["include_labs"] = True
    appendices["include_questions"] = True
    config["appendices"] = appendices
    chapters = collect_ordered_chapters(config)
    assert any("labs" in str(path) for path in chapters)
    assert any("questions" in str(path) for path in chapters)


def test_run_domain_smoke_exercises_all_packages() -> None:
    report = run_domain_smoke()
    names = {result.name for result in report.results}
    assert names == {
        "cell_biology",
        "genetics",
        "evolution",
        "ecology",
        "biochemistry",
        "physiology",
        "microbiology",
        "botany",
        "neuroscience",
    }
    payload = report.as_dict()
    assert payload["genetics"]["codons"] == 64


def test_write_figure_registry_and_visual_manifest(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    injected_dir = tmp_path / "output" / "manuscript"
    injected_dir.mkdir(parents=True)
    injected_dir.joinpath("sample.md").write_text(
        "\n".join(
            [
                "\\begin{figure}",
                "\\includegraphics{../figures/demo.png}",
                "\\caption{Demo}",
                "\\label{fig:unit_I_demo}",
                "\\end{figure}",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr("biology.pipeline.registries.OUTPUT_DIR", injected_dir)
    monkeypatch.setattr("biology.pipeline.registries.PROJECT_ROOT", tmp_path)

    registry_path = write_figure_registry()
    records = json.loads(registry_path.read_text(encoding="utf-8"))
    assert records[0]["label"] == "fig:unit_I_demo"

    manifest_path = write_visual_manifest()
    assert manifest_path.exists()


def test_analysis_report_round_trip(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("biology.pipeline.report.PROJECT_ROOT", tmp_path)
    smoke = run_domain_smoke()
    registry = tmp_path / "output" / "figures" / "figure_registry.json"
    manifest = tmp_path / "reports" / "visual_manifest.json"
    registry.parent.mkdir(parents=True, exist_ok=True)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    registry.write_text("[]\n", encoding="utf-8")
    manifest.write_text("{}\n", encoding="utf-8")
    report = build_analysis_report(
        smoke,
        chapters_injected=3,
        figure_registry=registry,
        visual_manifest=manifest,
    )
    out = write_analysis_report(report, tmp_path / "output" / "analysis_report.json")
    loaded = json.loads(out.read_text(encoding="utf-8"))
    assert loaded["chapters_injected"] == 3
    assert "cell_biology" in loaded


def test_clear_stale_slide_artifacts_removes_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    slides = tmp_path / "output" / "slides"
    slides.mkdir(parents=True)
    (slides / "old.pdf").write_text("stale", encoding="utf-8")
    monkeypatch.setattr("biology.pipeline.injection.PROJECT_ROOT", tmp_path)

    clear_stale_slide_artifacts()

    assert list(slides.iterdir()) == []


def test_inject_chapters_reveals_solutions_and_copies_aux(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript = tmp_path / "manuscript"
    manuscript.mkdir()
    (manuscript / "config.yaml").write_text("paper:\n  title: Demo\n", encoding="utf-8")
    cover = manuscript / "assets" / "cover"
    cover.mkdir(parents=True)
    (cover / "cover.png").write_bytes(b"png")

    source = tmp_path / "chapter.md"
    source.write_text(
        "<!-- SOLUTION\nAnswer line.\nSOLUTION -->\n# Chapter\n",
        encoding="utf-8",
    )
    output = tmp_path / "output" / "manuscript"
    monkeypatch.setattr("biology.pipeline.injection.OUTPUT_DIR", output)
    monkeypatch.setattr("biology.pipeline.injection.MANUSCRIPT_DIR", manuscript)
    monkeypatch.setattr("biology.pipeline.injection.PROJECT_ROOT", tmp_path)

    inject_chapters_for_rendering([source], include_solutions=True)

    injected = next(output.glob("*.md"))
    content = injected.read_text(encoding="utf-8")
    assert "> Answer line." in content
    assert (output / "config.yaml").exists()
    assert (output / "assets" / "cover" / "cover.png").exists()


def test_instructor_preamble_text_inserts_before_closing_fence() -> None:
    text = "header\n```latex\n\\usepackage{geometry}\n```\n"
    patched = instructor_preamble_text(text, watermark_instructor=True)
    assert patched.index("draftwatermark") > patched.index("\\usepackage{geometry}")
    assert patched.endswith("```\n")


def test_instructor_preamble_text_appends_when_no_latex_fence() -> None:
    preamble = instructor_preamble_text("plain preamble\n", watermark_instructor=True)
    assert "draftwatermark" in preamble


def test_instructor_preamble_text_is_noop_when_disabled() -> None:
    text = "```latex\n\\usepackage{geometry}\n```\n"
    assert instructor_preamble_text(text, watermark_instructor=False) == text


def test_inject_applies_instructor_watermark_to_preamble(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript = tmp_path / "manuscript"
    manuscript.mkdir()
    (manuscript / "preamble.md").write_text("```latex\n\\usepackage{geometry}\n```\n", encoding="utf-8")
    source = tmp_path / "chapter.md"
    source.write_text("# Chapter\n", encoding="utf-8")
    output = tmp_path / "output" / "manuscript"
    monkeypatch.setattr("biology.pipeline.injection.OUTPUT_DIR", output)
    monkeypatch.setattr("biology.pipeline.injection.MANUSCRIPT_DIR", manuscript)
    monkeypatch.setattr("biology.pipeline.injection.PROJECT_ROOT", tmp_path)

    inject_chapters_for_rendering(
        [source],
        include_solutions=True,
        watermark_instructor=True,
    )

    preamble = (output / "preamble.md").read_text(encoding="utf-8")
    assert "draftwatermark" in preamble
    assert "INSTRUCTOR EDITION" in preamble


def test_load_config_include_solutions_enabled_for_instructor_edition() -> None:
    config = load_config()
    export = config.get("export", {})
    assert export.get("include_solutions") is True
    assert export.get("watermark_instructor") is False


def test_inject_preserves_existing_skip_beamer_marker(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    source = tmp_path / "sample.md"
    source.write_text("<!-- render:skip-beamer -->\n\n# Sample\n", encoding="utf-8")
    output = tmp_path / "output" / "manuscript"
    monkeypatch.setattr("biology.pipeline.injection.OUTPUT_DIR", output)
    monkeypatch.setattr("biology.pipeline.injection.MANUSCRIPT_DIR", tmp_path)
    monkeypatch.setattr("biology.pipeline.injection.PROJECT_ROOT", tmp_path)

    inject_chapters_for_rendering([source])

    content = next(output.glob("*.md")).read_text(encoding="utf-8")
    assert content.count("<!-- render:skip-beamer -->") == 1
