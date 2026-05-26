# `src/biology/crossref/` — manuscript cross-reference validator

Package split from the former monolithic `crossref_validator.py`. Public API is re-exported from `biology.crossref_validator` for backward compatibility.

## Modules

| File | Role |
| --- | --- |
| `models.py` | `CrossRefIssue` dataclass; typed `ProblemCode` literal union |
| `patterns.py` | Regex catalogs for labels, refs, figures, equations, tables |
| `helpers.py` | Shared parsing helpers and fence-state utilities |
| `scan_context.py` | Mutable per-file scan state (`ScanContext`) |
| `scan_latex_envs.py` | LaTeX figure/table/equation environment handlers |
| `scan_markdown_ids.py` | Headings, images, block math, pipe table captions |
| `scan_ref_uses.py` | Reference uses and prose-xref anti-patterns |
| `scan_file.py` | Per-file scan orchestration |
| `table_captions.py` | Caption insertion for chapter/lab pipe tables (`scripts/annotate_table_captions.py`) |
| `validator.py` | `scan_directory`, `validate`, `suggest_id`, report assembly |
| `__init__.py` | Re-exports public surface |

## Public functions

```python
scan_file(path: Path) -> list[CrossRefIssue]
scan_directory(root: Path) -> list[CrossRefIssue]
validate(manuscript: Path) -> CrossRefReport
suggest_id(kind: str, stem: str) -> str
```

## Gate contract

- Invoked by `tests/test_crossref_validator*.py` and related crossref tests, plus `scripts/audit_textbook_quality.py`.
- Every issue carries a stable `problem` code from `ProblemCode`; renaming codes is a breaking change for audit filters.
