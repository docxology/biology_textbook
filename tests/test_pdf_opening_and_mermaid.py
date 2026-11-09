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
from pypdf import PdfReader

from biology.maintenance.chapter_badges import COURSE_GRID_COLUMN_SPEC
from biology.pipeline.orphan_figures import FigureInsertion, inject
from biology.pipeline.rendering import (
    _inline_diagram_bounds,
    _prepare_inline_diagrams,
    render_textbook,
)
from biology.visual_contracts.scan import inline_stem, normalise_inline_mermaid_source
from textbook_paths import PROJECT, discover_template_root


@pytest.mark.parametrize("watermark_instructor", [False, True])
def test_real_instructor_pdf_uses_fresh_sources_and_strict_png(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, watermark_instructor: bool,
) -> None:
    if discover_template_root(PROJECT) is None:
        pytest.skip("explicit template integration dependency is unavailable")
    if any(shutil.which(tool) is None for tool in ("mmdc", "pandoc", "xelatex", "bibtex", "pdftotext")):
        pytest.skip("native PDF toolchain is unavailable")
    manuscript = tmp_path / "docs" / "manuscript"
    unit_zero = manuscript / "unit_0" / "systems_science.md"
    unit_zero.parent.mkdir(parents=True)
    unit_zero.write_text(
        "# Opening foundations\n\nA supplied opening section.\n\n"
        "```mermaid\nflowchart LR\n C[Input] --> D[Output]\n```\n"
        "<!-- alt: A synthetic input is connected to an output. -->\n"
        r"*Openingcaption: $K_m$ with **Openingbold** and \citep[p. 7]{captionsecond}. "
        "Supplied operators A≤B, C≲D, E∝F, G⇌H, I⋅J, K∘L, 𝜑 and 𝜌. Openingend.*\n",
        encoding="utf-8",
    )
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
        r'<!-- alt: Conversion of substrate to product; }]' '\n'
        r'\end{figure}\typeout{ALTBOUNDARYEXECUTED}% $ # & _ { } ~ ^ -->' '\n'
        '*Captionplain *Captionemphasis* **Captionbold** `Captioncode`{.python}: '
        r'Na$^+$/K$^+$ transport with [**Captionglossary**](#gl:caption-substrate) '
        r'and [Captionlink](https://example.org/caption-proof); 50% & {bounded} #1. '
        'Literal % BIOLOGY-INLINE-CAPTION-END. '
        r'\citep{captionfixture,captionsecond}; \citet{captionfixture}. Captionend.*' '\n\n'
        '[**Substrate glossary entry**]{#gl:caption-substrate}\n\n'
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
    (manuscript / "references.bib").write_text(
        '@article{captionfixture, author={Captionauthor, Alice}, year={2024}, '
        'title={Synthetic renderer fixture}, journal={Fixture Journal}}\n'
        '@article{captionsecond, author={Secondauthor, Bob}, year={2025}, '
        'title={Second synthetic renderer fixture}, journal={Fixture Journal}}\n',
        encoding="utf-8",
    )
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
        ("biology.visual_contracts.render", "PROJECT_ROOT", tmp_path),
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
    opening_caption = re.search(r"Openingcaption:.*?Openingend", extracted, re.DOTALL)
    assert opening_caption is not None
    visible_opening = " ".join(opening_caption[0].split())
    assert all(text in visible_opening for text in ("Openingbold", "Secondauthor", "2025", "p. 7"))
    assert not any(token in visible_opening for token in (r"\cite", "$", "*", "`"))
    tex = pdf.with_name("_combined_manuscript.tex").read_text(encoding="utf-8")
    opening_tex = re.search(r"\\caption\{Openingcaption:(.*?)Openingend\.\}", tex, re.DOTALL)
    assert opening_tex is not None
    for command in ("leq", "lesssim", "propto", "rightleftharpoons", "cdot", "circ", "varphi", "rho"):
        assert "\\" + command in opening_tex[1]
    caption = re.search(r"Captionplain.*?Captionend\.", extracted, re.DOTALL)
    assert caption is not None
    visible_caption = " ".join(caption[0].split())
    for text in ("Captionemphasis", "Captionbold", "Captioncode", "Captionglossary", "Captionlink",
                 "Captionauthor", "2024", "Secondauthor", "2025", "50% & {bounded} #1"):
        assert text in visible_caption
    assert re.search(r"Na\s*\+\s*/K\s*\+", visible_caption)
    assert re.search(r"%\s+BIOLOGY-\s*INLINE-\s*CAPTION-\s*END", visible_caption)
    assert not any(token in visible_caption for token in (r"\cite", "$", "^", "*", "`"))
    assert "ALTBOUNDARYEXECUTED" not in extracted
    reader = PdfReader(pdf)
    probes = ("Captionplain", "Captionemphasis", "Captionbold", "Captioncode")
    fonts: dict[str, set[str]] = {probe: set() for probe in probes}
    links: list[dict] = []

    def record_font(text: str, _cm: list[float], _tm: list[float], font: dict | None, _size: float) -> None:
        for probe in probes:
            if probe in text and font is not None:
                fonts[probe].add(str(font["/BaseFont"]))

    for page in reader.pages:
        page.extract_text(visitor_text=record_font)
        links.extend(annotation.get_object() for annotation in page.get("/Annots", []))
    assert all(fonts.values())
    assert all(fonts[left].isdisjoint(fonts[right]) for index, left in enumerate(probes)
               for right in probes[index + 1:])
    actions = [link["/A"].get_object() for link in links if "/A" in link]
    assert any(action.get("/URI") == "https://example.org/caption-proof" for action in actions)
    assert any(action.get("/D") == destination("gl:caption-substrate") for action in actions)
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
    assert "ALTBOUNDARYEXECUTED" not in log
    dimensions = re.search(r"COURSEGRIDWIDTH=([0-9.]+)pt;AVAILABLE=([0-9.]+)pt", log)
    assert dimensions is not None
    assert float(dimensions[1]) <= float(dimensions[2]) + 0.2
    assert "STALE HYDRATION" not in extracted
    assert ("INSTRUCTOREDITION" in "".join(extracted.split())) is watermark_instructor
    assert not stale.exists()
    pngs = list(stale.parent.glob("inline_mermaid_*.png"))
    assert len(pngs) == 2
    for png in pngs:
        with Image.open(png) as image:
            assert image.format == "PNG"
            image.load()
            assert cast(tuple[int, int], image.convert("L").getextrema())[0] < 200


