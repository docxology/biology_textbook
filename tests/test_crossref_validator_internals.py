"""Coverage tests for :mod:`biology.crossref_validator` internals.

Exercises the parser against hand-crafted micro-manuscripts so every code
path (figure env, equation env, inline $$, table caption, prose xref,
heading, section duplicate) is hit.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


PROJECT = Path(__file__).resolve().parent.parent
MOD_PATH = PROJECT / "src" / "biology" / "crossref_validator.py"


def _load():
    spec = importlib.util.spec_from_file_location("crossref_validator", MOD_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load crossref validator from {MOD_PATH}")
    m = importlib.util.module_from_spec(spec)
    sys.modules["crossref_validator"] = m
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope="module")
def v():
    return _load()


# ---------------------------------------------------------------------------

def test_slugify_collapses_punctuation(v) -> None:
    slug = v.suggest_id("fig", Path("unit_I/foo.md"), "Hello, World!!")
    assert slug.endswith("hello-world")


def test_unit_tag_extraction_front_matter(v) -> None:
    slug = v.suggest_id("fig", Path("front_matter.md"), "foo")
    assert slug.startswith("front-")


def test_inline_display_eq_with_tag_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "x.md"
    f.write_text("# X\n\n$$ E = mc^2 \\tag{1.1} $$\n\n", encoding="utf-8")
    defined, _, issues = v.scan_file(f)
    assert not any(k == "eq" for k, _ in defined)
    assert any(i.kind == "equation" and i.problem == "hardcoded_equation_tag" for i in issues)
    assert any(i.kind == "equation" and i.problem == "missing_id" for i in issues)


def test_inline_display_eq_without_tag_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "y.md"
    f.write_text("# Y\n\n$$ x = y $$\n", encoding="utf-8")
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "equation" and i.problem == "missing_id" for i in issues)


def test_latex_figure_without_label_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "z.md"
    f.write_text(
        "# Z\n\n\\begin{figure}\n\\includegraphics{foo.png}\n\\caption{No label}\n\\end{figure}\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "figure" and i.problem == "missing_id" for i in issues)


def test_latex_figure_with_label_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "zl.md"
    f.write_text(
        "# Zl\n\n\\begin{figure}\n\\includegraphics{foo.png}\n\\label{fig:foo}\n\\end{figure}\n",
        encoding="utf-8",
    )
    defined, _, issues = v.scan_file(f)
    assert ("fig", "foo") in defined
    assert not [i for i in issues if i.kind == "figure" and i.problem == "missing_id"]


def test_latex_equation_env_with_label_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "eq.md"
    f.write_text(
        "# E\n\n\\begin{equation}\n    E = mc^2\n    \\label{eq:relativity}\n\\end{equation}\n",
        encoding="utf-8",
    )
    defined, _, _ = v.scan_file(f)
    assert ("eq", "relativity") in defined


def test_one_line_latex_equation_env_with_label_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "eq_inline.md"
    f.write_text(
        "# E\n\n\\begin{equation}E = mc^2\\label{eq:relativity}\\end{equation}\n\n"
        "See Sections 2 and 5 for a deliberately bad prose reference.\n",
        encoding="utf-8",
    )
    defined, _, issues = v.scan_file(f)
    assert ("eq", "relativity") in defined
    assert any(i.problem == "prose_xref" for i in issues)


def test_latex_equation_env_without_label_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "eq2.md"
    f.write_text(
        "# E2\n\n\\begin{equation}\n    a = b\n\\end{equation}\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "equation" and i.problem == "missing_id" for i in issues)


def test_latex_table_env_label_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "tbl.md"
    f.write_text(
        "# T\n\n\\begin{table}\n\\caption{Foo}\n\\label{tbl:foo}\n\\end{table}\n",
        encoding="utf-8",
    )
    defined, _, _ = v.scan_file(f)
    assert ("tbl", "foo") in defined


def test_latex_table_env_without_label_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "tbl2.md"
    f.write_text(
        "# T2\n\n\\begin{table}\n\\caption{Bar}\n\\end{table}\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "table" and i.problem == "missing_id" for i in issues)


def test_section_with_sec_id_detected(v, tmp_path: Path) -> None:
    f = tmp_path / "s.md"
    f.write_text("# H1\n\n## Sub {#sec:subsection}\n\nhello\n", encoding="utf-8")
    defined, _, _ = v.scan_file(f)
    assert ("sec", "subsection") in defined


def test_prose_xref_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "p.md"
    f.write_text("# P\n\nas explained, see Chapter 5 for more details.\n", encoding="utf-8")
    _, _, issues = v.scan_file(f)
    assert any(i.problem == "prose_xref" for i in issues)


def test_plain_numbered_xref_patterns_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "many.md"
    f.write_text(
        "# P\n\n"
        "See Figure 4.2, Equation 4.7, Section 3.1, and § 2 for numbered refs.\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.problem == "prose_xref" for i in issues)


def test_plural_numbered_xref_lists_are_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "plural.md"
    f.write_text(
        "# P\n\n"
        "Sections 2 and 5 introduce the dynamics, while Figures 3.1 and 3.2 show the phase portraits.\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    contexts = [i.context for i in issues if i.problem == "prose_xref"]
    assert contexts


def test_raw_latex_ref_commands_are_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "rawref.md"
    f.write_text(
        "# P\n\n"
        "Apply the model in Equation~\\eqref{eq:population_genetics_1}, "
        "Figure~\\ref{fig:example}, Section \\ref{sec:plain_space}, "
        "and the bare target \\autoref{tbl:plain_table}.\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    contexts = [i.context for i in issues if i.problem == "prose_xref"]
    assert contexts and "\\autoref{tbl:plain_table}" in contexts[0]


def test_inline_dollar_equation_with_tag_and_label_is_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "tag_label.md"
    f.write_text(
        "# P\n\n"
        r"$$ p^2 + 2pq + q^2 = 1 \tag{18.1} \label{eq:population_genetics_1}$$"
        "\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.problem == "tag_label_dollar_equation" for i in issues)
    assert any(i.problem == "hardcoded_equation_tag" for i in issues)


def test_latex_equation_environment_with_tag_is_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "env_tag.md"
    f.write_text(
        "# P\n\n"
        "\\begin{equation}\n"
        "x = y\n"
        "\\tag{2.4}\n"
        "\\label{eq:manual_tag}\n"
        "\\end{equation}\n",
        encoding="utf-8",
    )
    defined, _, issues = v.scan_file(f)
    assert ("eq", "manual_tag") in defined
    assert any(i.kind == "equation" and i.problem == "hardcoded_equation_tag" for i in issues)


def test_at_ref_collection(v, tmp_path: Path) -> None:
    f = tmp_path / "r.md"
    f.write_text("# R\n\nAs shown in @fig:foo and @eq:bar.\n", encoding="utf-8")
    _, refs, _ = v.scan_file(f)
    kinds = {r[0] for r in refs}
    assert kinds == {"fig", "eq"}


def test_scan_directory_detects_unresolved_refs(v, tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text(
        "# A\n\\label{sec:a}\n\nRefer to @sec:nonexistent here.\n", encoding="utf-8"
    )
    report = v.scan_directory(tmp_path)
    assert any(i.problem == "unresolved" for i in report.issues)


def test_duplicate_labels_detected_across_files(v, tmp_path: Path) -> None:
    (tmp_path / "a.md").write_text(
        "# A\n\n\\begin{figure}\n\\label{fig:shared}\n\\end{figure}\n", encoding="utf-8"
    )
    (tmp_path / "b.md").write_text(
        "# B\n\n\\begin{figure}\n\\label{fig:shared}\n\\end{figure}\n", encoding="utf-8"
    )
    report = v.scan_directory(tmp_path)
    assert any(i.problem == "duplicate" for i in report.issues)


def test_issue_as_row_and_report_summary(v, tmp_path: Path) -> None:
    f = tmp_path / "a.md"
    f.write_text("# A\n\n$$ x = 1 $$\n", encoding="utf-8")
    report = v.scan_directory(tmp_path)
    assert "missing=" in report.summary()
    for i in report.issues:
        row = i.as_row()
        assert set(row.keys()) == {"file", "line", "kind", "problem", "suggested_id", "context"}
