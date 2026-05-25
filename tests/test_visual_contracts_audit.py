"""Unit tests for visual contract audit helpers and check_records branches."""

from __future__ import annotations

from pathlib import Path

import pytest

from biology.visual_contracts import (
    VisualRecord,
    _contrast_ratio,
    _normalise_inline_mermaid_source,
    _review_action,
    check_records,
    write_review_matrix,
)


def _record(**overrides: object) -> VisualRecord:
    base = {
        "kind": "raw_figure",
        "source_path": "manuscript/unit_I/atoms_molecules.md",
        "line": 10,
        "label": "fig:unit_I_atoms_demo",
        "caption": "Atomic structure and bonding patterns in carbon compounds",
        "alt": "Diagram of atomic structure showing bonding patterns in carbon",
        "asset_path": "figures/demo.png",
        "generator": "plot_demo",
        "width_px": 800,
        "height_px": 800,
        "aspect_policy": "figure-square",
        "aspect_exception": "",
    }
    base.update(overrides)
    return VisualRecord(**base)  # type: ignore[arg-type]


def test_check_records_flags_duplicate_labels() -> None:
    first = _record(label="fig:dup")
    second = _record(label="fig:dup", line=20)
    findings = check_records([first, second])
    assert any(f.code == "duplicate-label" for f in findings)


def test_check_records_flags_unit_label_mismatch() -> None:
    bad = _record(label="fig:wrong_prefix", source_path="manuscript/unit_I/chapter.md")
    findings = check_records([bad])
    assert any(f.code == "unit-prefixed-label" for f in findings)


def test_check_records_flags_missing_caption_and_alt() -> None:
    missing = _record(caption="", alt="")
    findings = check_records([missing])
    codes = {f.code for f in findings}
    assert "missing-caption" in codes
    assert "missing-alt" in codes


def test_check_records_flags_caption_alt_drift() -> None:
    drift = _record(
        caption="Mitochondrial oxidative phosphorylation proton gradient dynamics",
        alt="Unrelated botanical leaf venation pattern schematic overview",
    )
    findings = check_records([drift])
    assert any(f.code == "caption-alt-drift" for f in findings)


def test_check_records_aspect_policies() -> None:
    square_bad = _record(width_px=1200, height_px=400, aspect_policy="figure-square")
    landscape_bad = _record(width_px=400, height_px=400, aspect_policy="figure-landscape")
    mermaid_bad = _record(
        kind="inline_mermaid",
        width_px=2000,
        height_px=400,
        aspect_policy="mermaid-square",
        label="mermaid-inline:demo",
    )
    findings = check_records([square_bad, landscape_bad, mermaid_bad])
    codes = {f.code for f in findings}
    assert "figure-square-aspect" in codes
    assert "figure-landscape-aspect" in codes
    assert "mermaid-square-aspect" in codes


def test_check_records_skips_aspect_when_exception_set() -> None:
    ok = _record(width_px=2000, height_px=400, aspect_exception="wide timeline panel")
    findings = [f for f in check_records([ok]) if "aspect" in f.code]
    assert findings == []


def test_review_action_and_matrix_for_missing_asset(tmp_path: Path) -> None:
    record = _record(width_px=0, height_px=0)
    assert _review_action(record) == "square-padded by matplotlib save helper"
    assert _review_action(_record(kind="registered_mermaid")) == "square viewport plus PNG padding"
    assert _review_action(_record(kind="inline_mermaid")) == "rendered through inline Mermaid review path"
    assert _review_action(_record(kind="other")) == "measured"

    path = write_review_matrix([record], tmp_path / "matrix.md")
    text = path.read_text(encoding="utf-8")
    assert "asset missing" in text
    assert "Visual Review Matrix" in text


def test_contrast_ratio_computes_luminance_difference() -> None:
    assert _contrast_ratio("#ffffff", "#000000") > 10.0
    assert _contrast_ratio("#aaaaaa", "#aaaaaa") == 1.0


def test_check_records_flags_mermaid_low_contrast(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeMatch:
        def group(self, name: str) -> str:
            if name == "props":
                return "fill:#aaaaaa,stroke:#bbbbbb"
            raise KeyError(name)

    class FakeStyleRe:
        @staticmethod
        def search(line: str) -> FakeMatch | None:
            return FakeMatch() if "style" in line else None

    monkeypatch.setattr("biology.visual_contracts._STYLE_COLOR_RE", FakeStyleRe)
    monkeypatch.setattr(
        "biology.visual_contracts._mermaid_sources",
        lambda: [("manuscript/unit_I/demo.md", 2, "flowchart TD\n  style A fill:#aaa,stroke:#bbb")],
    )
    monkeypatch.setattr("biology.visual_contracts._contrast_ratio", lambda _a, _b: 1.5)
    findings = check_records([])
    assert any(f.code == "mermaid-low-contrast" for f in findings)


def test_mermaid_newline_escape_finding(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "biology.visual_contracts._mermaid_sources",
        lambda: [("src/mermaid/biology_diagrams.py", 1, "flowchart TD\\n  A-->B")],
    )
    findings = check_records([])
    assert any(f.code == "mermaid-newline-escape" for f in findings)


def test_normalise_inline_mermaid_without_infrastructure(monkeypatch: pytest.MonkeyPatch) -> None:
    def broken_import(_name: str):
        raise ImportError("no infrastructure in unit test")

    monkeypatch.setattr("biology.visual_contracts.import_module", broken_import)
    result = _normalise_inline_mermaid_source("flowchart TD\\n  A-->B")
    assert "<br/>" in result


def test_render_inline_mermaid_assets_requires_mmdc(monkeypatch: pytest.MonkeyPatch) -> None:
    from biology.visual_contracts import render_inline_mermaid_assets

    monkeypatch.setattr("biology.visual_contracts.shutil.which", lambda _name: None)
    with pytest.raises(RuntimeError, match="mmdc"):
        render_inline_mermaid_assets()


def test_write_manifest_round_trip(tmp_path: Path) -> None:
    from biology.visual_contracts import write_manifest

    record = _record(asset_path="figures/demo.png")
    path = write_manifest([record], tmp_path / "manifest.json")
    payload = path.read_text(encoding="utf-8")
    assert "fig:unit_I_atoms_demo" in payload


def test_dimensions_returns_fallback_for_missing_asset() -> None:
    from biology.visual_contracts import _dimensions

    assert _dimensions("../figures/missing.png", fallback=(10, 20)) == (10, 20)


def test_first_alt_and_caption_after_mermaid_fence() -> None:
    from biology.visual_contracts import _first_alt_after, _first_caption_after_mermaid

    text = "\n".join(
        [
            "```mermaid",
            "flowchart TD",
            "  A-->B",
            "```",
            "<!-- alt: Directed graph from receptor to response node. -->",
            "",
            "*Signal flow from receptor activation to downstream response.*",
        ]
    )
    fence_end = text.index("```", len("```mermaid")) + 3
    assert "receptor" in _first_alt_after(text, fence_end).lower()
    assert "Signal flow" in _first_caption_after_mermaid(text, fence_end)
