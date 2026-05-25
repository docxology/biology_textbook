"""Tests for table caption annotation helpers."""

from __future__ import annotations

from pathlib import Path

from biology.crossref.table_captions import (
    CaptionPolicy,
    annotate_manuscript,
    apply_annotations,
    build_caption_text,
    find_table_annotations,
    polish_caption_text,
    polish_manuscript_captions,
)
from biology.crossref.patterns import RE_PIPE_TABLE_ROW, RE_TBL_CAPTION


def test_build_caption_text_uses_heading_and_headers() -> None:
    caption = build_caption_text("Michaelis-Menten parameters", ["Enzyme", "k_cat"], data_rows=5)
    assert caption == "Michaelis-Menten parameters: Enzyme and k_cat."


def test_build_caption_text_marks_small_tables_as_worked_examples() -> None:
    caption = build_caption_text("Lineweaver-Burk plot", ["[S] (mM)", "v0"], data_rows=2)
    assert caption == "Worked example: Lineweaver-Burk plot."


def test_polish_caption_text_strips_citep_and_redundancy() -> None:
    raw = "Worked example data for Source-Sink Dynamics \\citep{pulliam1988}."
    assert polish_caption_text(raw, tbl_id="unit_X_population_ecology_source_sink_dynamics_citep_pulliam1988") == (
        "Source and sink patch roles in metapopulation dynamics."
    )
    assert polish_caption_text("Worked example data for Worked Example: Kimura's Neutral Fixation Probability.") == (
        "Worked example: Kimura's Neutral Fixation Probability."
    )


def test_caption_policy_part_prefix_and_period() -> None:
    policy = CaptionPolicy(overrides={})
    assert policy.resolve("Worked example data for Part 2: Controls.", tbl_id="") == (
        "Sample data for Part 2: Controls."
    )
    assert policy.resolve("Summary table", tbl_id="") == "Summary table."


def test_build_caption_text_handles_part_sections() -> None:
    caption = build_caption_text("Part 3: Network Analysis", ["Node", "Edge"], data_rows=2)
    assert caption == "Sample data for Part 3: Network Analysis."


def test_collect_existing_tbl_ids_reads_latex_labels(tmp_path: Path) -> None:
    from biology.crossref.table_captions import collect_existing_tbl_ids

    md = tmp_path / "appendix.md"
    md.write_text(r"\label{tbl:demo_latex_label}", encoding="utf-8")
    assert "demo_latex_label" in collect_existing_tbl_ids(tmp_path)

    policy = CaptionPolicy(overrides={"demo_table": "Custom caption."})
    assert policy.resolve("ignored", tbl_id="demo_table") == "Custom caption."


def test_build_caption_text_summary_variants() -> None:
    assert build_caption_text("", ["Gene", "Effect"], data_rows=5) == "Summary table: Gene and Effect."
    assert build_caption_text("Drug classes", ["Class"], data_rows=4) == "Drug classes: Class and related columns."
    assert build_caption_text("", ["A"], data_rows=3) == "Summary table: A."


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
        "\n".join(
            [
                "### Demo",
                "",
                ": Worked example data for Demo table. {#tbl:unit_I_demo_demo}",
                "| A | B |",
                "| - | - |",
                "| 1 | 2 |",
                "",
            ]
        ),
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
        "\n".join(
            [
                "# Demo",
                "",
                ": Existing {#tbl:unit_I_demo_existing}",
                "| A | B |",
                "| - | - |",
                "| 1 | 2 |",
                "",
            ]
        ),
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
        "\n".join(
            [
                "### Growth rates",
                "",
                "| Time | Rate |",
                "| ---- | ---- |",
                "| 0 | 1 |",
                "| 1 | 2 |",
                "",
            ]
        ),
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
        "\n".join(
            [
                "### Rate constants",
                "",
                "| Enzyme | Rate |",
                "| ------ | ---- |",
                "| A | 1 |",
                "| B | 2 |",
                "| C | 3 |",
                "",
            ]
        ),
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
        "\n".join(
            [
                "### Demo",
                "",
                "| A | B |",
                "| - | - |",
                "| 1 | 2 |",
                "",
            ]
        ),
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
        "\n".join(
            [
                "### Blank worksheet rows",
                "",
                "| Taxon | Reads | p_i |",
                "| ----- | ----- | --- |",
                "| | | |",
                "| | | |",
                "",
            ]
        ),
        encoding="utf-8",
    )
    result = find_table_annotations(md, used_ids=set())
    assert len(result.annotations) == 1


def test_configured_manuscript_has_no_unlabeled_pipe_tables() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "manuscript"
    results, changed = annotate_manuscript(manuscript, write=False)
    assert changed == 0
    assert not results


def test_configured_table_captions_are_not_inside_pipe_tables() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "manuscript"
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


def test_generated_companion_source_module_has_stable_table_caption() -> None:
    from biology.enrichment.engine import companion_source_section
    from biology.enrichment.records import chapter_records

    record = chapter_records()[0]
    section = companion_source_section(record)

    assert f"{{#tbl:{record.unit_id}_{record.stem}_companion_source_surfaces}}" in section
    assert section.index("{#tbl:") < section.index("| Surface | Use it for |")


def test_configured_manuscript_table_captions_are_pdf_safe() -> None:
    manuscript = Path(__file__).resolve().parents[1] / "manuscript"
    offenders: list[str] = []
    for path in sorted(manuscript.rglob("*.md")):
        if path.name in {"README.md", "AGENTS.md"}:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            match = RE_TBL_CAPTION.match(line.strip())
            if match and "\\" in match.group("caption"):
                offenders.append(f"{path.relative_to(manuscript)}:{line_no}: {match.group('caption')}")

    assert not offenders
