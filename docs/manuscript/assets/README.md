# Manuscript assets

Static files referenced by the build but not authored as Markdown chapters.

## Cover image

| Item | Value |
| ---- | ----- |
| **Config key** | `docs/manuscript/config.yaml` → `book.cover.image` |
| **Default path** | `assets/cover/biology_textbook_cover.png` |
| **Alt text** | `book.cover.alt` in the same config block |
| **Regenerate** | From project root: `uv run python scripts/generate_cover_art.py` |

The PDF renderer places this image on the generated title page (page 1). Publishing metadata (DOI, source repository) comes from `publication.*` in `config.yaml`, not from files in this directory.

Do not hand-edit the PNG for typography or layout changes — adjust the generator script and re-run it so the asset stays reproducible.

## Layout

```text
assets/
├── README.md
├── AGENTS.md
└── cover/
    └── biology_textbook_cover.png   # generated; path must match config.yaml
```
