"""Tests for ``biology.pipeline.orphan_figures``."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from biology.pipeline.orphan_figures import (
    CATALOG_PATH,
    FigureInsertion,
    apply_orphan_figures,
    inject,
    load_insertions,
)


def test_catalog_yaml_loads_into_records() -> None:
    insertions = load_insertions()
    assert len(insertions) >= 18
    assert all(isinstance(i, FigureInsertion) for i in insertions)
    pngs = {i.png for i in insertions}
    assert "punnett_AaxAa" in pngs
    assert "logistic_growth" in pngs


def test_catalog_yaml_has_unique_labels_and_pngs() -> None:
    insertions = load_insertions()
    labels = [i.label for i in insertions]
    pngs = [i.png for i in insertions]
    assert len(labels) == len(set(labels)), "duplicate labels in orphan_figures.yaml"
    assert len(pngs) == len(set(pngs)), "duplicate png stems in orphan_figures.yaml"


def test_catalog_yaml_rows_have_required_fields() -> None:
    raw = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))
    required = {"png", "target", "anchor", "caption", "label", "alt"}
    for row in raw["insertions"]:
        missing = required - set(row)
        assert not missing, f"row {row.get('png')} missing fields {missing}"


def test_load_insertions_rejects_incomplete_row(tmp_path: Path) -> None:
    catalog = tmp_path / "bad.yaml"
    catalog.write_text(yaml.safe_dump({"insertions": [{"png": "x", "target": "t.md"}]}), encoding="utf-8")
    with pytest.raises(ValueError, match="missing fields"):
        load_insertions(catalog, manuscript_root=tmp_path)


def test_inject_writes_figure_block_after_anchor(tmp_path: Path) -> None:
    chapter = tmp_path / "ch.md"
    chapter.write_text("# Chapter\n\nHere is the Punnett Square section.\n\nMore text.\n", encoding="utf-8")
    ins = FigureInsertion(
        png="punnett_AaxAa",
        target=chapter,
        anchor="Punnett Square",
        caption="Caption.",
        label="fig:demo",
        alt="Alt.",
    )
    assert inject(chapter, ins)
    body = chapter.read_text(encoding="utf-8")
    assert "../figures/punnett_AaxAa.png" in body
    assert "\\label{fig:demo}" in body
    assert "<!-- alt: Alt." in body


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
