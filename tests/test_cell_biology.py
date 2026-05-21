"""Tests for cell biology module — Unit I/II."""

import pytest

from biology.cell import (
    IonConcentration,
    ORGANELLES, get_organelles_by_cell_type,
    count_membrane_bound_organelles,
    nernst_potential,
    goldman_equation,
    osmotic_pressure,
    diffusion_flux,
    compute_all_nernst_potentials,
    hill_equation,
    receptor_occupancy,
    signal_amplification,
)


# ---------------------------------------------------------------------------
# Organelle inventory
# ---------------------------------------------------------------------------

class TestOrganelleInventory:
    def test_organelle_count(self):
        assert len(ORGANELLES) >= 10

    def test_cell_types_prokaryote(self):
        prokaryote_organelles = get_organelles_by_cell_type("prokaryote")
        names = [o.name for o in prokaryote_organelles]
        assert "Ribosome" in names
        assert "Nucleus" not in names

    def test_cell_types_plant(self):
        plant_organelles = get_organelles_by_cell_type("plant")
        names = [o.name for o in plant_organelles]
        assert "Chloroplast" in names
        assert "Nucleus" in names
        assert "Mitochondria" in names

    def test_cell_types_animal(self):
        animal_organelles = get_organelles_by_cell_type("animal")
        names = [o.name for o in animal_organelles]
        assert "Lysosome" in names
        assert "Chloroplast" not in names

    def test_invalid_cell_type_raises(self):
        with pytest.raises(ValueError, match="Unknown cell_type"):
            get_organelles_by_cell_type("alien")

    def test_count_membrane_bound(self):
        plant_organelles = get_organelles_by_cell_type("plant")
        count = count_membrane_bound_organelles(plant_organelles)
        assert count >= 5   # nucleus, mito, chloroplast, ER, Golgi, etc.

    def test_organelle_summary(self):
        for org in ORGANELLES:
            summary = org.summary()
            assert org.name in summary
            assert len(summary) > 10

    def test_plant_has_no_centriole(self):
        plant = get_organelles_by_cell_type("plant")
        names = [o.name for o in plant]
        assert "Centriole" not in names


# ---------------------------------------------------------------------------
# Nernst Equation
# ---------------------------------------------------------------------------

class TestNernstPotential:
    def test_potassium_nernst(self):
        """K⁺ inside 140 mM, outside 5 mM at 310 K → Nernst ≈ -90 mV."""
        ion = IonConcentration("K⁺", +1, inside_mM=140.0, outside_mM=5.0)
        E = nernst_potential(ion, temperature_K=310.0)
        assert -100 < E < -80, f"K⁺ Nernst expected ~-90 mV, got {E:.2f}"

    def test_sodium_nernst(self):
        """Na⁺ inside 12 mM, outside 145 mM → Nernst ≈ +60 mV."""
        ion = IonConcentration("Na⁺", +1, inside_mM=12.0, outside_mM=145.0)
        E = nernst_potential(ion, temperature_K=310.0)
        assert 50 < E < 70, f"Na⁺ Nernst expected ~+60 mV, got {E:.2f}"

    def test_chloride_nernst_negative(self):
        """Cl⁻ reversal potential is negative."""
        ion = IonConcentration("Cl⁻", -1, inside_mM=4.0, outside_mM=110.0)
        E = nernst_potential(ion, temperature_K=310.0)
        assert E < -50

    def test_nernst_zero_charge_raises(self):
        ion = IonConcentration("X", 0, inside_mM=10.0, outside_mM=10.0)
        with pytest.raises(ValueError):
            nernst_potential(ion)

    def test_nernst_zero_concentration_raises(self):
        ion = IonConcentration("Y", +1, inside_mM=0.0, outside_mM=10.0)
        with pytest.raises(ValueError):
            nernst_potential(ion)

    def test_nernst_negative_temperature_raises(self):
        ion = IonConcentration("Z", +1, inside_mM=10.0, outside_mM=5.0)
        with pytest.raises(ValueError):
            nernst_potential(ion, temperature_K=-1.0)

    def test_equal_concentrations_gives_zero(self):
        ion = IonConcentration("Sym", +1, inside_mM=10.0, outside_mM=10.0)
        E = nernst_potential(ion)
        assert abs(E) < 1e-6

    def test_compute_all_nernst_potentials(self):
        results = compute_all_nernst_potentials()
        assert "K⁺" in results
        assert "Na⁺" in results
        assert results["K⁺"] < 0
        assert results["Na⁺"] > 0

    def test_compute_all_skips_invalid_ion(self):
        """Ions that violate nernst_potential preconditions are omitted (warning path)."""
        bad = IonConcentration("Bad", +1, inside_mM=0.0, outside_mM=10.0)
        good = IonConcentration("Good", +1, inside_mM=10.0, outside_mM=5.0)
        results = compute_all_nernst_potentials(ions=[bad, good])
        assert "Bad" not in results
        assert "Good" in results


