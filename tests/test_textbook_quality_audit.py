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

FIGURE_METADATA_ARTIFACT_EXAMPLES = {
    "stale-mermaid-title-prefix": "*Flowchart for Glycolysis: glucose and pyruvate form the diagram.*",
    "generic-figure-caption": "*Glucose, ATP, and pyruvate form the diagram's primary path or branches.*",
    "stale-sequence-caption": "*Sequence diagram for electron transport showing ordered interaction among NADH and oxygen.*",
}

HEADING_ARTIFACT_EXAMPLES = {
    "generic-worked-example-heading": "## Worked Example",
    "hardcoded-worked-example-heading": "## Worked Example: 28.Z — Bohr Effect",
    "inflated-comprehensive-heading": "### Complement System — Comprehensive Overview",
    "ascii-dash-heading": "### Part 2: Computational Biology Exercise - Data Analysis with Python",
    "uncommon-homeostasis-heading": "### Homoeostasis vs. Allostasis",
    "manual-subsection-prefix-heading": "## 7B Nutrient Cycling Models",
    "underspecified-standalone-heading": "### Overview",
}

FRONTIER_BOILERPLATE_EXAMPLES = {
    "frontier-boilerplate-model-claim": "Treat every model as a claim about mechanism: define the boundary.",
    "frontier-boilerplate-ai-model": "Use AI biomolecular models as hypothesis generators: compare confidence.",
    "frontier-boilerplate-cell-scale": "Ask what measurement scale is being claimed: nanometre structure.",
    "frontier-boilerplate-metabolic-flux": "A strong metabolic explanation names the flux and limiting step.",
    "frontier-boilerplate-genomic-reference": "When a genomic claim depends on a reference, ask whether short reads matter.",
    "frontier-boilerplate-evolution-alternatives": "Distinguish adaptation from drift, phylogenetic signal from convergence.",
    "frontier-boilerplate-pathogen-amr": "For AMR and pathogen claims, name the organism-resistance pair.",
    "frontier-boilerplate-plant-generic": "A strong plant explanation names the tissue, signal, and driver.",
    "frontier-boilerplate-physiology-generic": "Interpret physiological data by separating baseline variation.",
    "frontier-boilerplate-biodiversity-generic": "Use biodiversity metrics carefully: population indices answer questions.",
    "frontier-source-model-validation": "Use model-validation sources when available, and state which observation would falsify the model.",
    "frontier-source-structure-generic": "For structure and interaction claims, cite experimental structures when available and treat AlphaFold predictions as hypotheses.",
    "frontier-source-cell-generic": "For cell-state claims, distinguish microscopy, live-cell perturbation, and sequencing.",
    "frontier-source-metabolism-generic": "For metabolic claims, keep the organism, compartment, and measurement method visible.",
    "frontier-source-genetics-generic": "For inheritance and population claims, separate the model assumptions from sampling.",
    "frontier-source-evolution-generic": "For evolutionary claims, prefer evidence that compares alternatives.",
    "frontier-source-pathogen-generic": "For pathogen, AMR, and intervention claims, tie statements to surveillance evidence.",
    "frontier-source-plant-generic": "For plant-stress and crop claims, name the tissue and field context.",
    "frontier-source-physiology-generic": "For physiology claims, cite the measurement context and distinguish baseline variation.",
    "frontier-source-conservation-generic": "For conservation claims, cite assessment sources and state whether the evidence is an index.",
}


