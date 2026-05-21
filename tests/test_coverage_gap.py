"""Targeted tests to close the 2.5% coverage gap.

Covers previously untested branches and raises in:
- biology.biochemistry (enzyme_rate_curve, reaction_free_energy raises)
- biology.evolution (isolation_index raises, molecular_clock raises)
- biology.physiology (oxygen_dissociation_curve raise, poiseuille_flow raises)
- biology.botany (water_potential raises, plant_biomass_growth raises, light n_points raise)
- biology.genetics (gc_content empty, hw from dominant_homozygous_freq, chi2 length < 2)
- biology.microbiology (doubling_time_hr raises, mic_fold_dilution raises, growth curve raises)
- biology.neuroscience (HH, cable, synaptic, Hebbian branches)
- mermaid.diagrams (class_diagram, state_diagram, render_to_file fallback)
- mermaid.renderer (render_all, _write_mmd_source)
"""

from __future__ import annotations

from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Biochemistry
# ---------------------------------------------------------------------------

class TestEnzymeRateCurve:
    def test_curve_returns_correct_length(self):
        from biology.biochemistry.biochemistry import enzyme_rate_curve
        curve = enzyme_rate_curve(Vmax=10.0, Km=1.0, n_points=20)
        assert len(curve) == 21  # 0..20 inclusive

    def test_first_point_zero_substrate(self):
        from biology.biochemistry.biochemistry import enzyme_rate_curve
        curve = enzyme_rate_curve(Vmax=10.0, Km=1.0, n_points=10)
        assert curve[0].substrate_concentration == pytest.approx(0.0)
        assert curve[0].reaction_rate == pytest.approx(0.0)

    def test_curve_n_points_zero_raises(self):
        from biology.biochemistry.biochemistry import enzyme_rate_curve
        with pytest.raises(ValueError, match="n_points"):
            enzyme_rate_curve(Vmax=10.0, Km=1.0, n_points=0)

    def test_curve_uses_custom_max_conc(self):
        from biology.biochemistry.biochemistry import enzyme_rate_curve
        curve = enzyme_rate_curve(Vmax=10.0, Km=1.0, n_points=10, max_conc=5.0)
        assert curve[-1].substrate_concentration == pytest.approx(5.0)


class TestReactionFreeEnergy:
    def test_exergonic_reaction(self):
        from biology.biochemistry.biochemistry import reaction_free_energy
        dG = reaction_free_energy(
            delta_G_standard_kJ=-30.5,
            product_conc=0.01,
            reactant_conc=1.0,
            temperature_K=310.0,
        )
        assert dG < 0.0

    def test_zero_product_raises(self):
        from biology.biochemistry.biochemistry import reaction_free_energy
        with pytest.raises(ValueError):
            reaction_free_energy(-30.5, product_conc=0.0, reactant_conc=1.0)

    def test_zero_reactant_raises(self):
        from biology.biochemistry.biochemistry import reaction_free_energy
        with pytest.raises(ValueError):
            reaction_free_energy(-30.5, product_conc=1.0, reactant_conc=0.0)

    def test_zero_temperature_raises(self):
        from biology.biochemistry.biochemistry import reaction_free_energy
        with pytest.raises(ValueError):
            reaction_free_energy(-30.5, product_conc=1.0, reactant_conc=1.0, temperature_K=0.0)


# ---------------------------------------------------------------------------
# Evolution
# ---------------------------------------------------------------------------

class TestIsolationIndexEdgeCases:
    def test_negative_gene_flow_raises(self):
        from biology.evolution.evolution import isolation_index
        with pytest.raises(ValueError):
            isolation_index(gene_flow_rate=-0.1, mutation_rate=0.01)

    def test_negative_mutation_rate_raises(self):
        from biology.evolution.evolution import isolation_index
        with pytest.raises(ValueError):
            isolation_index(gene_flow_rate=0.1, mutation_rate=-0.01)


class TestMolecularClockEdgeCases:
    def test_negative_divergence_raises(self):
        from biology.evolution.evolution import molecular_clock_divergence_time
        with pytest.raises(ValueError):
            molecular_clock_divergence_time(substitution_rate_per_site_per_year=1e-8,
                                            sequence_divergence=-0.01)

    def test_zero_rate_raises(self):
        from biology.evolution.evolution import molecular_clock_divergence_time
        with pytest.raises(ValueError):
            molecular_clock_divergence_time(substitution_rate_per_site_per_year=0.0,
                                            sequence_divergence=0.05)

    def test_zero_divergence_returns_zero(self):
        from biology.evolution.evolution import molecular_clock_divergence_time
        t = molecular_clock_divergence_time(substitution_rate_per_site_per_year=1e-8,
                                            sequence_divergence=0.0)
        assert t == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# Physiology
