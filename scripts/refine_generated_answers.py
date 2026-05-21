#!/usr/bin/env python3
# ruff: noqa: E501
"""Answer-generator v3 — upgrade generated answers with improved heuristics.

The first generator passes gave every question a solution block, but many
remaining blocks were rubric-shaped rather than question-shaped. This script
detects generated answers by signature phrases and regenerates them with:

* Better question classification (``identify``, ``list``, ``state``, ``rank``
  all route to ``define``; ``a patient / student / researcher`` routes to
  ``apply``; ``formula`` / ``equation`` + numbers → ``calculate``).
* Wider subject-phrase extraction that respects sentence boundaries and
  preserves parentheticals.
* Chapter-category tier-closes so a physiology question gets physiological
  interpretation rather than a generic "experimental design" tail.
* Question-specific anchors, values, clauses, and named entities extracted from
  the prompt itself.
* Calculate-specific templates that require formula, substitution, units, and
  a biological range check.

The script is idempotent: running it multiple times converges. Hand-written
answers (those not containing generated-answer signature phrases) are never
touched.
"""

from __future__ import annotations

import logging
import re
import sys
from pathlib import Path

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


logger = logging.getLogger(__name__)
MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
QUESTIONS = MANUSCRIPT / "questions"


# ---------------------------------------------------------------------------
# generated-answer signature phrases — identify non-hand-written answers
# ---------------------------------------------------------------------------

_V1_SIGNATURES = (
    "This question asks for a definition or factual statement about:",
    "Construct a side-by-side contrast of",
    "This is a numerical problem. Begin by stating the formula",
    "Give a mechanistic explanation for *",
    "Outline an experimental or design response to the prompt on *",
    "Take a position on *",
    "Apply the chapter's framework to the specific scenario:",
    "Give the canonical definition of *",
    "Contrast the items in *",
    "Numerical problem on *",
    "Build a mechanistic answer to *",
    "Propose an experimental or engineering response to *",
    "Take a position on *",
    "Apply the chapter's principles to the scenario:",
    "Expected answer for *",
    "Prompt cues to cover:",
    "Source standard:",
    "Common pitfall:",
    "Chapter lens:",
    "boundary condition that prevents overgeneralising it",
    "Answer every requested clause rather than only the opening phrase",
    "Ground the answer in \\cref{",
    "Use \\cref{",
    "Extend \\cref{",
    "Carry through these values:",
    "Use these named items explicitly:",
    "set up the governing equation",
    "state a defensible judgment",
    "support it with two chapter-specific observations",
    "Name the biological players",
    "Ground the answer in \\cref",
    "Use \\cref",
    "Extend \\cref",
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
    "Trace *",
    "Give a precise account of *",
    "Set *",
    "Write the model for *",
    "Turn *",
    "Assess *",
    "Use the chapter principle with *",
    "Reference point: \\cref",
    "Key answer:",
    "Comparison answer:",
    "Calculation answer:",
    "Mechanistic answer:",
    "Design answer:",
    "Evaluation answer:",
    "Application answer:",
    "Chapter evidence:",
    "Recent and numeric claims should remain tied to authoritative sources",
)


def is_v1_generated(body: str) -> bool:
    return any(sig in body for sig in _V1_SIGNATURES)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

_TIER_HDR = re.compile(
    r"^##\s+Questions\s+(\d+)[–-](\d+):",
    re.IGNORECASE,
)
_QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$")
_LABEL_RE = re.compile(r"\\label\{sec:q_(unit_[0-9IVX]+)_([a-z_]+)\}")


def tier_for(q_num: int) -> str:
    if q_num <= 10:
        return "Recall"
    if q_num <= 20:
        return "Application"
    return "Synthesis"


# ---------------------------------------------------------------------------
# Improved question classification
# ---------------------------------------------------------------------------

