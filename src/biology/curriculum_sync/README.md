# Curriculum sync

TOC-driven H1, section-label, appendix, and front-matter scaffold sync. `scripts/sync_curriculum_materials.py` delegates to `engine.py`.

```bash
uv run python scripts/sync_curriculum_materials.py --dry-run
```

Tests: `tests/test_toc_consistency.py`, `tests/test_curriculum_metadata.py`. See [AGENTS.md](AGENTS.md).
