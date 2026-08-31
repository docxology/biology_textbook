# AGENTS — biology_textbook/src/biology/maintenance

Status: REAL (doc fleet, 2026-08-30)

Shared manuscript maintenance primitives: prose normalization, chapter scaffolding, glossary, badges.

## Layout (principals)
- `chapter_shells.py` — repair pedagogy shells on split (mega-chapter) chapters.
- `chapter_badges.py` — insert pedagogical metadata badges; refresh course planning pages.
- `american_english.py` — American-spelling normalization; wordlist in `data/british_to_american.yaml`.
- `glossary_cards.py` / `glossary_first_use.py` / `glossary_links.py` — glossary emission, first-use markers, cross-links.
- `further_reading.py`, `lab_workflows.py`, `lab_padding.py`, `manuscript_spans.py`, `manuscript_walker.py` — further-reading blocks, lab sections, manuscript traversal/span utilities.

## Invariants
- All edits are manuscript-tree rewrites driven by these functions; keep functions idempotent so reruns are no-ops.
