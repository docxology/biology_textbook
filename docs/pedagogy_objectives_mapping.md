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

Per-item assessment comments and reviewed lab alignment blocks are required source metadata parsed by biology.assessment and checked by assessment/pedagogy tests. They do not change PDF numbering. Semantic validity still requires author review; schema acceptance is not proof of pedagogical quality.

The project now also has a tested curriculum and standards spine:

- `src/biology/curriculum/` aligns each chapter with its companion lab,
  question bank, model/data skill, misconception probe, transfer task, and
  bridge API.
- `src/biology/alignment.py` aligns each chapter with Vision & Change,
  AP Biology, NGSS-style topics, BioSkills categories, and an instructor
  orchestration move.

Run `scripts/sync_curriculum_materials.py` after editing these records to refresh canonical H1s/identifiers, chapter Study Blueprints, navigation and generated curriculum/instructor appendices. It preserves authored lab evidence checklists, question coverage notes, procedures, prompts/keys and rubrics. `--dry-run` previews changes; it is not a failing drift gate. Validate reviewed assessment metadata with `scripts/sync_assessment_metadata.py --check` and the assessment/pedagogy tests.

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
| **Question bank** | `docs/manuscript/questions/unit_X/questions_<chapter_stem>.md` | Mixed (mostly Apply / Analyze / Evaluate) | 30 items per chapter; instructors draw from these for exams |
| **Lab worksheet** | `docs/manuscript/labs/unit_X/lab_<chapter_stem>.md` | Apply / Analyze / Create (procedural) | Hands-on or pen-and-paper procedure |

### Recommended mix for question banks (30 items per chapter)

| Level | Count | Typical format |
| ----- | ----- | -------------- |
| Remember | 4–6 | Multiple-choice; matching; fill-in |
| Understand | 6–8 | Short-answer; "explain in 2–3 sentences" |
| Apply | 8–10 | Numerical calculation; case-based application; predict-and-justify |
| Analyze | 4–6 | Compare-contrast; data-interpretation; figure analysis |
| Evaluate | 1–3 | Critique a claim; choose between competing models with rationale |
| Create | 0–2 | Design an experiment; write a hypothesis with predictions |

These proportions and formats are task-design suggestions, not a parser contract or an empirical learning-effect claim. Published banks currently use `format=short-answer`; multiple-choice/matching examples require deliberate format support, not an unsupported metadata value.

---

## Writing questions at different cognitive levels

Use the actual chapter objectives and supplied evidence to select a level, not the question number:

| Level | Biology task example |
| --- | --- |
| Remember | Name the four DNA bases. |
| Understand | Explain degeneracy versus ambiguity in the genetic code. |
| Apply | Compute Michaelis–Menten velocities from supplied parameters and concentrations. |
| Analyze | Compare explicitly supplied monovalent-ion permeability scenarios using GHK. |
| Evaluate | Compare divergence-time estimates using supplied sequence divergence and a stated substitution-rate calibration; critique clock assumptions. |
| Create | Design a controlled experiment to distinguish candidate histone-mark reader mechanisms. |

These are task-design examples, not substitute authored bank items or automatically assigned objective mappings. Every published item needs its own substantive solution, evidence and scoring expectations; unsupported automatic answer repair refuses without writing.

## Objective-question mapping convention

Chapter objectives are numbered under Learning Objectives and referenced as LO1, LO2, etc. In the corresponding bank, write one reviewed assess comment immediately before each numbered item:

```markdown
<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=8 -->
12. A synthetic enzyme has Vmax=12 micromoles/min and Km=0.5 mM. Calculate initial velocity at substrate concentrations 0.1 mM and 5 mM, stating the model assumptions.
```

LO4 above is illustrative: use it only if the actual fourth objective supports that task. Valid Bloom values are Remember, Understand, Apply, Analyze, Evaluate and Create. Difficulty bands are Recall, Application and Synthesis; format is short-answer and minutes must be a positive integer. Separate LO/bloom/difficulty comments and easy/medium/hard labels are not the parser contract.

Author all item mappings from meaning; ensure all chapter objectives are assessed and include reviewed difficulty and higher-order Bloom diversity. Lab alignment uses exactly one lab-alignment-start/end marker block with 3–4 measurable LO-mapped outcomes and task-specific evidence, controls, uncertainty, mechanism and transfer criteria. Preserve those rubrics rather than regenerate them from chapter order. Required lab tasks include finite printed data, tables/cards and explicit criteria, labeled synthetic or empirical with provenance.

---

## Maintenance

- When objectives or tasks change, review the actual semantic item/outcome mappings before updating comments and rubrics.
- Update curriculum/alignment source records when skills or emphasis change; regenerate only generator-owned navigation/scaffold blocks with scripts/sync_curriculum_materials.py.
- Validate with scripts/sync_assessment_metadata.py --dry-run or --check and tests/test_assessment_metadata.py plus tests/test_lab_pedagogy_alignment.py. The synchronizer preserves curated records and rejects authoring gaps without positional regeneration.
- Metadata validation is not scientific answer verification or evidence of a fresh full publication pass.
- For instructor editions where solutions appear, see `export.include_solutions` in [accessibility.md](accessibility.md#export).

---

## See also

- [agent_instructions.md](agent_instructions.md) — chapter template, vignette and Concept Check construction
- [manuscript_guide.md](manuscript_guide.md) — LaTeX patterns, citation commands
- [composable_authoring.md](composable_authoring.md) — question-bank file naming and `config.yaml` appendices
- [testing_guide.md](testing_guide.md) — invariant tests for question banks (`test_build_invariants.py::test_every_question_links_to_parent_chapter`)
