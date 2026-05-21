"""Tests for microbiology, botany, and neuroscience modules — Units VII/VIII/IX."""

import math
import pytest

from biology.microbiology import (
    bacterial_growth_curve, doubling_time, mic_fold_dilution,
    basic_reproduction_number, sir_model,
    VIRAL_REPLICATION_CYCLES, REFERENCE_ORGANISMS,
)
from biology.botany import (
    water_potential, transpiration_flux, photosynthesis_rate,
    light_response_curve, PHOTOSYNTHESIS_PATHWAYS, plant_biomass_growth,
)
from biology.neuroscience import (
    action_potential_hh, cable_voltage_attenuation,
    synaptic_current, hebbian_weight_update, BRAIN_REGIONS,
)


# ===========================================================================
# MICROBIOLOGY TESTS
# ===========================================================================

class TestBacterialGrowth:
    def test_growth_curve_length(self):
        result = bacterial_growth_curve(N0=1e4, doubling_time_hr=0.5, t_end_hr=8.0, steps=100)
        assert len(result.times_hr) == 101

    def test_growth_curve_exponential_phase_increases(self):
        result = bacterial_growth_curve(1e4, 0.5, 5.0, steps=100, lag_phase_hr=0.5)
        # Population should increase substantially during exponential phase
        assert result.populations[-1] > result.populations[0] * 10

    def test_growth_rate_computed(self):
        result = bacterial_growth_curve(1e4, 1.0, 5.0, steps=50)
        assert abs(result.growth_rate_per_hr - math.log(2)) < 1e-9

    def test_doubling_time_calculation(self):
        td = doubling_time(N0=100.0, Nt=200.0, elapsed_time_hr=1.0)
        assert abs(td - 1.0) < 1e-9

    def test_doubling_time_invalid_N_raises(self):
        with pytest.raises(ValueError, match="greater than N0"):
            doubling_time(N0=200.0, Nt=100.0, elapsed_time_hr=1.0)

    def test_invalid_N0_raises(self):
        with pytest.raises(ValueError):
            bacterial_growth_curve(N0=0.0, doubling_time_hr=0.5, t_end_hr=5.0, steps=50)

    def test_log_populations_present(self):
        result = bacterial_growth_curve(1e4, 0.5, 3.0, steps=50)
        assert len(result.log_populations) == len(result.times_hr)
        assert all(v >= 0 for v in result.log_populations)


class TestMICDilution:
    def test_mic_series_length(self):
        series = mic_fold_dilution(128.0, dilution_factor=2, n_tubes=8)
        assert len(series) == 8

    def test_mic_series_descending(self):
        series = mic_fold_dilution(64.0, dilution_factor=2, n_tubes=7)
        for i in range(len(series) - 1):
            assert series[i] > series[i + 1]

    def test_mic_halving_at_factor_2(self):
        series = mic_fold_dilution(64.0, dilution_factor=2, n_tubes=3)
        assert abs(series[1] - 32.0) < 1e-9
        assert abs(series[2] - 16.0) < 1e-9


class TestSIRModel:
    def test_basic_reproduction_number_ratio(self):
        assert basic_reproduction_number(beta_per_day=0.6, gamma_per_day=0.2) == pytest.approx(3.0)

    def test_sir_population_conserved(self):
        result = sir_model(
            population=1000,
            initial_infected=10,
            beta_per_day=0.4,
            gamma_per_day=0.1,
            days=20,
        )
        assert result.r0 == pytest.approx(4.0)
        totals = [s + i + r for s, i, r in zip(result.susceptible, result.infected, result.recovered)]
        assert all(total == pytest.approx(1000.0, rel=1e-6) for total in totals)
        assert max(result.infected) > result.infected[0]

    def test_sir_invalid_parameters_raise(self):
        with pytest.raises(ValueError, match="initial_infected"):
            sir_model(population=100, initial_infected=0, beta_per_day=0.4, gamma_per_day=0.1, days=10)
        with pytest.raises(ValueError, match="gamma"):
            basic_reproduction_number(beta_per_day=0.4, gamma_per_day=0.0)


class TestViralData:
    def test_viral_cycles_present(self):
        assert "T4 bacteriophage (lytic)" in VIRAL_REPLICATION_CYCLES

    def test_lytic_cycle_burst_size(self):
        t4 = VIRAL_REPLICATION_CYCLES["T4 bacteriophage (lytic)"]
        assert t4.burst_size > 100

    def test_reference_organisms_present(self):
        names = [o.name for o in REFERENCE_ORGANISMS]
        assert "Escherichia coli" in names

    def test_gram_stain_ecoli_negative(self):
        ecoli = next(o for o in REFERENCE_ORGANISMS if o.name == "Escherichia coli")
        assert ecoli.gram_stain == "negative"


# ===========================================================================
# BOTANY TESTS
# ===========================================================================

class TestWaterPotential:
    def test_negative_osmotic_potential(self):
        result = water_potential(0.3, turgor_pressure_MPa=0.5)
        assert result.osmotic_potential_MPa < 0

    def test_water_potential_sum(self):
        result = water_potential(0.3, turgor_pressure_MPa=0.5)
        assert abs(result.water_potential_MPa -
                   (result.osmotic_potential_MPa + result.pressure_potential_MPa)) < 1e-9

    def test_invalid_concentration_raises(self):
        with pytest.raises(ValueError):
            water_potential(0.0, 0.5)

    def test_wilted_cell_negative_water_potential(self):
        """A wilted cell with no turgor has negative ψ."""
        result = water_potential(0.5, turgor_pressure_MPa=0.0)
        assert result.water_potential_MPa < 0


