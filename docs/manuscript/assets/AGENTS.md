# `docs/manuscript/assets/` — AGENTS.md

## Role

Binary and static assets consumed by the rendering pipeline. This tree is **not** part of the Markdown chapter DAG in `config.yaml`.

## Cover art contract

- **Source of truth for path:** `book.cover.image` and `book.cover.alt` in [`../config.yaml`](../config.yaml).
- **Generator:** [`../../scripts/generate_cover_art.py`](../../scripts/generate_cover_art.py) delegates to [`../../src/biology/assets/cover_art.py`](../../src/biology/assets/cover_art.py) (Pillow raster; text-free montage).
- **Pipeline copy:** `biology_analysis.py` copies live `config.yaml`, `preamble.md`, `references.bib`, and cover assets into `output/manuscript/` before render.

## Editing rules

1. Prefer regenerating via `generate_cover_art.py` over editing pixels in place.
2. If the filename changes, update `book.cover.image` in `config.yaml` and any docs that cite the path.
3. Do not commit alternate cover variants here without updating config — the title page resolves a single configured path.

## Related documentation

- [`README.md`](README.md) — quick reference
- [`../AGENTS.md`](../AGENTS.md) — manuscript-wide conventions
- [`../../docs/visualization_guide.md`](../../docs/visualization_guide.md) — figure and diagram workflows (matplotlib / Mermaid)
