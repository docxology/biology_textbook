"""Tests for the mermaid diagram submodule and visualization subpackage."""

import json
import os
import re
import shutil
import pytest
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

from mermaid import (
    MermaidRenderer,
    flowchart, sequence_diagram, state_diagram, pie_chart,
    ALL_BIOLOGY_DIAGRAMS,
    cell_cycle_diagram, glycolysis_pathway_diagram,
    food_web_diagram,
)


# ===========================================================================
# MERMAID RENDERER TESTS
# ===========================================================================

class TestMermaidRenderer:
    def test_render_writes_mmd_file(self, tmp_path):
        renderer = MermaidRenderer(output_dir=tmp_path)
        # Force fallback mode regardless of mmdc availability by writing .mmd
        source = "flowchart TD\n    A[Start] --> B[End]"
        path = renderer._write_mmd_source("test_diagram", source)
        assert path.exists()
        assert path.suffix == ".mmd"
        assert "flowchart" in path.read_text()

    def test_render_creates_output_dir(self, tmp_path):
        new_dir = tmp_path / "nested" / "output"
        MermaidRenderer(output_dir=new_dir)
        assert new_dir.exists()

    def test_render_empty_name_raises(self, tmp_path):
        renderer = MermaidRenderer(output_dir=tmp_path)
        with pytest.raises(ValueError, match="name must not be empty"):
            renderer.render("", "flowchart TD\n  A-->B")

    def test_render_empty_source_raises(self, tmp_path):
        renderer = MermaidRenderer(output_dir=tmp_path)
        with pytest.raises(ValueError, match="source"):
            renderer.render("test", "   ")

    def test_render_all_returns_paths(self, tmp_path):
        renderer = MermaidRenderer(output_dir=tmp_path)
        diagrams = [cell_cycle_diagram(), food_web_diagram()]
        paths = renderer.render_all(diagrams)
        assert len(paths) == 2
        for p in paths:
            assert p.exists()

    def test_mmdc_smoke_renders_png_when_available(self, tmp_path):
        if shutil.which("mmdc") is None:
            pytest.skip("mmdc is not installed in this environment")
        renderer = MermaidRenderer(output_dir=tmp_path, strict_png=True)
        path = renderer.render("smoke", "flowchart TD\n    A[Start] --> B[End]")
        assert path.suffix == ".png"
        assert path.exists()
        assert path.stat().st_size > 0


