# Absolute-Language Triage

The scanner records broad language as a **raw review candidate**, not proof that
the biology is wrong. Publication requires zero blocking errors and zero
**outstanding** advisories. Individually justified scientific absolutes remain
visible with severity `reviewed`; the report shows raw, reviewed and outstanding
counts separately. The zero budget is not raised and no regex bucket is ignored.

`docs/manuscript/quality_advisories.yaml` records each review:

- `advisory_id`: scanner code, exact repository-relative source path, line number and excerpt digest.
- `source_path`, positive integer `line`, and `excerpt`: must match the current finding exactly.
- `classification`: one of the categories below.
- `rationale`: a nonempty scientific explanation required for acceptance, naming
  the definition, mathematical condition, explicit finite set or qualified scope.

| Category | Treatment |
| --- | --- |
| `valid_scientific_absolute` | Keep a defensible definition, mathematical/taxonomic statement, named technical term or explicitly bounded case. Promote only after exact source binding and rationale validation. |
| `needs_qualifier` | Repair an empirical trend, scenario, treatment effect or count falsely presented as universal. It remains a blocking error while present. Track fast-moving facts in `current_claims.yaml`. |
| `copyedit_artifact` | Repair malformed or scope-distorting prose. It remains a blocking error while present. |

```bash
uv run --frozen --extra dev python scripts/audit_textbook_quality.py --check --max-advisories 0
```

Untriaged, unresolved, duplicate, malformed, mismatched and stale accepted reviews
fail closed. A copied ID cannot authorize a different path, line or excerpt.
Repeated identical claims on different lines have distinct IDs and require
independent reviews; duplicate reviews of the same occurrence are rejected.
Moving or changing a claim requires refreshing its locator and review. Changed
surrounding context with an unchanged locator/excerpt is not detected by this
binding check: it requires human scientific re-review, not automatic approval.
Remove stale acceptances after repairing their source, and review any new
candidate independently. Other advisory classes still count toward the same
outstanding budget. A positive rationale is a recorded reviewer judgment, not an
externally signed certification or evidence that every textbook claim was checked.
