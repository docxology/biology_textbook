"""Project-wide textbook quality audit tests."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT / "manuscript"
SCRIPT = PROJECT / "scripts" / "audit_textbook_quality.py"

spec = importlib.util.spec_from_file_location("audit_textbook_quality", SCRIPT)
assert spec is not None
audit = importlib.util.module_from_spec(spec)
sys.modules["audit_textbook_quality"] = audit
assert spec.loader is not None
spec.loader.exec_module(audit)


GENERIC_ANSWER_PHRASES = (
    "Build a mechanistic answer",
    "Give the canonical definition",
    "Numerical problem on",
    "Take a position on *",
    "Propose an experimental or engineering response",
    "Rubric for *",
    "name the relevant players",
    "scale-setting detail",
    "state the judgment, cite two lines of evidence",
    "identify the governing equation or ratio",
    "specify the manipulated variable",
    "propose one comparative or population-genomic test",
    "propose one clinical intervention",
    "propose one molecular intervention",
    "Name the term in ",
    "Evidence anchor:",
    "Credit requires an explicit mechanism",
    "prompt-linked evidence",
    "Core response for *",
    "Expected answer for *",
    "Prompt cues to cover:",
    "Source standard:",
    "Common pitfall:",
    "Chapter lens:",
    "set up the governing equation",
    "state a defensible judgment",
    "support it with two chapter-specific observations",
    "Answer every requested clause",
    "Ground the answer in \\cref",
    "Use \\cref",
    "Extend \\cref",
    "Name the biological players",
    "name one limitation or counterexample",
    "boundary condition that prevents overgeneralising",
    "Carry through these values:",
    "Use these named items explicitly:",
    "Define *",
    "Compare *",
    "Solve *",
    "Explain *",
    "Design the test for *",
    "Evaluate *",
    "Apply the chapter principle to *",
    "Required clauses:",
    "Use the stated values explicitly:",
    "Named evidence to include:",
    "Do not stop at the first noun phrase",
    "Anchor the response to \\cref",
    "A complete response should",
    "Expected reasoning:",
    "Scoring focus:",
    "Key answer:",
    "Comparison answer:",
    "Calculation answer:",
    "Mechanistic answer:",
    "Design answer:",
    "Evaluation answer:",
    "Application answer:",
    "Chapter evidence:",
    "Evidence check:",
    "Trace *",
    "Give a precise account of *",
    "Write the model for *",
    "Turn *",
    "Assess *",
    "Use the chapter principle with *",
    "Reference point: \\cref",
)


GENERIC_COMPANION_SOURCE_PHRASES = (
    "The computational concepts discussed in this chapter are implemented",
    "Companion source note:",
    "*Module:",
    "*Figure:",
    "*Diagram:",
    "*Cross-references:",
)


COPYEDIT_ARTIFACT_EXAMPLES = {
    "copyedit-uppercase-most": "T-MOST should be T-ALL.",
    "copyedit-not-most": "Not most screen readers behave the same way.",
    "copyedit-most-involve": "Wikipedia most involve layers of interpretation.",
    "copyedit-most-the": "Photosynthesis produces most the oxygen in the atmosphere.",
    "copyedit-most-four": "The mechanism engages most four pathways.",
    "copyedit-virtually-most": "Virtually most secreted proteins are glycosylated.",
    "copyedit-almost-most": "Almost most lactic acid is ionised.",
    "copyedit-quantified-of-most": "Approximately 80% of most land plant species form mycorrhizae.",
    "copyedit-of-most-known-recorded": "The island holds 5% of most known species.",
    "copyedit-of-most-time": "It became one of the highest-selling drugs of most time.",
    "copyedit-most-bear": "Major crop genomes most bear paleopolyploid signatures.",
    "copyedit-sum-of-most": "The sum of most flux coefficients equals 1.",
    "copyedit-space-of-most": "Phase space is the space of most possible states.",
    "copyedit-set-of-most": "The gene pool is the complete set of most alleles.",
    "copyedit-partition-of-most": "The blanket defines a partition of most states.",
    "copyedit-primarily-quantifier": "The sample contains primarily ~20% of the signal.",
    "copyedit-primarily-a-has": "Influenza primarily a has wide animal host range.",
    "copyedit-the-primarily": "This is the primarily open system.",
    "copyedit-primarily-partially": "Would the inhibitor work fully, or primarily partially?",
    "copyedit-primarily-by-approx": "The value changes primarily by ~sigma.",
    "copyedit-primarily-as-good": "The model is primarily as good as its inputs.",
    "copyedit-need-primarily-open": "The channels need primarily open briefly.",
    "copyedit-hyphen-primarily": "This is a hospital-primarily issue.",
}


def test_textbook_quality_audit_has_no_blocking_findings() -> None:
    findings = audit.collect_findings()
    errors = [finding.format() for finding in findings if finding.severity == "error"]
    assert not errors


def test_quality_audit_flags_bare_structural_references() -> None:
    examples = (
        "See Unit I for the chemistry background.",
        "Units VII–IX extend this logic.",
        "Review Appendix C before solving the model.",
        "Figure FM-1 shows the route.",
        "Chapter numbers follow the PDF table of contents.",
    )
    for example in examples:
        assert audit.HARDCODED_STRUCTURAL_REF.search(example), example


def test_absolute_language_advisories_are_triaged_in_ledger() -> None:
    findings = audit.collect_findings()
    absolute_findings = [finding for finding in findings if finding.code == "absolute-language-review"]
    ledger, ledger_errors = audit.load_quality_advisory_ledger()
    missing = [
        audit.quality_advisory_id(finding)
        for finding in absolute_findings
        if audit.quality_advisory_id(finding) not in ledger
    ]
    unresolved = [
        audit.quality_advisory_id(finding)
        for finding in absolute_findings
        if ledger.get(audit.quality_advisory_id(finding), {}).get("classification")
        != "valid_scientific_absolute"
    ]
    assert not [finding.format() for finding in ledger_errors]
    assert not missing
    assert not unresolved


def test_quality_advisory_ledger_blocks_untriaged_and_unresolved(
    tmp_path: Path,
    monkeypatch: Any,
) -> None:
    ledger_path = tmp_path / "quality_advisories.yaml"
    monkeypatch.setattr(audit, "QUALITY_ADVISORIES", ledger_path)
    finding = audit.Finding(
        "advisory",
        "absolute-language-review",
        MANUSCRIPT / "unit_0" / "systems_science.md",
        1,
        "All model states are included here.",
    )

    findings = [finding]
    audit.audit_quality_advisory_ledger(findings)
    assert any(result.code == "missing-quality-advisory-ledger" for result in findings)

    advisory_id = audit.quality_advisory_id(finding)
    ledger_path.write_text(
        "\n".join(
            [
                "version: 1",
                "checked_as_of: '2026-05-20'",
                "absolute_language:",
                f"- advisory_id: {advisory_id}",
                "  source_path: manuscript/unit_0/systems_science.md",
                "  line: 1",
                "  classification: needs_qualifier",
                "  excerpt: All model states are included here.",
            ]
        ),
        encoding="utf-8",
    )
    findings = [finding]
    audit.audit_quality_advisory_ledger(findings)
    assert any(result.code == "unresolved-triaged-absolute-language" for result in findings)

    ledger_path.write_text(
        ledger_path.read_text(encoding="utf-8").replace("needs_qualifier", "valid_scientific_absolute"),
        encoding="utf-8",
    )
    findings = [finding]
    audit.audit_quality_advisory_ledger(findings)
    assert not [result.format() for result in findings if result.severity == "error"]


def test_question_banks_have_exactly_thirty_questions_and_solutions() -> None:
    offenders: list[str] = []
    for path in sorted((MANUSCRIPT / "questions").rglob("questions_*.md")):
        text = path.read_text(encoding="utf-8")
        q_numbers = [int(match.group(1)) for match in re.finditer(r"^(\d{1,2})\.\s+", text, re.MULTILINE)]
        solution_count = len(re.findall(r"<!-- SOLUTION\s*\n", text))
        if q_numbers != list(range(1, 31)):
            offenders.append(f"{path.relative_to(MANUSCRIPT)} questions={q_numbers}")
        if solution_count != 30:
            offenders.append(f"{path.relative_to(MANUSCRIPT)} solutions={solution_count}")
    assert not offenders


def test_question_solution_blocks_have_no_generic_answer_signatures() -> None:
    offenders: list[str] = []
    for path in sorted((MANUSCRIPT / "questions").rglob("questions_*.md")):
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for phrase in GENERIC_ANSWER_PHRASES:
                if phrase in line:
                    offenders.append(f"{path.relative_to(MANUSCRIPT)}:{line_no}: {phrase}")
    assert not offenders


def test_chapter_companion_source_modules_are_specific_and_canonical() -> None:
    offenders: list[str] = []
    for path in sorted(MANUSCRIPT.glob("unit_*/*.md")):
        if path.name in {"AGENTS.md", "README.md", "unit_intro.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if len(re.findall(r"^#{2,3}\s+Companion Source Module$", text, re.MULTILINE)) != 1:
            offenders.append(f"{path.relative_to(MANUSCRIPT)} has non-canonical companion source count")
        for phrase in GENERIC_COMPANION_SOURCE_PHRASES:
            if phrase in text:
                offenders.append(f"{path.relative_to(MANUSCRIPT)} contains stale companion phrase {phrase!r}")
    assert not offenders


def test_copyedit_artifact_patterns_are_enforced(tmp_path: Path) -> None:
    path = tmp_path / "copyedit.md"
    path.write_text("\n".join(COPYEDIT_ARTIFACT_EXAMPLES.values()), encoding="utf-8")
    findings: list[Any] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        audit.add_line_findings(
            findings,
            path=path,
            line_no=line_no,
            line=line,
            patterns=audit.COPYEDIT_ARTIFACT_PATTERNS,
        )
    assert {finding.code for finding in findings} == set(COPYEDIT_ARTIFACT_EXAMPLES)


def test_current_science_claims_have_reviewed_citations() -> None:
    required_pairs = {
        "who2025tb": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "who2025malaria": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "unaids2025factsheet": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "cdc2025lenacapavirprep": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "who2025spatialemanators": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "longcovid2026mechanisms": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "cdc2026candidaauris": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "cdc2024candidaauristreatment": MANUSCRIPT / "unit_VII" / "infectious_disease.md",
        "murray2022amr": MANUSCRIPT / "unit_VII" / "bacteria_archaea_viruses.md",
        "cdc2025antibioticuse": MANUSCRIPT / "unit_VII" / "bacteria_archaea_viruses.md",
        "velankar2026alphafolddb2025": MANUSCRIPT / "unit_I" / "macromolecules.md",
        "emblebi2026alphafoldcomplexes": MANUSCRIPT / "unit_I" / "macromolecules.md",
        "fda2024casgevythalassemia": MANUSCRIPT / "unit_IV" / "mutations_and_genomics.md",
        "chalumeau2025primeediting": MANUSCRIPT / "unit_IV" / "mutations_and_genomics.md",
        "wwf2024livingplanet": MANUSCRIPT / "unit_X" / "biomes_and_conservation.md",
        "strader2022coralheat": MANUSCRIPT / "unit_X" / "biomes_and_conservation.md",
        "fao2025sofi": MANUSCRIPT / "unit_X" / "biomes_and_conservation.md",
        "richardson2023earth": MANUSCRIPT / "unit_X" / "ecosystem_ecology.md",
        "un2024population": MANUSCRIPT / "unit_X" / "population_ecology.md",
        "lai2024gppcarbonylsulfide": MANUSCRIPT / "unit_III" / "photosynthesis.md",
        "feldman2024rainfallvariability": MANUSCRIPT / "unit_X" / "ecosystem_ecology.md",
        "huang2024guardcells": MANUSCRIPT / "unit_VIII" / "plant_responses.md",
        "zheng2025tmem63channelopathies": MANUSCRIPT / "unit_II" / "membrane_transport.md",
    }
    missing = [
        f"{path.relative_to(MANUSCRIPT)} missing {key}"
        for key, path in required_pairs.items()
        if key not in path.read_text(encoding="utf-8")
    ]
    assert not missing


def test_known_stale_population_and_conservation_counts_are_absent() -> None:
    stale = (
        "10.4 billion around 2080-2100 (UN 2022 revision)",
        "44,016 classified as threatened",
        "IUCN Red List Categories (2024 Update)",
        "Living Planet Report (2022)",
        "69% average decline",
        "feeding a projected 10 billion people by 2050",
        "all β-lactams",
        "universal energy currency",
    )
    offenders: list[str] = []
    for path in sorted(MANUSCRIPT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for phrase in stale:
            if phrase in text:
                offenders.append(f"{path.relative_to(MANUSCRIPT)} contains {phrase!r}")
    assert not offenders


def test_student_facing_prose_has_no_authoring_source_boilerplate() -> None:
    offenders: list[str] = []
    phrase = "Recent and numeric claims should remain tied to authoritative sources"
    for path in sorted(MANUSCRIPT.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if phrase in text:
            offenders.append(str(path.relative_to(MANUSCRIPT)))
    assert not offenders


def test_embedded_enrichment_surfaces_are_present() -> None:
    assert (PROJECT / "docs" / "embedded_enrichment_audit_matrix.md").is_file()
    missing: list[str] = []
    for path in sorted(MANUSCRIPT.glob("unit_*/*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == "unit_intro.md":
            expected = "## Current Evidence Thread"
        else:
            expected = "## Current Evidence and Frontier Biology"
        if expected not in text:
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing {expected}")
        if path.name != "unit_intro.md" and "- **What to cite:**" not in text:
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing source-practice scholarship bullet")
    for path in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        if "## Paper-Based Evidence Upgrade" not in path.read_text(encoding="utf-8"):
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing Paper-Based Evidence Upgrade")
    assert not missing
