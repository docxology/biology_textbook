"""Render the live textbook using read-only, externally supplied template code."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from biology.citations import iter_citations
from biology.pipeline.collection import collect_ordered_chapters, load_config
from biology.pipeline.injection import inject_chapters_for_rendering
from biology.pipeline.paths import OUTPUT_DIR, PROJECT_ROOT
from biology.visual_contracts.render import render_inline_mermaid_assets
from biology.visual_contracts.scan import inline_stem, normalise_inline_mermaid_source
from textbook_io import require_independent_file_target, write_text_atomic
from textbook_paths import discover_template_root, require_project_output_directory


def _inline_diagram_bounds(path: Path) -> tuple[int, int, int, int]:
    """Find visible PNG content plus two pixels, excluding white/transparent padding."""
    from PIL import Image, ImageChops

    with Image.open(path) as image:
        canvas = Image.new("RGBA", image.size, "white")
        canvas.alpha_composite(image.convert("RGBA"))
        background = Image.new("RGB", image.size, "white")
        bounds = ImageChops.difference(canvas.convert("RGB"), background).getbbox()
        if bounds is None:
            raise ValueError(f"Inline Mermaid PNG contains no visible diagram: {path}")
        left, top, right, bottom = bounds
        return max(0, left - 2), max(0, top - 2), min(image.width, right + 2), min(image.height, bottom + 2)


_CAPTION_MATH_COMMANDS = frozenset(
    (
        "alpha", "beta", "gamma", "delta", "epsilon", "theta", "lambda", "mu",
        "nu", "pi", "rho", "sigma", "tau", "phi", "chi", "psi", "omega",
        "Gamma", "Delta", "Theta", "Lambda", "Pi", "Sigma", "Phi", "Psi", "Omega",
        "mathrm", "mathit", "mathbf", "mathsf", "mathtt", "text", "frac", "dfrac", "tfrac", "sqrt",
        "left", "right", "cdot", "times", "div", "pm", "mp", "le", "leq", "ge", "geq", "ne", "neq",
        "approx", "sim", "simeq", "equiv", "to", "rightarrow", "leftrightarrow", "infty",
        "rightleftharpoons", "lesssim", "propto", "circ", "varphi",
        "sum", "prod", "int", "log", "ln", "exp", "sin", "cos", "tan", "min", "max",
        "underbrace", "overbrace", "overline", "underline", "hat", "bar", "vec",
        "dot", "ddot", "quad", "qquad",
    )
)


def _validate_caption_node(node: Any) -> None:
    """Admit prose inlines, not arbitrary raw TeX, HTML, images or block content."""
    if isinstance(node, list):
        for child in node:
            _validate_caption_node(child)
    elif isinstance(node, dict):
        kind = node.get("t")
        if kind == "RawInline":
            format_name, text = node["c"]
            citations = list(iter_citations(text))
            # Shared citation parsing defines commands; this narrower grammar
            # prevents citekeys and plain pre/post-notes becoming a TeX escape.
            safe_arguments = re.fullmatch(
                r"\\[A-Za-z]+\*?(?:\[[^\\{}%$&#_^~\[\]\r\n]*\]){0,2}"
                r"\{[A-Za-z0-9_:.+/, \t-]+\}", text,
            )
            if (format_name not in {"tex", "latex"} or len(citations) != 1
                    or citations[0].start != 0 or citations[0].end != len(text)
                    or safe_arguments is None):
                raise ValueError("Inline Mermaid captions support raw TeX only for natbib citations")
        elif kind == "Math":
            math_kind, text = node["c"]
            if math_kind["t"] != "InlineMath":
                raise ValueError("Inline Mermaid captions require inline, not display, math")
            if "^^" in text:
                raise ValueError("Unsafe character-code escape in inline Mermaid caption math")
            depth = 0
            for token in re.findall(r"\\[A-Za-z]+|\\.|[^\\]", text):
                if token.startswith("\\"):
                    if token[1:] not in _CAPTION_MATH_COMMANDS and token not in {
                        r"\,", r"\;", r"\:", r"\!", r"\{", r"\}", r"\%", r"\_", r"\ ",
                    }:
                        raise ValueError(f"Unsupported inline Mermaid caption math command: {token}")
                elif token == "{":
                    depth += 1
                elif token == "}":
                    depth -= 1
                elif token in "%&#$" or ord(token) < 32:
                    raise ValueError("Unsafe token in inline Mermaid caption math")
                if depth < 0:
                    raise ValueError("Unbalanced inline Mermaid caption math")
            if depth != 0 or text.endswith("\\"):
                raise ValueError("Unbalanced inline Mermaid caption math")
        elif kind == "Link":
            target = node["c"][2][0]
            if (not (target.startswith("#") or urlsplit(target).scheme in {"http", "https", "mailto"})
                    or "\\" in target or any(ord(char) < 32 for char in target)):
                raise ValueError("Inline Mermaid caption links require a fragment, HTTP(S) or mailto target")
            _validate_caption_node(node["c"][1])
        elif kind in {
            "Para", "Plain", "Str", "Space", "SoftBreak", "LineBreak", "Emph", "Strong",
            "Superscript", "Subscript", "SmallCaps", "Quoted", "Code",
            "SingleQuote", "DoubleQuote",
        }:
            _validate_caption_node(node.get("c"))
        else:
            raise ValueError(f"Unsupported inline Mermaid caption element: {kind}")


def _inline_captions_latex(captions: list[str]) -> list[str]:
    """Use two Pandoc processes per book, preserving reviewed inline semantics.

    Authored captions are constrained Markdown, not an arbitrary-TeX interface.
    Alt metadata never enters this conversion. Disable reader macro expansion
    before inspecting the AST, then admit only bounded natbib and math TeX.
    """
    if not captions:
        return []
    parsed = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars+raw_tex-latex_macros", "--to=json"],
        input="\n\n".join(captions), capture_output=True, text=True, check=True,
    )
    document = json.loads(parsed.stdout)
    blocks = document["blocks"]
    if len(blocks) != len(captions) or any(block["t"] != "Para" for block in blocks):
        raise ValueError("Each inline Mermaid caption must be one Markdown paragraph")
    for block in blocks:
        _validate_caption_node(block)
    # Only complete owned comment lines delimit output; authored percent signs escape.
    marker = "% BIOLOGY-INLINE-CAPTION-END"
    document["blocks"] = [
        item for block in blocks
        for item in (block, {"t": "RawBlock", "c": ["latex", marker]})
    ]
    converted = subprocess.run(
        ["pandoc", "--from=json", "--to=latex", "--wrap=none", "--syntax-highlighting=none"],
        input=json.dumps(document), capture_output=True, text=True, check=True,
    )
    chunks = re.split(r"(?m)^" + re.escape(marker) + r"\r?$", converted.stdout)
    if len(chunks) != len(captions) + 1 or chunks[-1].strip():
        raise RuntimeError("Pandoc changed its inline caption batch emission contract")
    return [chunk.strip() for chunk in chunks[:-1]]


def _prepare_inline_diagrams(sources: list[Path], assets: list[Path]) -> None:
    """Bind rich authored captions and safe alt text to source-audited, print-fit PNGs."""
    from infrastructure.rendering._pdf_mermaid import _MERMAID_BLOCK_RE  # type: ignore[import-not-found]
    from infrastructure.rendering._pdf_title_page_latex import (  # type: ignore[import-not-found]
        _latex_graphic_alt_text,
    )
    from PIL import Image

    contents = [(path, path.read_text(encoding="utf-8")) for path in sources]
    captions = _inline_captions_latex([
        (match.group("caption_text") or "").strip()
        for _, content in contents for match in _MERMAID_BLOCK_RE.finditer(content)
    ])

    index = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal index
        source = normalise_inline_mermaid_source(match.group("source").strip())
        expected = inline_stem(index + 1, source)
        if index >= len(assets) or assets[index].stem != expected:
            raise RuntimeError(f"Hydrated Mermaid source does not match rendered asset {expected}")
        path = assets[index]
        index += 1
        caption = captions[index - 1]
        alts = re.findall(r"<!--\s*alt:\s*(.*?)\s*-->", match.group("alts") or "", re.DOTALL)
        if len(alts) != 1 or not alts[0].strip():
            raise ValueError("Inline Mermaid figures require exactly one nonempty plain-text alt")
        alt = _latex_graphic_alt_text(alts[0])
        left, top, right, bottom = _inline_diagram_bounds(path)
        with Image.open(path) as image:
            dpi_x, dpi_y = image.info.get("dpi", (72.0, 72.0))
            if dpi_x <= 0 or dpi_y <= 0:
                raise ValueError(f"Inline Mermaid PNG has an invalid resolution: {path}")
            trim = (left * 72 / dpi_x, (image.height - bottom) * 72 / dpi_y,
                    (image.width - right) * 72 / dpi_x, top * 72 / dpi_y)
        # Print at 144 raster pixels per inch or denser; never enlarge a tiny graph
        # to fill a page. The original square PNG and its audited hash stay intact.
        width, height = (right - left) / 2, (bottom - top) / 2
        options = (
            "trim={" + " ".join(f"{value:.6f}bp" for value in trim) + "},clip,"
            rf"width={{\ifdim {width:.6f}bp<0.96\linewidth {width:.6f}bp\else0.96\linewidth\fi}},"
            rf"height={{\ifdim {height:.6f}bp<8.5in {height:.6f}bp\else8.5in\fi}},keepaspectratio,"
        )
        return (
            "\n\\begin{figure}[htbp]\n\\centering\n"
            + r"\includegraphics[" + options + f"alt={{{alt}}}]"
            + f"{{../figures/mermaid_inline/{path.name}}}\n"
            + f"\\caption{{{caption}}}\n\\end{{figure}}\n"
        )

    for path, content in contents:
        replaced = _MERMAID_BLOCK_RE.sub(replace, content)
        if replaced != content:
            write_text_atomic(path, replaced)
    if index != len(assets):
        raise RuntimeError("Rendered Mermaid assets do not match the hydrated manuscript")


def render_textbook() -> Path:
    """Hydrate live sources and publish a successful render from a fresh workspace.

    The read-only template writes into an independent sibling of output/pdf, so
    existing compiler/temp-file aliases cannot become source writes. Keep failed
    workspaces and the previous final PDF; publish the new final PDF last.
    """
    output = require_project_output_directory(PROJECT_ROOT, PROJECT_ROOT / "output")
    require_project_output_directory(PROJECT_ROOT, OUTPUT_DIR)
    figures = require_project_output_directory(PROJECT_ROOT, output / "figures")
    require_project_output_directory(PROJECT_ROOT, figures / "mermaid_inline")
    pdf_dir = require_project_output_directory(PROJECT_ROOT, output / "pdf")
    template = discover_template_root(PROJECT_ROOT)
    if template is None:
        raise RuntimeError("Set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT to an installed template checkout")
    if shutil.which("mmdc") is None:
        raise RuntimeError("Mermaid CLI 'mmdc' is required for textbook PDF rendering")

    from infrastructure.rendering.config import RenderingConfig  # type: ignore[import-not-found]
    from infrastructure.rendering.pdf_renderer import PDFRenderer  # type: ignore[import-not-found]
    from PIL import Image

    config = load_config()
    chapters = collect_ordered_chapters(config)
    export = config.get("export", {})
    include_solutions = export.get("include_solutions", False) or os.environ.get("BIOLOGY_INCLUDE_SOLUTIONS") == "1"
    inject_chapters_for_rendering(
        chapters,
        include_solutions=include_solutions,
        watermark_instructor=export.get("watermark_instructor", False),
    )
    sources = sorted(path for path in OUTPUT_DIR.glob("*.md") if path.name != "preamble.md")
    inline_pngs = render_inline_mermaid_assets(figures)
    _prepare_inline_diagrams(sources, inline_pngs)
    stage = Path(tempfile.mkdtemp(prefix=".pdf-stage-", dir=output))
    try:
        renderer = PDFRenderer(RenderingConfig(
            manuscript_dir=str(OUTPUT_DIR),
            figures_dir=str(figures),
            output_dir=str(output),
            pdf_dir=str(stage),
            template_dir=str(template / "infrastructure" / "rendering" / "templates"),
        ))
        pdf = renderer.render_combined(sources, OUTPUT_DIR, project_name="biology_textbook")
        # A sibling workspace preserves the existing ../figures references.
        for path in inline_pngs:
            with Image.open(path) as image:
                if image.format != "PNG":
                    raise RuntimeError(f"Not a PNG diagram: {path}")
                image.verify()
        files = sorted(stage.iterdir(), key=lambda path: (path == pdf, path.name))
        if pdf not in files:
            raise RuntimeError("The backend did not produce its PDF in the owned workspace")
        # Admit every actual native output, not a guessed list of compiler sidecars.
        # Unknown existing destination entries are deliberately left untouched.
        for path in files:
            require_independent_file_target(path)
            require_independent_file_target(pdf_dir / path.name)
        pdf_dir.mkdir(parents=True, exist_ok=True)
        for path in files:
            path.replace(pdf_dir / path.name)
        stage.rmdir()
        return pdf_dir / pdf.name
    except BaseException as error:
        error.add_note(f"Native render workspace retained for inspection: {stage}")
        raise
