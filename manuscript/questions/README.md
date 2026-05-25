# Question Banks

This directory contains **44 comprehensive question banks** — one per textbook chapter (including the four Unit 0 orientation chapters) — with **30 questions each**, ordered from simplest recall to most sophisticated synthesis and evaluation.

## File Naming Convention

```
questions_{chapter_filename}.md
```

Organised under unit subdirectories:

```
questions/
├── README.md                           ← this file
├── AGENTS.md                           ← authoring conventions (agent-facing)
├── unit_0/, unit_I/, … unit_X/         ← 11 unit subdirectories
│   └── questions_{chapter}.md         ← one 30-question file per chapter (39 total)
```

## Question Difficulty Tiers

| Questions | Tier | Bloom's Level |
| --------- | ---- | ------------- |
| 1–10 | **Recall and Comprehension** | Remember, Understand |
| 11–20 | **Application and Analysis** | Apply, Analyse |
| 21–30 | **Synthesis and Evaluation** | Evaluate, Create |

## Structural Conventions

Every question-bank file carries:

- An H1 title generated from the parent chapter title by `../../scripts/sync_curriculum_materials.py`, followed by `\label{sec:q_unit_X_<stem>}`
- An opening `\cref{sec:unit_X_<stem>}` one-liner linking back to the parent textbook chapter (inserted by `../../scripts/link_labs_to_chapters.py`)
- Exactly 30 questions in the 10 + 10 + 10 tier split above

The H1 form is enforced by `tests/test_toc_consistency.py`; presence of the
label and back-link is enforced by
`tests/test_build_invariants.py::test_every_question_links_to_parent_chapter`.

## Learning-objective mapping

Question-bank items carry lightweight HTML comments above questions to show which chapter learning objective, Bloom level, difficulty, format, and estimated minutes are being assessed. Maintain them with `../../scripts/sync_assessment_metadata.py --check`:

```markdown
<!-- LO:2,4 -->
## Q12. Application
```

This authoring metadata is parsed by `src/biology/assessment.py` and enforced by `tests/test_assessment_metadata.py`. It should not alter rendered numbering.

## Rendering

Question banks are included when `appendices.include_questions: true` in `manuscript/config.yaml`.
Question-bank appendix entries store only file names in
`appendices.questions[].files[]`; do not add duplicated `title:` strings there.
The instructor edition with `<!-- SOLUTION ... SOLUTION -->` answer blocks revealed is controlled by `export.include_solutions` in the same file (`false` = student edition by default) or by `BIOLOGY_INCLUDE_SOLUTIONS=1`.
When `include_questions` is `false`, only core chapters (and optional labs) are rendered.

## Answer-key quality standard

Each question bank must contain exactly **30** `<!-- SOLUTION ... SOLUTION -->` blocks. Answer keys should give chapter-specific reasoning: the mechanism or model, evidence or data cue, units or calculation check when relevant, a common pitfall, and the parent-chapter `\cref{...}` anchor. Do not leave generated scaffolds such as `Expected reasoning:`, `A complete response should`, `Required clauses:`, or generic "build a mechanistic answer" language. Run:

```bash
uv run python scripts/refine_generated_answers.py --dry-run
uv run python scripts/audit_textbook_quality.py --check
```

## Optional: regenerate manuscript figures

From this project root:

```bash
uv run python scripts/generate_figures.py
```

Outputs go to `output/figures/`. See `src/visualization/plots.py` for registered `plot_*` generators.