# ---------------------------------------------------------------------------

class TestPhysiologyEdgeCases:
    def test_oxygen_dissociation_curve_n_points_raise(self):
        from biology.physiology.physiology import oxygen_dissociation_curve
        with pytest.raises(ValueError, match="n_points"):
            oxygen_dissociation_curve(n_points=0)

    def test_oxygen_dissociation_curve_correct_length(self):
        from biology.physiology.physiology import oxygen_dissociation_curve
        curve = oxygen_dissociation_curve(n_points=10)
        assert len(curve) == 11

    def test_poiseuille_zero_length_raises(self):
        from biology.physiology.physiology import poiseuille_flow
        with pytest.raises(ValueError):
            poiseuille_flow(radius_m=0.001, pressure_difference_Pa=100.0, length_m=0.0)

    def test_oxygen_saturation_invalid_hill_raises(self):
        from biology.physiology.physiology import oxygen_saturation
        with pytest.raises(ValueError, match="hill_coefficient"):
            oxygen_saturation(pO2_mmHg=50.0, p50_mmHg=26.0, hill_coefficient=0.0)

    def test_poiseuille_zero_viscosity_raises(self):
        from biology.physiology.physiology import poiseuille_flow
        with pytest.raises(ValueError):
            poiseuille_flow(radius_m=0.001, pressure_difference_Pa=100.0, length_m=0.1,
                            viscosity_Pa_s=0.0)


# ---------------------------------------------------------------------------
# Botany
# ---------------------------------------------------------------------------

class TestBotanyEdgeCases:
    def test_water_potential_zero_concentration_raises(self):
        from biology.botany.botany import water_potential
        with pytest.raises(ValueError):
            water_potential(solute_concentration_M=0.0, turgor_pressure_MPa=0.5)

    def test_water_potential_zero_temperature_raises(self):
        from biology.botany.botany import water_potential
        with pytest.raises(ValueError):
            water_potential(solute_concentration_M=0.1, turgor_pressure_MPa=0.5, temperature_K=0.0)

    def test_photosynthesis_n_points_raise(self):
        from biology.botany.botany import light_response_curve
        with pytest.raises(ValueError):
            light_response_curve(n_points=0)

    def test_plant_growth_invalid_initial_biomass_raises(self):
        from biology.botany.botany import plant_biomass_growth
        with pytest.raises(ValueError):
            plant_biomass_growth(initial_biomass_g=0.0, relative_growth_rate=0.1,
                                 carrying_capacity_g=1000.0, duration_days=30.0)

    def test_plant_growth_invalid_carrying_capacity_raises(self):
        from biology.botany.botany import plant_biomass_growth
        with pytest.raises(ValueError):
            plant_biomass_growth(initial_biomass_g=100.0, relative_growth_rate=0.1,
                                 carrying_capacity_g=50.0, duration_days=30.0)

    def test_plant_growth_invalid_duration_raises(self):
        from biology.botany.botany import plant_biomass_growth
        with pytest.raises(ValueError):
            plant_biomass_growth(initial_biomass_g=100.0, relative_growth_rate=0.1,
                                 carrying_capacity_g=1000.0, duration_days=0.0)

    def test_plant_growth_invalid_rgr_raises(self):
        from biology.botany.botany import plant_biomass_growth
        with pytest.raises(ValueError):
            plant_biomass_growth(initial_biomass_g=100.0, relative_growth_rate=0.0,
                                 carrying_capacity_g=1000.0, duration_days=30.0)

    def test_transpiration_invalid_conductance_units(self):
        from biology.botany.botany import transpiration_flux
        with pytest.raises(ValueError):
            transpiration_flux(
                stomatal_conductance_mol_m2_s=-0.1,
                internal_vapor_conc_mol_m3=0.5,
                external_vapor_conc_mol_m3=0.4,
            )


# ---------------------------------------------------------------------------
# Genetics
# ---------------------------------------------------------------------------

class TestGeneticsEdgeCases:
    def test_gc_content_empty_raises(self):
        from biology.genetics.genetics import gc_content
        with pytest.raises(ValueError):
            gc_content("")

    def test_hw_from_dominant_homozygous_freq(self):
        from biology.genetics.genetics import hardy_weinberg
        # AA frequency = 0.49 → p = 0.7
        hw = hardy_weinberg(dominant_homozygous_freq=0.49)
        assert hw.p == pytest.approx(0.7, abs=1e-4)
        assert hw.q == pytest.approx(0.3, abs=1e-4)

    def test_chi2_less_than_2_categories_raises(self):
        from biology.genetics.genetics import chi_squared_test
        with pytest.raises(ValueError, match="at least 2"):
            chi_squared_test(observed=[50], expected=[50.0])

    def test_hamming_distance_partial(self):
        from biology.genetics.genetics import hamming_distance
        d = hamming_distance("ATCG", "ATGG")
        assert d == 1  # one mismatch (C->G), returns int


