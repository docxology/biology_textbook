"""Real-source boundary regressions for spelling, identities and metadata."""

from pathlib import Path

import pytest

from biology.assessment import parse_question_bank
from biology.crossref.parent_chapter_links import insert_parent_chapter_cref
from biology.crossref.validator import scan_directory
from biology.maintenance.american_english import (
    find_british_spellings,
    iter_target_files,
    normalize_text,
)
from biology.maintenance.lab_padding import derive_chapter_label_from_lab


@pytest.mark.parametrize("source,expected,count", [
    ("(self-organised criticality), self-organised!", "(self-organized criticality), self-organized!", 2),
    ("Colour-vision; colour-blind, colour-calibration.", "Color-vision; color-blind, color-calibration.", 3),
    ("NEIGHBOURHOOD / neighbourhoods / neighbour.", "NEIGHBORHOOD / neighborhoods / neighbor.", 3),
])
def test_spelling_uses_longest_original_nonoverlapping_matches(source: str, expected: str, count: int) -> None:
    normalized, replacements = normalize_text(source)
    assert (normalized, replacements) == (expected, count)
    assert normalize_text(normalized) == (expected, 0)
    assert not find_british_spellings(normalized)


def test_spelling_exclusions_apply_to_every_discovery_branch(tmp_path: Path) -> None:
    paths = [
        tmp_path / "docs" / "manuscript" / "preamble.md",
        tmp_path / "docs" / "preamble.md",
        tmp_path / "src" / "biology" / "preamble.md",
        tmp_path / "docs" / "manuscript" / "chapter.md",
        tmp_path / "docs" / "guide.md",
    ]
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("colour\n", encoding="utf-8")
    assert set(iter_target_files(tmp_path)) == set(paths[-2:])


@pytest.mark.parametrize("command", [
    r"\cref{sec:present, sec:missing}",
    r"\Cref{sec:present,sec:missing}",
    r"\nameref{sec:missing}",
    r"\hyperref[sec:missing]{target}",
    r"\ref{sec:missing}",
    r"\eqref{sec:missing}",
    r"\autoref{sec:missing}",
])
def test_raw_reference_commands_really_detect_dangling_targets(tmp_path: Path, command: str) -> None:
    path = tmp_path / "chapter.md"
    path.write_text("# Chapter {#sec:present}\n\n" + command + "\n", encoding="utf-8")
    report = scan_directory(tmp_path)
    assert {issue.suggested_id for issue in report.unresolved} == {"missing"}
    assert not report.duplicates


def test_all_targets_inside_latex_environment_are_validated(tmp_path: Path) -> None:
    path = tmp_path / "chapter.md"
    path.write_text("\\begin{figure}\n\\label{fig:known}\n\\caption{See \\cref{sec:missing}.}\n\\end{figure}\n", encoding="utf-8")
    report = scan_directory(tmp_path)
    assert any(issue.suggested_id == "missing" for issue in report.unresolved)
    assert ("fig", "known") in report.defined


@pytest.mark.parametrize("source", [
    "\\label{sec:duplicate}\n\\label{sec:duplicate}\n",
    "# Chapter {#sec:duplicate}\n\\label{sec:duplicate}\n",
    "\\label{fig:duplicate}\n\\label{fig:duplicate}\n",
    "\\label{plain_label}\n\\label{plain_label}\n",
])
def test_duplicate_raw_or_mixed_definitions_are_not_overwritten(tmp_path: Path, source: str) -> None:
    (tmp_path / "chapter.md").write_text(source, encoding="utf-8")
    report = scan_directory(tmp_path)
    assert len(report.duplicates) == 1


def test_examples_are_protected_but_instructor_solution_refs_are_real(tmp_path: Path) -> None:
    source = r"""# Chapter {#sec:real}
`\label{sec:example}` and `\cref{sec:example}` demonstrate syntax.
<!-- Ordinary comment: \label{sec:comment} \cref{sec:comment_missing} -->
% \label{sec:tex_comment} \cref{sec:tex_comment_missing}
````markdown
# Example {#sec:example_heading}
```
\label{sec:example_label}
\Cref{sec:example_missing}
````
~~~text
\nameref{sec:tilde_missing}
~~~
At 25% coverage, see \cref{sec:real}.
<!-- SOLUTION
**Answer (Q1, Recall).** This instructor explanation cites \cref{sec:instructor_missing}.
SOLUTION -->
"""
    (tmp_path / "chapter.md").write_text(source, encoding="utf-8")
    report = scan_directory(tmp_path)
    assert set(report.defined) == {("sec", "real")}
    assert {issue.suggested_id for issue in report.unresolved} == {"instructor_missing"}
    assert any(kind == "sec" and target == "real" for kind, target, _, _ in report.references)


def test_raw_latex_fence_is_rendered_not_an_example(tmp_path: Path) -> None:
    (tmp_path / "chapter.md").write_text("```{=latex}\n\\label{sec:raw}\n\\cref{sec:missing}\n```\n", encoding="utf-8")
    report = scan_directory(tmp_path)
    assert ("sec", "raw") in report.defined
    assert {issue.suggested_id for issue in report.unresolved} == {"missing"}


