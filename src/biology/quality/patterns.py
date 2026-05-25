"""Regex and pattern catalogs for textbook quality auditing."""

from __future__ import annotations

import re

ALLOWED_ADVISORY_CLASSIFICATIONS = {
    "valid_scientific_absolute",
    "needs_qualifier",
    "copyedit_artifact",
}

EXPECTED_CONFIGURED_SURFACE_COUNTS = {
    "front_matter": 2,
    "unit_intro": 11,
    "chapter": 44,
    "lab": 44,
    "question": 44,
    "appendix": 7,
}


QUESTION_GENERIC_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("generic-answer-define", re.compile(r"Give the canonical definition of")),
    ("generic-answer-mechanism", re.compile(r"Build a mechanistic answer")),
    ("generic-answer-numeric", re.compile(r"Numerical problem on")),
    ("generic-answer-position", re.compile(r"Take a position on \*")),
    ("generic-answer-design", re.compile(r"Propose an experimental or engineering response")),
    ("generic-answer-rubric", re.compile(r"Rubric for \*")),
    ("generic-answer-players", re.compile(r"name the relevant players")),
    ("generic-answer-scale-setting", re.compile(r"scale-setting detail")),
    ("generic-answer-thin-evidence", re.compile(r"state the judgment, cite two lines of evidence")),
    ("generic-answer-thin-numeric", re.compile(r"identify the governing equation or ratio")),
    ("generic-answer-thin-design", re.compile(r"specify the manipulated variable")),
    ("generic-answer-key-prefix", re.compile(r"Answer key for \*")),
    ("generic-answer-define-precisely", re.compile(r"define the concept precisely")),
    ("generic-answer-scale", re.compile(r"place it at the correct biological scale")),
    ("generic-answer-causal-sequence", re.compile(r"trace the causal sequence")),
    ("generic-answer-equation-ratio", re.compile(r"choose the relevant equation, ratio, or probability model")),
    ("generic-answer-hypothesis-variable", re.compile(r"state the hypothesis, variable being changed")),
    ("generic-answer-judgment", re.compile(r"make a justified judgment")),
    ("generic-answer-vocab-pitfall", re.compile(r"giving a vocabulary-only answer")),
    ("generic-answer-name-term", re.compile(r"Name the term in ")),
    ("generic-answer-evidence-anchor", re.compile(r"Evidence anchor:")),
    ("generic-answer-credit-requires", re.compile(r"Credit requires an explicit mechanism")),
    ("generic-answer-prompt-linked", re.compile(r"prompt-linked evidence")),
    ("generic-answer-core-response", re.compile(r"Core response for \*")),
    ("generic-answer-expected-answer", re.compile(r"Expected answer for \*")),
    ("generic-answer-prompt-cues", re.compile(r"Prompt cues to cover:")),
    ("generic-answer-source-standard", re.compile(r"Source standard:")),
    ("generic-answer-common-pitfall", re.compile(r"Common pitfall:")),
    ("generic-answer-chapter-lens", re.compile(r"Chapter lens:")),
    ("generic-answer-governing-equation", re.compile(r"set up the governing equation")),
    ("generic-answer-defensible-judgment", re.compile(r"state a defensible judgment")),
    ("generic-answer-two-observations", re.compile(r"support it with two chapter-specific observations")),
    ("generic-answer-every-clause", re.compile(r"Answer every requested clause")),
    ("generic-answer-ground-cref", re.compile(r"Ground the answer in \\cref")),
    ("generic-answer-use-cref", re.compile(r"Use \\cref")),
    ("generic-answer-extend-cref", re.compile(r"Extend \\cref")),
    ("generic-answer-biological-players", re.compile(r"Name the biological players")),
    ("generic-answer-one-limitation", re.compile(r"name one limitation or counterexample")),
    ("generic-answer-boundary-condition", re.compile(r"boundary condition that prevents overgeneralising")),
    ("generic-answer-carry-values", re.compile(r"Carry through these values:")),
    ("generic-answer-named-items", re.compile(r"Use these named items explicitly:")),
    ("generic-answer-current-define", re.compile(r"Define \*")),
    ("generic-answer-current-compare", re.compile(r"Compare \*")),
    ("generic-answer-current-solve", re.compile(r"Solve \*")),
    ("generic-answer-current-explain", re.compile(r"Explain \*")),
    ("generic-answer-current-design", re.compile(r"Design the test for \*")),
    ("generic-answer-current-evaluate", re.compile(r"Evaluate \*")),
    ("generic-answer-current-apply", re.compile(r"Apply the chapter principle to \*")),
    ("generic-answer-current-required-clauses", re.compile(r"Required clauses:")),
    ("generic-answer-current-values", re.compile(r"Use the stated values explicitly:")),
    ("generic-answer-current-named-evidence", re.compile(r"Named evidence to include:")),
    ("generic-answer-current-first-noun", re.compile(r"Do not stop at the first noun phrase")),
    ("generic-answer-current-anchor", re.compile(r"Anchor the response to \\cref")),
    ("generic-answer-complete-response", re.compile(r"A complete response should")),
    ("generic-answer-expected-reasoning", re.compile(r"Expected reasoning:")),
    ("generic-answer-scoring-focus", re.compile(r"Scoring focus:")),
    ("generic-answer-key-label", re.compile(r"Key answer:")),
    ("generic-answer-comparison-label", re.compile(r"Comparison answer:")),
    ("generic-answer-calculation-label", re.compile(r"Calculation answer:")),
    ("generic-answer-mechanistic-label", re.compile(r"Mechanistic answer:")),
    ("generic-answer-design-label", re.compile(r"Design answer:")),
    ("generic-answer-evaluation-label", re.compile(r"Evaluation answer:")),
    ("generic-answer-application-label", re.compile(r"Application answer:")),
    ("generic-answer-chapter-evidence-label", re.compile(r"Chapter evidence:")),
    ("generic-answer-evidence-check-label", re.compile(r"Evidence check:")),
    ("generic-answer-trace-star", re.compile(r"Trace \*")),
    ("generic-answer-precise-account", re.compile(r"Give a precise account of \*")),
    ("generic-answer-write-model", re.compile(r"Write the model for \*")),
    ("generic-answer-turn-star", re.compile(r"Turn \*")),
    ("generic-answer-assess-star", re.compile(r"Assess \*")),
    ("generic-answer-use-principle", re.compile(r"Use the chapter principle with \*")),
    ("generic-answer-reference-point", re.compile(r"Reference point: \\cref")),
    ("generic-answer-v3-mechanism", re.compile(r"should first state the chapter.s concrete mechanism")),
    ("generic-answer-v3-causal-chain", re.compile(r"should give the causal chain")),
    ("generic-answer-v3-shared-principle", re.compile(r"should name the shared biological principle")),
    ("generic-answer-v3-model-substitute", re.compile(r"should name the model, substitute the stated values")),
    ("generic-answer-v3-scholarship-standard", re.compile(r"Scholarship standard:")),
    ("generic-answer-v3-pitfall", re.compile(r"Pitfall to avoid:")),
    ("generic-answer-v3-chapter-anchor", re.compile(r"Chapter anchor:")),
    (
        "generic-answer-v3-same-scale",
        re.compile(r"Then give one same-scale example or boundary condition using this evidence"),
    ),
    ("generic-answer-v3-decisive-contrast", re.compile(r"The decisive contrast or boundary condition is")),
    ("generic-answer-v3-interpret-outcome", re.compile(r"Interpret the outcome using:")),
    ("mismatched-popgen-tail", re.compile(r"propose one comparative or population-genomic test")),
    ("mismatched-clinical-tail", re.compile(r"propose one clinical intervention")),
    ("mismatched-molecular-tail", re.compile(r"propose one molecular intervention")),
)

