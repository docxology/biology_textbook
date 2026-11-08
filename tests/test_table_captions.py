"""Tests for table caption annotation helpers."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.patterns import RE_PIPE_TABLE_ROW, RE_TBL_CAPTION
from biology.crossref.table_captions import (
    annotate_manuscript,
    apply_annotations,
    find_table_annotations,
    polish_manuscript_captions,
)


def test_collect_existing_tbl_ids_reads_latex_labels(tmp_path: Path) -> None:
    from biology.crossref.table_captions import collect_existing_tbl_ids

    md = tmp_path / "appendix.md"
    md.write_text(r"\label{tbl:demo_latex_label}", encoding="utf-8")
    assert "demo_latex_label" in collect_existing_tbl_ids(tmp_path)



def test_in_scope_files_includes_labs(tmp_path: Path) -> None:
    from biology.crossref.table_captions import in_scope_files

    manuscript = tmp_path / "manuscript"
    labs = manuscript / "labs" / "unit_I"
    labs.mkdir(parents=True)
    lab = labs / "lab_demo.md"
    lab.write_text("# Lab\n", encoding="utf-8")
    assert lab in in_scope_files(manuscript)


def test_polish_manuscript_captions_rewrites_weak_captions(tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript" / "unit_I"
    manuscript.mkdir(parents=True)
    target = manuscript / "demo.md"
    target.write_text(
        "### Demo\n\n"
        ": Worked example data for Demo table. {#tbl:unit_I_demo_demo}\n"
        "| A | B |\n| - | - |\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    changed, examined = polish_manuscript_captions(tmp_path / "manuscript", write=True)
    assert examined == 1
    assert changed == 1
    updated = target.read_text(encoding="utf-8")
    assert "Worked example: Demo table." in updated
    assert "Worked example data for" not in updated


def test_collect_existing_tbl_ids_and_in_scope_files(tmp_path: Path) -> None:
    from biology.crossref.table_captions import (
        annotate_manuscript,
        collect_existing_tbl_ids,
        in_scope_files,
    )

    manuscript = tmp_path / "manuscript"
    unit = manuscript / "unit_I"
    unit.mkdir(parents=True)
    chapter = unit / "demo.md"
    chapter.write_text(
        "# Demo\n\n"
        ": Existing {#tbl:unit_I_demo_existing}\n"
        "| A | B |\n| - | - |\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    ids = collect_existing_tbl_ids(manuscript)
    assert "unit_I_demo_existing" in ids
    assert chapter in in_scope_files(manuscript)
    results, changed = annotate_manuscript(manuscript, write=False)
    assert changed == 0
    assert not results


def test_annotate_manuscript_inserts_missing_captions(tmp_path: Path) -> None:
    from biology.crossref.table_captions import annotate_manuscript

    manuscript = tmp_path / "manuscript"
    unit = manuscript / "unit_I"
    unit.mkdir(parents=True)
    chapter = unit / "metrics.md"
    chapter.write_text(
        "### Growth rates\n\n"
        "| Time | Rate |\n| ---- | ---- |\n| 0 | 1 |\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    results, changed = annotate_manuscript(manuscript, write=True)
    assert changed == 1
    assert results and results[0].annotations
    updated = chapter.read_text(encoding="utf-8")
    assert ": Worked example: Growth rates." in updated
    assert "{#tbl:" in updated


def test_find_table_annotations_inserts_caption_before_pipe_table(tmp_path: Path) -> None:
    md = tmp_path / "unit_I" / "demo.md"
    md.parent.mkdir()
    md.write_text(
        "### Rate constants\n\n"
        "| Enzyme | Rate |\n| ------ | ---- |\n| A | 1 |\n| B | 2 |\n| C | 3 |\n",
        encoding="utf-8",
    )
    result = find_table_annotations(md, used_ids=set())
    assert len(result.annotations) == 1
    assert "Rate constants:" in result.annotations[0].caption_line
    assert "{#tbl:unit_I_demo_" in result.annotations[0].caption_line


def test_apply_annotations_is_idempotent(tmp_path: Path) -> None:
    md = tmp_path / "unit_I" / "demo.md"
    md.parent.mkdir()
    md.write_text(
        "### Demo\n\n| A | B |\n| - | - |\n| 1 | 2 |\n",
        encoding="utf-8",
    )
    first = find_table_annotations(md, used_ids=set())
    apply_annotations(md, first.annotations)
    second = find_table_annotations(md, used_ids={"unit_I_demo_demo"})
    assert not second.annotations


def test_blank_pipe_rows_are_not_separator_rows(tmp_path: Path) -> None:
    md = tmp_path / "unit_I" / "blank_rows.md"
    md.parent.mkdir()
    md.write_text(
        "### Blank worksheet rows\n\n"
        "| Taxon | Reads | p_i |\n| ----- | ----- | --- |\n| | | |\n| | | |\n",
        encoding="utf-8",
    )
    result = find_table_annotations(md, used_ids=set())
    assert len(result.annotations) == 1


def test_configured_manuscript_has_no_unlabeled_pipe_tables() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "docs" / "manuscript"
    results, changed = annotate_manuscript(manuscript, write=False)
    assert changed == 0
    assert not results


def test_configured_table_captions_are_not_inside_pipe_tables() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "docs" / "manuscript"
    offenders: list[str] = []
    for md in sorted(manuscript.rglob("*.md")):
        if md.name in {"README.md", "AGENTS.md"}:
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            if not RE_TBL_CAPTION.match(line.strip()):
                continue
            if idx > 0 and RE_PIPE_TABLE_ROW.match(lines[idx - 1]):
                offenders.append(f"{md.relative_to(manuscript)}:{idx + 1}")
    assert offenders == []



def test_configured_manuscript_table_captions_are_pdf_safe() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "docs" / "manuscript"
    offenders: list[str] = []
    for path in sorted(manuscript.rglob("*.md")):
        if path.name in {"README.md", "AGENTS.md"}:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = RE_TBL_CAPTION.match(line.strip())
            if match and "\\" in match.group("caption"):
                offenders.append(f"{path.relative_to(manuscript)}:{line_no}: {match.group('caption')}")

    assert not offenders


def test_annotation_preserves_unpublished_examples_and_numbers_rendered_solution(tmp_path: Path) -> None:
    path = tmp_path / "unit_I/demo.md"
    path.parent.mkdir()
    example = "| Example | Value |\n| --- | --- |\n| 1 | 2 |\n"
    protected = "~~~markdown\n" + example + "~~~\n\n<!-- ordinary comment\n" + example + "-->\n"
    rendered = "| Condition | Rate |\n| --- | --- |\n| A | 1 |\n| B | 2 |\n| C | 3 |\n"
    original = "# Demo\n\n### Old context\n\n" + protected + "\n<!-- SOLUTION\n## Recorded kinetics {.unnumbered}\n\n" + rendered + "SOLUTION -->\n"
    path.write_text(original)
    result = find_table_annotations(path, used_ids=set())
    assert [annotation.tbl_id for annotation in result.annotations] == ["unit_I_demo_recorded_kinetics"]
    apply_annotations(path, result.annotations)
    updated = path.read_text()
    assert protected in updated
    assert updated.index("{#tbl:unit_I_demo_recorded_kinetics}") > updated.index("<!-- SOLUTION")
    assert rendered in updated
