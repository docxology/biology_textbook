"""Chapter-specific evidence selection for answer refinement."""

from __future__ import annotations

import logging
from pathlib import Path

from biology.answer_refinement.classification import (
    _NAMED_ENTITY_RE,
    _STOP_NAMED,
    _STOPWORDS,
    _candidate_sentences,
    _tokens,
    subject_phrase,
)
from biology.answer_refinement.paths import MANUSCRIPT

logger = logging.getLogger(__name__)

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
            "Cell biology explanations should locate the process in a cell type, compartment, membrane, organelle, or signaling step before predicting an outcome.",
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
        "cell": "Pitfall to avoid: naming a structure without locating the transport, signaling, or compartment process.",
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
    ("Recall", "cell"):                 "Ground the answer in \\cref{{{r}}} with a cell type, organelle, membrane process, or signaling component.",
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
        "cell": "tie the answer to cell type, compartment, membrane process, signaling step, or measurement scale",
        "biochemistry": "include molecule, reaction, energetic direction, kinetic term, pH/pKa, or pathway flux as appropriate",
        "general": "name the biological scale, mechanism, evidence, and boundary condition",
    }
    return methods.get(category, methods["general"])