@pytest.mark.parametrize("fields", [
    "LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer",  # missing minutes
    "LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=0",
    "LO=LO1; bloom=Invent; difficulty=Recall; format=short-answer; minutes=2",
    "LO=LO1; bloom=Remember; difficulty=Unknown; format=short-answer; minutes=2",
    "LO=LO1; bloom=Remember; difficulty=Recall; format=essay; minutes=2",
    "LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2; mystery=yes",
    "LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2; malformed",
])
def test_corrupt_item_schema_is_rejected_without_writes(tmp_path: Path, fields: str) -> None:
    bank = tmp_path / "questions.md"
    source = f"<!-- assess: {fields} -->\n1. Calculate twice 3.\n"
    bank.write_text(source, encoding="utf-8")
    with pytest.raises(ValueError):
        parse_question_bank(bank)
    assert bank.read_text(encoding="utf-8") == source


def test_question_parser_ignores_fenced_and_comment_examples(tmp_path: Path) -> None:
    source = """```text
1. A pedagogical example, not a bank item.
```
<!--
2. Another example.
-->
<!-- assess: LO=LO1; bloom=Apply; difficulty=Application; format=short-answer; minutes=2 -->
1. Calculate twice 3.
<!-- SOLUTION
**Answer (Q1, Application).** 2 × 3 = 6.
1. An intermediate numbered reasoning step is not a new question.
SOLUTION -->
"""
    bank = tmp_path / "questions.md"
    bank.write_text(source, encoding="utf-8")
    assert [item.number for item in parse_question_bank(bank).items] == [1]


def test_canonical_h1_labels_drive_lab_and_parent_maintenance() -> None:
    text = "# Lab {#sec:lab_unit_II_cell_signaling .unnumbered}\n\nPerform the experiment.\n"
    assert derive_chapter_label_from_lab(text) == "sec:unit_II_cell_signaling"
    path = Path("docs/manuscript/labs/unit_II/lab_cell_signaling.md")
    updated = insert_parent_chapter_cref(text, path)
    assert updated is not None and "\\cref{sec:unit_II_cell_signaling}" in updated
    assert insert_parent_chapter_cref(updated, path) is None


def test_wrapped_raw_definitions_and_comma_references_keep_their_identity(tmp_path: Path) -> None:
    source = "\\label{\nsec:present\n}\nSee \\cref{\nsec:present,\nsec:missing\n}.\n"
    (tmp_path / "chapter.md").write_text(source, encoding="utf-8")
    report = scan_directory(tmp_path)
    assert ("sec", "present") in report.defined
    assert {issue.suggested_id for issue in report.unresolved} == {"missing"}


@pytest.mark.parametrize("command", [r"\cref{}", r"\hyperref[]{empty}"])
def test_empty_raw_reference_is_a_failure_not_a_silent_skip(tmp_path: Path, command: str) -> None:
    (tmp_path / "chapter.md").write_text(command + "\n", encoding="utf-8")
    assert scan_directory(tmp_path).unresolved


def test_empty_raw_label_is_invalid(tmp_path: Path) -> None:
    (tmp_path / "chapter.md").write_text("\\label{}\n", encoding="utf-8")
    report = scan_directory(tmp_path)
    assert not report.defined
    assert report.missing


def test_recursive_discovery_rejects_an_external_manuscript_ancestor(tmp_path: Path) -> None:
    from biology.maintenance.manuscript_walker import manuscript_markdown_files

    project = tmp_path / "project"
    project.mkdir()
    external = tmp_path / "external"
    manuscript = external / "manuscript"
    manuscript.mkdir(parents=True)
    (manuscript / "chapter.md").write_bytes(b"\xffprivate source")
    (project / "docs").symlink_to(external, target_is_directory=True)
    with pytest.raises(ValueError, match="escapes project"):
        manuscript_markdown_files(project / "docs" / "manuscript", project_root=project)
    assert (manuscript / "chapter.md").read_bytes() == b"\xffprivate source"


def test_recursive_discovery_preserves_internal_directory_aliases_and_exclusions(tmp_path: Path) -> None:
    from biology.maintenance.manuscript_walker import manuscript_markdown_files

    root = tmp_path / "manuscript"
    chapter = root / "unit_I" / "chapter.md"
    chapter.parent.mkdir(parents=True)
    chapter.write_text("# Authored chapter\n", encoding="utf-8")
    (root / "README.md").write_bytes(b"\xffexcluded guide")
    (chapter.parent / "AGENTS.md").write_bytes(b"\xffexcluded contract")
    (root / "unit_alias").symlink_to(chapter.parent, target_is_directory=True)
    files = manuscript_markdown_files(root)
    assert files == [chapter, root / "unit_alias" / "chapter.md"]
    assert all(path.read_text(encoding="utf-8") == "# Authored chapter\n" for path in files)


def test_recursive_discovery_refuses_cycles_instead_of_revisiting_sources(tmp_path: Path) -> None:
    from biology.maintenance.manuscript_walker import manuscript_markdown_files

    root = tmp_path / "manuscript"
    root.mkdir()
    chapter = root / "chapter.md"
    chapter.write_text("# Authored chapter\n", encoding="utf-8")
    (root / "loop").symlink_to(root, target_is_directory=True)
    with pytest.raises(ValueError, match="Cyclic"):
        manuscript_markdown_files(root)
    assert chapter.read_text(encoding="utf-8") == "# Authored chapter\n"
