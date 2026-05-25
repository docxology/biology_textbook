# Learning Objectives, Bloom's Taxonomy, and Assessments

> [!NOTE]
> **See also:** [agent_instructions.md](agent_instructions.md) for the chapter structure checklist; [manuscript_guide.md](manuscript_guide.md) for LaTeX patterns; [composable_authoring.md](composable_authoring.md) for question-bank file naming and `config.yaml` appendices.

---

## Table of contents

- [Purpose](#purpose)
- [Bloom's Taxonomy — applied to biology learning objectives](#blooms-taxonomy--applied-to-biology-learning-objectives)
- [Action verbs by cognitive level](#action-verbs-by-cognitive-level)
- [Recommended chapter mix](#recommended-chapter-mix)
- [Question types mapped to textbook sections](#question-types-mapped-to-textbook-sections)
- [Writing questions at different cognitive levels](#writing-questions-at-different-cognitive-levels)
- [Objective-question mapping convention](#objective-question-mapping-convention)
- [Maintenance](#maintenance)
- [See also](#see-also)

---

## Purpose

Two complementary goals:

1. **Author-facing**: a shared cognitive-level vocabulary so every chapter's Learning Objectives, Concept Checks, Worked Examples, and Review Questions span the same range — recall, application, and synthesis — instead of clustering at one level.
2. **Instructor-facing**: a lightweight mapping from chapter Learning Objectives to appendix question banks so a course coordinator can trace coverage without a database.

This is **documentation and optional HTML comments** in `manuscript/questions/`; it does not change PDF numbering and does not introduce new tests.

The project now also has a tested curriculum and standards spine:

- `src/biology/curriculum.py` aligns each chapter with its companion lab,
  question bank, model/data skill, misconception probe, transfer task, and
  bridge API.
- `src/biology/alignment.py` aligns each chapter with Vision & Change,
  AP Biology, NGSS-style topics, BioSkills categories, and an instructor
  orchestration move.

Run `uv run python scripts/sync_curriculum_materials.py` after editing either
record set; the script refreshes chapter Study Blueprints, lab evidence
checklists, question-bank coverage notes, Appendix A's curriculum map, and
Appendix B's instructor orchestration guide. `tests/test_curriculum_metadata.py`
enforces completeness.

---

## Bloom's Taxonomy — applied to biology learning objectives

The 2001 revision of Bloom's Taxonomy (Anderson, Krathwohl, et al.) names six cognitive levels, ascending in complexity:

| Level | Name | Cognitive demand | Biology example |
| ----- | ---- | ---------------- | --------------- |
| 1 | **Remember** | Recall facts and concepts | "List the four nucleotide bases in DNA." |
| 2 | **Understand** | Explain ideas; summarize; classify | "Explain why the genetic code is degenerate." |
| 3 | **Apply** | Use a procedure or model in a new situation | "Calculate $K_m$ given $V_{\max}$ and $v_0$ at three substrate concentrations." |
| 4 | **Analyze** | Differentiate parts; identify relationships | "Compare the energy yields of aerobic and anaerobic respiration; identify the bottleneck." |
| 5 | **Evaluate** | Justify a decision; critique; check | "Given two competing models for prion propagation, which is more consistent with these published data?" |
| 6 | **Create** | Generate new patterns; design; produce | "Design an experiment to distinguish chromatin-mediated from sequence-mediated silencing." |

> [!TIP]
> Most biology textbook content sits at levels **2–4** (understand / apply / analyze). Levels 1 and 5–6 should appear, but in proportion. A chapter built entirely from level-1 recall is too shallow; one built entirely from level-6 design questions is impossible to assess in a 90-minute exam.

---

## Action verbs by cognitive level

> [!IMPORTANT]
> **Every Learning Objective must begin with an action verb.** No "understand", "know", or "be familiar with" — these are not measurable. Pick the verb that matches the Bloom level you intend to assess; the verb table below is the canonical reference.

| Level | Action verbs (use these) | Banned verbs (replace) |
| ----- | ------------------------ | ---------------------- |
| **Remember** | List, Name, Identify, Define, Recall, Recite, State, Label, Match | "Know", "Memorise" (vague) |
| **Understand** | Describe, Explain, Summarize, Classify, Compare, Contrast, Paraphrase, Interpret, Outline | "Understand", "Be aware of" |
| **Apply** | Calculate, Compute, Predict, Solve, Implement, Use, Apply, Demonstrate, Estimate | "Try to", "Attempt" |
| **Analyze** | Differentiate, Distinguish, Examine, Decompose, Diagram, Trace, Deconstruct, Categorize | "Look at", "Consider" |
| **Evaluate** | Justify, Critique, Argue, Defend, Judge, Assess, Validate, Prioritize, Recommend | "Think about", "Discuss" (vague) |
| **Create** | Design, Construct, Develop, Formulate, Propose, Hypothesize, Synthesize, Generate, Devise | "Make up", "Come up with" |

### Section-type → recommended Bloom level mapping

| Section type | Typical Bloom level | Why |
| ------------ | ------------------- | --- |
| Opening Vignette | n/a (narrative) | Sets context; not assessed directly |
| First section after vignette (introductory) | Remember + Understand | Reader needs vocabulary before applying it |
| Middle sections (the chapter's core) | Apply + Analyze | Where the textbook earns its keep |
| Worked examples | Apply (with full solution shown) | Models the reasoning explicitly |
| Concept Checks | Apply or Analyze (mostly) | Spot-check, not recall |
| Clinical Connection | Apply | Connects mechanism to a real case |
| End-of-chapter Review Questions | Mixed (Remember → Analyze), 8–10 items | Ensures coverage at multiple levels |
| Capstone / Unit X chapters | Add Evaluate + Create | Synthesis across the whole unit |
| Question-bank items (30 per chapter) | See [Recommended mix](#recommended-mix-for-question-banks-30-items-per-chapter) | Spans the full taxonomy |

### Verb pairing examples

| Bad (vague / unmeasurable) | Good (specific / measurable) |
| -------------------------- | ---------------------------- |
| "Understand enzyme kinetics" | "**Calculate** $K_m$ from a Lineweaver–Burk plot given five data points" |
| "Know the parts of a cell" | "**Label** the major organelles on an electron micrograph and **state** one function of each" |
| "Be familiar with Mendelian genetics" | "**Predict** the phenotypic ratios of a dihybrid cross using a Punnett square" |
| "Learn about evolution" | "**Differentiate** drift from selection in a small population, given allele-frequency time series" |
| "Appreciate the diversity of life" | "**Compare** the four major eukaryotic supergroups by cell-wall composition, photosynthetic mode, and motility" |

---

## Recommended chapter mix

For a typical chapter with 7–9 Learning Objectives, distribute across cognitive levels approximately like this:

| Level | Target proportion | Typical count (in 8 LOs) |
| ----- | ----------------- | ------------------------ |
| Remember | 10–15% | 1 |
| Understand | 25–35% | 2–3 |
| Apply | 25–35% | 2–3 |
| Analyze | 15–25% | 1–2 |
| Evaluate | 5–10% | 0–1 |
| Create | 0–5% | 0–1 |

> [!TIP]
> **Quantitative chapters** (biochemistry, genetics, ecology models) should skew toward Apply/Analyze. **Survey chapters** (organelle inventory, biome distribution) may skew toward Understand. **Capstone chapters** (Unit X, integrative neuroscience) should include at least one Evaluate or Create objective.

---

## Question types mapped to textbook sections

Each chapter has multiple "question surfaces":

| Surface | Where it appears | Typical Bloom level | Authoring goal |
| ------- | ---------------- | ------------------- | -------------- |
| **Concept Check** | After each major `##` section in the chapter body | Apply or Analyze | Diagnostic; spot-check that the section's idea was internalised |
| **Worked Example** | Numbered, in-line with the chapter content | Apply (with full solution shown) | Model the reasoning; calibrate the difficulty |
| **Review Questions** (end-of-chapter) | `## Review Questions` block | Mixed (Remember → Analyze) | 8–10 items spanning the LOs |
| **Question bank** | `manuscript/questions/unit_X/questions_<chapter_stem>.md` | Mixed (mostly Apply / Analyze / Evaluate) | 30 items per chapter; instructors draw from these for exams |
| **Lab worksheet** | `manuscript/labs/unit_X/lab_<chapter_stem>.md` | Apply / Analyze / Create (procedural) | Hands-on or pen-and-paper procedure |

### Recommended mix for question banks (30 items per chapter)

| Level | Count | Typical format |
| ----- | ----- | -------------- |
| Remember | 4–6 | Multiple-choice; matching; fill-in |
| Understand | 6–8 | Short-answer; "explain in 2–3 sentences" |
| Apply | 8–10 | Numerical calculation; case-based application; predict-and-justify |
| Analyze | 4–6 | Compare-contrast; data-interpretation; figure analysis |
| Evaluate | 1–3 | Critique a claim; choose between competing models with rationale |
| Create | 0–2 | Design an experiment; write a hypothesis with predictions |

---

## Writing questions at different cognitive levels

### Level 1 — Remember

```markdown
**Q1.** List the four nitrogenous bases that pair to form the rungs of the
DNA double helix.

<!-- LO:1 -->
<!-- bloom: remember -->
```

### Level 2 — Understand

```markdown
**Q5.** Explain why the genetic code is described as "degenerate" but
not "ambiguous." Give one example codon family that illustrates each
property.

<!-- LO:2 -->
<!-- bloom: understand -->
```

### Level 3 — Apply

```markdown
**Q12.** A purified enzyme has $V_{\max} = 12$ µmol min$^{-1}$ and
$K_m = 0.5$ mM. Calculate the initial velocity at $[S] = 0.1$ mM and
at $[S] = 5$ mM. Which substrate concentration is closer to saturation,
and by what fold?

<!-- LO:4 -->
<!-- bloom: apply -->
```

### Level 4 — Analyze

```markdown
**Q18.** A patient's resting membrane potential is $-50$ mV instead of
the typical $-70$ mV. Using the Goldman equation, identify the **two**
ionic-permeability changes that could each independently produce this
shift, and explain how you would distinguish them experimentally.

<!-- LO:5,6 -->
<!-- bloom: analyze -->
```

### Level 5 — Evaluate

```markdown
**Q24.** Two papers report conflicting estimates of the human-chimp
divergence time: 5 Mya \citep{paper_a} and 7 Mya \citep{paper_b}.
Given (i) a mutation rate of $0.5 \times 10^{-9}$ per site per year and
(ii) the observed divergence values from each paper, evaluate which
estimate is more consistent with a constant molecular clock. State your
assumptions explicitly.

<!-- LO:7 -->
<!-- bloom: evaluate -->
```

### Level 6 — Create

```markdown
**Q30.** Design a controlled experiment to distinguish whether a newly
discovered methylation mark on histone H3 is read by a chromodomain or
a Tudor domain. Specify (i) the cell line or system, (ii) the candidate
reader proteins to test, (iii) the assay readout, and (iv) at least one
negative control.

<!-- LO:8 -->
<!-- bloom: create -->
```

---

## Objective-question mapping convention

In each chapter, objectives are numbered `1.`, `2.`, … under `## Learning Objectives`. In the matching question file `manuscript/questions/unit_*/questions_<chapter_stem>.md`, optional **HTML comments** above each question record:

| Comment | Meaning |
| ------- | ------- |
| `<!-- LO:2 -->` | This question maps to Learning Objective 2 of the chapter |
| `<!-- LO:1,3 -->` | Maps to multiple objectives |
| `<!-- maps-to: ch objective 2 -->` | Verbose form (equivalent) |
| `<!-- bloom: apply -->` | Cognitive level (one of `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create`) |
| `<!-- difficulty: medium -->` | Optional: `easy` \| `medium` \| `hard` |
| `<!-- estimated-time: 5 min -->` | Optional: time for a typical student |

### Example

```markdown
<!-- LO:4 -->
<!-- bloom: apply -->
<!-- difficulty: medium -->
<!-- estimated-time: 8 min -->
**Q12.** A purified enzyme has $V_{\max} = 12$ µmol min$^{-1}$ and
$K_m = 0.5$ mM. Calculate the initial velocity at $[S] = 0.1$ mM ...
```

---

## Maintenance

- When chapter objectives are renumbered or split, update the `<!-- LO:N -->` comments in the question file for that chapter.
- When a chapter's model, data skill, misconception, lab emphasis, or transfer task changes, update `src/biology/curriculum.py` and rerun `scripts/sync_curriculum_materials.py`.
- This convention does **not** replace invariant tests; it is for **curriculum review** and instructor editions.
- Bulk editing: `rg "<!-- LO:" manuscript/questions/` lists every mapped question.
- For instructor editions where solutions appear, see `export.include_solutions` in [accessibility.md](accessibility.md#export).

---

## See also

- [agent_instructions.md](agent_instructions.md) — chapter template, vignette and Concept Check construction
- [manuscript_guide.md](manuscript_guide.md) — LaTeX patterns, citation commands
- [composable_authoring.md](composable_authoring.md) — question-bank file naming and `config.yaml` appendices
- [testing_guide.md](testing_guide.md) — invariant tests for question banks (`test_build_invariants.py::test_every_question_links_to_parent_chapter`)