_DEFINE_VERBS = (
    "define ", "what is ", "what are ", "state ", "list ", "identify ",
    "name ", "rank ", "describe the structure", "describe the function",
    "describe the ", "outline the ", "sketch a ", "draw a ", "give an example",
    "write the ", "write an ",
)
_CALCULATE_TRIGGERS = (
    "calculate ", "compute ", "what is the value", "estimate ",
    "determine the ", "find the ", "how many ", "how much ",
    "what fraction ", "what proportion ", "what probability ",
    "what is the probability", "expected ratio", "expected phenotype ratio",
    "chi-square", "chi square", "χ²", "binomial", "recombination frequency",
    "allele frequency",
)
_COMPARE_TRIGGERS = (
    "compare ", "contrast ", "distinguish ", "differentiate ",
)
_EXPLAIN_TRIGGERS = (
    "explain ", "describe how", "describe why", "why does ", "why is ",
    "why do ", "how does ", "how do ", "how would ", "how can ",
    "describe the mechanism",
)
_DESIGN_TRIGGERS = (
    "propose ", "design ", "devise ", "suggest ",
    "what experiment", "what would you do", "outline an experiment",
    "create ", "develop a ",
)
_EVALUATE_TRIGGERS = (
    "evaluate ", "assess ", "critique ", "argue ", "judge ",
    "weigh ", "defend or refute",
)
_APPLY_TRIGGERS = (
    "a patient ", "a student ", "a researcher ", "a scientist ",
    "a doctor ", "a clinician ", "a farmer ", "a breeder ", "a conservationist ",
    "given that ", "given a ", "given the ", "consider a ", "consider the ",
    "suppose ", "imagine ",
)
_FORMULA_CUES = (
    "formula", "equation", "henderson", "hardy-weinberg", "nernst",
    "logistic", "michaelis", "hill equation", "hodgkin", "fst", "kimura",
    "pka", "ph =", "dg =", "δg", "mpa", "molar",
)
_FORMULA_CUE_RE = re.compile(
    r"\b(?:formula|equation|henderson|hardy-weinberg|nernst|logistic|michaelis|hill equation|hodgkin|fst|kimura|pka|ph|dg|δg|molar)\b|MPa",
    flags=re.IGNORECASE,
)

_CLAUSE_RE = re.compile(r"\(([a-e])\)\s*([^;(]+(?:\([^)]*\))?)")
_QUANTITY_RE = re.compile(
    r"(?<![-A-Za-z])(?P<op>[~≈<>])?\s*(?P<num>\d+(?:\.\d+)?)\s*"
    r"(?P<unit>%|mL/h|m/h|MPa|km²|ha|mm|cm|µm|nm|m|°C|yr|years?|days?|generations?|individuals?|species|s⁻¹|kDa|M)?"
    r"(?:\s*(?P<scale>million|billion|trillion))?",
    flags=re.IGNORECASE,
)
_NAMED_ENTITY_RE = re.compile(r"\b[A-Z][A-Za-z0-9+/βαγδκλ⁺⁻-]{2,}\b")
_STOP_NAMED = {
    "Apply",
    "Assess",
    "At",
    "Calculate",
    "Compare",
    "Construct",
    "Critically",
    "Define",
    "Describe",
    "Design",
    "Determine",
    "Distinguish",
    "During",
    "Evaluate",
    "Explain",
    "For",
    "Give",
    "How",
    "Identify",
    "List",
    "Name",
    "Predict",
    "Propose",
    "Rank",
    "State",
    "The",
    "This",
    "Under",
    "Using",
    "When",
    "Where",
    "What",
    "Which",
    "Why",
}


def classify_question(text: str) -> str:
    t = text.lower().strip()

    # Strong command verbs at the front should dominate incidental numbers in
    # the prompt. This prevents evaluation questions with extinction rates or
    # percentages from being treated as calculation-only problems.
    if any(trig in t[:80] for trig in _EVALUATE_TRIGGERS) or " evaluate:" in t[:160]:
        return "evaluate"
    if any(trig in t[:70] for trig in _DESIGN_TRIGGERS) or "design an experiment" in t:
        return "design"
    if any(trig in t[:80] for trig in _COMPARE_TRIGGERS) or "difference between" in t:
        return "compare"

    # Calculate — most specific first (numeric questions often start with context)
    if any(trig in t[:100] for trig in _CALCULATE_TRIGGERS) or (
        re.search(r"\b(calculate|compute|estimate|determine|find|solve)\b", t)
        and re.search(r"\d|%|χ²|=", t)
    ):
        return "calculate"
    # Also if the question mentions a named equation/formula + asks for a number
    if _FORMULA_CUE_RE.search(text) and re.search(
        r"\b(calculate|compute|estimate|determine|find|solve|what is the value)\b", t
    ):
        return "calculate"

    # Define / recall
    if t.startswith(_DEFINE_VERBS):
        return "define"

    # Apply (scenario-driven)
    if any(trig in t[:60] for trig in _APPLY_TRIGGERS):
        return "apply"

    # Explain (fall-through for "why/how" questions)
    if any(trig in t[:40] for trig in _EXPLAIN_TRIGGERS) or "mechanism" in t:
        return "explain"

    # Default
    return "explain"


# ---------------------------------------------------------------------------
# Improved subject extraction
# ---------------------------------------------------------------------------