BROKEN_CREF_RE = re.compile(r"(?<!\\)\bcref\{")
BROKEN_NAMEREF_RE = re.compile(r"(?<!\\)\bnameref\{")
BROKEN_NAMEREF_TAIL_RE = re.compile(r"(?<![A-Za-z\\])ameref\{")
COLLAPSED_UNIT_CREF_RE = re.compile(r"\\cref\{sec:unit[IVX]+[a-z]")


STALE_CLAIM_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("stale-who-2022", re.compile(r"\bWHO 2022\b")),
    ("stale-tb-burden", re.compile(r"10\.6 million new cases and 1\.3 million deaths")),
    ("stale-malaria-burden", re.compile(r"247 million cases and 619,000 deaths")),
    ("unsupported-antibiotic-void", re.compile(r"no new antibiotic classes have been approved since 2003")),
    ("overfixed-livestock-share", re.compile(r"70% of antibiotics sold in the U\.S\. are used in livestock")),
    ("overfixed-outpatient-share", re.compile(r"estimated 30% of outpatient prescriptions are unnecessary")),
    ("stale-un-population-2022", re.compile(r"10\.4 billion around 2080-2100 \(UN 2022 revision\)")),
    ("stale-iucn-2024-count", re.compile(r"44,016 classified as threatened")),
    ("stale-living-planet-2022", re.compile(r"Living Planet Report \(2022\)")),
    ("stale-living-planet-69", re.compile(r"69% average decline")),
    ("stale-food-10b-2050", re.compile(r"feeding a projected 10 billion people by 2050")),
    ("overbroad-beta-lactam", re.compile(r"all β-lactams", flags=re.IGNORECASE)),
    ("overbroad-atp-currency", re.compile(r"universal energy currency", flags=re.IGNORECASE)),
)