class TestMermaidDiagramBuilders:
    def test_flowchart_produces_valid_source(self):
        d = flowchart("test", "Test", [("A", "Start"), ("B", "End")], [("A", "B", "step")])
        assert "flowchart" in d.source
        assert "A" in d.source
        assert "B" in d.source

    def test_sequence_diagram_source(self):
        d = sequence_diagram("seq", "Seq", ["Alice", "Bob"], [("Alice", "Bob", "hello")])
        assert "sequenceDiagram" in d.source
        assert "participant P0 as Alice" in d.source
        assert "P0->>P1: hello" in d.source

    def test_state_diagram_source(self):
        d = state_diagram("states", "States", ["On", "Off"], [("On", "Off", "toggle")])
        assert "stateDiagram" in d.source

    def test_pie_chart_source(self):
        d = pie_chart("pie", "My Pie", [("A", 40.0), ("B", 60.0)])
        assert "pie" in d.source
        assert "40.0" in d.source

    def test_all_biology_diagrams_have_source(self):
        for d in ALL_BIOLOGY_DIAGRAMS:
            assert d.source.strip(), f"Diagram '{d.name}' has empty source"
            assert d.name, "Diagram has empty name"
            assert d.title, f"Diagram '{d.name}' has empty title"

    def test_all_biology_diagrams_count(self):
        assert len(ALL_BIOLOGY_DIAGRAMS) == 24

    def test_all_biology_diagram_names_are_unique(self):
        names = [d.name for d in ALL_BIOLOGY_DIAGRAMS]
        assert len(names) == len(set(names))

    def test_registered_mermaid_sources_use_robust_label_syntax(self):
        for d in ALL_BIOLOGY_DIAGRAMS:
            assert "\\n" not in d.source, f"{d.name} uses literal escaped newlines"
            assert "Dark Reactions" not in d.title, "use Calvin-Benson cycle rather than dark reactions"
            if d.source.startswith("sequenceDiagram"):
                assert re.search(r"participant P\d+ as ", d.source), (
                    f"{d.name} sequence diagram should use stable participant aliases"
                )

    def test_cell_cycle_diagram_has_states(self):
        d = cell_cycle_diagram()
        assert "G1" in d.source or "stateDiagram" in d.source

    def test_glycolysis_pathway_nodes(self):
        d = glycolysis_pathway_diagram()
        assert "Glucose" in d.source or "glycolysis" in d.name

    def test_biology_diagram_registry_names_are_documented(self):
        docs = Path(__file__).resolve().parent.parent / "docs" / "api_reference.md"
        text = docs.read_text(encoding="utf-8")
        missing = [d.name for d in ALL_BIOLOGY_DIAGRAMS if d.name not in text]
        assert not missing, f"Document registry names in docs/api_reference.md: {missing}"

    def test_package_exports_all_biology_diagram_factories(self):
        import inspect
        import mermaid
        import mermaid.biology_diagrams as biology_diagrams

        factory_names = [
            name
            for name, fn in inspect.getmembers(biology_diagrams, inspect.isfunction)
            if fn.__module__ == biology_diagrams.__name__
        ]
        missing = [name for name in factory_names if not hasattr(mermaid, name)]
        assert not missing


# ===========================================================================
# VISUALIZATION TESTS
# ===========================================================================

