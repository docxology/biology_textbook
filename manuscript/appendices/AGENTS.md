# `manuscript/appendices/` — AGENTS.md

## Role

Reference appendices for reusable material: math review, units/constants, periodic-table support, and the glossary-derived index. These are distinct from:

- `../labs/` — one paper-based lab per chapter
- `../questions/` — one 30-question bank per chapter

## Authoring Contract

- Use descriptive filenames: `appendix_<topic>.md`.
- Put `\label{sec:appendix_<topic>}` immediately after the H1 title.
- Cross-reference from chapters with `\cref{sec:appendix_<topic>}` rather than hard-coded appendix letters.
- Keep generated/reference content honest: if a script is named in a maintenance note, the script must exist before relying on it.

## Rendering

These appendices are not toggled by `appendices.include_labs` or `appendices.include_questions`. They render when `appendices.include_reference: true`; their order is the `appendices.reference[]` list in `manuscript/config.yaml`. If a new reference appendix should appear in the combined PDF, add it to that list and add or adjust tests so ordering stays stable.

## Maintenance Checklist

- [ ] Labels use the `sec:appendix_*` namespace.
- [ ] Any table or figure intended for cross-reference has a `tbl:` or `fig:` label.
- [ ] Accessibility comments follow the same descriptive HTML alt-comment convention as chapters when figures or Mermaid blocks are added.
- [ ] `README.md` lists the file and its role.
