"""Visibility boundaries exercised through actual advisory and crossref consumers."""
from __future__ import annotations

from pathlib import Path

import pytest

from biology.crossref.source import visible_text
from biology.crossref.validator import scan_directory
from biology.maintenance import manuscript_walker
from biology.quality import paths
from biology.quality.audits.advisories import audit_absolute_language
from biology.quality.models import Finding

CLAIM = "Always apply transition T in this stipulated four-state simulation."
REFERENCE = r"See \cref{sec:missing}."


@pytest.fixture
def consumer_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    manuscript = tmp_path / "docs/manuscript"
    source = manuscript / "unit_test/model.md"
    source.parent.mkdir(parents=True)
    monkeypatch.setattr(manuscript_walker, "MANUSCRIPT", manuscript)
    monkeypatch.setattr(paths, "PROJECT", tmp_path)
    return source


def assert_consumer_output(source: Path, text: str, *, rendered_label: bool = False) -> None:
    source.write_text(text, encoding="utf-8")
    lines = text.splitlines()
    claim_line = lines.index(CLAIM) + 1
    reference_line = lines.index(REFERENCE) + 1
    findings: list[Finding] = []
    audit_absolute_language(findings)
    assert [(finding.path, finding.line, finding.message) for finding in findings] == [
        (source, claim_line, CLAIM),
    ]
    report = scan_directory(source.parent)
    assert [(issue.suggested_id, issue.line) for issue in report.unresolved] == [
        ("missing", reference_line),
    ]
    expected_labels = {("sec", "real")}
    if rendered_label:
        expected_labels.add(("sec", "rendered"))
    assert set(report.defined) == expected_labels
    assert not report.duplicates
    visible = visible_text(text)
    assert len(visible) == len(text)
    assert [index for index, char in enumerate(visible) if char == "\n"] == [
        index for index, char in enumerate(text) if char == "\n"
    ]
    for rendered in (CLAIM, REFERENCE):
        start = text.index(rendered)
        assert visible[start:start + len(rendered)] == rendered


@pytest.mark.parametrize("marker", ["`", "``", "```", "````", "~~~", "~~~~", "`\n~~~"])
def test_comment_contained_markers_cannot_hide_subsequent_real_content(
    consumer_tree: Path, marker: str,
) -> None:
    text = (
        "# Chapter {#sec:real}\n\n<!-- draft marker\n"
        + marker
        + "\nAlways hide this draft instruction.\n"
        + "\\label{sec:hidden}\n\\cref{sec:hidden_missing}\n-->\n"
        + CLAIM + "\n" + REFERENCE + "\n"
    )
    assert_consumer_output(consumer_tree, text)


@pytest.mark.parametrize("example", [
    "`<!-- Always hide this example; \\label{sec:hidden} \\cref{sec:hidden_missing}`\n",
    "``<!-- Always hide ` this example; \\label{sec:hidden} \\cref{sec:hidden_missing}``\n",
    "```text\n<!--\nAlways hide this example.\n\\label{sec:hidden}\n\\cref{sec:hidden_missing}\n```\n",
    "~~~text\n<!--\nAlways hide this example.\n\\label{sec:hidden}\n\\cref{sec:hidden_missing}\n~~~\n",
    "````text\n<!--\n```\nAlways hide this example.\n\\label{sec:hidden}\n\\cref{sec:hidden_missing}\n````\n",
    "<!-- Always hide this comment. \\label{sec:hidden} \\cref{sec:hidden_missing} -->\n",
])
def test_comment_tokens_inside_examples_remain_inert(consumer_tree: Path, example: str) -> None:
    text = "# Chapter {#sec:real}\n" + example + CLAIM + "\n" + REFERENCE + "\n"
    assert_consumer_output(consumer_tree, text)


@pytest.mark.parametrize("opening,closing", [
    ("<!-- SOLUTION", "SOLUTION -->"),
    ("```{=latex}", "```"),
    ("~~~{=tex}", "~~~"),
])
def test_instructor_and_raw_latex_bodies_reach_both_consumers(
    consumer_tree: Path, opening: str, closing: str,
) -> None:
    text = (
        "# Chapter {#sec:real}\n" + opening + "\n"
        + "\\label{sec:rendered}\n" + CLAIM + "\n" + REFERENCE + "\n"
        + closing + "\n"
        + "<!-- Ordinary comment: Always hide this draft. \\cref{sec:hidden_missing} -->\n"
        + "`Always hide this example; \\cref{sec:example_missing}`\n"
    )
    assert_consumer_output(consumer_tree, text, rendered_label=True)


def test_raw_latex_comment_looking_text_does_not_hide_later_content(consumer_tree: Path) -> None:
    text = (
        "# Chapter {#sec:real}\n```{=latex}\n\\texttt{<!--}\n"
        + CLAIM + "\n" + REFERENCE + "\n```\n"
    )
    assert_consumer_output(consumer_tree, text)