BANNED_REQUIRED_LAB_TERMS = re.compile(
    r"\b("
    r"beakers?|pipettes?|reagents?|Benedict'?s|Biuret|Sudan|HCl|NaOH|"
    r"hot water bath|compound microscope|dissecting microscope|glass slides?|"
    r"coverslips?|wet mounts?|cheek swabs?|agar plates?|LB agar|Mueller-Hinton|"
    r"swabbed|duckweed cultures?|pollen germination medium|"
    r"fresh flowers?|dissect(?:ion|ed|ing)|sharp knife|celery cross-sections?|"
    r"microscope magnification|staining protocol|sample preparation"
    r")\b",
    flags=re.IGNORECASE,
)


GENERIC_MERMAID_METADATA = (
    "flowchart depicting biological process or pathway",
    "network graph showing biological relationships",
    "sequence diagram showing step-by-step molecular or cellular interactions",
    "mermaid directed graph summarising a conceptual relationship described in the surrounding text",
)

FIGURE_METADATA_ARTIFACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "stale-mermaid-title-prefix",
        re.compile(r"(?:<!--\s*alt:\s*)?\*?\s*(?:Flowchart for|Sequence diagram for)\b", flags=re.IGNORECASE),
    ),
    (
        "generic-figure-caption",
        re.compile(r"\bform the diagram's primary (?:path|branches)\b|\bprimary path or branches\b", flags=re.IGNORECASE),
    ),
    (
        "stale-sequence-caption",
        re.compile(r"\bshowing ordered interaction among\b", flags=re.IGNORECASE),
    ),
)


HEADING_ARTIFACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("generic-worked-example-heading", re.compile(r"^#{2,4}\s+Worked Examples?\s*(?:\{[^}]*\})?\s*$")),
    (
        "hardcoded-worked-example-heading",
        re.compile(r"^#{2,5}\s+Worked Examples?(?:\s+\d|:\s*\d+(?:\.[A-Za-z0-9]+|\.Z))"),
    ),
    (
        "inflated-comprehensive-heading",
        re.compile(r"^#{2,5}\s+.*\bComprehensive(?:\s+(?:Overview|Reference|Table|Mechanism|Catalogue))?\b"),
    ),
    ("ascii-dash-heading", re.compile(r"^#{2,5}\s+.*\s-\s.*")),
    ("uncommon-homeostasis-heading", re.compile(r"^#{2,5}\s+.*\bHomoeostasis\b")),
    ("manual-subsection-prefix-heading", re.compile(r"^#{2,5}\s+\d+[A-Z]\s+\b")),
    (
        "underspecified-standalone-heading",
        re.compile(
            r"^#{2,5}\s+(?:Overview|Anatomy|Principles|Phases|Key Functions|Key Enzymes|"
            r"Other Key Structures|Other Tropisms|Key Agreements|Comparison|Molecular Mechanism|"
            r"Definition and Significance|Distance Methods|Limitations|Mutation|Homeostasis)"
            r"(?:\s+\{[^}]*\})?\s*$"
        ),
    ),
)


GENERIC_COMPANION_SOURCE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "generic-companion-source-intro",
        re.compile(r"The computational concepts discussed in this chapter are implemented"),
    ),
    ("stale-companion-source-note", re.compile(r"Companion source note:")),
    ("stale-companion-module-line", re.compile(r"^\*Module:")),
    ("stale-companion-figure-line", re.compile(r"^\*Figure:")),
    ("stale-companion-diagram-line", re.compile(r"^\*Diagram:")),
    ("stale-companion-crossrefs-line", re.compile(r"^\*Cross-references:")),
)


STUDENT_FACING_AUTHORING_BOILERPLATE: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "student-facing-current-source-boilerplate",
        re.compile(r"Recent and numeric claims should remain tied to authoritative sources"),
    ),
)

