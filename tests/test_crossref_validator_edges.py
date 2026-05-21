"""Exercise rarely-hit branches of :mod:`biology.crossref_validator`.

Focuses on paths missed by the canonical tests: markdown image with ``{#fig:}``
attrs, multi-line block equations with labels on the line after the closing
``$$``, duplicate markdown-figure ids, section {#sec:} duplicates, and table
caption detection.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest


MOD_PATH = Path(__file__).resolve().parent.parent / "src" / "biology" / "crossref_validator.py"


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


def test_markdown_image_with_fig_id(v, tmp_path: Path) -> None:
    f = tmp_path / "a.md"
    f.write_text("# A\n\n![caption](foo.png){#fig:foo}\n", encoding="utf-8")
    defined, _, _ = v.scan_file(f)
    assert ("fig", "foo") in defined


def test_markdown_image_without_id_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "b.md"
    f.write_text("# B\n\n![caption](foo.png)\n", encoding="utf-8")
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "figure" and i.problem == "missing_id" for i in issues)


def test_duplicate_fig_id_in_one_file(v, tmp_path: Path) -> None:
    f = tmp_path / "dupl.md"
    f.write_text(
        "# D\n\n![x](a.png){#fig:same}\n\n![y](b.png){#fig:same}\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.problem == "duplicate" for i in issues)


def test_block_equation_id_on_following_line(v, tmp_path: Path) -> None:
    f = tmp_path / "eqq.md"
    # Multi-line $$…$$ with the id on the *next* line.
    f.write_text(
        "# E\n\n$$\n    E = mc^2\n$$\n{#eq:relativity}\n",
        encoding="utf-8",
    )
    defined, _, _ = v.scan_file(f)
    assert ("eq", "relativity") in defined


def test_block_equation_no_id_flagged(v, tmp_path: Path) -> None:
    f = tmp_path / "eqq2.md"
    f.write_text("# E2\n\n$$\n    a = b\n$$\n", encoding="utf-8")
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "equation" and i.problem == "missing_id" for i in issues)


def test_table_caption_with_id(v, tmp_path: Path) -> None:
    f = tmp_path / "t.md"
    f.write_text(
        "# T\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\nTable: A demo caption {#tbl:demo}\n",
        encoding="utf-8",
    )
    defined, _, _ = v.scan_file(f)
    assert ("tbl", "demo") in defined


def test_heading_with_duplicate_sec_id(v, tmp_path: Path) -> None:
    f = tmp_path / "d.md"
    f.write_text(
        "# D\n\n## Foo {#sec:same}\n\n## Bar {#sec:same}\n",
        encoding="utf-8",
    )
    _, _, issues = v.scan_file(f)
    assert any(i.kind == "section" and i.problem == "duplicate" for i in issues)


def test_missing_file_flagged_gracefully(v, tmp_path: Path) -> None:
    f = tmp_path / "never.md"
    defined, refs, issues = v.scan_file(f)
    # Unreadable file yields a single "file" issue, not a crash.
    assert any(i.kind == "file" for i in issues)


def test_report_grouping_helpers(v, tmp_path: Path) -> None:
    f = tmp_path / "a.md"
    f.write_text("# A\n\n$$ x = 1 $$\n\nsee Chapter 2\n", encoding="utf-8")
    report = v.scan_directory(tmp_path)
    # Access all grouping properties
    _ = report.missing
    _ = report.unresolved
    _ = report.duplicates
    _ = report.prose
    summary = report.summary()
    assert "missing=" in summary
