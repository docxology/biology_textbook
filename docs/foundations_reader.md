# Foundations reader

The reader presents three authored passages from the [history and philosophy of biology chapter](manuscript/unit_0/history_philosophy_biology.md), covering Darwin and Wallace, biological instruments and evidence, and the explanatory role of models. It includes the original cover, the project’s historical timeline, and only the bibliography records cited in the selection. Source text and artwork retain their [CC BY 4.0 license](../LICENSE-CONTENT). The [native manuscript](manuscript/README.md) contains the complete textbook and uses its own project-local renderer.

## Export and check

From a clean textbook checkout with the project’s locked Python environment installed, choose a new absolute path ending in `biology_textbook` for the isolated reader project:

```bash
uv sync --frozen --extra dev
uv run --no-sync python scripts/prepare_foundations_reader.py "$READER_ROOT"
uv run --no-sync python -m pytest -o addopts= -q tests/test_foundations.py::TestHistoryOfBiology
```

The export creates a standalone `docs/manuscript/` source directory from the [reader configuration](manuscript/reader/config.yaml) and writes both images to `output/figures/`. It needs no Node installation or online data. For PDF and HTML, use a separate, initialized [Template checkout](https://github.com/docxology/template/tree/87704feae0a4490ef7dad9c931d268e8c30273c2) pinned to the linked commit, with Pandoc, pandoc-crossref, and a supported LaTeX installation on PATH. From that checkout, register the **exported** project under an unused working name and run:

```bash
git -C "$READER_ROOT" init --quiet
git -C "$READER_ROOT" add docs/manuscript output/figures
ln -s "$READER_ROOT" projects/working/biology_textbook
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/biology_textbook --skip-manuscript-hydration
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/biology_textbook
```

Inspect the combined PDF, the HTML figures and bibliography, and the Stage 04 report under the exported project’s `output/` directory. This check covers the selected reader only. Edition 1.1 has no new deposition. DOI [10.5281/zenodo.20286478](https://doi.org/10.5281/zenodo.20286478) identifies prior release 1.0.0.

## Replay the Unit 0 flowcharts

The optional diagram replay renders the 11 reviewed inline flowcharts from the systems science, complex adaptive systems, and active inference chapters. It uses the committed Mermaid sources and verifies their diagram structure, rendered labels, and PNG decoding. Install the separate npm lock with lifecycle scripts disabled. With Node 24, Inkscape 1.4, DejaVu Sans, and the textbook's locked Python environment available, run from the textbook checkout:

```bash
npm --prefix scripts/unit0_flowcharts ci --ignore-scripts
uv run --no-sync python scripts/prepare_foundations_reader.py --unit0-flowcharts output/unit0-flowcharts
```

Use a new destination for each replay. The output includes exact `.mmd` inputs, SVGs, PNGs, and a hash and diagram-count manifest. The renderer uses Beautiful Mermaid 1.1.3 without a browser. It uses a local font and its layout differs from the native Mermaid CLI. Source changes require review before their checksums are admitted. This command covers the 11 selected flowcharts and leaves native publication verification to the full textbook workflow.
