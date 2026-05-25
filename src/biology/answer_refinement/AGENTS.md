# `src/biology/answer_refinement/` — question-bank answer refinement

Logic extracted from `scripts/refine_generated_answers.py`. The script delegates to `biology.answer_refinement.cli.main`.

## Modules

| File | Role |
| --- | --- |
| `paths.py` | `PROJECT`, `MANUSCRIPT`, `QUESTIONS` |
| `engine.py` | `process_bank`, heuristic answer replacement; preserves hand-written `<!-- SOLUTION -->` blocks |
| `cli.py` | `--dry-run` / apply reporting across all `questions_*.md` banks |

## CLI

```bash
uv run python scripts/refine_generated_answers.py --dry-run
uv run python scripts/refine_generated_answers.py
```

Dry-run reports banks that would change; a stable pass reports `refined=0` when all auto-generated stubs are already upgraded.
