"""Real PNG artifact and CLI failure contracts; no mocked renderer results."""

from __future__ import annotations

import os
import shutil
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pytest
from PIL import Image

from mermaid import (
    MermaidRenderer,
    flowchart,
    pie_chart,
    sequence_diagram,
    state_diagram,
)
from mermaid.renderer import _find_puppeteer_config
from visualization.plots import ALL_FIGURE_GENERATORS, FIGURE_ASPECT


def require_mermaid_cli() -> None:
    if shutil.which("mmdc") is None:
        pytest.skip("real Mermaid CLI is unavailable")


def test_missing_cli_is_a_failure_in_strict_mode(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PATH", str(tmp_path / "empty-bin"))
    source = "flowchart TD\n  A[Input] --> B[Output]"
    fallback = MermaidRenderer(tmp_path / "review").render("review", source)
    assert fallback.suffix == ".mmd"
    assert not fallback.with_suffix(".png").exists()
    with pytest.raises(RuntimeError):
        MermaidRenderer(tmp_path / "publication", strict_png=True).render("publication", source)


@pytest.mark.parametrize("bad_name", ["", "..", "../escape", r"..\escape"])
def test_diagram_name_cannot_escape_output_directory(tmp_path: Path, bad_name: str) -> None:
    renderer = MermaidRenderer(tmp_path / "rendered")
    with pytest.raises(ValueError):
        renderer.render(bad_name, "flowchart TD\n A-->B")
    assert not (tmp_path / "escape.mmd").exists()


def test_absolute_diagram_name_is_refused(tmp_path: Path) -> None:
    renderer = MermaidRenderer(tmp_path / "rendered")
    with pytest.raises(ValueError):
        renderer.render(str(tmp_path / "escape"), "flowchart TD\n A-->B")
    assert not (tmp_path / "escape.mmd").exists()


def test_puppeteer_configuration_is_project_scoped(tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()
    (tmp_path / ".puppeteer.json").write_text("{}", encoding="utf-8")
    assert _find_puppeteer_config(project) is None
    selected = project / ".puppeteer.json"
    selected.write_text("{}", encoding="utf-8")
    assert _find_puppeteer_config(project) == selected


@pytest.mark.parametrize("diagram", [
    flowchart("flow", "Transfer", [("A", "Input"), ("B", "Output")], [("A", "B", "transfer")]),
    sequence_diagram("sequence", "Binding", ["Ligand", "Receptor"], [("Ligand", "Receptor", "binds")]),
    state_diagram("state", "Cycle", ["G1", "S"], [("G1", "S", "replication")]),
    pie_chart("pie", "Counts", [("A", 3.0), ("B", 1.0)]),
], ids=lambda diagram: diagram.name)
def test_public_diagram_builders_produce_real_pngs(tmp_path: Path, diagram) -> None:
    require_mermaid_cli()
    path = MermaidRenderer(tmp_path, strict_png=True).render(diagram.name, diagram.source)
    with Image.open(path) as image:
        assert image.format == "PNG"
        image.load()
        assert image.width == image.height
        assert cast(tuple[int, int], image.convert("L").getextrema())[0] < 200


@pytest.mark.parametrize("strict", [False, True])
def test_invalid_source_cannot_be_reported_as_a_stale_success(tmp_path: Path, strict: bool) -> None:
    require_mermaid_cli()
    previous = tmp_path / "broken.png"
    Image.new("RGB", (30, 30), "white").save(previous)
    before = previous.read_bytes()
    renderer = MermaidRenderer(tmp_path, strict_png=strict)
    if strict:
        with pytest.raises(RuntimeError):
            renderer.render("broken", "this is not Mermaid syntax")
    else:
        assert renderer.render("broken", "this is not Mermaid syntax").suffix == ".mmd"
    assert previous.read_bytes() == before
    assert not list(tmp_path.glob(".broken-*.png"))


def test_explicit_unsquared_output_retains_rectangular_diagram(tmp_path: Path) -> None:
    require_mermaid_cli()
    path = MermaidRenderer(tmp_path, strict_png=True).render(
        "wide", "flowchart LR\n A[Input] --> B[Transfer] --> C[Output]", square=False
    )
    with Image.open(path) as image:
        image.load()
        assert image.width > 2 * image.height


@pytest.mark.parametrize("generator", [generator for _name, generator in ALL_FIGURE_GENERATORS],
                         ids=[name for name, _generator in ALL_FIGURE_GENERATORS])
def test_registered_figures_are_decodable_pngs_in_requested_destination(
    tmp_path: Path, generator: Callable[..., Path]
) -> None:
    path = generator(output_dir=tmp_path)
    assert path.parent == tmp_path
    with Image.open(path) as image:
        assert image.format == "PNG"
        image.load()
        assert cast(tuple[int, int], image.convert("L").getextrema())[0] < 200
        ratio = image.width / image.height
        if FIGURE_ASPECT.get(path.stem) == "landscape":
            assert 1.05 <= ratio <= 3.5
        else:
            assert 0.85 <= ratio <= 1.18


@pytest.mark.parametrize("alias_kind", ["symlink", "hardlink"])
def test_shared_figure_writer_cannot_overwrite_an_aliased_source(
    tmp_path: Path, alias_kind: str,
) -> None:
    from visualization.plots_evolution import plot_fitness_landscape

    source = tmp_path / "authored.md"
    source.write_bytes(b"authored science, not a generated image\n")
    figures = tmp_path / "figures"
    figures.mkdir()
    alias = figures / "fitness_landscape.png"
    if alias_kind == "symlink":
        alias.symlink_to(source)
    else:
        alias.hardlink_to(source)
    unknown = figures / "author-note.txt"
    unknown.write_bytes(b"unrelated output note\n")
    before = set(figures.iterdir())
    with pytest.raises(ValueError):
        plot_fitness_landscape(figures)
    assert source.read_bytes() == b"authored science, not a generated image\n"
    assert unknown.read_bytes() == b"unrelated output note\n"
    assert set(figures.iterdir()) == before
    assert alias.samefile(source)


def test_failed_figure_publication_preserves_previous_image_and_unknown_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    from visualization.plots_evolution import plot_fitness_landscape

    target = tmp_path / "fitness_landscape.png"
    Image.new("RGB", (20, 20), "white").save(target)
    previous = target.read_bytes()
    unknown = tmp_path / "author-note.txt"
    unknown.write_bytes(b"unrelated output note\n")
    before = set(tmp_path.iterdir())
    replace = os.replace

    def refuse_publication(source: str | Path, destination: str | Path) -> None:
        if Path(destination) == target:
            raise OSError("owned publication failure fixture")
        replace(source, destination)

    monkeypatch.setattr(os, "replace", refuse_publication)
    with pytest.raises(OSError):
        plot_fitness_landscape(tmp_path)
    assert target.read_bytes() == previous
    assert unknown.read_bytes() == b"unrelated output note\n"
    assert set(tmp_path.iterdir()) == before
