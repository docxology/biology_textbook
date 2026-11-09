"""Real-filesystem counterexamples for generated output and source custody."""

from __future__ import annotations

import runpy
import shutil
import sys
from pathlib import Path

import pytest

from biology.crossref.table_captions import (
    collect_existing_tbl_ids,
    in_scope_files,
    polish_manuscript_captions,
)
from biology.maintenance import glossary_links, manuscript_walker
from biology.pipeline import collection, injection, rendering
from biology.quality.audits.advisories import audit_absolute_language
from biology.quality.models import Finding


@pytest.fixture
def book(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path, Path]:
    project = tmp_path / "project"
    manuscript = project / "docs" / "manuscript"
    manuscript.mkdir(parents=True)
    chapter = manuscript / "chapter.md"
    chapter.write_text("# Authored chapter\n\nAlways use this stipulated rule.\n", encoding="utf-8")
    (manuscript / "unselected.txt").write_bytes(b"authored unselected sentinel\x00")
    (manuscript / "config.yaml").write_text(
        "front_matter:\n  include_front_matter: true\n  files:\n    - file: chapter.md\nunits: []\n",
        encoding="utf-8",
    )
    output = project / "output" / "manuscript"
    for module in (collection, injection, rendering):
        monkeypatch.setattr(module, "PROJECT_ROOT", project)
    for module in (collection, injection):
        monkeypatch.setattr(module, "MANUSCRIPT_DIR", manuscript)
    monkeypatch.setattr(collection, "CONFIG_FILE", manuscript / "config.yaml")
    for module in (injection, rendering):
        monkeypatch.setattr(module, "OUTPUT_DIR", output)
    monkeypatch.setattr(manuscript_walker, "PROJECT", project)
    monkeypatch.setattr(manuscript_walker, "MANUSCRIPT", manuscript)
    monkeypatch.setattr(glossary_links, "PROJECT", project)
    monkeypatch.setattr(glossary_links, "GLOSSARY", manuscript / "glossary.md")
    monkeypatch.setattr(glossary_links, "INDEX", manuscript / "appendices" / "appendix_index.md")
    return project, manuscript, output


