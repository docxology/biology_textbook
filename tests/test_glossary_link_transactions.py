"""Glossary candidate validation precedes publication of every pending file."""

from pathlib import Path

import pytest
import yaml

from biology.maintenance import glossary_links


def _glossary_project(root: Path, monkeypatch: pytest.MonkeyPatch, *, link: str) -> tuple[Path, Path]:
    manuscript = root / "docs" / "manuscript"
    chapter = manuscript / "unit_I" / "atoms_molecules.md"
    glossary = manuscript / "glossary.md"
    index = manuscript / "appendices" / "appendix_index.md"
    chapter.parent.mkdir(parents=True)
    index.parent.mkdir(parents=True)
    chapter.write_text(f"# Chapter {{#sec:unit_I_atoms_molecules}}\n\nA [cell](#{link}) is a living unit.\n", encoding="utf-8")
    glossary.write_text("[**Cell**]{#gl:old} — A membrane-bounded structural and functional unit. → \\cref{sec:unit_I_atoms_molecules}\n", encoding="utf-8")
    index.write_text("Previously reviewed index, not yet rebuilt.\n", encoding="utf-8")
    config = {"units": [{"id": "unit_I", "directory": "unit_I", "chapters": [{"file": chapter.name, "title": "Atoms and Molecules"}]}]}
    (manuscript / "config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    # Inject real resource locations only; every parser and writer is exercised.
    monkeypatch.setattr(glossary_links, "PROJECT", root)
    monkeypatch.setattr(glossary_links, "GLOSSARY", glossary)
    monkeypatch.setattr(glossary_links, "INDEX", index)
    return glossary, index


def test_candidate_anchors_not_stale_disk_anchors_are_validated(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    glossary, index = _glossary_project(tmp_path, monkeypatch, link="gl:cell")
    code, stats = glossary_links.run_glossary_sync()
    assert code == 0 and not stats["failed"]
    assert "{#gl:cell}" in glossary.read_text(encoding="utf-8")
    assert "gl:cell" in index.read_text(encoding="utf-8")
    assert glossary_links.find_dangling_glossary_links() == {}


def test_normalization_cannot_publish_a_dangling_old_slug(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    glossary, index = _glossary_project(tmp_path, monkeypatch, link="gl:old")
    before = {path: path.read_bytes() for path in (glossary, index)}
    code, stats = glossary_links.run_glossary_sync()
    assert code == 1 and stats["failed"]
    assert {path: path.read_bytes() for path in before} == before
    links = glossary_links.collect_manuscript_glossary_links()
    assert links["gl:old"] == ["unit_I/atoms_molecules.md:3"]


def test_duplicate_candidate_slug_aborts_both_writes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    glossary, index = _glossary_project(tmp_path, monkeypatch, link="gl:cell")
    glossary.write_text("[**Cell (animal)**]{#gl:animal} — An animal cell.\n[**Cell (plant)**]{#gl:plant} — A plant cell.\n", encoding="utf-8")
    before = {path: path.read_bytes() for path in (glossary, index)}
    code, _ = glossary_links.run_glossary_sync()
    assert code == 1
    assert {path: path.read_bytes() for path in before} == before


def test_invalid_candidate_cref_aborts_both_writes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    glossary, index = _glossary_project(tmp_path, monkeypatch, link="gl:cell")
    glossary.write_text("[**Cell**]{#gl:old} — A living unit. → \\cref{sec:missing}\n", encoding="utf-8")
    before = {path: path.read_bytes() for path in (glossary, index)}
    assert glossary_links.run_glossary_sync()[0] == 1
    assert {path: path.read_bytes() for path in before} == before


@pytest.mark.parametrize("dry_run,check,exit_code", [(True, False, 0), (False, True, 1)])
def test_valid_pending_candidates_obey_nonwriting_modes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, dry_run: bool, check: bool, exit_code: int) -> None:
    glossary, index = _glossary_project(tmp_path, monkeypatch, link="gl:cell")
    before = {path: path.read_bytes() for path in (glossary, index)}
    code, stats = glossary_links.run_glossary_sync(dry_run=dry_run, check=check)
    assert code == exit_code and stats["pending_changes"]
    assert {path: path.read_bytes() for path in before} == before


@pytest.mark.parametrize("term", [
    "Cortisol", "GLP-1 (glucagon-like peptide-1)", "GLUT4",
    "HPA axis (hypothalamic–pituitary–adrenal axis)",
    "HPG axis (hypothalamic–pituitary–gonadal axis)",
    "HPT axis (hypothalamic–pituitary–thyroid axis)", "Insulin receptor",
])
def test_reviewed_endocrine_destinations_survive_glossary_and_index_generation(term: str) -> None:
    source = f"[**{term}**]{{#gl:old}} — A mechanistic endocrine entry. → \\cref{{sec:unit_IX_immune_system_defense}}\n"
    refs = {
        "endocrine": "sec:unit_IX_endocrine_signaling",
        "immune": "sec:unit_IX_immune_system_defense",
    }
    revised, _, _, failures = glossary_links.rewrite_glossary(source, refs)
    assert not failures
    entry = glossary_links.parse_glossary_index_entries(revised)[0]
    assert entry.backref == "→ \\cref{sec:unit_IX_endocrine_signaling}"
    index = glossary_links.build_appendix_index(revised)
    index_entries = [line for line in index.splitlines() if line.startswith(f"**{term}**")]
    assert len(index_entries) == 1 and entry.backref in index_entries[0]
    assert glossary_links.rewrite_glossary(revised, refs) == (revised, 0, 0, [])


def test_numeric_glossary_terms_have_nonempty_rendered_index_headings() -> None:
    from biology.crossref.source import iter_headings
    from biology.curriculum_sync.sync_blocks import _split_heading_parts

    source = "[**5-Methylcytosine**]{#gl:5-methylcytosine} — A modified base. → \\cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms}\n"
    index = glossary_links.build_appendix_index(source)
    assert all(_split_heading_parts(heading.title)[0] for heading in iter_headings(index))
    assert "**5-Methylcytosine** (`#gl:5-methylcytosine`)" in index
    assert r"\cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms}" in index
