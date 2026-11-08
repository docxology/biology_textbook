# Biology Question Banks and Instructor Answers

The configured 44 banks contain 30 items each: 10 Recall, 10 Application, and 10 Synthesis questions. They accompany the 44 core chapters, including Unit 0, in `questions_<chapter_stem>.md` files under each unit.

## Use a bank

Follow its parent-chapter link. Numbered items carry authoring metadata connecting the prompt to a chapter learning objective, Bloom level, difficulty, short-answer format, and estimated minutes. These mappings are required semantic records, not evidence that every item achieves its intended cognitive demand.

Each item has one authored SOLUTION block. Answers must address the actual prompt and distinguish supplied synthetic inputs from empirical evidence. The current `../config.yaml` selects the instructor edition with `export.include_solutions: true`; false selects student output, and `BIOLOGY_INCLUDE_SOLUTIONS` can override that selection. Bank inclusion/order use `appendices.include_questions` and `appendices.questions`.

[AGENTS.md](AGENTS.md) owns item grammar, source identifiers, answer authoring, and validation. [The pedagogy guide](../../pedagogy_objectives_mapping.md) explains semantic mapping. Figure generation belongs to [the visualization guide](../../visualization_guide.md), not a second template-root recipe.
