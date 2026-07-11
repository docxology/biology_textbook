"""PDF opening and inline Mermaid rendering invariants."""

from __future__ import annotations

from pathlib import Path

import pytest

_pdf_combined_renderer = pytest.importorskip("infrastructure.rendering._pdf_combined_renderer")
_pdf_latex_helpers = pytest.importorskip("infrastructure.rendering._pdf_latex_helpers")

preprocess_combined_markdown = _pdf_combined_renderer.preprocess_combined_markdown
generate_title_page_body = _pdf_latex_helpers.generate_title_page_body
generate_title_page_preamble = _pdf_latex_helpers.generate_title_page_preamble


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"


from biology.pipeline import injection as pipeline_injection


def test_book_metadata_drives_pdf_opening_title() -> None:
    preamble = generate_title_page_preamble(MANUSCRIPT)
    body = generate_title_page_body(MANUSCRIPT)

    # The subtitle renders on the title page body, not inside \title{} metadata
    # (infrastructure.rendering._pdf_title_page's documented contract — see
    # test_subtitle_not_embedded_in_title_command in the template repo).
    assert "Introduction to Biology" in preamble
    assert "Research Paper" not in preamble
    assert "Introduction to Biology" in body
    assert "A Generative Approach" in body
    assert "Publishing Information" in body
    assert "Research Paper" not in body


def test_pdf_opening_places_contents_after_cover_and_publishing_page() -> None:
    body = generate_title_page_body(MANUSCRIPT)
    titlepage_end = body.index(r"\end{titlepage}")
    publishing_info = body.index("Publishing Information")
    contents = body.index(r"\tableofcontents")

    assert titlepage_end < publishing_info < contents
    assert body.count(r"\clearpage") >= 3
    assert r"\includegraphics" in body
    assert "biology_textbook_cover.png" in body
    assert r"\addcontentsline{toc}{section}{Publishing Information}" not in body


def test_pdf_publishing_page_includes_configured_quote_and_acknowledgements() -> None:
    body = generate_title_page_body(MANUSCRIPT)

    assert "The tree which moves some to tears of joy" in body
    assert "William Blake" in body
    assert r"\fcolorbox{red!55!black}{red!3}" in body
    assert "This open textbook is built from a living chain" in body
    assert r"\fcolorbox{black!35}{black!2}" in body


def test_configured_cover_asset_exists() -> None:
    cover = MANUSCRIPT / "assets" / "cover" / "biology_textbook_cover.png"
    assert cover.is_file()
    assert cover.stat().st_size > 50_000


