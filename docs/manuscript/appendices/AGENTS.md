# `docs/manuscript/appendices/` — AGENTS.md

## Role

Reference appendices for reusable material: math review, units/constants, periodic-table support, and the glossary-derived index. These are distinct from:

- `../labs/` — one paper-based lab per chapter
- `../questions/` — one 30-question bank per chapter

## Authoring Contract

- Use descriptive filenames: `appendix_<topic>.md`.
- Put the canonical section id on the H1 as a Pandoc identifier, e.g. `# Appendix A — Curriculum Map {#sec:appendix_curriculum_map .unnumbered}`. Do **not** use a standalone `\label{sec:appendix_<topic>}` line between H1 and the first `##` heading.
- Cross-reference from chapters with `\nameref{sec:appendix_<topic>}` (not `\cref`) because reference appendices render as unnumbered `\section*` headings.
- Keep generated/reference content honest: if a script is named in a maintenance note, the script must exist before relying on it.

## Rendering

These appendices are not toggled by `appendices.include_labs` or `appendices.include_questions`. They render when `appendices.include_reference: true`; their order is the `appendices.reference[]` list in `docs/manuscript/config.yaml`. If a new reference appendix should appear in the combined PDF, add it to that list and add or adjust tests so ordering stays stable.

## Maintenance Checklist

- [ ] H1 identifiers use the `sec:appendix_*` namespace with `{#sec:appendix_* .unnumbered}`.
- [ ] Prose cross-references use `\nameref{sec:appendix_*}`.
- [ ] Any table or figure intended for cross-reference has a `tbl:` or `fig:` label.
- [ ] Accessibility comments follow the same descriptive HTML alt-comment convention as chapters when figures or Mermaid blocks are added.
- [ ] `README.md` lists the file and its role.
