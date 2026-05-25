# `src/biology/curriculum_sync/` — curriculum scaffold synchronization

Logic extracted from `scripts/sync_curriculum_materials.py`. The script delegates to `biology.curriculum_sync.cli.main`.

## Modules

| File | Role |
| --- | --- |
| `paths.py` | `PROJECT`, `MANUSCRIPT` |
| `engine.py` | Study Blueprint blocks, lab evidence checklists, question-bank instructor notes, appendix curriculum maps, front-matter navigation |
| `cli.py` | `--dry-run` / apply; coordinates TOC-driven rewrites from `biology.toc` and `biology.curriculum` |

## CLI

```bash
uv run python scripts/sync_curriculum_materials.py --dry-run
uv run python scripts/sync_curriculum_materials.py --check
uv run python scripts/sync_curriculum_materials.py
```

Idempotent: re-running without TOC or curriculum changes leaves manuscript files unchanged.