def test_analysis_injection_copies_live_config_for_cover_metadata(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "manuscript"
    output = tmp_path / "output" / "manuscript"
    cover_dir = source / "assets" / "cover"
    cover_dir.mkdir(parents=True)
    chapter = source / "chapter.md"
    chapter.write_text("# Chapter\n\nBody.\n", encoding="utf-8")
    (cover_dir / "test_cover.png").write_bytes(b"cover image")
    (source / "config.yaml").write_text(
        "book:\n"
        "  title: Test Book\n"
        "  cover:\n"
        "    image: assets/cover/test_cover.png\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(pipeline_injection, "MANUSCRIPT_DIR", source)
    monkeypatch.setattr(pipeline_injection, "OUTPUT_DIR", output)

    pipeline_injection.inject_chapters_for_rendering([chapter])

    assert (output / "config.yaml").read_text(encoding="utf-8") == (source / "config.yaml").read_text(
        encoding="utf-8"
    )
    assert (output / "assets" / "cover" / "test_cover.png").read_bytes() == b"cover image"


def test_inline_mermaid_is_rendered_to_png_reference(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A rendered Mermaid block becomes an image reference, not stripped text."""
    manuscript_dir = tmp_path / "manuscript"
    manuscript_dir.mkdir()
    (tmp_path / ".puppeteer.json").write_text("{}", encoding="utf-8")

    def fake_run(cmd: list[str], **_kwargs: object):
        output = Path(cmd[cmd.index("--output") + 1])
        output.write_bytes(b"png")

        class Result:
            returncode = 0
            stdout = ""
            stderr = ""

        return Result()

    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/mmdc" if name == "mmdc" else None)
    monkeypatch.setattr("subprocess.run", fake_run)

    content = """Before
```mermaid
graph TD
    A[One\\nTwo] --> B
```
<!-- alt: A small test Mermaid graph -->
*A concise visible Mermaid caption.*
After
"""
    result = preprocess_combined_markdown(content, manuscript_dir=manuscript_dir)
    rendered_source = next((tmp_path / "output" / "figures" / "mermaid_inline").glob("*.mmd")).read_text(
        encoding="utf-8"
    )

    assert result.mermaid_blocks_processed == 1
    assert "```mermaid" not in result.content
    assert "../figures/mermaid_inline/inline_mermaid_0001_" in result.content
    assert "\\includegraphics[width=0.82\\linewidth,height=4.2in,keepaspectratio]" in result.content
    assert "\\caption{A concise visible Mermaid caption.}" in result.content
    assert "*A concise visible Mermaid caption.*" not in result.content
    assert (tmp_path / "output" / "figures" / "mermaid_inline").is_dir()
    assert "One<br/>Two" in rendered_source


def _enable_inline_mermaid_render(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Provide puppeteer config + mmdc so inline Mermaid renders to PNG in tests."""
    (tmp_path / ".puppeteer.json").write_text("{}", encoding="utf-8")

    def fake_run(cmd: list[str], **_kwargs: object):
        output = Path(cmd[cmd.index("--output") + 1])
        output.write_bytes(b"png")

        class Result:
            returncode = 0
            stdout = ""
            stderr = ""

        return Result()

    monkeypatch.setattr("shutil.which", lambda name: "/usr/bin/mmdc" if name == "mmdc" else None)
    monkeypatch.setattr("subprocess.run", fake_run)


def test_inline_mermaid_output_directory_is_cleaned_before_render(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Stale inline Mermaid artifacts should not remain in copied outputs."""
    manuscript_dir = tmp_path / "manuscript"
    stale_dir = tmp_path / "output" / "figures" / "mermaid_inline"
    stale_dir.mkdir(parents=True)
    (stale_dir / "inline_mermaid_9999_stale.png").write_bytes(b"old")
    (stale_dir / "inline_mermaid_9999_stale.mmd").write_text("graph TD\nOLD-->OLD\n", encoding="utf-8")
    manuscript_dir.mkdir()
    _enable_inline_mermaid_render(tmp_path, monkeypatch)

    preprocess_combined_markdown("```mermaid\ngraph TD\nA-->B\n```", manuscript_dir=manuscript_dir)

    assert not (stale_dir / "inline_mermaid_9999_stale.png").exists()
    assert not (stale_dir / "inline_mermaid_9999_stale.mmd").exists()
    assert len(list(stale_dir.glob("inline_mermaid_*.png"))) == 1


def test_inline_sequence_mermaid_sanitizes_label_semicolons(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    manuscript_dir = tmp_path / "manuscript"
    manuscript_dir.mkdir()
    _enable_inline_mermaid_render(tmp_path, monkeypatch)

    content = """```mermaid
sequenceDiagram
    A->>B: first clause; second clause
```
"""
    preprocess_combined_markdown(content, manuscript_dir=manuscript_dir)
    rendered_source = next((tmp_path / "output" / "figures" / "mermaid_inline").glob("*.mmd")).read_text(
        encoding="utf-8"
    )

    assert "first clause, second clause" in rendered_source


def test_inline_state_mermaid_preserves_state_syntax(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    manuscript_dir = tmp_path / "manuscript"
    manuscript_dir.mkdir()
    _enable_inline_mermaid_render(tmp_path, monkeypatch)

    content = """```mermaid
stateDiagram-v2
    A: Alpha
    B: Beta: secondary detail
    A --> B: Step 1: Citrate synthase; next clause<br/>next line
    Note right of B: INPUT:<br/>ATP
```
"""
    preprocess_combined_markdown(content, manuscript_dir=manuscript_dir)
    rendered_source = next((tmp_path / "output" / "figures" / "mermaid_inline").glob("*.mmd")).read_text(
        encoding="utf-8"
    )

    assert "A --> B: Step 1 - Citrate synthase, next clause\\nnext line" in rendered_source
    assert "B: Beta - secondary detail" in rendered_source
    assert "Note right of B: INPUT -\\nATP" in rendered_source


def test_inline_mermaid_requires_renderer_when_pdf_rendering(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Without Chrome or mmdc, inline Mermaid falls back to a verbatim figure block."""
    manuscript_dir = tmp_path / "manuscript"
    manuscript_dir.mkdir()
    monkeypatch.setattr("shutil.which", lambda _name: None)
    pdf_mermaid = pytest.importorskip("infrastructure.rendering._pdf_mermaid")
    monkeypatch.setattr(pdf_mermaid, "_resolve_chrome_executable", lambda: None)

    result = preprocess_combined_markdown("```mermaid\ngraph TD\nA-->B\n```", manuscript_dir=manuscript_dir)

    assert result.mermaid_blocks_processed == 0
    assert "\\begin{verbatim}" in result.content
    assert "graph TD" in result.content
