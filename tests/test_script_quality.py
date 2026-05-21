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
    PROJECT / "REVIEW.md",
    PROJECT / "docs" / "architecture.md",
    PROJECT / "docs" / "pipeline_guide.md",
    PROJECT / "docs" / "testing_guide.md",
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
    assert "root-render" not in default_names
    assert {"coverage", "root-setup", "root-project-tests", "root-render", "root-validate-output"} <= full_names


def test_publication_readiness_gate_uses_check_mode_for_mutating_sync_scripts() -> None:
    namespace = runpy.run_path(str(SCRIPTS / "audit_publication_readiness.py"))
    build_command_steps = namespace["build_command_steps"]
    commands = {step.name: step.command for step in build_command_steps(full=False)}

    assert "--check" in commands["assessment-sync"]
    assert "--check" in commands["mermaid-alt-sync"]


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


def test_documented_project_counts_match_live_inventory() -> None:
    """Docs should not drift from the live script/test inventory."""
    script_count = len(_script_files())
    test_count = len(sorted((PROJECT / "tests").glob("test_*.py")))
    stale_patterns = (
        r"\b20 Python files\b",
        r"\b21 Python files\b",
        r"\b22 Python files\b",
        r"\b16 test modules\b",
        r"\b18 test files\b",
        r"\b19 test modules\b",
        r"13 matplotlib",
        r"568 passed",
        r"92\.33%",
    )
    offenders: list[str] = []
    for path in DOC_PATHS:
        text = path.read_text(encoding="utf-8")
        if f"{script_count} Python files" not in text and path.name in {"README.md", "architecture.md"}:
            offenders.append(f"{path.relative_to(PROJECT)} missing live script count {script_count}")
        if path.name in {"README.md", "testing_guide.md"} and str(test_count) not in text:
            offenders.append(f"{path.relative_to(PROJECT)} missing live test count {test_count}")
        for pattern in stale_patterns:
            if re.search(pattern, text):
                offenders.append(f"{path.relative_to(PROJECT)} contains stale pattern {pattern!r}")
    assert not offenders