def _snapshot(root: Path) -> dict[str, bytes]:
    return {path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*") if path.is_file() and not path.is_symlink()}


@pytest.mark.parametrize("target_kind", ["docs", "external"])
def test_output_ancestor_alias_cannot_replace_authored_or_external_tree(
    book: tuple[Path, Path, Path], tmp_path: Path, target_kind: str,
) -> None:
    project, manuscript, output = book
    chapters = collection.collect_ordered_chapters(collection.load_config())
    target = project / "docs" if target_kind == "docs" else tmp_path / "external"
    if target_kind == "external":
        (target / "manuscript").mkdir(parents=True)
        (target / "manuscript" / "old.md").write_bytes(b"external old injection")
        (target / "slides").mkdir()
        (target / "slides" / "old.pdf").write_bytes(b"external slide")
    else:
        (target / "slides").mkdir()
        (target / "slides" / "old.pdf").write_bytes(b"authored slide sentinel")
    source_before, target_before = _snapshot(manuscript), _snapshot(target)
    output.parent.symlink_to(target, target_is_directory=True)
    with pytest.raises(ValueError, match="aliased"):
        injection.inject_chapters_for_rendering(chapters)
    with pytest.raises(ValueError, match="aliased"):
        injection.clear_stale_slide_artifacts()
    with pytest.raises(ValueError, match="aliased"):
        rendering.render_textbook()
    assert _snapshot(manuscript) == source_before
    assert _snapshot(target) == target_before
    assert not list(target.glob(".manuscript-stage-*"))


@pytest.mark.parametrize("name", ["manuscript", "slides", "figures", "figures/mermaid_inline", "pdf"])
def test_final_artifact_directory_alias_is_rejected_before_render_preflight(
    book: tuple[Path, Path, Path], tmp_path: Path, name: str,
) -> None:
    _project, manuscript, output = book
    target = tmp_path / "private"
    target.mkdir()
    (target / "sentinel").write_bytes(b"must survive")
    output.parent.mkdir()
    alias = output.parent / name
    alias.parent.mkdir(parents=True, exist_ok=True)
    alias.symlink_to(target, target_is_directory=True)
    if name != "manuscript":
        output.mkdir()
        (output / "old.md").write_bytes(b"previous complete injection")
    before = _snapshot(manuscript)
    if name == "slides":
        with pytest.raises(ValueError, match="aliased"):
            injection.clear_stale_slide_artifacts()
    else:
        with pytest.raises(ValueError, match="aliased"):
            rendering.render_textbook()
    assert _snapshot(manuscript) == before
    assert _snapshot(target) == {"sentinel": b"must survive"}
    if name != "manuscript":
        assert _snapshot(output) == {"old.md": b"previous complete injection"}


def test_non_directory_output_ancestor_is_not_replaced(book: tuple[Path, Path, Path]) -> None:
    _project, manuscript, output = book
    output.parent.write_bytes(b"not a directory")
    before = _snapshot(manuscript)
    with pytest.raises(ValueError, match="non-directory"):
        injection.inject_chapters_for_rendering([manuscript / "chapter.md"])
    assert output.parent.read_bytes() == b"not a directory"
    assert _snapshot(manuscript) == before


@pytest.mark.parametrize("name", ["config.yaml", "references.bib", "preamble.md",
                                  "assets/cover/private.bin", "assets/cover/nested/private.bin"])
def test_external_auxiliary_refuses_before_chapter_reads_or_staging(
    book: tuple[Path, Path, Path], tmp_path: Path, name: str,
) -> None:
    _, manuscript, output = book
    output.mkdir(parents=True)
    (output / "old.md").write_bytes(b"previous complete injection")
    chapter = manuscript / "chapter.md"
    # An attempted chapter read would raise UnicodeDecodeError, not admission's ValueError.
    chapter.write_bytes(b"\xff")
    external = tmp_path / "private.bin"
    external.write_bytes(b"private source bytes\xff")
    alias = manuscript / name
    alias.parent.mkdir(parents=True, exist_ok=True)
    if alias.exists():
        alias.unlink()
    alias.symlink_to(external)
    before = _snapshot(output)
    with pytest.raises(ValueError, match="escapes manuscript"):
        injection.inject_chapters_for_rendering([chapter])
    assert _snapshot(output) == before
    assert chapter.read_bytes() == b"\xff"
    assert external.read_bytes() == b"private source bytes\xff"
    assert (manuscript / "unselected.txt").read_bytes() == b"authored unselected sentinel\x00"
    assert not list(output.parent.glob(".manuscript-stage-*"))


@pytest.mark.parametrize("name", ["assets", "assets/cover", "assets/cover/nested"])
def test_external_cover_directory_alias_is_rejected_recursively(
    book: tuple[Path, Path, Path], tmp_path: Path, name: str,
) -> None:
    _, manuscript, output = book
    output.mkdir(parents=True)
    (output / "old.md").write_bytes(b"previous output")
    external = tmp_path / "private"
    external.mkdir()
    (external / "private.bin").write_bytes(b"private cover bytes")
    alias = manuscript / name
    alias.parent.mkdir(parents=True, exist_ok=True)
    alias.symlink_to(external, target_is_directory=True)
    with pytest.raises(ValueError, match="escapes manuscript"):
        injection.inject_chapters_for_rendering([manuscript / "chapter.md"])
    assert _snapshot(output) == {"old.md": b"previous output"}
    assert _snapshot(external) == {"private.bin": b"private cover bytes"}
    assert not list(output.parent.glob(".manuscript-stage-*"))


def test_external_config_refuses_before_yaml_decode(
    book: tuple[Path, Path, Path], tmp_path: Path,
) -> None:
    _, manuscript, output = book
    external = tmp_path / "private.yaml"
    external.write_bytes(b"\xffnot yaml")
    config = manuscript / "config.yaml"
    config.unlink()
    config.symlink_to(external)
    for load in (collection.load_config, manuscript_walker.load_manuscript_config):
        with pytest.raises(ValueError, match="escapes manuscript"):
            load()
    assert external.read_bytes() == b"\xffnot yaml"
    assert not output.parent.exists()


@pytest.mark.parametrize("alias_kind", ["file", "directory"])
def test_selected_source_alias_cannot_leave_manuscript(
    book: tuple[Path, Path, Path], alias_kind: str,
) -> None:
    project, manuscript, _ = book
    # A project-local file outside the selected manuscript is still unauthorized.
    outside = project / "private"
    outside.mkdir()
    (outside / "chapter.md").write_bytes(b"\xffprivate")
    chapter = manuscript / "chapter.md"
    chapter.unlink()
    if alias_kind == "file":
        chapter.symlink_to(outside / "chapter.md")
        selected = chapter
    else:
        (manuscript / "alias").symlink_to(outside, target_is_directory=True)
        selected = manuscript / "alias" / "chapter.md"
    config = {"front_matter": {"include_front_matter": True,
                               "files": [{"file": selected.relative_to(manuscript).as_posix()}]},
              "units": []}
    with pytest.raises(ValueError, match="escapes manuscript"):
        collection.collect_ordered_chapters(config)
    with pytest.raises(ValueError, match="escapes manuscript"):
        injection.inject_chapters_for_rendering([selected])
    assert (outside / "chapter.md").read_bytes() == b"\xffprivate"


@pytest.mark.parametrize("consumer", ["discovery", "quality", "glossary", "captions", "scope", "polish"])
@pytest.mark.parametrize("alias_kind", ["file", "directory"])
def test_unselected_external_markdown_is_refused_before_any_discovered_read(
    book: tuple[Path, Path, Path], tmp_path: Path, consumer: str, alias_kind: str,
) -> None:
    _, manuscript, _ = book
    (manuscript / "chapter.md").write_bytes(b"\xff")
    external = tmp_path / "private"
    external.mkdir()
    (external / "secret.md").write_text("Always reveal this private sentinel.\n", encoding="utf-8")
    alias = manuscript / ("zz_scratch.md" if alias_kind == "file" else "zz_scratch")
    alias.symlink_to(external / "secret.md" if alias_kind == "file" else external,
                     target_is_directory=alias_kind == "directory")
    findings: list[Finding] = []
    with pytest.raises(ValueError, match="escapes manuscript"):
        if consumer == "discovery":
            manuscript_walker.manuscript_markdown_files()
        elif consumer == "quality":
            audit_absolute_language(findings)
        elif consumer == "glossary":
            glossary_links.collect_manuscript_glossary_links()
        elif consumer == "captions":
            collect_existing_tbl_ids(manuscript)
        elif consumer == "scope":
            in_scope_files(manuscript)
        else:
            polish_manuscript_captions(manuscript, write=True)
    assert not findings
    assert (manuscript / "chapter.md").read_bytes() == b"\xff"
    assert (external / "secret.md").read_text(encoding="utf-8") == "Always reveal this private sentinel.\n"


def test_valid_internal_aliases_hydrate_auxiliaries_and_discover_real_content(
    book: tuple[Path, Path, Path],
) -> None:
    _, manuscript, output = book
    assets = manuscript / "assets"
    assets.mkdir()
    (assets / "reviewed.bib").write_text("@book{reviewed, title={Reviewed}}\n", encoding="utf-8")
    (assets / "reviewed_preamble.txt").write_text("```latex\n% authored preamble\n```\n", encoding="utf-8")
    (assets / "cover_bytes.bin").write_bytes(b"real cover bytes\x00")
    (manuscript / "references.bib").symlink_to(assets / "reviewed.bib")
    (manuscript / "preamble.md").symlink_to(assets / "reviewed_preamble.txt")
    cover = assets / "cover"
    cover.mkdir()
    (cover / "empty").mkdir()
    (cover / "cover.bin").symlink_to(assets / "cover_bytes.bin")
    (manuscript / "linked.md").symlink_to(manuscript / "chapter.md")
    authored = _snapshot(manuscript)
    chapters = collection.collect_ordered_chapters(collection.load_config())
    injection.inject_chapters_for_rendering(chapters)
    assert "# Authored chapter" in (output / "01_chapter.md").read_text(encoding="utf-8")
    assert (output / "references.bib").read_bytes() == (assets / "reviewed.bib").read_bytes()
    assert (output / "preamble.md").read_bytes() == (assets / "reviewed_preamble.txt").read_bytes()
    assert (output / "assets/cover/cover.bin").read_bytes() == b"real cover bytes\x00"
    assert (output / "assets/cover/empty").is_dir()
    assert not (output / "assets/cover/cover.bin").is_symlink()
    assert manuscript / "linked.md" in manuscript_walker.manuscript_markdown_files()
    findings: list[Finding] = []
    audit_absolute_language(findings)
    assert any(finding.path == manuscript / "chapter.md" for finding in findings)
    assert _snapshot(manuscript) == authored


@pytest.mark.parametrize("name", ["glossary.md", "appendices/appendix_index.md"])
def test_glossary_regeneration_rejects_external_targets_before_loading_sources(
    book: tuple[Path, Path, Path], tmp_path: Path, name: str,
) -> None:
    _, manuscript, output = book
    external = tmp_path / "private.md"
    external.write_bytes(b"\xffprivate glossary bytes")
    alias = manuscript / name
    alias.parent.mkdir(parents=True, exist_ok=True)
    alias.symlink_to(external)
    before = _snapshot(manuscript)
    with pytest.raises(ValueError, match="escapes manuscript"):
        glossary_links.run_glossary_sync()
    assert external.read_bytes() == b"\xffprivate glossary bytes"
    assert _snapshot(manuscript) == before
    assert not output.parent.exists()


def test_configured_quality_surfaces_admit_paths_before_consumers_open_them(
    book: tuple[Path, Path, Path], tmp_path: Path,
) -> None:
    _, manuscript, _ = book
    external = tmp_path / "private.md"
    external.write_bytes(b"\xffprivate surface bytes")
    (manuscript / "chapter.md").unlink()
    (manuscript / "chapter.md").symlink_to(external)
    with pytest.raises(ValueError, match="escapes manuscript"):
        manuscript_walker.configured_manuscript_surfaces()
    assert external.read_bytes() == b"\xffprivate surface bytes"


@pytest.mark.parametrize("script,relative", [
    ("generate_figures.py", "figures"),
    ("generate_diagrams.py", "figures/mermaid"),
])
def test_default_visual_cli_cannot_write_through_an_output_directory_alias(
    book: tuple[Path, Path, Path], monkeypatch: pytest.MonkeyPatch, script: str, relative: str,
) -> None:
    project, manuscript, output = book
    output.parent.mkdir()
    alias = output.parent / relative
    alias.parent.mkdir(parents=True, exist_ok=True)
    alias.symlink_to(manuscript, target_is_directory=True)
    before = _snapshot(manuscript)
    entrypoint = Path(__file__).resolve().parents[1] / "scripts" / script
    main = runpy.run_path(str(entrypoint))["main"]
    monkeypatch.setitem(main.__globals__, "PROJECT_DIR", project)
    if "CONFIG_FILE" in main.__globals__:
        monkeypatch.setitem(main.__globals__, "CONFIG_FILE", manuscript / "config.yaml")
    monkeypatch.setattr(sys, "argv", [script])
    with pytest.raises(ValueError):
        main()
    assert _snapshot(manuscript) == before
    assert alias.is_symlink()


@pytest.fixture
def native_book(
    book: tuple[Path, Path, Path], monkeypatch: pytest.MonkeyPatch,
) -> tuple[Path, Path, Path]:
    from textbook_paths import PROJECT, discover_template_root

    if discover_template_root(PROJECT) is None or any(
        shutil.which(tool) is None for tool in ("mmdc", "pandoc", "xelatex", "bibtex")
    ):
        pytest.skip("explicit template and native PDF toolchain are unavailable")
    project, manuscript, output = book
    config = manuscript / "config.yaml"
    config.write_text(
        config.read_text(encoding="utf-8")
        + "book:\n  title: Owned native custody fixture\n  author: Synthetic fixture\n  edition: '1.1'\n",
        encoding="utf-8",
    )
    (manuscript / "preamble.md").write_text("```latex\n\\usepackage{array}\n```\n", encoding="utf-8")
    monkeypatch.setattr("biology.pipeline.numbering.MANUSCRIPT_DIR", manuscript)
    monkeypatch.setattr("biology.visual_contracts.render.PROJECT_ROOT", project)
    return project, manuscript, output


def test_native_compiler_failure_preserves_previous_pdf_and_retains_diagnostics(
    native_book: tuple[Path, Path, Path],
) -> None:
    from importlib import import_module

    rendering_error = import_module("infrastructure.core.exceptions").RenderingError

    project, manuscript, output = native_book
    (manuscript / "chapter.md").write_text(
        "# Authored chapter\n\n\\NativeOwnedFixtureFailure\n", encoding="utf-8",
    )
    pdf_dir = output.parent / "pdf"
    pdf_dir.mkdir(parents=True)
    previous = pdf_dir / "biology_textbook_combined.pdf"
    previous.write_bytes(b"previous validated PDF bytes\n")
    unknown = pdf_dir / "author-note.txt"
    unknown.write_bytes(b"unrelated output note\n")
    with pytest.raises(rendering_error):
        rendering.render_textbook()
    assert previous.read_bytes() == b"previous validated PDF bytes\n"
    assert unknown.read_bytes() == b"unrelated output note\n"
    stages = list((project / "output").glob(".pdf-stage-*"))
    assert len(stages) == 1
    assert (stages[0] / "_combined_manuscript.tex").is_file()


def test_native_sidecar_alias_refuses_publication_without_damaging_source_or_prior_pdf(
    native_book: tuple[Path, Path, Path],
) -> None:
    project, manuscript, output = native_book
    sentinel = manuscript / "author-note.txt"
    sentinel.write_bytes(b"authored source must survive native output\n")
    pdf_dir = output.parent / "pdf"
    pdf_dir.mkdir(parents=True)
    alias = pdf_dir / "_latex_stdout.log"
    alias.hardlink_to(sentinel)
    previous = pdf_dir / "biology_textbook_combined.pdf"
    previous.write_bytes(b"previous validated PDF bytes\n")
    unknown = pdf_dir / "author-note.txt"
    unknown.write_bytes(b"unrelated output note\n")
    with pytest.raises(ValueError):
        rendering.render_textbook()
    assert sentinel.read_bytes() == b"authored source must survive native output\n"
    assert alias.samefile(sentinel)
    assert previous.read_bytes() == b"previous validated PDF bytes\n"
    assert unknown.read_bytes() == b"unrelated output note\n"
    assert list((project / "output").glob(".pdf-stage-*"))


def test_native_final_pdf_publication_failure_retains_prior_pdf_after_sidecars_move(
    native_book: tuple[Path, Path, Path], monkeypatch: pytest.MonkeyPatch,
) -> None:
    project, _, output = native_book
    pdf_dir = output.parent / "pdf"
    pdf_dir.mkdir(parents=True)
    previous = pdf_dir / "biology_textbook_combined.pdf"
    previous.write_bytes(b"previous validated PDF bytes\n")
    sidecar = pdf_dir / "_combined_manuscript.tex"
    sidecar.write_bytes(b"previous TeX bytes\n")
    unknown = pdf_dir / "author-note.txt"
    unknown.write_bytes(b"unrelated output note\n")
    replace = Path.replace

    def fail_final_pdf(source: Path, target: str | Path) -> Path:
        if Path(target) == previous:
            raise OSError("owned final PDF publication failure")
        return replace(source, target)

    monkeypatch.setattr(Path, "replace", fail_final_pdf)
    with pytest.raises(OSError, match="owned final PDF publication failure"):
        rendering.render_textbook()
    assert previous.read_bytes() == b"previous validated PDF bytes\n"
    assert unknown.read_bytes() == b"unrelated output note\n"
    assert sidecar.read_bytes() != b"previous TeX bytes\n"
    stages = list((project / "output").glob(".pdf-stage-*"))
    assert len(stages) == 1
    with (stages[0] / previous.name).open("rb") as retained:
        assert retained.read(5) == b"%PDF-"
    assert not (stages[0] / sidecar.name).exists()