_PREAMBLE_RE = re.compile(
    r"^(?:A\s+(?:student|patient|researcher|scientist|clinician|farmer|breeder|conservationist)\s+[^.]*\.\s*"
    r"|Consider(?:\s+a|\s+the)?\s+[^.]*\.\s*"
    r"|Given\s+[^.]*\.\s*"
    r"|Suppose\s+[^.]*\.\s*"
    r"|Imagine\s+[^.]*\.\s*)",
    re.IGNORECASE,
)


def subject_phrase(text: str) -> str:
    """Extract the core question subject, robust to preambles and punctuation."""
    s = text.strip().rstrip(". ")

    # Strip a leading scenario preamble if the question has one
    s = _PREAMBLE_RE.sub("", s).strip()

    verb_prefixes = (
        "state ", "define ", "list ", "identify ", "name ", "rank ",
        "describe ", "describe the ", "outline ", "outline the ",
        "sketch ", "draw ", "write ", "write the ", "give ",
        "what is ", "what are ", "compare ", "contrast ", "distinguish ",
        "differentiate ", "explain ", "evaluate ", "assess ", "critique ",
        "calculate ", "compute ", "estimate ", "determine ", "find ",
        "design ", "propose ", "devise ", "suggest ",
    )
    lowered = s.lower()
    for prefix in sorted(verb_prefixes, key=len, reverse=True):
        if lowered.startswith(prefix):
            s = s[len(prefix):].lstrip()
            break

    # Prefer the first sentence over arbitrary punctuation splits.
    # Split on ". " but keep periods that are part of abbreviations like "e.g."
    # Simple heuristic: first period followed by a capital letter or question mark.
    for i in range(len(s) - 1):
        if s[i] == "." and i + 1 < len(s) and s[i + 1] in " \n" and (
            i + 2 >= len(s) or s[i + 2].isupper()
        ):
            s = s[:i]
            break

    # Trim at ? if present
    if "?" in s:
        s = s.split("?")[0]

    # Keep up to ~180 chars, preserving parentheticals
    if len(s) > 180:
        # Try to break at ", " or " — " near 160 chars
        brk = s.rfind(", ", 0, 160)
        if brk == -1:
            brk = s.rfind(" — ", 0, 160)
        if brk == -1:
            brk = 177
        s = s[:brk].rstrip(", ") + "…"
    return s.strip()


def prompt_specific_anchor(text: str) -> str:
    """Return compact prompt-specific details to keep generated keys concrete."""

    clauses = []
    for marker, body in _CLAUSE_RE.findall(text):
        cue = " ".join(body.split()).strip(" .")
        if cue:
            clauses.append(f"{marker}) {cue}")
    if clauses:
        return "Address these prompt parts: " + "; ".join(clauses[:5]) + "."

    quantities: list[str] = []
    for match in _QUANTITY_RE.finditer(text):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if not (op or unit or scale or "." in num or float(num) > 10):
            continue
        quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        unique = list(dict.fromkeys(quantities))[:6]
        return "Carry these quantities through the reasoning: " + ", ".join(unique) + "."

    named_items = [item for item in _NAMED_ENTITY_RE.findall(text) if item not in _STOP_NAMED]
    if named_items:
        unique = list(dict.fromkeys(named_items))[:6]
        return "Work these named items into the mechanism: " + ", ".join(unique) + "."

    return "Tie the conclusion back to the scenario, interpretation, or consequence requested in the prompt."


# ---------------------------------------------------------------------------
# Extractive chapter evidence
# ---------------------------------------------------------------------------

_STOPWORDS = {
    "about",
    "after",
    "again",
    "against",
    "also",
    "because",
    "before",
    "between",
    "biology",
    "chapter",
    "could",
    "describe",
    "does",
    "during",
    "each",
    "explain",
    "from",
    "give",
    "have",
    "into",
    "make",
    "more",
    "most",
    "name",
    "only",
    "other",
    "should",
    "show",
    "state",
    "than",
    "that",
    "their",
    "then",
    "there",
    "these",
    "this",
    "through",
    "using",
    "what",
    "when",
    "where",
    "which",
    "while",
    "with",
    "would",
    "your",
}

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(*`])")
_MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_INLINE_FORMAT_RE = re.compile(r"[*_`]+")
_LATEX_INLINE_PROTECT_RE = re.compile(r"\\(?:cref|label|citep|citet|cite)\{[^}]*\}")
_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_MARKDOWN_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_CITATION_TAIL_RE = re.compile(r"^[A-Z]\., \d")


