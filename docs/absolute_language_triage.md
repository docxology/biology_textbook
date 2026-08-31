# Absolute-Language Triage

The publication audit still emits `absolute-language-review` as an advisory
class internally, but the readiness policy now expects zero active advisory
findings before publication.

Current triage rule is recorded in `docs/manuscript/quality_advisories.yaml`.
The ledger stores a stable advisory ID, source path, line, classification, and
excerpt for every accepted `absolute-language-review` finding.

| Category | Treatment |
| --- | --- |
| Valid scientific absolute | Keep when the statement is definitional, mathematical, taxonomic, a named technical term, or tied to an explicit closed set such as "all four floral whorls" or "only one tested pathway." The ledger classification is `valid_scientific_absolute`. |
| Needed qualifier | Edit when the line turns an empirical trend, scenario, treatment effect, or current count into a universal claim. Fast-moving examples belong in `docs/manuscript/current_claims.yaml`. If the same advisory remains with `needs_qualifier`, the audit fails. |
| Copyedit artifact | Block through `scripts/audit_textbook_quality.py` when broad edits produce malformed phrases such as uppercase `MOST`, `almost most`, `of most known`, or misplaced `primarily` before a number. If the same advisory remains with `copyedit_artifact`, the audit fails. |

Run:

```bash
uv run python scripts/audit_textbook_quality.py --check --max-advisories 0
```

The expected steady state is zero blocking errors plus zero advisory findings.
New untriaged absolute-language findings fail until they are revised out of the
manuscript or added to the ledger with a valid disposition for explicit review.