class TestTranspiration:
    def test_flux_direction(self):
        result = transpiration_flux(0.2, internal_vapor_conc_mol_m3=0.5, external_vapor_conc_mol_m3=0.3)
        assert result.flux_mol_m2_s > 0  # outward

    def test_invalid_conductance_raises(self):
        with pytest.raises(ValueError):
            transpiration_flux(0.0, 0.5, 0.3)

    def test_mmol_equals_1000x_mol(self):
        result = transpiration_flux(0.2, 0.5, 0.3)
        assert abs(result.flux_mmol_m2_s - result.flux_mol_m2_s * 1000) < 1e-9


class TestPhotosynthesis:
    def test_dark_zero_light(self):
        """No light → A_net equals -respiration."""
        A = photosynthesis_rate(0.0, max_rate_µmol_CO2_m2_s=20.0, dark_respiration_µmol_CO2_m2_s=2.0)
        assert A == pytest.approx(-2.0)

    def test_high_light_approaches_max(self):
        A = photosynthesis_rate(10000.0, max_rate_µmol_CO2_m2_s=20.0, light_saturation_point=500.0)
        assert A > 15.0

    def test_light_response_curve_length(self):
        curve = light_response_curve(n_points=50)
        assert len(curve) == 51

    def test_c4_has_higher_saturation_than_c3(self):
        c3 = next(p for p in PHOTOSYNTHESIS_PATHWAYS if p.pathway == "C3")
        c4 = next(p for p in PHOTOSYNTHESIS_PATHWAYS if p.pathway == "C4")
        assert c4.light_saturation_point_µmol_m2_s > c3.light_saturation_point_µmol_m2_s

    def test_cam_no_photorespiration(self):
        cam = next(p for p in PHOTOSYNTHESIS_PATHWAYS if p.pathway == "CAM")
        assert not cam.photorespiration

    def test_plant_biomass_growth_runs(self):
        result = plant_biomass_growth(1.0, 0.1, 100.0, 30.0, 100)
        assert result.biomass_g[-1] > 1.0
        assert len(result.times_days) == 101


# ===========================================================================
# NEUROSCIENCE TESTS
# ===========================================================================

class TestHodgkinHuxley:
    def test_action_potential_fires(self):
        result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0)
        assert result.fired

    def test_action_potential_peak_voltage_positive(self):
        """Action potential should depolarize well above 0 mV (Na+ reversal ≈ +55 mV)."""
        result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0)
        assert result.peak_voltage_mV > 10.0

    def test_peak_voltage_above_threshold(self):
        result = action_potential_hh(stimulus_current_µA=10.0, t_end_ms=30.0)
        assert result.peak_voltage_mV > result.threshold_mV

    def test_voltage_time_series_length(self):
        result = action_potential_hh(t_end_ms=10.0, steps=500)
        assert len(result.times_ms) == 501  # steps iterations + final append

    def test_invalid_steps_raises(self):
        with pytest.raises(ValueError):
            action_potential_hh(steps=0)


class TestCableEquation:
    def test_voltage_attenuates_with_distance(self):
        result = cable_voltage_attenuation(V0_mV=10.0, max_distance_µm=2000.0, n_points=100)
        assert result.voltages_mV[0] > result.voltages_mV[-1]

    def test_space_constant_positive(self):
        result = cable_voltage_attenuation(V0_mV=10.0)
        assert result.lambda_µm > 0

    def test_voltage_at_lambda_is_37_percent(self):
        result = cable_voltage_attenuation(V0_mV=100.0, max_distance_µm=5000.0, n_points=500)
        # Find point closest to lambda
        lam = result.lambda_µm
        idx = min(range(len(result.distances_µm)),
                  key=lambda i: abs(result.distances_µm[i] - lam))
        v_at_lambda = result.voltages_mV[idx]
        assert abs(v_at_lambda - 100.0 * math.exp(-1)) < 5.0  # within 5 mV

    def test_zero_V0_raises(self):
        with pytest.raises(ValueError):
            cable_voltage_attenuation(V0_mV=0.0)


class TestSynapticTransmission:
    def test_excitatory_synapse_inward_current(self):
        result = synaptic_current(0.0, -70.0, 10.0, "excitatory")
        assert result.peak_current_pA < 0  # inward (negative by convention: Vm < E_rev)

    def test_inhibitory_synapse_small_current_at_rest(self):
        result = synaptic_current(-70.0, -70.0, 10.0, "inhibitory")
        assert result.driving_force_mV == 0.0

    def test_invalid_conductance_raises(self):
        with pytest.raises(ValueError):
            synaptic_current(0.0, -70.0, 0.0)

    def test_brain_regions_populated(self):
        assert "Hippocampus" in BRAIN_REGIONS
        assert "Cerebral Cortex" in BRAIN_REGIONS
        assert len(BRAIN_REGIONS) >= 5


class TestHebbianPlasticity:
    def test_weight_increases_with_activity(self):
        w0 = 0.5
        w1 = hebbian_weight_update(w0, pre_activity=1.0, post_activity=1.0, learning_rate=0.1)
        assert w1 > w0

    def test_weight_clipped_at_max(self):
        w = hebbian_weight_update(1.0, pre_activity=1.0, post_activity=1.0,
                                  learning_rate=0.5, weight_max=1.0)
        assert w == 1.0

    def test_zero_activity_no_change(self):
        w0 = 0.3
        w1 = hebbian_weight_update(w0, pre_activity=0.0, post_activity=0.0)
        assert w1 == w0

    def test_invalid_learning_rate_raises(self):
        with pytest.raises(ValueError):
            hebbian_weight_update(0.5, 1.0, 1.0, learning_rate=0.0)