def _tokens(text: str) -> set[str]:
    return {
        tok
        for tok in re.findall(r"[A-Za-z][A-Za-z0-9+-]{2,}", text.lower())
        if tok not in _STOPWORDS and len(tok) > 3
    }


def _clean_sentence(sentence: str) -> str:
    sentence = _MARKDOWN_LINK_RE.sub(r"\1", sentence)
    protected_tokens: dict[str, str] = {}

    def protect(match: re.Match[str]) -> str:
        token_index = len(protected_tokens)
        placeholder = f"XLATEXPROTECT{token_index}X"
        while placeholder in sentence or placeholder in protected_tokens:
            token_index += 1
            placeholder = f"XLATEXPROTECT{token_index}X"
        protected_tokens[placeholder] = match.group(0)
        return placeholder

    sentence = _LATEX_INLINE_PROTECT_RE.sub(protect, sentence)
    sentence = _INLINE_FORMAT_RE.sub("", sentence)
    sentence = re.sub(r"\s+", " ", sentence).strip()
    sentence = sentence.strip(" -")
    for placeholder, original in protected_tokens.items():
        sentence = sentence.replace(placeholder, original)
    return sentence


def _candidate_sentences(chapter_text: str) -> list[str]:
    text = _FENCE_RE.sub(" ", chapter_text)
    text = _COMMENT_RE.sub(" ", text)
    lines: list[str] = []
    skip_heading_level: int | None = None
    in_curriculum_scaffold = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if in_curriculum_scaffold:
            if "-->" in line:
                in_curriculum_scaffold = False
            continue
        if "<!-- curriculum-scaffold" in line:
            if "-->" not in line:
                in_curriculum_scaffold = True
            continue
        heading_match = _MARKDOWN_HEADING_RE.match(line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_title = heading_match.group(2).strip().lower()
            if skip_heading_level is not None and heading_level <= skip_heading_level:
                skip_heading_level = None
            if heading_title in {"learning objectives", "study blueprint"}:
                skip_heading_level = heading_level
                continue
        # If no equal-or-higher heading appears, this conservative skip region runs to EOF.
        if skip_heading_level is not None:
            continue
        if line.startswith("> "):
            continue
        if line.startswith(("#", "|", "!", "$$", "\\", "{", "}", ":::")):
            continue
        if line.startswith(("-", "*")) and len(line) < 90:
            continue
        if line.startswith("Figure") or line.startswith("Table"):
            continue
        lines.append(line)

    joined = " ".join(lines)
    sentences: list[str] = []
    for sentence in _SENTENCE_SPLIT_RE.split(joined):
        cleaned = _clean_sentence(sentence)
        if not 70 <= len(cleaned) <= 320:
            continue
        lowered = cleaned.lower()
        if any(skip in lowered for skip in ("learning objectives", "source code module", "further reading")):
            continue
        if any(skip in cleaned for skip in ("?", "Problem:", "Concept Check", "Why might", "What does this imply")):
            continue
        if ">" in cleaned or "Primary source:" in cleaned or _CITATION_TAIL_RE.match(cleaned):
            continue
        sentences.append(cleaned)
    return sentences


def chapter_path_for(unit: str, stem: str) -> Path:
    return MANUSCRIPT / unit / f"{stem}.md"


_CHAPTER_SENTENCE_CACHE: dict[str, list[tuple[Path, list[str]]]] = {}


def chapter_sentence_cache(unit: str) -> list[tuple[Path, list[str]]]:
    if unit in _CHAPTER_SENTENCE_CACHE:
        return _CHAPTER_SENTENCE_CACHE[unit]

    chapter_files = [
        path
        for path in sorted((MANUSCRIPT / unit).glob("*.md"))
        if path.name not in {"README.md", "AGENTS.md", "unit_intro.md"}
    ]
    cached: list[tuple[Path, list[str]]] = []
    for path in chapter_files:
        try:
            cached.append((path, _candidate_sentences(path.read_text(encoding="utf-8"))))
        except OSError as exc:
            logger.warning("Skipping unreadable chapter file %s: %s", path, exc)
            continue
    _CHAPTER_SENTENCE_CACHE[unit] = cached
    return cached


def chapter_evidence(unit: str, stem: str, q_text: str, category: str) -> tuple[str, str]:
    """Return two chapter-specific sentences relevant to the question."""
    primary_path = chapter_path_for(unit, stem)
    q_tokens = _tokens(q_text)
    subject = subject_phrase(q_text)
    subject_tokens = _tokens(subject)
    named = {item.lower() for item in _NAMED_ENTITY_RE.findall(q_text) if item not in _STOP_NAMED}
    query = q_tokens | subject_tokens | named
    subject_norm = " ".join(sorted(subject_tokens))
    subject_words = [tok for tok in subject.lower().split() if len(tok) > 3 and tok not in _STOPWORDS]

    scored: list[tuple[int, int, str]] = []
    sentence_index = 0
    for path, sentences in chapter_sentence_cache(unit):
        for sentence in sentences:
            sentence_index += 1
            lowered_sentence = sentence.lower()
            s_tokens = _tokens(sentence)
            overlap = len(query & s_tokens)
            phrase_bonus = sum(2 for tok in query if tok in lowered_sentence)
            named_bonus = sum(3 for item in named if item and item in lowered_sentence)
            exact_subject_bonus = 0
            if subject and subject.lower() in lowered_sentence:
                exact_subject_bonus += 20
            if subject_norm and subject_norm == " ".join(sorted(subject_tokens & s_tokens)):
                exact_subject_bonus += 8
            if len(subject_words) >= 2 and all(word in lowered_sentence for word in subject_words[:4]):
                exact_subject_bonus += 12
            locality_bonus = 8 if path == primary_path else 4 if path.parent.name == unit else 0
            category_bonus = 1 if any(tok in s_tokens for tok in category.split("_")) else 0
            score = overlap * 4 + phrase_bonus + named_bonus + exact_subject_bonus + locality_bonus + category_bonus
            if score > 0:
                scored.append((score, -sentence_index, sentence))

    if not scored:
        return fallback_evidence(category)

    selected: list[str] = []
    seen_tokens: set[str] = set()
    for _score, _neg_idx, sentence in sorted(scored, reverse=True):
        s_tokens = _tokens(sentence)
        if selected and len(s_tokens & seen_tokens) > max(3, len(s_tokens) // 2):
            continue
        selected.append(sentence)
        seen_tokens |= s_tokens
        if len(selected) == 2:
            break

    if len(selected) == 1:
        selected.append(fallback_evidence(category)[1])
    return selected[0], selected[1]


def fallback_evidence(category: str) -> tuple[str, str]:
    fallbacks = {
        "ecology": (
            "Ecological interpretation requires stating the spatial scale, measured response variable, and the process linking organisms to resources or interactions.",
            "A strong answer separates pattern from mechanism and notes the sampling limit that could change the management conclusion.",
        ),
        "evolution_genetics": (
            "Genetic and evolutionary explanations should identify the inheritance pattern or evolutionary force before interpreting an observed phenotype or allele-frequency pattern.",
            "A strong answer states the assumptions, predicts a measurable population or pedigree outcome, and names evidence that would distinguish alternatives.",
        ),
        "physiology": (
            "Physiological explanations should connect a mechanism to organ-system function, compensation, and an observable variable such as pressure, concentration, firing rate, or hormone level.",
            "A strong answer treats normal range and context as part of the interpretation rather than assuming one fixed value applies in every condition.",
        ),
        "microbiology": (
            "Microbiology explanations should identify the organism or virus, its growth or transmission route, and the evidence used for diagnosis, surveillance, or control.",
            "A strong answer distinguishes colonization, infection, immunity, and resistance before recommending an intervention.",
        ),
        "botany": (
            "Plant biology explanations should name the tissue, developmental stage, environmental driver, and water, hormone, or carbon variable being interpreted.",
            "A strong answer links structure to transport, growth, reproduction, or stress response while noting the tradeoff involved.",
        ),
        "molecular_genetics": (
            "Molecular genetics explanations should distinguish sequence, expression, chromatin state, assay evidence, and clinical or evolutionary interpretation.",
            "A strong answer names the molecular machine or variant, predicts a molecular outcome, and states what evidence would confirm it.",
        ),
        "cell": (
            "Cell biology explanations should locate the process in a cell type, compartment, membrane, organelle, or signalling step before predicting an outcome.",
            "A strong answer identifies the measurement scale and avoids treating static structures as if they explain dynamics by themselves.",
        ),
        "biochemistry": (
            "Biochemical explanations should name the molecule, reaction direction, energetic or kinetic term, and pathway context being interpreted.",
            "A strong answer checks units and plausibility, especially for pH, pKa, catalytic rate, saturation, and pathway-flux questions.",
        ),
        "general": (
            "Systems explanations should define the boundary, components, interactions, feedback sign, and measurement scale before drawing a conclusion.",
            "A strong answer distinguishes a list of parts from a causal model and states what evidence would change the interpretation.",
        ),
    }
    return fallbacks.get(category, fallbacks["general"])


def pitfall_for(kind: str, category: str) -> str:
    if kind == "calculate":
        return "Pitfall to avoid: reporting a number without units, assumptions, and a short biological interpretation."
    if kind == "compare":
        return "Pitfall to avoid: making a two-column vocabulary list without naming the mechanism that creates the difference."
    if kind == "design":
        return "Pitfall to avoid: proposing an activity without a control, measured outcome, replication, and decision rule."
    if kind == "evaluate":
        return "Pitfall to avoid: treating a conditional evidence claim as universal or settled."
    category_pitfalls = {
        "ecology": "Pitfall to avoid: confusing a field pattern with proof of mechanism without scale, sampling, and uncertainty.",
        "evolution_genetics": "Pitfall to avoid: invoking selection when drift, linkage, migration, or sampling could also explain the pattern.",
        "physiology": "Pitfall to avoid: naming an organ without connecting stimulus, sensor, effector, compensation, and measured response.",
        "microbiology": "Pitfall to avoid: conflating exposure, colonization, infection, immunity, and transmission.",
        "botany": "Pitfall to avoid: explaining the trait without the water, hormone, carbon, or developmental tradeoff.",
        "molecular_genetics": "Pitfall to avoid: moving from a DNA change to a phenotype without expression, protein, or assay evidence.",
        "cell": "Pitfall to avoid: naming a structure without locating the transport, signalling, or compartment process.",
        "biochemistry": "Pitfall to avoid: naming a molecule without the reaction direction, energetic term, or kinetic consequence.",
        "general": "Pitfall to avoid: listing parts without specifying interactions and feedback.",
    }
    return category_pitfalls.get(category, category_pitfalls["general"])


# ---------------------------------------------------------------------------
# Chapter-category tier-close variants
# ---------------------------------------------------------------------------

def chapter_category(chapter_stem: str) -> str:
    """Coarse topical category from the chapter stem."""
    s = chapter_stem.lower()
    if any(k in s for k in ("ecosystem", "biome", "community", "population_ecology",
                              "conservation", "microbial_ecology")):
        return "ecology"
    if any(k in s for k in ("evolution", "drift", "speciation", "phylogenetics",
                              "mendelian", "chromosomal", "population_genetics")):
        return "evolution_genetics"
    if any(k in s for k in ("nervous", "synap", "action_potential", "endocrine",
                              "immune", "circulation", "respiration", "homeostasis")):
        return "physiology"
    if any(k in s for k in ("bacteria", "archaea", "virus", "infectious", "micro")):
        return "microbiology"
    if any(k in s for k in ("plant", "botany", "photosynthesis")):
        return "botany"
    if any(k in s for k in ("dna", "gene", "mutation", "genomic", "epigenetic")):
        return "molecular_genetics"
    if any(k in s for k in ("cell_", "membrane", "organelle", "signaling")):
        return "cell"
    if any(k in s for k in ("atom", "water", "macromolecule", "enzyme", "bioenergetic",
                              "metabol")):
        return "biochemistry"
    return "general"


_TIER_CLOSE = {
    ("Recall", "ecology"):              "Ground the answer in \\cref{{{r}}} with one named ecosystem, population, or field-study example.",
    ("Recall", "physiology"):           "Ground the answer in \\cref{{{r}}} with a normal range, organ-system context, or named disorder.",
    ("Recall", "molecular_genetics"):   "Ground the answer in \\cref{{{r}}} with the experiment, sequence feature, or molecular machine that establishes it.",
    ("Recall", "evolution_genetics"):   "Ground the answer in \\cref{{{r}}} with a named organism, population, allele, or lineage.",
    ("Recall", "microbiology"):         "Ground the answer in \\cref{{{r}}} with a named microbial taxon, virus, resistance marker, or infection context.",
    ("Recall", "botany"):               "Ground the answer in \\cref{{{r}}} with a plant tissue, hormone, water-relation variable, or ecological setting.",
    ("Recall", "cell"):                 "Ground the answer in \\cref{{{r}}} with a cell type, organelle, membrane process, or signalling component.",
    ("Recall", "biochemistry"):         "Ground the answer in \\cref{{{r}}} with a representative molecule, reaction, equation, or energetic value.",
    ("Recall", "general"):              "Ground the answer in \\cref{{{r}}} with one named biological example.",
    ("Application", "ecology"):         "Use \\cref{{{r}}} to interpret the result as coexistence, extinction risk, biodiversity change, or resource limitation.",
    ("Application", "physiology"):      "Use \\cref{{{r}}} to connect the result to homeostatic range, organ performance, or a diagnostic pattern.",
    ("Application", "molecular_genetics"): "Use \\cref{{{r}}} to interpret the result as a change in sequence, expression, inheritance, or variant evidence.",
    ("Application", "evolution_genetics"): "Use \\cref{{{r}}} to interpret the result as selection, drift, linkage, disequilibrium, or allele-frequency change.",
    ("Application", "microbiology"):    "Use \\cref{{{r}}} to connect the result to growth, transmission, resistance, immunity, or replication.",
    ("Application", "botany"):          "Use \\cref{{{r}}} to connect the result to water potential, gas exchange, growth, or developmental regulation.",
    ("Application", "cell"):            "Use \\cref{{{r}}} to connect the result to transport, membrane potential, organelle function, or signal flow.",
    ("Application", "biochemistry"):    "Use \\cref{{{r}}} to connect the result to ΔG, pH, pKa, catalytic rate, saturation, or pathway flux.",
    ("Application", "general"):         "Use \\cref{{{r}}} to check the result against a plausible biological range.",
    ("Synthesis", "ecology"):           "Extend \\cref{{{r}}} by naming the management decision, response variable, and uncertainty that would change the conclusion.",
    ("Synthesis", "physiology"):        "Extend \\cref{{{r}}} by naming the intervention or perturbation, the measured variable, and the expected physiological direction.",
    ("Synthesis", "molecular_genetics"): "Extend \\cref{{{r}}} by naming the assay, edit, or sequencing evidence and predicting the molecular outcome.",
    ("Synthesis", "evolution_genetics"): "Extend \\cref{{{r}}} by naming the comparison, population sample, or lineage evidence and predicting the evolutionary pattern.",
    ("Synthesis", "microbiology"):      "Extend \\cref{{{r}}} by naming the diagnostic, prevention, treatment, or surveillance evidence that would decide the case.",
    ("Synthesis", "botany"):            "Extend \\cref{{{r}}} by naming the plant trait, environmental driver, and physiological measurement that would decide the case.",
    ("Synthesis", "cell"):              "Extend \\cref{{{r}}} by naming the perturbed component, assay readout, and expected cellular change.",
    ("Synthesis", "biochemistry"):      "Extend \\cref{{{r}}} by naming the enzyme, metabolite, or pathway perturbation and the kinetic/thermodynamic readout.",
    ("Synthesis", "general"):           "Extend \\cref{{{r}}} with a testable prediction and the evidence that would change your judgment.",
}


# ---------------------------------------------------------------------------
# Improved answer templates
# ---------------------------------------------------------------------------

def chapter_method(category: str) -> str:
    methods = {
        "ecology": "state the spatial scale, response variable, sampling limit, and management implication",
        "evolution_genetics": "name the inheritance or evolutionary force, the assumptions, and the evidence that would distinguish alternatives",
        "physiology": "connect mechanism to organ-system range, compensation, and the observable sign or measurement",
        "microbiology": "identify the taxon or pathogen, growth/transmission mechanism, and diagnostic or surveillance evidence",
        "botany": "name the tissue, water or hormone variable, environmental driver, and growth-reproduction tradeoff",
        "molecular_genetics": "separate sequence, expression, variant evidence, assay, and clinical or evolutionary interpretation",
        "cell": "tie the answer to cell type, compartment, membrane process, signalling step, or measurement scale",
        "biochemistry": "include molecule, reaction, energetic direction, kinetic term, pH/pKa, or pathway flux as appropriate",
        "general": "name the biological scale, mechanism, evidence, and boundary condition",
    }
    return methods.get(category, methods["general"])


def answer_clauses(q_text: str) -> str:
    clauses = [
        f"{marker}) {body.strip(' .')}"
        for marker, body in _CLAUSE_RE.findall(q_text)
        if body.strip(" .")
    ]
    if clauses:
        return " Address the requested parts explicitly: " + "; ".join(clauses[:5]) + "."
    quantities = []
    for match in _QUANTITY_RE.finditer(q_text):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if op or unit or scale or "." in num or float(num) > 10:
            quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        return " Use the stated quantitative evidence: " + ", ".join(list(dict.fromkeys(quantities))[:6]) + "."
    named_items = [item for item in _NAMED_ENTITY_RE.findall(q_text) if item not in _STOP_NAMED]
    if named_items:
        return " Include the named evidence: " + ", ".join(list(dict.fromkeys(named_items))[:6]) + "."
    return ""


def generate_answer(
    q_num: int,
    tier: str,
    q_text: str,
    chapter_ref: str,
    category: str,
    evidence: tuple[str, str] | None = None,
) -> str:
    kind = classify_question(q_text)
    subject = subject_phrase(q_text)
    evidence_1, evidence_2 = evidence or fallback_evidence(category)
    clause_text = answer_clauses(q_text)
    pitfall = pitfall_for(kind, category)
    method = chapter_method(category)
    templates = {
        "define": (
            f"The response on *{subject}* should first state the chapter's concrete mechanism: {evidence_1} "
            f"Then give one same-scale example or boundary condition using this evidence: {evidence_2}"
        ),
        "compare": (
            f"The response on *{subject}* should name the shared biological principle and the difference that changes interpretation. "
            f"The shared principle is supported by: {evidence_1} The decisive contrast or boundary condition is: {evidence_2}"
        ),
        "calculate": (
            f"The response on *{subject}* should name the model, substitute the stated values with units, and check the biological range. "
            f"Use this chapter context for the interpretation: {evidence_1} Check the result against: {evidence_2}"
        ),
        "explain": (
            f"The response on *{subject}* should give the causal chain: initiating condition, changed component, intermediate mechanism, and observable outcome. "
            f"The mechanism should be grounded in: {evidence_1} Interpret the outcome using: {evidence_2}"
        ),
        "design": (
            f"The response on *{subject}* should name the hypothesis, comparison/control, changed factor, measured outcome, replication, and falsifying result. "
            f"The mechanistic basis is: {evidence_1} The decision rule should distinguish that mechanism from the alternative implied by: {evidence_2}"
        ),
        "evaluate": (
            f"The response on *{subject}* should separate empirical evidence from the judgment and name what would change the conclusion. "
            f"Use this evidence line: {evidence_1} State this limitation or boundary condition: {evidence_2}"
        ),
        "apply": (
            f"The response on *{subject}* should identify the relevant variable, mechanism, prediction, and evidence that would decide the case. "
            f"Use this mechanism: {evidence_1} Evidence that would support or weaken the prediction is: {evidence_2}"
        ),
    }

    body = templates[kind]
    return (
        f"**Answer (Q{q_num}, {tier}).** {body}{clause_text} "
        f"Scholarship standard: {method}. {pitfall} Chapter anchor: \\cref{{{chapter_ref}}}."
    )


# ---------------------------------------------------------------------------
# Bank processing
# ---------------------------------------------------------------------------

# Match a full SOLUTION block with its Answer body
_BLOCK_RE = re.compile(
    r"(<!-- SOLUTION\s*\n)"
    r"(\*\*Answer \(Q(\d+),\s*[^)]+\)\.\*\*[^\n]*(?:\n(?!SOLUTION -->)[^\n]*)*)"
    r"(\n\s*SOLUTION -->)",
    re.DOTALL,
)


def process_bank(path: Path, dry_run: bool = False) -> tuple[int, int]:
    """Refine every v1-generated answer. Return (refined, skipped_non_v1)."""
    text = path.read_text(encoding="utf-8")

    m = _LABEL_RE.search(text)
    if not m:
        return (0, 0)
    unit, stem = m.group(1), m.group(2)
    chapter_ref = f"sec:{unit}_{stem}"
    category = chapter_category(stem)

    # Extract question-number → question-text map
    q_text: dict[int, str] = {}
    for line in text.splitlines():
        if (qm := _QUESTION_LINE.match(line)):
            n = int(qm.group(1))
            if 1 <= n <= 30:
                q_text[n] = qm.group(2)

    refined = 0
    skipped = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal refined, skipped
        opener, body, q_num_str, closer = match.group(1), match.group(2), match.group(3), match.group(4)
        if not is_v1_generated(body):
            skipped += 1
            return match.group(0)
        q_num = int(q_num_str)
        tier = tier_for(q_num)
        qt = q_text.get(q_num, "")
        evidence = chapter_evidence(unit, stem, qt, category)
        new_body = generate_answer(q_num, tier, qt, chapter_ref, category, evidence)
        if new_body == body:
            skipped += 1
            return match.group(0)
        refined += 1
        return f"{opener}{new_body}{closer}"

    new_text = _BLOCK_RE.sub(repl, text)
    if refined and not dry_run:
        write_text_atomic(path, new_text)
    return (refined, skipped)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total_refined = 0
    total_skipped = 0
    files = 0
    for bank in sorted(QUESTIONS.rglob("questions_*.md")):
        r, s = process_bank(bank, dry_run=dry_run)
        if r or s:
            files += 1
        if r:
            total_refined += r
            print(f"  [{'D' if dry_run else '+'}] {bank.relative_to(MANUSCRIPT)}: refined {r}, preserved {s} hand-written")
        total_skipped += s
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] refined={total_refined}  hand_written_preserved={total_skipped}  files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
