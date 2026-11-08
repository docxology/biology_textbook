# Authored Answer Preservation and Unsupported-Repair Refusal

The thin answer-maintenance scripts delegate here. Prompt classification or chapter excerpts cannot establish a correct prompt-specific worked answer. There are no reviewed automatic solvers registered in `generation.py`; `UnsupportedAnswerRepair` requires an author to supply the solution without changing the source.

## Source responsibilities

`engine.py` and `cli.py` inspect authored banks and report required review actions. `classification.py` identifies legacy signatures; `evidence.py` locates context, not answer truth. `scaffolds.py` and the fill CLI refuse unsupported generation rather than replacing missing answers with generic guidance. Preserve existing reviewed SOLUTION blocks.

Run `scripts/refine_generated_answers.py --dry-run` from the repository root under inherited admission to preview authoring needs. Do not expect heuristic replacement counts or use an apply command to manufacture keys. Author missing substantive answers directly, then exercise the answer-refinement, assessment, and textbook-quality checks described in [the testing guide](../../../docs/testing_guide.md).

Canonical item grammar and solution visibility belong to [the question-bank contract](../../../docs/manuscript/questions/AGENTS.md). New automatic solvers would require independently reviewed prompt-specific correctness and preservation regressions; adding a heuristic is not authorized by this guide.
