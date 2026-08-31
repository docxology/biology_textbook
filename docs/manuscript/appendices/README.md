# Reference Appendices

This directory contains reference appendices that support the textbook but are separate from the lab and question-bank appendices:

| File | Role |
| ---- | ---- |
| `appendix_curriculum_map.md` | Generated chapter/lab/question/model alignment from `src/biology/curriculum.py` |
| `appendix_instructor_orchestration.md` | Generated standards, skills, and instructor sequence map from `src/biology/alignment.py` |
| `appendix_math_review.md` | Algebra, logarithms, units, and graph reading used by quantitative chapters |
| `appendix_units_and_constants.md` | SI units, biological constants, and conversion reminders |
| `appendix_periodic_table.md` | Chemistry reference for Unit I and biochemical chapters |
| `appendix_index.md` | Generated key-term index linked to `glossary.md` anchors |
| [`../glossary.md`](../glossary.md) | Appendix F — master glossary (source at manuscript root; `appendices.reference[]` uses `file: glossary.md`) |

Labs and question banks are controlled by `config.yaml` under `appendices.include_labs` and `appendices.include_questions`. These reference appendices are controlled separately by `appendices.include_reference`; when enabled, the combined PDF uses the order in `appendices.reference[]`.

## Maintenance

- Keep glossary index entries aligned with `glossary.md`.
- Use semantic section labels (`sec:appendix_*`) and `\cref{}` when cross-referencing from chapters.
- If a new appendix is added, document it here and add an invariant test once it becomes part of the render order.
