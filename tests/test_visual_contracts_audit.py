"""Visual artifact failures and contrast checks using real inputs."""

from __future__ import annotations

from pathlib import Path

import pytest
from PIL import Image

from biology.visual_contracts import VisualRecord, check_records
from biology.visual_contracts.audit import contrast_ratio
from biology.visual_contracts.helpers import dimensions
from biology.visual_contracts.scan import normalise_inline_mermaid_source


def record(**overrides: object) -> VisualRecord:
    fields: dict[str, object] = {
        "kind": "raw_figure", "source_path": "docs/manuscript/unit_I/atoms_molecules.md",
        "line": 10, "label": "fig:unit_I_atoms_demo",
        "caption": "Atomic structure and bonding patterns in carbon compounds",
        "alt": "Diagram of atomic structure showing bonding patterns in carbon",
        "asset_path": "../figures/demo.png", "generator": "plot_demo",
        "width_px": 800, "height_px": 800, "aspect_policy": "figure-square",
    }
    fields.update(overrides)
    return VisualRecord(**fields)  # type: ignore[arg-type]


def test_duplicate_labels_across_sources_are_rejected() -> None:
    first = record()
    second = record(source_path="docs/manuscript/unit_II/cell_structure.md", line=20)
    assert any(f.code == "duplicate-label" for f in check_records([first, second]))


def test_live_unit_path_requires_unit_scoped_label() -> None:
    assert any(f.code == "unit-prefixed-label" for f in check_records([record(label="fig:wrong")]))


def test_missing_or_corrupt_asset_cannot_pass_on_absent_dimensions() -> None:
    findings = check_records([record(width_px=0, height_px=0)])
    assert any(f.code == "unavailable-png" for f in findings)


@pytest.mark.parametrize("kind", ["missing", "corrupt", "renamed-jpeg", "truncated-png"])
def test_unavailable_asset_has_no_fabricated_dimensions(tmp_path: Path, kind: str) -> None:
    path = tmp_path / "asset.png"
    if kind == "corrupt":
        path.write_bytes(b"not an image")
    elif kind == "renamed-jpeg":
        Image.new("RGB", (20, 30), "white").save(path, format="JPEG")
    elif kind == "truncated-png":
        Image.new("RGB", (20, 30), "white").save(path)
        path.write_bytes(path.read_bytes()[:35])
    assert dimensions(str(path)) == (0, 0)


def test_dimensions_decode_the_actual_png(tmp_path: Path) -> None:
    path = tmp_path / "asset.png"
    Image.new("RGB", (41, 67), "white").save(path)
    assert dimensions(str(path)) == (41, 67)


def test_missing_caption_and_alt_remain_blocking() -> None:
    codes = {f.code for f in check_records([record(caption="", alt="")])}
    assert {"missing-caption", "missing-alt"} <= codes


def test_domain_inconsistent_caption_and_alt_are_flagged() -> None:
    findings = check_records([record(caption="Mitochondrial proton gradient dynamics",
                                    alt="Botanical leaf venation pattern schematic")])
    assert any(f.code == "caption-alt-drift" for f in findings)


@pytest.mark.parametrize("policy,width,height,code", [
    ("figure-square", 1200, 400, "figure-square-aspect"),
    ("figure-landscape", 400, 400, "figure-landscape-aspect"),
    ("mermaid-square", 2000, 400, "mermaid-square-aspect"),
])
def test_explicit_aspect_contracts(policy: str, width: int, height: int, code: str) -> None:
    findings = check_records([record(aspect_policy=policy, width_px=width, height_px=height)])
    assert any(f.code == code for f in findings)


def test_real_style_declaration_reports_insufficient_contrast(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    path = tmp_path / "contrast.md"
    path.write_text("```mermaid\nflowchart TD\n A[Input] --> B[Output]\n"
                    " style A fill:#aaaaaa,stroke:#bbbbbb\n```\n", encoding="utf-8")
    monkeypatch.setattr("biology.visual_contracts.audit.MANUSCRIPT_DIR", tmp_path)
    findings = check_records([])
    assert any(f.code == "mermaid-low-contrast" and f.source_path.endswith("/contrast.md") for f in findings)
    assert contrast_ratio("#ffffff", "#000000") == pytest.approx(21)


def test_explicit_source_line_break_survives_standalone_normalization(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("BIOLOGY_TEXTBOOK_TEMPLATE_ROOT", raising=False)
    normalized = normalise_inline_mermaid_source('flowchart TD\n A["Cell\\nmembrane"] --> B["Response"]')
    assert "Cell<br/>membrane" in normalized
    assert r"\n" not in normalized


def test_inline_publication_requires_real_cli(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from biology.visual_contracts import render_inline_mermaid_assets

    monkeypatch.setenv("PATH", str(tmp_path / "empty-bin"))
    with pytest.raises(RuntimeError):
        render_inline_mermaid_assets(tmp_path / "figures")
