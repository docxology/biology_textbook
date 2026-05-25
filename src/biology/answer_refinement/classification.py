"""Answer refinement engine."""

from __future__ import annotations

import logging
import re


logger = logging.getLogger(__name__)

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
    "Apply the chapter's principles to the scenario:",
    "Expected answer for *",
    "Prompt cues to cover:",
    "Source standard:",
    "Common pitfall:",
    "Chapter lens:",
    "boundary condition that prevents overgeneralizing it",
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

_VOCAB_MAP = {
    "define": "definition",
    "explain": "mechanism",
    "compare": "comparison",
    "calculate": "quantitative",
    "design": "experimental",
    "evaluate": "evaluation",
    "apply": "application",
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


def question_kind(text: str) -> str:
    """Map refinement question types to enrichment answer-key vocabulary."""

    return _VOCAB_MAP[classify_question(text)]


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