FRONTIER_BOILERPLATE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("frontier-boilerplate-model-claim", re.compile(r"Treat every model as a claim about mechanism")),
    ("frontier-boilerplate-ai-model", re.compile(r"Use AI biomolecular models as hypothesis generators")),
    ("frontier-boilerplate-cell-scale", re.compile(r"Ask what measurement scale is being claimed")),
    ("frontier-boilerplate-metabolic-flux", re.compile(r"A strong metabolic explanation names the flux")),
    ("frontier-boilerplate-genomic-reference", re.compile(r"When a genomic claim depends on a reference")),
    ("frontier-boilerplate-evolution-alternatives", re.compile(r"Distinguish adaptation from drift")),
    ("frontier-boilerplate-pathogen-amr", re.compile(r"For AMR and pathogen claims")),
    ("frontier-boilerplate-plant-generic", re.compile(r"A strong plant explanation names the tissue")),
    ("frontier-boilerplate-physiology-generic", re.compile(r"Interpret physiological data by separating")),
    ("frontier-boilerplate-biodiversity-generic", re.compile(r"Use biodiversity metrics carefully")),
    ("frontier-source-model-validation", re.compile(r"Use model-validation sources when available")),
    (
        "frontier-source-structure-generic",
        re.compile(r"For structure and interaction claims, cite experimental structures when available and treat"),
    ),
    ("frontier-source-cell-generic", re.compile(r"For cell-state claims, distinguish microscopy")),
    ("frontier-source-metabolism-generic", re.compile(r"For metabolic claims, keep the organism")),
    (
        "frontier-source-genetics-generic",
        re.compile(r"For inheritance and population claims, separate the model assumptions"),
    ),
    (
        "frontier-source-evolution-generic",
        re.compile(r"For evolutionary claims, prefer evidence that compares alternatives"),
    ),
    ("frontier-source-pathogen-generic", re.compile(r"For pathogen, AMR, and intervention claims")),
    ("frontier-source-plant-generic", re.compile(r"For plant-stress and crop claims")),
    ("frontier-source-physiology-generic", re.compile(r"For physiology claims, cite the measurement context")),
    ("frontier-source-conservation-generic", re.compile(r"For conservation claims, cite assessment sources")),
)


COPYEDIT_ARTIFACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("copyedit-uppercase-most", re.compile(r"\bMOST\b")),
    ("copyedit-not-most", re.compile(r"\bNot most\b")),
    ("copyedit-most-involve", re.compile(r"\bmost involve\b")),
    ("copyedit-most-the", re.compile(r"\bmost the\b")),
    ("copyedit-most-four", re.compile(r"\bmost four\b")),
    (
        "copyedit-most-number",
        re.compile(
            r"(?<!\bat\s)\bmost\s+(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\b",
            flags=re.IGNORECASE,
        ),
    ),
    ("copyedit-nearly-most", re.compile(r"\bnearly most\b", flags=re.IGNORECASE)),
    ("copyedit-primarily-then", re.compile(r"\bprimarily then\b", flags=re.IGNORECASE)),
    ("copyedit-virtually-most", re.compile(r"\bvirtually most\b", flags=re.IGNORECASE)),
    ("copyedit-almost-most", re.compile(r"\balmost most\b", flags=re.IGNORECASE)),
    (
        "copyedit-quantified-of-most",
        re.compile(r"\b(?:approximately\s+|~)?\d+(?:[-–]\d+)?\s*%?\s+of most\b", flags=re.IGNORECASE),
    ),
    ("copyedit-of-most-known-recorded", re.compile(r"\bof most (?:known|recorded)\b")),
    ("copyedit-of-most-time", re.compile(r"\bof most time\b")),
    ("copyedit-most-bear", re.compile(r"\bmost bear\b")),
    ("copyedit-sum-of-most", re.compile(r"\bsum of most\b")),
    ("copyedit-space-of-most", re.compile(r"\bspace of most\b")),
    ("copyedit-set-of-most", re.compile(r"\bset of most\b")),
    ("copyedit-partition-of-most", re.compile(r"\bpartition of most\b")),
    ("copyedit-primarily-quantifier", re.compile(r"\bprimarily\s+~?\d")),
    ("copyedit-primarily-a-has", re.compile(r"\bprimarily a has\b")),
    ("copyedit-the-primarily", re.compile(r"\bthe primarily\b")),
    ("copyedit-primarily-partially", re.compile(r"\bprimarily partially\b")),
    ("copyedit-primarily-by-approx", re.compile(r"\bprimarily by ~")),
    ("copyedit-primarily-as-good", re.compile(r"\bprimarily as good as\b")),
    ("copyedit-need-primarily-open", re.compile(r"\bneed primarily open\b")),
    ("copyedit-hyphen-primarily", re.compile(r"\b[A-Za-z]+-primarily\b")),
)


