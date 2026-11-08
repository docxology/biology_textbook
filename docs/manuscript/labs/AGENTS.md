# Paper-Lab Authoring Contract

The configured labs are self-contained paper activities paired with core chapters. Ordering and filenames belong to `docs/manuscript/config.yaml`; do not duplicate titles there. Commands and `src/`, `scripts/`, `tests/`, `output/` paths below are repository-root paths. Use the inherited execution/admission policy.

## Source identity and references

- Store `lab_<chapter_stem>.md` in the matching unit directory and register its filename under `appendices.labs[].files[]`.
- Preserve the H1 Pandoc identifier `{#sec:lab_unit_X_<stem> .unnumbered}`. Do not add a duplicate standalone LaTeX section label.
- Link to the numbered parent chapter with `\cref{sec:unit_X_<stem>}`. References to an unnumbered lab use `\nameref{sec:lab_unit_X_<stem>}`.
- `sync_curriculum_materials.py` maintains canonical titles and navigation, not authored lab bodies.

## Evidence, outcomes, and paper self-containment

Provide measurable learning objectives, chapter context, finite materials/data packets, executable paper procedures, recording space, analysis, and safety/ethics. Label synthetic inputs and distinguish them from observations. Supply every denominator, unit, decision rule, and required datum; a hidden notebook or unavailable experiment cannot be part of the required path.

Learning outcomes, LO coverage, and rubric dimensions are authored semantic records. `scripts/sync_assessment_metadata.py --dry-run` previews required author actions; `--check` validates without manufacturing alignment. Review the actual task and scoring criteria before changing those records.

Wet-lab, culture, specimen, reagent, heating, dissection, microscope, and specialized-equipment variants belong only in clearly marked optional extensions. Estimate activity time from the actual tasks, not the parent chapter's lecture-time field. Keep enough print space for handwriting and inspect the rendered tables; a compilation success is not a usability review.

## Validation and shared owners

Run project-local assessment, lab-integrity, lab-pedagogy, accessibility, ToC, and build-invariant checks after edits. Commands and failure-to-fix mapping belong to [the testing guide](../../testing_guide.md); source/reference conventions belong to [the manuscript contract](../AGENTS.md). [README.md](README.md) describes the reader-facing lab structure.