# ---------------------------------------------------------------------------
# Goldman Equation
# ---------------------------------------------------------------------------

class TestGoldmanEquation:
    def test_typical_resting_potential(self):
        """Goldman equation with physiological ions gives ≈ -70 mV resting."""
        ions = [
            IonConcentration("K⁺",  +1, inside_mM=140.0, outside_mM=5.0),
            IonConcentration("Na⁺", +1, inside_mM=12.0,  outside_mM=145.0),
            IonConcentration("Cl⁻", -1, inside_mM=4.0,   outside_mM=110.0),
        ]
        perms = [1.0, 0.04, 0.45]
        V = goldman_equation(ions, perms, temperature_K=310.0)
        assert -90 < V < -50, f"Goldman Vm expected ~-70 mV, got {V:.2f}"

    def test_length_mismatch_raises(self):
        ions = [IonConcentration("K⁺", +1, 140.0, 5.0)]
        with pytest.raises(ValueError, match="equal length"):
            goldman_equation(ions, [1.0, 2.0])

    def test_negative_permeability_raises(self):
        ions = [IonConcentration("K⁺", +1, 140.0, 5.0)]
        with pytest.raises(ValueError):
            goldman_equation(ions, [-0.5])

    def test_non_positive_temperature_raises(self):
        ions = [IonConcentration("K⁺", +1, 140.0, 5.0)]
        with pytest.raises(ValueError, match="temperature_K"):
            goldman_equation(ions, [1.0], temperature_K=0.0)

    def test_zero_denominator_raises(self):
        """Cation with zero intracellular concentration yields zero Goldman denominator."""
        ions = [IonConcentration("K⁺", +1, inside_mM=0.0, outside_mM=10.0)]
        with pytest.raises(ValueError, match="denominator"):
            goldman_equation(ions, [1.0], temperature_K=310.0)


# ---------------------------------------------------------------------------
# Osmotic Pressure
# ---------------------------------------------------------------------------

class TestOsmoticPressure:
    def test_seawater_osmolarity(self):
        """0.6 M NaCl (i=2) at 310 K → ~3 MPa range."""
        pi = osmotic_pressure(0.6, temperature_K=310.0, solute_count=2)
        assert pi > 1e6  # Pa

    def test_zero_concentration_raises(self):
        with pytest.raises(ValueError):
            osmotic_pressure(0.0)

    def test_invalid_solute_count_raises(self):
        with pytest.raises(ValueError):
            osmotic_pressure(0.1, solute_count=0)

    def test_non_positive_temperature_raises(self):
        with pytest.raises(ValueError, match="temperature_K"):
            osmotic_pressure(0.1, temperature_K=0.0)

    def test_proportional_to_concentration(self):
        """Doubling concentration doubles osmotic pressure."""
        pi1 = osmotic_pressure(0.1)
        pi2 = osmotic_pressure(0.2)
        assert abs(pi2 / pi1 - 2.0) < 1e-9


# ---------------------------------------------------------------------------
# Fick's Law
# ---------------------------------------------------------------------------

class TestDiffusionFlux:
    def test_direction_of_flux(self):
        """Positive gradient (outside > inside) → negative flux (inward)."""
        f = diffusion_flux(1e-9, 100.0)  # dC/dx > 0 means outward gradient
        assert f < 0

    def test_zero_diffusion_coefficient_raises(self):
        with pytest.raises(ValueError):
            diffusion_flux(0.0, 100.0)

    def test_negative_diffusion_coefficient_raises(self):
        with pytest.raises(ValueError):
            diffusion_flux(-1e-9, 100.0)

    def test_flux_magnitude_scales_with_D(self):
        f1 = abs(diffusion_flux(1e-9, 100.0))
        f2 = abs(diffusion_flux(2e-9, 100.0))
        assert abs(f2 / f1 - 2.0) < 1e-9


# ---------------------------------------------------------------------------
# Signalling (receptor occupancy, Hill, amplification)
# ---------------------------------------------------------------------------

class TestReceptorAndHill:
    def test_receptor_occupancy_half_max(self):
        assert receptor_occupancy(ligand_concentration=1.0, kd=1.0) == pytest.approx(0.5)

    def test_receptor_occupancy_negative_ligand_raises(self):
        with pytest.raises(ValueError):
            receptor_occupancy(-1.0, kd=1.0)

    def test_receptor_occupancy_non_positive_kd_raises(self):
        with pytest.raises(ValueError):
            receptor_occupancy(1.0, kd=0.0)

    def test_hill_zero_ligand_returns_zero(self):
        assert hill_equation(0.0, kd=1.0, hill_coefficient=2.0) == 0.0

    def test_hill_negative_ligand_raises(self):
        with pytest.raises(ValueError):
            hill_equation(-0.1, kd=1.0, hill_coefficient=2.0)

    def test_signal_amplification_product(self):
        assert signal_amplification([2.0, 3.0, 0.5]) == pytest.approx(3.0)

    def test_signal_amplification_empty_is_unity(self):
        assert signal_amplification([]) == 1.0