def test_real_pdf_chapter_links_survive_unit_zero_counter_reset(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Resolve native PDF links, not just matching labels in a shared aux file."""
    if discover_template_root(PROJECT) is None:
        pytest.skip("explicit template integration dependency is unavailable")
    if any(shutil.which(tool) is None for tool in ("mmdc", "pandoc", "xelatex", "bibtex", "pdftotext")):
        pytest.skip("native PDF toolchain is unavailable")
    manuscript = tmp_path / "docs" / "manuscript"
    fixtures = {}
    units = []
    canonical_config = yaml.safe_load(
        (PROJECT / "docs" / "manuscript" / "config.yaml").read_text(encoding="utf-8"),
    )
    for unit, prefix, title_prefix in (
        ("unit_0", "opening", "Opening"), ("unit_I", "core", "Core"),
    ):
        configured_chapters = []
        source_unit = next(record for record in canonical_config["units"] if record["id"] == unit)
        for number, chapter in enumerate(source_unit["chapters"][:4], start=1):
            path = manuscript / unit / chapter["file"]
            title, slug, label = (
                f"{title_prefix} chapter {number}", f"{prefix}-{number}", f"sec:{prefix}_{number}",
            )
            marker = f"TARGET{prefix.upper()}{number}"
            fixtures[path] = (
                title, slug, label, f"0.{number}" if unit == "unit_0" else str(number), marker,
            )
            body = (
                f"# {title} {{#{slug}}}\n\n"
                + rf"\label{{{label}}}" + "\n\n"
                f"{marker}\n\n## Detail\n\n" + rf"\label{{{label}_detail}}" + "\n\n"
                "Detail body.\n\n### Nested detail\n\n"
                + rf"\label{{{label}_nested}}" + "\n\nNested body.\n\n\\clearpage\n"
            )
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")
            configured_chapters.append({"file": path.name, "title": title})
        units.append({"id": unit, "label": "0" if unit == "unit_0" else "I",
                      "title": title_prefix, "directory": unit, "chapters": configured_chapters})
    (manuscript / "unit_I" / "unit_intro.md").write_text(
        "# Core orientation {.unnumbered}\n\nORIENTATIONPAGE\n\n\\clearpage\n", encoding="utf-8",
    )
    navigation = ["# Navigation {.unnumbered}\n\nNAVIGATIONPROBE"]
    for title, slug, label, _display_number, _marker in fixtures.values():
        navigation.append(
            f"[{title}](#{slug}): "
            + rf"\cref{{{label}}}; \cref{{{label}_detail}}; \cref{{{label}_nested}}."
        )
    (manuscript / "navigation.md").write_text(
        "\n\n".join([*navigation, r"\clearpage"]), encoding="utf-8",
    )
    shutil.copy2(PROJECT / "docs" / "manuscript" / "preamble.md", manuscript / "preamble.md")
    config = {
        "book": {"title": "Chapter navigation regression", "author": "Fixture Author",
                 "edition": "1.1", "year": 2026, "license": "CC BY 4.0", "code_license": "Apache-2.0"},
        "units": units,
        "front_matter": {"include_front_matter": True, "files": ["navigation.md"]},
    }
    (manuscript / "config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    injected = tmp_path / "output" / "manuscript"
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
        ("biology.visual_contracts.render", "PROJECT_ROOT", tmp_path),
    ):
        monkeypatch.setattr(f"{module}.{name}", value)
    pdf = render_textbook()
    reader = PdfReader(pdf)
    extracted = subprocess.run(
        ["pdftotext", str(pdf), "-"], capture_output=True, text=True,
        check=True, stdin=subprocess.DEVNULL,
    ).stdout
    page_texts = [" ".join(text.split()) for text in extracted.rstrip("\f").split("\f")]
    assert len(page_texts) == len(reader.pages)
    navigation_pages = [index for index, text in enumerate(page_texts) if "NAVIGATIONPROBE" in text]
    assert len(navigation_pages) == 1
    auxiliary = pdf.with_name("_combined_manuscript.aux").read_text(encoding="utf-8")
    named_destinations = reader.named_destinations
    link_targets = []
    for reference in reader.pages[navigation_pages[0]].get("/Annots", []):
        annotation = reference.get_object()
        if annotation.get("/Subtype") != "/Link":
            continue
        if "/Dest" in annotation:
            link_targets.append(annotation["/Dest"])
        elif "/A" in annotation:
            action = annotation["/A"].get_object()
            if action.get("/S") == "/GoTo":
                link_targets.append(action["/D"])
    chapter_destinations = set()
    target_pages = set()
    for title, _slug, label, display_number, marker in fixtures.values():
        expected_pages = [index for index, text in enumerate(page_texts) if marker in text]
        assert len(expected_pages) == 1
        expected_page = expected_pages[0]
        assert re.search(
            r"(?<![\d.])" + re.escape(display_number) + r"\s*"
            + r"\s*".join(re.escape(word) for word in title.split()) + r"\b", page_texts[expected_page],
        )
        for suffix in ("", "_detail", "_nested"):
            # Aux labels identify the link name; only PDF objects prove its target.
            match = re.search(
                r"\\newlabel\{" + re.escape(label + suffix)
                + r"\}\{\{[^}]*\}\{[^}]*\}\{[^}]*\}\{([^}]*)\}", auxiliary,
            )
            assert match is not None
            destination_name = match[1]
            assert destination_name in link_targets
            destination = named_destinations[destination_name]
            actual_page = reader.get_destination_page_number(destination)
            assert actual_page == expected_page, (label + suffix, expected_page, actual_page)
            if not suffix:
                chapter_destinations.add(destination_name)
                target_pages.add(actual_page)
    assert len(chapter_destinations) == len(fixtures)
    assert len(target_pages) == len(fixtures)


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


@pytest.mark.parametrize("caption", [
    r"Unsafe \input{caption-secret}",
    r"Unsafe $\input{caption-secret}$",
    r"Unsafe $\csname input\endcsname{caption-secret}$",
    r"Unsafe $^^5cinput{caption-secret}$",
    r"Unsafe $\rightleftharpoons\input{caption-secret}$",
    r"Unsafe \citep[\input{caption-secret}]{captionfixture}",
    r"Unsafe `\input{caption-secret}`{=latex}",
    "Unsafe <script>caption-secret</script>",
    "Unsafe ![nested image](caption-secret.png)",
    "Unsafe [link](javascript:caption-secret)",
    "Unsafe $$x^2$$",
    "Unsupported ~~obsolete~~ replacement",
    "",
])
def test_inline_caption_boundary_refuses_unsafe_or_unsupported_content(
    tmp_path: Path, caption: str,
) -> None:
    if discover_template_root(PROJECT) is None or shutil.which("pandoc") is None:
        pytest.skip("explicit template and native Pandoc dependencies are unavailable")
    source = "flowchart TD\n A[Substrate] --> B[Product]"
    manuscript = tmp_path / "chapter.md"
    content = (f"```mermaid\n{source}\n```\n"
               "<!-- alt: Substrate becomes product in a synthetic process diagram. -->\n"
               f"*{caption}*\n")
    manuscript.write_text(content, encoding="utf-8")
    png = tmp_path / f"{inline_stem(1, normalise_inline_mermaid_source(source))}.png"
    Image.new("RGB", (20, 20), "black").save(png)
    original_png = png.read_bytes()
    with pytest.raises(ValueError, match="caption"):
        _prepare_inline_diagrams([manuscript], [png])
    assert manuscript.read_text(encoding="utf-8") == content
    assert png.read_bytes() == original_png


def test_inline_rich_caption_does_not_bypass_asset_source_identity(tmp_path: Path) -> None:
    if discover_template_root(PROJECT) is None or shutil.which("pandoc") is None:
        pytest.skip("explicit template and native Pandoc dependencies are unavailable")
    manuscript = tmp_path / "chapter.md"
    content = ("```mermaid\nflowchart LR\n A --> B\n```\n"
               "<!-- alt: Two nodes connected by a directed synthetic transition. -->\n"
               r"*Na$^+$ transport with **retained** citation \citep{captionfixture}.*" "\n")
    manuscript.write_text(content, encoding="utf-8")
    with pytest.raises(RuntimeError, match="source does not match rendered asset"):
        _prepare_inline_diagrams([manuscript], [tmp_path / "inline_mermaid_0001_wrong.png"])
    assert manuscript.read_text(encoding="utf-8") == content
