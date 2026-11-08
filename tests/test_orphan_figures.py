"""Tests for ``biology.pipeline.orphan_figures``."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from biology.pipeline.orphan_figures import (
    FigureInsertion,
    apply_orphan_figures,
    inject,
    load_insertions,
)


def test_catalog_yaml_has_unique_labels_and_pngs() -> None:
    insertions = load_insertions()
    labels = [i.label for i in insertions]
    pngs = [i.png for i in insertions]
    assert len(labels) == len(set(labels)), "duplicate labels in orphan_figures.yaml"
    assert len(pngs) == len(set(pngs)), "duplicate png stems in orphan_figures.yaml"


def test_load_insertions_rejects_incomplete_row(tmp_path: Path) -> None:
    catalog = tmp_path / "bad.yaml"
    catalog.write_text(yaml.safe_dump({"insertions": [{"png": "x", "target": "t.md"}]}), encoding="utf-8")
    with pytest.raises(ValueError, match="missing fields"):
        load_insertions(catalog, manuscript_root=tmp_path)


def test_inject_is_idempotent(tmp_path: Path) -> None:
    chapter = tmp_path / "ch.md"
    chapter.write_text("# X\n\nPunnett Square paragraph.\n\nMore.\n", encoding="utf-8")
    ins = FigureInsertion(
        png="punnett_AaxAa",
        target=chapter,
        anchor="Punnett Square",
        caption="c",
        label="fig:p",
        alt="a",
    )
    assert inject(chapter, ins)
    assert not inject(chapter, ins)


def test_apply_orphan_figures_dry_run_skips_writes(tmp_path: Path) -> None:
    chapter = tmp_path / "ch.md"
    chapter.write_text("# X\n\nPunnett Square here.\n\nMore.\n", encoding="utf-8")
    catalog = tmp_path / "catalog.yaml"
    catalog.write_text(
        yaml.safe_dump(
            {
                "insertions": [
                    {
                        "png": "punnett_AaxAa",
                        "target": "ch.md",
                        "anchor": "Punnett Square",
                        "caption": "c",
                        "label": "fig:p",
                        "alt": "a",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    writes: list[Path] = []
    result = apply_orphan_figures(
        dry_run=True,
        catalog_path=catalog,
        manuscript_root=tmp_path,
        write_fn=lambda p, _t: writes.append(p),
    )
    assert result.inserted == 1
    assert result.total == 1
    assert writes == []


@pytest.mark.parametrize("mention", [
    "The companion generator writes `punnett_AaxAa.png`.",
    "<!-- \\includegraphics{../figures/punnett_AaxAa.png} -->",
    "```latex\n\\includegraphics{../figures/punnett_AaxAa.png}\n```",
    "[Download source image](../figures/punnett_AaxAa.png)",
])
def test_filename_mentions_are_not_embedded_figures(tmp_path: Path, mention: str) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("# Chapter\n\nPunnett Square evidence.\n\n" + mention + "\n", encoding="utf-8")
    ins = FigureInsertion("punnett_AaxAa", chapter, "Punnett Square", "A cross.", "fig:cross", "Four offspring cells.")
    assert inject(chapter, ins)
    after = chapter.read_text(encoding="utf-8")
    assert mention in after
    assert after.count("\\label{fig:cross}") == 1
    assert not inject(chapter, ins)
    assert chapter.read_text(encoding="utf-8") == after


def test_markdown_image_is_an_existing_embed(tmp_path: Path) -> None:
    chapter = tmp_path / "chapter.md"
    original = "# Chapter\n\nPunnett Square.\n\n![Four cells](../figures/punnett_AaxAa.png)\n"
    chapter.write_text(original, encoding="utf-8")
    ins = FigureInsertion("punnett_AaxAa", chapter, "Punnett Square", "A cross.", "fig:cross", "Four cells.")
    assert not inject(chapter, ins)
    assert chapter.read_text(encoding="utf-8") == original


@pytest.mark.parametrize("literal", [
    "<!-- Header anchor -->",
    "```markdown\nHeader anchor\n```",
])
def test_literal_only_anchor_preserves_authored_file(tmp_path: Path, literal: str) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("# Real chapter\n\n" + literal + "\n\nAuthored prose.\n", encoding="utf-8")
    before = chapter.read_bytes()
    stamp = chapter.stat()
    insertion = FigureInsertion("diagram", chapter, "Header anchor", "A diagram.", "fig:proof", "A test diagram.")
    assert not inject(chapter, insertion)
    assert chapter.read_bytes() == before
    assert (chapter.stat().st_mtime_ns, chapter.stat().st_ino) == (stamp.st_mtime_ns, stamp.st_ino)
