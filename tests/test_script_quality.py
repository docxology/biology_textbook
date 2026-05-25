"""Script-level quality checks for project maintenance utilities."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import runpy
import sys


PROJECT = Path(__file__).resolve().parent.parent
SCRIPTS = PROJECT / "scripts"
DOC_PATHS = [
    PROJECT / "README.md",
    PROJECT / "AGENTS.md",
    PROJECT / "REVIEW.md",
    PROJECT / "docs" / "README.md",
    PROJECT / "docs" / "architecture.md",
    PROJECT / "docs" / "pipeline_guide.md",
    PROJECT / "docs" / "testing_guide.md",
    PROJECT / "manuscript" / "README.md",
    PROJECT / "tests" / "README.md",
    PROJECT / "tests" / "AGENTS.md",
    PROJECT / "scripts" / "AGENTS.md",
]
GENERIC_OVERVIEW_HEADING_PATHS = [
    PROJECT / "AGENTS.md",
    PROJECT / "docs" / "AGENTS.md",
    PROJECT / "docs" / "pipeline_guide.md",
    PROJECT / "docs" / "visualisation_guide.md",
    PROJECT / "manuscript" / "README.md",
    PROJECT / "manuscript" / "unit_0" / "AGENTS.md",
    PROJECT / "scripts" / "AGENTS.md",
]


def _script_files() -> list[Path]:
    return sorted(SCRIPTS.glob("*.py"))


def test_scripts_do_not_embed_absolute_checkout_paths() -> None:
    forbidden_fragments = (
        "/Users/",
        "projects_in_progress/biology_textbook",
    )
    offenders: list[str] = []
    for script in _script_files():
        text = script.read_text(encoding="utf-8")
        for fragment in forbidden_fragments:
            if fragment in text:
                offenders.append(f"{script.name} contains {fragment!r}")
    assert not offenders


def test_scripts_parse_as_python_modules() -> None:
    failures: list[str] = []
    for script in _script_files():
        try:
            ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
        except SyntaxError as exc:  # pragma: no cover - assertion path carries details
            failures.append(f"{script.name}: {exc}")
    assert not failures


def test_no_legacy_mermaid_alt_maintenance_clones() -> None:
    names = {script.name for script in _script_files()}
    assert "add_mermaid_alt_text.py" in names
    assert "add_mermaid_alt_text_v2.py" not in names
    assert "fix_mermaid_alts.py" not in names


def test_mermaid_alt_text_preserves_acronym_prefixes() -> None:
    """Generated alt text should not lowercase acronyms such as TLR4."""
    namespace = runpy.run_path(str(SCRIPTS / "add_mermaid_alt_text.py"))
    alt_from_caption = namespace["_alt_from_caption"]

    alt = alt_from_caption(
        "TLR4/MyD88/NF-κB pathway. LBP and CD14 deliver bacterial LPS.",
        "flowchart TD\n    A[TLR4 receptor complex] --> B[NF-κB]",
        "## Pattern Recognition Receptors",
    )

    assert "Flowchart showing TLR4/MyD88" in alt
    assert "Flowchart showing tLR4" not in alt


def test_mermaid_alt_text_cleans_nameref_artifacts() -> None:
    """Caption cleanup should not leak malformed ``amerefsec:`` text into alt comments."""
    namespace = runpy.run_path(str(SCRIPTS / "add_mermaid_alt_text.py"))
    alt_from_caption = namespace["_alt_from_caption"]
    metadata_is_weak = namespace["_metadata_is_weak"]

    alt = alt_from_caption(
        r"\nameref{sec:unit_I_unit_intro} concept map — Chemistry of Life.",
        "graph TD\n    A[Atoms] --> B[Macromolecules]",
        "## Chemistry of Life",
    )

    assert "amerefsec" not in alt
    assert metadata_is_weak("Graph showing amerefsec:unit_I_unit_intro concept map")


def test_publication_readiness_gate_documents_default_and_full_scope() -> None:
    namespace = runpy.run_path(str(SCRIPTS / "audit_publication_readiness.py"))
    build_command_steps = namespace["build_command_steps"]

    default_names = {step.name for step in build_command_steps(full=False)}
    full_names = {step.name for step in build_command_steps(full=True)}

    assert "quality-audit" in default_names
    assert "current-claims" in default_names
    assert "diagrams-strict" in default_names
    assert "root-wip-resolver-smoke" in default_names
    assert "coverage" not in default_names
    assert "project-tests-gate" not in default_names
    assert "root-render" not in default_names
    assert {"project-tests-gate", "root-setup", "root-render", "root-validate-output", "root-pdf-log"} <= full_names


def test_publication_readiness_gate_uses_check_mode_for_mutating_sync_scripts() -> None:
    namespace = runpy.run_path(str(SCRIPTS / "audit_publication_readiness.py"))
    build_command_steps = namespace["build_command_steps"]
    commands = {step.name: step.command for step in build_command_steps(full=False)}

    assert "--check" in commands["assessment-sync"]
    assert "--check" in commands["mermaid-alt-sync"]


def test_publication_readiness_gate_uses_temporary_visual_outputs(tmp_path: Path) -> None:
    namespace = runpy.run_path(str(SCRIPTS / "audit_publication_readiness.py"))
    build_command_steps = namespace["build_command_steps"]
    commands = {
        step.name: step.command
        for step in build_command_steps(full=False, artifact_dir=tmp_path)
    }
    project_output = str(PROJECT / "output")

    assert "--output" in commands["visual-contracts"]
    assert "--output-dir" in commands["figures-strict"]
    assert "--output-dir" in commands["diagrams-strict"]
    for command in commands.values():
        assert not any(part.startswith(project_output) for part in command)


def test_publication_readiness_project_tests_gate_uses_module_pytest_entrypoint() -> None:
    namespace = runpy.run_path(str(SCRIPTS / "audit_publication_readiness.py"))
    build_command_steps = namespace["build_command_steps"]
    commands = {step.name: step.command for step in build_command_steps(full=True)}

    assert commands["project-tests-gate"][:3] == ("uv", "run", "pytest")
    assert "--cov-fail-under=90" in commands["project-tests-gate"]


def test_further_reading_inserter_uses_specialized_source_heading() -> None:
    namespace = runpy.run_path(str(SCRIPTS / "insert_further_reading.py"))
    bib_entry = namespace["BibEntry"](
        key="example",
        entry_type="article",
        author="Example, Ada",
        year="2026",
        title="Source governance in biology",
        journal="Journal of Biology Sources",
    )

    section = namespace["render_section"]([bib_entry], "Cell Theory")

    assert "## Further Reading and Source Notes: Cell Theory" in section
    assert "\n## Further Reading\n" not in section


def test_assessment_sync_dry_run_path_does_not_write(tmp_path: Path) -> None:
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    namespace = runpy.run_path(str(SCRIPTS / "sync_assessment_metadata.py"))
    write_or_record = namespace["_write_or_record"]
    target = tmp_path / "lab.md"
    target.write_text("original\n", encoding="utf-8")

    changed = write_or_record(target, "updated\n", write=False)

    assert changed == [target]
    assert target.read_text(encoding="utf-8") == "original\n"


def test_extract_glossary_cards_parser_matches_live_glossary() -> None:
    """Glossary-card export should parse the current bracketed-span glossary format."""
    namespace = runpy.run_path(str(SCRIPTS / "extract_glossary_cards.py"))
    parse_glossary = namespace["parse_glossary"]

    entries = parse_glossary(PROJECT / "manuscript" / "glossary.md")

    assert len(entries) > 100
    assert entries[0]["term"] == "Abiotic"
    assert entries[0]["slug"] == "abiotic"
    assert "\\cref" not in entries[0]["definition"]


def test_documentation_headings_avoid_generic_overview() -> None:
    offenders: list[str] = []
    pattern = re.compile(r"^## Overview$", flags=re.MULTILINE)
    for path in GENERIC_OVERVIEW_HEADING_PATHS:
        if pattern.search(path.read_text(encoding="utf-8")):
            offenders.append(str(path.relative_to(PROJECT)))
    assert not offenders


def test_documented_project_counts_match_live_inventory() -> None:
    """Docs should not drift from the live script/test inventory."""
    script_count = len(_script_files())
    test_count = len(sorted((PROJECT / "tests").glob("test_*.py")))
    stale_patterns = (
        r"\b20 Python files\b",
        r"\b21 Python files\b",
        r"\b22 Python files\b",
        r"\b29 `test_",
        r"\b29 Python files\b",
        r"\b38 labs\b",
        r"\b38 question banks\b",
        r"\b16 test modules\b",
        r"\b18 test files\b",
        r"\b19 test modules\b",
        r"\b38 configured chapters\b",
        r"\b38-chapter\b",
        r"\b38/38/38\b",
        r"13 matplotlib",
        r"14 matplotlib generators",
        r"\b18 `plot_\*`",
        r"\b18 matplotlib",
        r"\b18 registered matplotlib",
        r"\b18 plots\b",
        r"568 passed",
        r"92\.33%",
    )
    offenders: list[str] = []
    for path in DOC_PATHS:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(PROJECT).as_posix()
        if f"{script_count} Python files" not in text and rel in {"README.md", "docs/architecture.md"}:
            offenders.append(f"{rel} missing live script count {script_count}")
        if "44 chapters" not in text and rel == "README.md":
            offenders.append(f"{rel} missing live 44-chapter count")
        if rel == "manuscript/README.md" and "**44**" not in text:
            offenders.append(f"{rel} missing live 44-chapter total in unit map")
        if rel in {"README.md", "docs/testing_guide.md", "tests/README.md"} and str(test_count) not in text:
            offenders.append(f"{rel} missing live test count {test_count}")
        if rel == "README.md" and "test_chapter_pedagogy_coverage" not in text:
            offenders.append(f"{rel} missing pedagogy regression test signpost")
        for pattern in stale_patterns:
            if rel == "REVIEW.md":
                continue
            if re.search(pattern, text):
                offenders.append(f"{path.relative_to(PROJECT)} contains stale pattern {pattern!r}")
    assert not offenders
