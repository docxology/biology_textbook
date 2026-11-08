"""Exercise actual source hydration, strict diagrams and the installed PDF backend."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import cast

import pytest
import yaml
from PIL import Image, ImageDraw

from biology.maintenance.chapter_badges import COURSE_GRID_COLUMN_SPEC
from biology.pipeline.orphan_figures import FigureInsertion, inject
from biology.pipeline.rendering import _inline_diagram_bounds, render_textbook
from textbook_paths import PROJECT, discover_template_root


@pytest.mark.parametrize("watermark_instructor", [False, True])
def test_real_instructor_pdf_uses_fresh_sources_and_strict_png(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, watermark_instructor: bool,
) -> None:
    if discover_template_root(PROJECT) is None:
        pytest.skip("explicit template integration dependency is unavailable")
    if any(shutil.which(tool) is None for tool in ("mmdc", "pandoc", "xelatex", "pdftotext")):
        pytest.skip("native PDF toolchain is unavailable")
    manuscript = tmp_path / "docs" / "manuscript"
    unit_zero = manuscript / "unit_0" / "systems_science.md"
    unit_zero.parent.mkdir(parents=True)
    unit_zero.write_text("# Opening foundations\n\nA supplied opening section.\n", encoding="utf-8")
    chapter = manuscript / "unit_I" / "atoms_molecules.md"
    chapter.parent.mkdir(parents=True)
    width_probe = (
        "\n```{=latex}\n"
        r"\newsavebox{\CourseGridProof}" "\n"
        r"\begingroup\setlength{\tabcolsep}{2pt}\footnotesize" "\n"
        rf"\sbox{{\CourseGridProof}}{{\begin{{tabular}}{{{COURSE_GRID_COLUMN_SPEC}}}"
        r"Unit & Number & Chapter & Difficulty & Reading & Lecture\\\end{tabular}}" "\n"
        r"\typeout{COURSEGRIDWIDTH=\the\wd\CourseGridProof;AVAILABLE=\the\textwidth}" "\n"
        r"\endgroup" "\n```\n"
    )
    chapter.write_text(
        '# Render sample\n\n\\label{sec:fixture_heading}\n\nA fresh, source-bound process diagram.\n\n'
        '```mermaid\nflowchart TD\n A[Substrate] --> B[Product]\n```\n'
        '<!-- alt: Conversion of substrate to product in a two-node process. -->\n'
        '*Substrate conversion to product in a simple process model.*\n\n'
        '1. FIRST QUESTION: identify the product.\n\n'
        '<!-- SOLUTION\nINSTRUCTOR PROOF: the supplied substrate becomes product.\nSOLUTION -->\n'
        '<!-- assess: LO=LO1; bloom=Understand -->\n'
        '2. FOLLOWING QUESTION: explain the conversion.\n' + width_probe,
        encoding="utf-8",
    )
    opening = tmp_path / "output" / "figures" / "opening.png"
    opening.parent.mkdir(parents=True)
    Image.new("RGB", (300, 40), "#123456").save(opening)
    inject(chapter, FigureInsertion(
        "opening", chapter, "# Render sample",
        "A test swatch separates heading destinations from floating figure destinations.",
        "fig:fixture_opening", "A dark rectangular swatch used for hyperlink-destination regression.",
    ))
    (manuscript / "preamble.md").write_text("```latex\n\\usepackage{array}\n```\n", encoding="utf-8")
    config = {
        "book": {"title": "Renderer regression", "author": "Daniel Ari Friedman", "edition": "1.1",
                 "year": 2026, "license": "CC BY 4.0", "code_license": "Apache-2.0"},
        "units": [
            {"id": "unit_0", "label": "0", "title": "Opening", "directory": "unit_0",
             "chapters": [{"file": "systems_science.md", "title": "Opening foundations"}]},
            {"id": "unit_I", "label": "I", "title": "Foundations", "directory": "unit_I",
             "chapters": [{"file": "atoms_molecules.md", "title": "Render sample"}]},
        ],
        "export": {"include_solutions": True, "watermark_instructor": watermark_instructor},
    }
    (manuscript / "config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    injected = tmp_path / "output" / "manuscript"
    injected.mkdir(parents=True)
    (injected / "old.md").write_text("STALE HYDRATION MUST NOT APPEAR", encoding="utf-8")
    stale = tmp_path / "output" / "figures" / "mermaid_inline" / "inline_mermaid_9999_stale.png"
    stale.parent.mkdir(parents=True)
    stale.write_bytes(b"obsolete invalid image")
    for module, name, value in (
        ("biology.pipeline.collection", "PROJECT_ROOT", tmp_path),
        ("biology.pipeline.collection", "MANUSCRIPT_DIR", manuscript),
        ("biology.pipeline.collection", "CONFIG_FILE", manuscript / "config.yaml"),
        ("biology.pipeline.injection", "PROJECT_ROOT", tmp_path),
        ("biology.pipeline.injection", "MANUSCRIPT_DIR", manuscript),
        ("biology.pipeline.injection", "OUTPUT_DIR", injected),
        ("biology.pipeline.numbering", "MANUSCRIPT_DIR", manuscript),
        ("biology.pipeline.rendering", "PROJECT_ROOT", tmp_path),
        ("biology.pipeline.rendering", "OUTPUT_DIR", injected),
    ):
        monkeypatch.setattr(f"{module}.{name}", value)
    pdf = render_textbook()
    auxiliary = pdf.with_name("_combined_manuscript.aux").read_text(encoding="utf-8")

    def destination(label: str) -> str:
        match = re.search(
            r"\\newlabel\{" + re.escape(label) + r"\}\{\{[^}]*\}\{[^}]*\}\{[^}]*\}\{([^}]*)\}",
            auxiliary,
        )
        assert match is not None
        return match[1]

    assert destination("sec:fixture_heading") == destination("render-sample")
    assert destination("fig:fixture_opening") != destination("sec:fixture_heading")
    extracted = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True,
                               check=True, stdin=subprocess.DEVNULL).stdout
    assert "Renderer regression" in extracted
    assert "INSTRUCTOR PROOF" in extracted
    assert "FOLLOWING QUESTION" in extracted
    assert re.search(r"\b0\.1\s+Opening foundations\b", extracted)
    assert re.search(r"(?m)^1\s+Render sample\b", extracted)
    hydrated = next(injected.glob("*atoms_molecules.md"))
    parsed = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars+raw_tex+header_attributes", "--to=json", str(hydrated)],
        capture_output=True, text=True, check=True, stdin=subprocess.DEVNULL,
    )
    blocks = json.loads(parsed.stdout)["blocks"]
    assert [block["c"][0][0] for block in blocks if block["t"] == "OrderedList"] == [1, 2]
    answers = [block for block in blocks if block["t"] == "BlockQuote"]
    assert len(answers) == 1
    assert "FOLLOWING" not in json.dumps(answers[0])
    log = pdf.with_name("_combined_manuscript.log").read_text(encoding="utf-8")
    dimensions = re.search(r"COURSEGRIDWIDTH=([0-9.]+)pt;AVAILABLE=([0-9.]+)pt", log)
    assert dimensions is not None
    assert float(dimensions[1]) <= float(dimensions[2]) + 0.2
    assert "STALE HYDRATION" not in extracted
    assert ("INSTRUCTOREDITION" in "".join(extracted.split())) is watermark_instructor
    assert not stale.exists()
    pngs = list(stale.parent.glob("inline_mermaid_*.png"))
    assert len(pngs) == 1
    with Image.open(pngs[0]) as image:
        assert image.format == "PNG"
        image.load()
        assert cast(tuple[int, int], image.convert("L").getextrema())[0] < 200


@pytest.mark.parametrize("mode,rectangle,expected", [
    ("RGB", (10, 15, 89, 64), (8, 13, 92, 67)),
    ("RGBA", (10, 15, 89, 64), (8, 13, 92, 67)),
    ("RGBA", (0, 0, 99, 79), (0, 0, 100, 80)),
])
def test_inline_diagram_crop_preserves_visible_edges_not_hidden_rgb(
    tmp_path: Path, mode: str, rectangle: tuple[int, int, int, int],
    expected: tuple[int, int, int, int],
) -> None:
    background = (255, 0, 255, 0) if mode == "RGBA" else (255, 255, 255)
    image = Image.new(mode, (100, 80), background)
    ImageDraw.Draw(image).rectangle(rectangle, fill=(30, 40, 50, 255) if mode == "RGBA" else (30, 40, 50))
    path = tmp_path / "diagram.png"
    image.save(path)
    assert _inline_diagram_bounds(path) == expected


def test_invisible_inline_diagram_cannot_be_printed_as_success(tmp_path: Path) -> None:
    path = tmp_path / "invisible.png"
    Image.new("RGBA", (100, 80), (255, 0, 255, 0)).save(path)
    with pytest.raises(ValueError, match="no visible diagram"):
        _inline_diagram_bounds(path)
