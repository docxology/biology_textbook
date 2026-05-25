# `src/biology/answer_refinement/` — question-bank answer refinement

Logic extracted from `scripts/refine_generated_answers.py` and `scripts/fill_answer_scaffolds.py`. Both scripts delegate to entry points on `biology.answer_refinement.cli`.

## Modules

| File | Role |
| --- | --- |
| `paths.py` | `PROJECT`, `MANUSCRIPT`, `QUESTIONS` |
| `classification.py` | Canonical `classify_question`, `subject_phrase`, `tier_for`, `question_kind` (enrichment vocabulary); V1-signature catalog and shared regex |
| `evidence.py` | Manuscript-anchored evidence sentence selection for refined answers |
| `generation.py` | Refined answer body composition from classified prompts |
| `engine.py` | `process_bank`, heuristic answer replacement; preserves hand-written `<!-- SOLUTION -->` blocks |
| `scaffolds.py` | V1 instructor-scaffold filling (`process_bank`, `generate_answer`) reusing classification helpers |
| `cli.py` | `main()` (refine) and `fill_main()` (V1 scaffold fill) — `--dry-run` / apply reporting across all `questions_*.md` banks |

## CLI

```bash
uv run python scripts/refine_generated_answers.py --dry-run
uv run python scripts/refine_generated_answers.py
uv run python scripts/fill_answer_scaffolds.py --dry-run
uv run python scripts/fill_answer_scaffolds.py
```

Dry-run reports banks that would change; a stable pass reports `refined=0` (refine path) or `scaffolds_filled=0` (fill path) when all auto-generated stubs are already upgraded.
