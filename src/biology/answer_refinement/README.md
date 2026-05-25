# Answer refinement

Heuristic upgrades for generated question-bank answers. Logic lives in `engine.py`; `scripts/refine_generated_answers.py` is the thin CLI wrapper.

```bash
uv run python scripts/refine_generated_answers.py --dry-run
```

Tests: `tests/test_question_answer_refinement.py`. See [AGENTS.md](AGENTS.md) for module layout.
