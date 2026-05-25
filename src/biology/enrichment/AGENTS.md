# `src/biology/enrichment/` — embedded enrichment engine

Logic extracted from `scripts/enrich_embedded_textbook.py` (formerly 1406 lines). The script delegates to `biology.enrichment.cli.main`.

## Modules

| File | Role |
| --- | --- |
| `paths.py` | `PROJECT`, `MANUSCRIPT`, `DOCS` |
| `models.py` | `ChapterRecord` dataclass |
| `records.py` | `chapter_records()` from TOC |
| `catalog.py` | Declarative frontier/companion/lab focus tables by unit/stem |
| `engine.py` | Frontier biology, lab evidence, audit matrix; re-exports companion + answer-key APIs for backward compatibility |
| `companion.py` | `companion_source_section`, `normalize_companion_source_modules`, table-caption helpers |
| `answer_keys.py` | `refine_question_banks`, `answer_key`, evidence/scholarship/pitfall helpers (imports `question_kind`, `subject_phrase` from `biology.answer_refinement.classification`) |
| `cli.py` | `--dry-run` / apply reporting |

## CLI

```bash
uv run python scripts/enrich_embedded_textbook.py --dry-run
uv run python scripts/enrich_embedded_textbook.py          # apply
```

Dry-run counts surfaces that would change; after a stable apply pass, chapter counts should drop to zero except the audit matrix when live character counts drift.