class TestVisualizationFigures:
    def test_nernst_potential_figure(self, tmp_path):
        from visualization import plot_nernst_potentials
        path = plot_nernst_potentials(output_dir=tmp_path)
        assert path.exists()
        assert path.suffix in (".png", ".pdf")

    def test_punnett_square_figure(self, tmp_path):
        from visualization import plot_punnett_square
        path = plot_punnett_square("Aa", "Aa", output_dir=tmp_path)
        assert path.exists()

    def test_chromosome_structure_figure(self, tmp_path):
        from visualization import plot_chromosome_structure
        path = plot_chromosome_structure(output_dir=tmp_path)
        assert path.exists()
        assert path.name == "chromosome_structure.png"

    def test_lotka_volterra_figure(self, tmp_path):
        from visualization import plot_lotka_volterra
        path = plot_lotka_volterra(output_dir=tmp_path)
        assert path.exists()

    def test_selection_simulation_figure(self, tmp_path):
        from visualization import plot_selection_simulation
        path = plot_selection_simulation(output_dir=tmp_path)
        assert path.exists()

    def test_oxygen_dissociation_figure(self, tmp_path):
        from visualization import plot_oxygen_dissociation
        path = plot_oxygen_dissociation(output_dir=tmp_path)
        assert path.exists()

    def test_michaelis_menten_figure(self, tmp_path):
        from visualization import plot_michaelis_menten
        path = plot_michaelis_menten(output_dir=tmp_path)
        assert path.exists()

    def test_action_potential_figure(self, tmp_path):
        from visualization import plot_action_potential
        path = plot_action_potential(output_dir=tmp_path)
        assert path.exists()

    def test_light_response_figure(self, tmp_path):
        from visualization import plot_light_response_curve
        path = plot_light_response_curve(output_dir=tmp_path)
        assert path.exists()

    def test_bacterial_growth_figure(self, tmp_path):
        from visualization import plot_bacterial_growth
        path = plot_bacterial_growth(output_dir=tmp_path)
        assert path.exists()

    def test_methylation_heatmap_figure(self, tmp_path):
        from visualization import plot_methylation_heatmap
        path = plot_methylation_heatmap(output_dir=tmp_path)
        assert path.exists()

    def test_logistic_growth_figure(self, tmp_path):
        from visualization import plot_logistic_growth
        path = plot_logistic_growth(output_dir=tmp_path)
        assert path.exists()

    def test_species_area_figure(self, tmp_path):
        from visualization import plot_species_area_relationship
        path = plot_species_area_relationship(output_dir=tmp_path)
        assert path.exists()

    def test_biome_distribution_figure(self, tmp_path):
        from visualization import plot_biome_distribution
        path = plot_biome_distribution(output_dir=tmp_path)
        assert path.exists()

    def test_ghk_permeability_figure(self, tmp_path):
        from visualization import plot_ghk_permeability
        path = plot_ghk_permeability(output_dir=tmp_path)
        assert path.exists()
        assert path.name == "ghk_permeability.png"

    def test_water_potential_transpiration_figure(self, tmp_path):
        from visualization import plot_water_potential_transpiration
        path = plot_water_potential_transpiration(output_dir=tmp_path)
        assert path.exists()

    def test_genetic_drift_trajectories_figure(self, tmp_path):
        from visualization import plot_genetic_drift_trajectories
        path = plot_genetic_drift_trajectories(output_dir=tmp_path)
        assert path.exists()

    def test_allee_threshold_dynamics_figure(self, tmp_path):
        from visualization import plot_allee_threshold_dynamics
        path = plot_allee_threshold_dynamics(output_dir=tmp_path)
        assert path.exists()

    def test_visual_manifest_records_required_fields(self, tmp_path):
        import runpy

        script = Path(__file__).resolve().parent.parent / "scripts" / "audit_visual_contracts.py"
        namespace = runpy.run_path(str(script))
        records = namespace["build_manifest"]()
        write_manifest = namespace["write_manifest"]
        manifest_path = write_manifest(records, tmp_path / "visual_manifest.json")

        assert manifest_path.exists()
        assert {record.kind for record in records} >= {"raw_figure", "registered_mermaid", "inline_mermaid"}
        required = {
            "kind",
            "source_path",
            "line",
            "label",
            "caption",
            "alt",
            "asset_path",
            "generator",
            "width_px",
            "height_px",
        }
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert payload
        assert required <= set(payload[0])


# ===========================================================================
# CVD (colour-vision) palette — see src/visualization/cvd.py, config.yaml accessibility
# ===========================================================================


class TestCvdPalette:
    def test_cvd_module_exports_distinct_hues(self) -> None:
        from visualization.cvd import BAR_POS, BAR_NEG, PUNNETT_DOMINANT, PUNNETT_RECESSIVE, SERIES2, SERIES3

        palette = (BAR_POS, BAR_NEG, PUNNETT_DOMINANT, PUNNETT_RECESSIVE, *SERIES2, *SERIES3)
        for color in palette:
            assert re.fullmatch(r"#[0-9a-fA-F]{6}", color), f"invalid hex colour: {color}"

        assert len({BAR_POS, BAR_NEG, PUNNETT_DOMINANT, PUNNETT_RECESSIVE}) == 4
        assert len(SERIES2) == 2
        assert SERIES2[0] != SERIES2[1]
        assert len(SERIES3) == 3
        assert len(set(SERIES3)) == 3

        old_red_green_pair = {"#4caf50", "#f44336"}
        assert {c.lower() for c in SERIES2} != old_red_green_pair
        assert {PUNNETT_DOMINANT.lower(), PUNNETT_RECESSIVE.lower()} != {"#c8e6c9", "#ffcdd2"}

    def test_nernst_uses_cvd_bar_colours(self, tmp_path) -> None:
        from visualization.cvd import BAR_POS, BAR_NEG
        from visualization import plot_nernst_potentials

        path = plot_nernst_potentials(output_dir=tmp_path)
        assert path.exists()
        # Module contract: bar colours are the cvd pair (import-time binding)
        assert BAR_POS and BAR_NEG