# ---------------------------------------------------------------------------
# Microbiology
# ---------------------------------------------------------------------------

class TestMicrobiologyEdgeCases:
    def test_doubling_time_zero_N0_raises(self):
        from biology.microbiology.microbiology import doubling_time
        with pytest.raises(ValueError):
            doubling_time(N0=0.0, Nt=1e9, elapsed_time_hr=6.0)

    def test_doubling_time_nt_le_n0_raises(self):
        from biology.microbiology.microbiology import doubling_time
        with pytest.raises(ValueError):
            doubling_time(N0=1e9, Nt=1e6, elapsed_time_hr=6.0)

    def test_doubling_time_zero_elapsed_raises(self):
        from biology.microbiology.microbiology import doubling_time
        with pytest.raises(ValueError):
            doubling_time(N0=1e6, Nt=1e9, elapsed_time_hr=0.0)

    def test_mic_zero_starting_conc_raises(self):
        from biology.microbiology.microbiology import mic_fold_dilution
        with pytest.raises(ValueError):
            mic_fold_dilution(starting_concentration_ug_mL=0.0, dilution_factor=2, n_tubes=8)

    def test_mic_dilution_factor_too_small_raises(self):
        from biology.microbiology.microbiology import mic_fold_dilution
        with pytest.raises(ValueError):
            mic_fold_dilution(starting_concentration_ug_mL=64.0, dilution_factor=1, n_tubes=8)

    def test_mic_zero_tubes_raises(self):
        from biology.microbiology.microbiology import mic_fold_dilution
        with pytest.raises(ValueError):
            mic_fold_dilution(starting_concentration_ug_mL=64.0, dilution_factor=2, n_tubes=0)

    def test_growth_curve_zero_doubling_time_raises(self):
        from biology.microbiology.microbiology import bacterial_growth_curve
        with pytest.raises(ValueError):
            bacterial_growth_curve(N0=1e6, doubling_time_hr=0.0, t_end_hr=6.0)

    def test_growth_curve_zero_N0_raises(self):
        from biology.microbiology.microbiology import bacterial_growth_curve
        with pytest.raises(ValueError):
            bacterial_growth_curve(N0=0.0, doubling_time_hr=0.5, t_end_hr=6.0)


# ---------------------------------------------------------------------------
# Mermaid Diagrams
# ---------------------------------------------------------------------------

class TestMermaidClassDiagram:
    def test_class_diagram_has_class_keyword(self):
        from mermaid.diagrams import class_diagram
        diagram = class_diagram(
            name="test_class",
            title="Test Class Diagram",
            classes=[("Animal", ["name: str"], ["speak"])],
            relationships=[],
        )
        assert "classDiagram" in diagram.source
        assert "Animal" in diagram.source

    def test_class_diagram_with_relationship(self):
        from mermaid.diagrams import class_diagram
        diagram = class_diagram(
            name="rel_test",
            title="Relationship",
            classes=[("Animal", [], []), ("Dog", [], [])],
            relationships=[("Animal", "<|--", "Dog")],
        )
        assert "Dog" in diagram.source


class TestMermaidStateDiagram:
    def test_state_diagram_has_statediagram(self):
        from mermaid.diagrams import state_diagram
        diagram = state_diagram(
            name="cell_states",
            title="Cell States",
            states=["G1", "S", "G2", "M"],
            transitions=[("G1", "S", "restriction point"), ("S", "G2", ""), ("G2", "M", "")],
            initial_state="G1",
            final_states=["M"],
        )
        assert "stateDiagram" in diagram.source
        assert "G1" in diagram.source
        assert "[*]" in diagram.source


class TestMermaidRendererAll:
    def test_render_all_writes_mmd_files(self, tmp_path: Path):
        from mermaid.diagrams import flowchart
        from mermaid.renderer import MermaidRenderer
        diagrams = [
            flowchart("d1", "A", nodes=[("A", "Start"), ("B", "End")], edges=[("A", "B", "")]),
            flowchart("d2", "B", nodes=[("X", "X"), ("Y", "Y")], edges=[("X", "Y", "")]),
        ]
        r = MermaidRenderer(output_dir=tmp_path)
        paths = r.render_all(diagrams)
        assert len(paths) == 2
        for p in paths:
            assert p.exists()
