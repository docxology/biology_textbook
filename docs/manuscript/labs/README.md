# Laboratory Activities

This directory contains **44 paper-based laboratory activities** — one per textbook chapter (including the four Unit 0 orientation chapters) — designed for individual or small-group work (~4 students) without requiring wet-lab access or specialized equipment. The required path uses printed datasets, image/card packets, decision matrices, graphing tasks, control logic, uncertainty analysis, and reproducibility checks. Wet-lab, microscope, culture, reagent, specimen, heating, or dissection variants belong only in clearly marked optional extensions.

## Lab File Naming Convention

```
lab_{chapter_filename}.md
```

Each lab is organized under its unit subdirectory:

```
labs/
├── README.md                       ← this file
├── AGENTS.md                       ← authoring conventions (agent-facing)
├── unit_0/, unit_I/, … unit_X/    ← 11 unit subdirectories
│   └── lab_{chapter}.md           ← one lab per chapter (39 total)
```

## Standard Lab Structure

Each lab follows this template:

| Section | Purpose |
| ------- | ------- |
| **H1 title** followed by `\label{sec:lab_unit_X_<stem>}` | H1 is generated from the parent chapter title by `../../scripts/sync_curriculum_materials.py`; the label enables `\cref{}` cross-referencing from the parent chapter |
| **Opening `\cref`-link** | One sentence pointing back to the parent textbook chapter (auto-inserted by `../../scripts/link_labs_to_chapters.py`) |
| **Learning Objectives** | 3–4 measurable outcomes tied to chapter objectives |
| **Lab Context: `<Parent Chapter Title>`** | ~150 words connecting theory to the activity |
| **Materials** | Per-group materials list; household/classroom items only |
| **Paper-Based Investigation / Procedure** | 5–8 numbered steps using datasets, cards, diagrams, model tables, or decision matrices |
| **Data Recording** | Table or observation template |
| **Paper-Based Evidence Upgrade** | Evidence-control-uncertainty rubric maintained across all labs |
| **Analysis Questions** | 5 graded questions (recall → synthesis) |
| **Safety and Ethics** | Brief safety or ethical notes where relevant |

The H1 form is enforced by `tests/test_toc_consistency.py`; the section label
and `\cref{}` back-link are enforced by `tests/test_build_invariants.py`.
Lab learning-outcome and rubric alignment blocks are synchronized by
`../../scripts/sync_assessment_metadata.py --check` and enforced by
`tests/test_lab_pedagogy_alignment.py`.

## Accessibility and print usability

- Keep tables wide enough for handwriting; blank cells are intentional student workspace, not incomplete content.
- Add a descriptive HTML alt comment after any Mermaid block or figure introduced in a lab. `tests/test_accessibility.py` checks lab files as well as chapters.
- When color is used in a diagram, pair it with labels, symbols, hatching, or line styles so printed grayscale copies remain usable.

## Rendering

Labs are included as an appendix when `appendices.include_labs: true` in `docs/manuscript/config.yaml`.
Lab appendix entries store only file names in `appendices.labs[].files[]`; do
not add duplicated `title:` strings there.
When `false`, only core chapters are rendered. The student PDF uses compact typography (9 pt body, 2 mm margins); allow extra time for handwriting in paper labs.

## Optional: regenerate manuscript figures

From this project root (with repo dependencies installed via `uv sync` at the template root):

```bash
uv run python scripts/generate_figures.py
```

Figures are written to `output/figures/`. Registry entries live in `src/visualization/plots.py` (`ALL_FIGURE_GENERATORS`). Mermaid diagrams use `src/mermaid/biology_diagrams.py`.
