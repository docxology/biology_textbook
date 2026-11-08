# Question-Bank Authoring Contract

Each configured core chapter has a 30-item bank: 10 Recall, 10 Application, and 10 Synthesis items, with independently authored prompt-specific solutions. Filenames, ordering, and canonical titles belong to `docs/manuscript/config.yaml`. Commands and `src/`, `scripts/`, `tests/`, `output/` paths below are repository-root paths under inherited admission.

## Identity and item grammar

Store `questions_<chapter_stem>.md` under its unit, registering only its filename in `appendices.questions[].files[]`. Preserve the H1 identifier `{#sec:q_unit_X_<stem> .unnumbered}`; do not add a duplicate standalone section label. Link to the numbered parent with `\cref{sec:unit_X_<stem>}`; an unnumbered bank target uses `\nameref{sec:q_unit_X_<stem>}`.

Items are numbered paragraphs, not `## Q1` headings. Every item requires its reviewed semantic assessment comment; Bloom level is not inferred merely from the ordinal tier. For example:

```markdown
<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define an allele.

<!-- SOLUTION
**Answer (Q1, Recall).** An allele is a sequence variant at a genetic locus. A phenotype alone does not uniquely identify the underlying allele.
SOLUTION -->
```

Author LO identifiers, Bloom levels, difficulty, format, and estimated minutes against the actual prompt and answer. `scripts/sync_assessment_metadata.py --dry-run` previews author actions; `--check` validates without generating those judgments.

## Instructor and student rendering

The current config sets `export.include_solutions: true` for the instructor edition; false selects student output. `BIOLOGY_INCLUDE_SOLUTIONS` overrides that selection. Preserve exactly one `<!-- SOLUTION ... SOLUTION -->` block per item, with the matching answer number and tier. The staging pipeline handles visibility while preserving literal code examples.

## Substantive answer and evidence checks

Give the requested biological mechanism or calculation, relevant evidence and limitations, units/denominators, scoring expectations, and a common misconception where appropriate. Explicitly label synthetic inputs; do not pass them off as measurements. Cite matched sources for empirical claims. No boilerplate, missing data, invented clinical inference, or heuristic replacement can stand in for an answer.

`refine_generated_answers.py --dry-run` reports authoring needs. Unsupported automatic answer filling refuses without writing; do not expect a `refined=0` replacement workflow. Review item-to-LO and rubric meaning, not just metadata presence.

[The testing guide](../../testing_guide.md) owns commands and gates. [The pedagogy mapping guide](../../pedagogy_objectives_mapping.md) owns semantic mapping detail; [the manuscript contract](../AGENTS.md) owns references and source boundaries. [README.md](README.md) is the reader-facing overview.