COPYEDIT_ARTIFACT_EXAMPLES = {
    "copyedit-uppercase-most": "T-MOST should be T-ALL.",
    "copyedit-not-most": "Not most screen readers behave the same way.",
    "copyedit-most-involve": "Wikipedia most involve layers of interpretation.",
    "copyedit-most-the": "Photosynthesis produces most the oxygen in the atmosphere.",
    "copyedit-most-four": "The mechanism engages most four pathways.",
    "copyedit-most-number": "Describe most 10 steps in glycolysis.",
    "copyedit-nearly-most": "This applies to nearly most mammalian cells.",
    "copyedit-primarily-then": "Primarily then did Darwin understand the specimens.",
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


def test_quality_audit_flags_plural_rendered_reference_lists() -> None:
    examples = (
        "Sections 2 and 5 introduced the dynamics.",
        "Figures 3.1 and 3.2 compare the phase portraits.",
        "Equations 4.7-4.9 define the model.",
        "Tables 1 and 2 summarize the data.",
    )
    for example in examples:
        assert audit.HARDCODED_REF.search(example), example


def test_quality_audit_flags_raw_latex_reference_commands() -> None:
    examples = (
        "Apply the Hardy-Weinberg model in Equation~\\eqref{eq:population_genetics_1}.",
        "Apply the Hardy-Weinberg model in Equation \\eqref{eq:population_genetics_1}.",
        "Compare the trends in Figure~\\ref{fig:unit_I_michaelis_menten}.",
        "Compare the trends in Figure \\ref{fig:unit_I_michaelis_menten}.",
        "Review Section~\\ref{sec:unit_I_water_and_life}.",
        "Review Section \\ref{sec:unit_I_water_and_life}.",
    )
    for example in examples:
        assert audit.HARDCODED_REF.search(example), example


def test_quality_audit_flags_bare_raw_latex_reference_commands() -> None:
    examples = (
        "Apply the Hardy-Weinberg model in \\eqref{eq:population_genetics_1}.",
        "Compare the trends in \\ref{fig:unit_I_michaelis_menten}.",
        "Review \\autoref{sec:unit_I_water_and_life}.",
    )
    for example in examples:
        assert audit.RAW_LATEX_RENDERED_REF.search(example), example


def test_quality_audit_flags_dollar_equations_with_tag_and_label() -> None:
    line = r"$$ p^2 + 2pq + q^2 = 1 \tag{18.1} \label{eq:population_genetics_1}$$"
    assert audit.DOLLAR_TAG_LABEL_RE.search(line)


def test_quality_audit_flags_manual_equation_tags() -> None:
    examples = (
        r"$$ p^2 + 2pq + q^2 = 1 \tag{18.1} $$",
        r"\begin{equation} x = y \tag{2.4} \label{eq:manual} \end{equation}",
    )
    for example in examples:
        assert audit.LATEX_EQUATION_TAG_RE.search(example), example


def test_quality_audit_flags_inline_circ_prime_double_superscript_risk() -> None:
    unsafe = r"Net energy is $\Delta G^\circ' = +104$ kJ/mol."
    safe = r"Net energy is $\Delta G^{\circ\prime} = +104$ kJ/mol."

    assert audit.INLINE_CIRC_PRIME_RE.search(unsafe)
    assert audit.INLINE_CIRC_PRIME_RE.search(safe) is None


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
    monkeypatch.setattr("biology.quality.paths.QUALITY_ADVISORIES", ledger_path)
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
    for path, title in sorted(audit.engine.configured_chapter_title_by_path().items()):
        text = path.read_text(encoding="utf-8")
        expected = f"## Companion Source Module: {title}"
        if len(re.findall(rf"^{re.escape(expected)}$", text, re.MULTILINE)) != 1:
            offenders.append(
                f"{path.relative_to(MANUSCRIPT)} has non-canonical companion source count"
            )
        for phrase in GENERIC_COMPANION_SOURCE_PHRASES:
            if phrase in text:
                offenders.append(f"{path.relative_to(MANUSCRIPT)} contains stale companion phrase {phrase!r}")
    assert not offenders


def test_chapter_source_section_headings_are_chapter_specific() -> None:
    source_sections = (
        "Current Evidence and Frontier Biology",
        "Further Reading and Source Notes",
        "Companion Source Module",
    )
    bare_heading = re.compile(
        r"^## (?:Current Evidence and Frontier Biology|Further Reading and Source Notes|Companion Source Module)$",
        flags=re.MULTILINE,
    )
    offenders: list[str] = []
    for path, title in sorted(audit.engine.configured_chapter_title_by_path().items()):
        text = path.read_text(encoding="utf-8")
        for section in source_sections:
            expected = f"## {section}: {title}"
            if not re.search(rf"^{re.escape(expected)}$", text, flags=re.MULTILINE):
                offenders.append(f"{path.relative_to(MANUSCRIPT)} missing {expected!r}")
        for match in bare_heading.finditer(text):
            offenders.append(f"{path.relative_to(MANUSCRIPT)} has bare source heading {match.group(0)!r}")
    assert not offenders


def test_core_chapter_structure_patterns_accept_existing_chapter_styles() -> None:
    examples = {
        "opening_heading": ("## Opening Vignette: A Field Case", audit.OPENING_VIGNETTE_RE),
        "opening_blockquote": ("> **Opening Vignette: The Protein That Won Two Nobel Prizes**", audit.OPENING_VIGNETTE_RE),
        "summary_plain": ("## Summary", audit.SUMMARY_HEADING_RE),
        "summary_attr": ("## Summary {.unnumbered}", audit.SUMMARY_HEADING_RE),
        "concept_numbered": ("> **Concept Check 1:** Explain the boundary.", audit.CONCEPT_CHECK_RE),
        "concept_lettered": ("> **Concept Check 1a:** Explain the boundary.", audit.CONCEPT_CHECK_RE),
        "concept_named": ("> **Concept Check (Analysis):** Explain the boundary.", audit.CONCEPT_CHECK_RE),
        "concept_plain": ("> **Concept Check:** Explain the boundary.", audit.CONCEPT_CHECK_RE),
        "concept_unquoted": ("**Concept Check 1:** Explain the boundary.", audit.CONCEPT_CHECK_RE),
    }
    for label, (text, pattern) in examples.items():
        assert pattern.search(text), label


def test_core_chapter_structure_audit_is_config_driven(
    tmp_path: Path,
    monkeypatch: Any,
) -> None:
    manuscript = tmp_path / "manuscript"
    chapter_dir = manuscript / "unit_0"
    chapter_dir.mkdir(parents=True)
    config = "\n".join(
        [
            "units:",
            "  - id: unit_0",
            "    directory: unit_0",
            "    chapters:",
            "      - file: incomplete.md",
            "        title: Incomplete",
            "      - file: disabled.md",
            "        title: Disabled",
            "        enabled: false",
        ]
    )
    (manuscript / "config.yaml").write_text(config, encoding="utf-8")
    incomplete = chapter_dir / "incomplete.md"
    incomplete.write_text(
        "# Incomplete\n\n\\label{sec:unit_0_incomplete}\n\n## Learning Objectives\n",
        encoding="utf-8",
    )
    (chapter_dir / "disabled.md").write_text("", encoding="utf-8")

    monkeypatch.setattr("biology.quality.paths.MANUSCRIPT", manuscript)
    monkeypatch.setattr("biology.maintenance.manuscript_walker.MANUSCRIPT", manuscript)
    findings: list[Any] = []
    audit.audit_core_chapter_structure(findings)

    assert [path.name for path in audit.configured_chapter_files()] == ["incomplete.md"]
    assert {finding.code for finding in findings} == {
        "missing-opening-vignette",
        "missing-summary-section",
        "missing-concept-check",
    }
    assert {finding.path for finding in findings} == {incomplete}


def test_configured_manuscript_surfaces_cover_whole_textbook() -> None:
    surfaces = audit.configured_manuscript_surfaces()
    counts: dict[str, int] = {}
    for surface in surfaces:
        counts[surface.category] = counts.get(surface.category, 0) + 1

    assert counts == audit.EXPECTED_CONFIGURED_SURFACE_COUNTS
    assert len({surface.path for surface in surfaces}) == 152
    assert not [surface.path for surface in surfaces if not surface.path.is_file()]


def test_configured_surface_audit_flags_missing_and_count_drift(
    tmp_path: Path,
    monkeypatch: Any,
) -> None:
    manuscript = tmp_path / "manuscript"
    (manuscript / "unit_0").mkdir(parents=True)
    (manuscript / "front_matter.md").write_text("# Front\n", encoding="utf-8")
    (manuscript / "unit_0" / "unit_intro.md").write_text("# Unit\n", encoding="utf-8")
    (manuscript / "unit_0" / "chapter.md").write_text("# Chapter\n", encoding="utf-8")
    (manuscript / "config.yaml").write_text(
        "\n".join(
            [
                "front_matter:",
                "  files:",
                "    - file: front_matter.md",
                "units:",
                "  - id: unit_0",
                "    directory: unit_0",
                "    chapters:",
                "      - file: chapter.md",
                "appendices:",
                "  labs: []",
                "  questions: []",
                "  reference:",
                "    - file: missing_appendix.md",
                "      title: Missing",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr("biology.quality.paths.MANUSCRIPT", manuscript)
    monkeypatch.setattr("biology.maintenance.manuscript_walker.MANUSCRIPT", manuscript)
    findings: list[Any] = []
    audit.audit_configured_surfaces(findings)

    codes = {finding.code for finding in findings}
    assert "missing-configured-surface" in codes
    assert "configured-surface-count-drift" in codes


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


def test_figure_metadata_artifact_patterns_are_enforced(tmp_path: Path) -> None:
    path = tmp_path / "figure_metadata.md"
    path.write_text("\n".join(FIGURE_METADATA_ARTIFACT_EXAMPLES.values()), encoding="utf-8")
    findings: list[Any] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        audit.add_line_findings(
            findings,
            path=path,
            line_no=line_no,
            line=line,
            patterns=audit.FIGURE_METADATA_ARTIFACT_PATTERNS,
        )
    assert {finding.code for finding in findings} == set(FIGURE_METADATA_ARTIFACT_EXAMPLES)


def test_student_facing_figure_metadata_has_no_generated_caption_fragments() -> None:
    offenders: list[str] = []
    for path in sorted(MANUSCRIPT.rglob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            findings: list[Any] = []
            audit.add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=audit.FIGURE_METADATA_ARTIFACT_PATTERNS,
            )
            offenders.extend(
                f"{path.relative_to(MANUSCRIPT)}:{line_no}: {finding.code}"
                for finding in findings
            )
    assert not offenders


def test_heading_artifact_patterns_are_enforced(tmp_path: Path) -> None:
    path = tmp_path / "headings.md"
    path.write_text("\n".join(HEADING_ARTIFACT_EXAMPLES.values()), encoding="utf-8")
    findings: list[Any] = []
    for line_no, line in audit.iter_markdown_headings(path):
        audit.add_line_findings(
            findings,
            path=path,
            line_no=line_no,
            line=line,
            patterns=audit.HEADING_ARTIFACT_PATTERNS,
        )
    assert {finding.code for finding in findings} == set(HEADING_ARTIFACT_EXAMPLES)


def test_student_facing_section_titles_have_no_confirmed_artifacts() -> None:
    offenders: list[str] = []
    for surface in audit.configured_manuscript_surfaces():
        path = surface.path
        if not path.exists():
            continue
        generated_lines = audit._generated_block_line_numbers(path)
        for line_no, line in audit.iter_markdown_headings(path):
            if line_no in generated_lines:
                continue
            findings: list[Any] = []
            audit.add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=audit.HEADING_ARTIFACT_PATTERNS,
            )
            offenders.extend(
                f"{path.relative_to(MANUSCRIPT)}:{line_no}: {finding.code}"
                for finding in findings
            )
    assert not offenders


def test_frontier_boilerplate_patterns_are_enforced(tmp_path: Path) -> None:
    path = tmp_path / "frontier.md"
    path.write_text("\n".join(FRONTIER_BOILERPLATE_EXAMPLES.values()), encoding="utf-8")
    findings: list[Any] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        audit.add_line_findings(
            findings,
            path=path,
            line_no=line_no,
            line=line,
            patterns=audit.FRONTIER_BOILERPLATE_PATTERNS,
        )
    assert {finding.code for finding in findings} == set(FRONTIER_BOILERPLATE_EXAMPLES)


def test_student_facing_frontier_boxes_do_not_use_confirmed_boilerplate() -> None:
    offenders: list[str] = []
    for path in audit.configured_chapter_files():
        for line_no, line in audit.iter_prose_lines(path):
            findings: list[Any] = []
            audit.add_line_findings(
                findings,
                path=path,
                line_no=line_no,
                line=line,
                patterns=audit.FRONTIER_BOILERPLATE_PATTERNS,
            )
            offenders.extend(
                f"{path.relative_to(MANUSCRIPT)}:{line_no}: {finding.code}"
                for finding in findings
            )
    assert not offenders


def test_current_science_claims_have_reviewed_citations() -> None:
    required_pairs = {
        "who2025tb": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "who2025malaria": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "unaids2025factsheet": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "cdc2025lenacapavirprep": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "who2025spatialemanators": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "longcovid2026mechanisms": MANUSCRIPT / "unit_VII" / "host_immunity_and_vaccines.md",
        "cdc2026candidaauris": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "cdc2024candidaauristreatment": MANUSCRIPT / "unit_VII" / "antimicrobial_resistance_and_epidemiology.md",
        "murray2022amr": MANUSCRIPT / "unit_VII" / "bacteria_archaea_viruses.md",
        "cdc2025antibioticuse": MANUSCRIPT / "unit_VII" / "bacteria_archaea_viruses.md",
        "velankar2026alphafolddb2025": MANUSCRIPT / "unit_I" / "macromolecules.md",
        "emblebi2026alphafoldcomplexes": MANUSCRIPT / "unit_I" / "macromolecules.md",
        "fda2024casgevythalassemia": MANUSCRIPT / "unit_IV" / "mutations_and_genomics.md",
        "chalumeau2025primeediting": MANUSCRIPT / "unit_IV" / "mutations_and_genomics.md",
        "rigden2026nardatabase": MANUSCRIPT / "unit_IV" / "gene_expression.md",
        "rnacentral2026": MANUSCRIPT / "unit_IV" / "gene_expression.md",
        "parks2026gtdb": MANUSCRIPT / "unit_VII" / "microbial_ecology.md",
        "schreiber2024plantpangenomes": MANUSCRIPT / "unit_VIII" / "plant_reproduction.md",
        "yao2023mousebrainatlas": MANUSCRIPT / "unit_IX" / "nervous_system.md",
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
    chapter_titles = audit.engine.configured_chapter_title_by_path()
    for path in sorted(MANUSCRIPT.glob("unit_*/*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if path.name == "unit_intro.md":
            expected = "## Current Evidence Thread"
        else:
            expected = f"## Current Evidence and Frontier Biology: {chapter_titles[path]}"
        if expected not in text:
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing {expected}")
        if path.name != "unit_intro.md" and "- **What to cite:**" not in text:
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing source-practice scholarship bullet")
    for path in sorted((MANUSCRIPT / "labs").rglob("lab_*.md")):
        if "## Paper-Based Evidence Upgrade" not in path.read_text(encoding="utf-8"):
            missing.append(f"{path.relative_to(MANUSCRIPT)} missing Paper-Based Evidence Upgrade")
    assert not missing