HARDCODED_REF = re.compile(
    r"(?<![A-Za-z])(?:Chapter|Ch\.?|Figure|Fig\.?|Equation|Eq\.?|Section|Table)s?"
    r"\s*\d+(?:\.\d+)*"
    r"(?:\s*(?:,|and|or|/|[–-])\s*"
    r"(?:(?:Chapter|Ch\.?|Figure|Fig\.?|Equation|Eq\.?|Section|Table)s?\s*)?"
    r"\d+(?:\.\d+)*)*"
    r"|§\s*\d+(?:\.\d+)*"
    r"|\b(?:Chapter|Ch\.?|Figure|Fig\.?|Equation|Eq\.?|Section|Table)s?(?:~|\s+)?\\(?:eqref|ref)\{[^}]+\}",
)

RAW_LATEX_RENDERED_REF = re.compile(r"\\(?:eqref|ref|autoref)\{(?:sec|fig|eq|tbl):[^}]+\}")

DOLLAR_TAG_LABEL_RE = re.compile(
    r"^\s*\$\$.*\\tag\{[^}]+\}.*\\label\{eq:[^}]+\}.*\$\$\s*$"
    r"|^\s*\$\$.*\\label\{eq:[^}]+\}.*\\tag\{[^}]+\}.*\$\$\s*$"
)
LATEX_EQUATION_TAG_RE = re.compile(r"\\tag\{[^}]+\}")
INLINE_CIRC_PRIME_RE = re.compile(r"\$[^$\n]*\^\\circ'[^$\n]*\$")

HARDCODED_STRUCTURAL_REF = re.compile(
    r"\bUnits?\s+(?:0(?:\.\d+)?(?:'s)?|[IVX]+(?:\s*[–-]\s*[IVX]+)?"
    r"(?:\s*(?:,|and|or|/|\+)\s*[IVX]+)*)\b"
    r"|\bAppendix\s+[A-Z]\b"
    r"|\b(?:Figure|Fig\.)\s+FM-\d+\b"
    r"|\bChapter numbers\b"
)

FRONT_MATTER_GENERATED_MARKERS: tuple[tuple[str, str], ...] = (
    ("<!-- toc-navigation-start -->", "<!-- toc-navigation-end -->"),
    ("<!-- suggested-reading-paths-start -->", "<!-- suggested-reading-paths-end -->"),
    ("<!-- textbook-concept-map-start -->", "<!-- textbook-concept-map-end -->"),
    ("<!-- course-planning-grid-start -->", "<!-- course-planning-grid-end -->"),
)


ABSOLUTE_LANGUAGE = re.compile(
    r"\b(always|never|universal|universally|all|only|impossible|guarantees?)\b",
    flags=re.IGNORECASE,
)


BENIGN_ABSOLUTE_CONTEXTS = (
    "all requested clause",
    "all requested clauses",
    "all figures were generated",
    "all numerical",
    "all 10 units",
    "all ordered chapter files",
    "applies only to",
    "belongs only in an optional extension",
    "equipment version belongs only in an optional extension",
    "not always",
    "not all",
    "not only",
    "only about",
    "only tools needed",
    "reference only",
    "almost universally",
    "near-universal",
    "universal donor",
    "universal recipient",
    "universal genetic code",
    "universal primers",
    "universal primer",
    "ab only",
    "o only",
    "all rights reserved",
    "all-or-none",
    "almost always",
    "nearly universal",
    "*pan* = all",
    "one-size-fits-all",
)



PAPER_EVIDENCE_UPGRADE_HEADING_RE = re.compile(
    r"^## Paper-Based Evidence Upgrade(?:\s+\{[^}]*\})?\s*$",
    flags=re.MULTILINE,
)

COMPANION_SOURCE_MODULE_HEADING_RE = re.compile(
    r"^#{2,3}\s+Companion Source Module(?::\s+.+?)?(?:\s+\{[^}]*\})?\s*$",
    flags=re.MULTILINE,
)

OPENING_VIGNETTE_RE = re.compile(
    r"^(?:#{2,3}\s+Opening Vignette\b|>\s*\*\*Opening Vignette\b)",
    flags=re.MULTILINE,
)
SUMMARY_HEADING_RE = re.compile(r"^## Summary(?:\b|[\s{:])", flags=re.MULTILINE)
CONCEPT_CHECK_RE = re.compile(r"^\s*>?\s*\*\*Concept Check(?:\b|\s|\d|\()", flags=re.MULTILINE)
