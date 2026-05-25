"""Domain smoke tests executed during the analysis stage."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)


def _require_nonempty(name: str, value: object) -> None:
    if not value:
        raise RuntimeError(f"Expected non-empty {name} registry during analysis.")


@dataclass(frozen=True)
class DomainSmokeResult:
    """Summary metrics from one domain smoke pass."""

    name: str
    metrics: dict[str, Any]


@dataclass(frozen=True)
class SmokeReport:
    """Aggregated smoke metrics for all nine domain packages."""

    results: tuple[DomainSmokeResult, ...]

    def as_dict(self) -> dict[str, Any]:
        return {result.name: result.metrics for result in self.results}


def run_domain_smoke() -> SmokeReport:
    """Exercise each domain package with fixed deterministic inputs."""
    results: list[DomainSmokeResult] = []

    from biology.cell.cell_biology import ORGANELLES, IonConcentration, nernst_potential

    logger.info("Running cell_biology analysis...")
    ions = [
        IonConcentration(ion="K+", charge=1, inside_mM=140.0, outside_mM=5.0),
        IonConcentration(ion="Na+", charge=1, inside_mM=15.0, outside_mM=145.0),
        IonConcentration(ion="Ca2+", charge=2, inside_mM=0.1, outside_mM=2.0),
        IonConcentration(ion="Cl-", charge=-1, inside_mM=10.0, outside_mM=110.0),
    ]
    e_potentials = [nernst_potential(ion) for ion in ions]
    n_organelles = len(ORGANELLES)
    logger.info("Cell biology: %d Nernst potentials; %d organelles", len(e_potentials), n_organelles)
    results.append(
        DomainSmokeResult("cell_biology", {"nernst_potentials": len(e_potentials), "organelles": n_organelles})
    )

    from biology.genetics.genetics import (
        GENETIC_CODE,
        dna_complement,
        hardy_weinberg,
        transcribe_dna_to_mrna,
        translate_mrna,
    )

    logger.info("Running genetics analysis...")
    seq = "ATCGATCG"
    _comp = dna_complement(seq)
    _mrna = transcribe_dna_to_mrna(seq)
    _protein = translate_mrna(_mrna)
    _hw = hardy_weinberg(p=0.6, q=0.4)
    if len(GENETIC_CODE) != 64:
        raise RuntimeError(f"Expected 64 genetic-code entries, got {len(GENETIC_CODE)}.")
    logger.info("Genetics analysis complete.")
    results.append(DomainSmokeResult("genetics", {"codons": len(GENETIC_CODE)}))

    from biology.evolution.evolution import Population, simulate_selection

    logger.info("Running evolution analysis...")
    pop = Population(name="demo", p=0.3, q=0.7, fitness_AA=1.0, fitness_Aa=0.9, fitness_aa=0.5)
    history = simulate_selection(pop, generations=50)
    logger.info("Evolution: %d generations; final p=%.6f", len(history), history[-1].p)
    results.append(
        DomainSmokeResult("evolution", {"generations": len(history), "final_p": history[-1].p})
    )

    from biology.ecology.ecology import BIOMES, biodiversity_indices, logistic_growth

    logger.info("Running ecology analysis...")
    _growth = logistic_growth(N0=100, r=0.3, K=1000, t_end=50)
    div = biodiversity_indices([120, 80, 60])
    _require_nonempty("BIOMES", BIOMES)
    logger.info("Ecology analysis complete.")
    results.append(
        DomainSmokeResult("ecology", {"biomes": len(BIOMES), "shannon_index": div.shannon_index})
    )

    from biology.biochemistry.biochemistry import atp_free_energy, glycolysis_summary

    logger.info("Running biochemistry analysis...")
    glycolysis = glycolysis_summary()
    _atp = atp_free_energy()
    logger.info(
        "Glycolysis: net ATP=%s, ΔG_total=%.1f kJ/mol",
        glycolysis.net_atp,
        glycolysis.total_delta_G_kJ,
    )
    results.append(
        DomainSmokeResult(
            "biochemistry",
            {"net_atp": glycolysis.net_atp, "dG_kJ": glycolysis.total_delta_G_kJ},
        )
    )

    from biology.physiology.physiology import (
        ORGAN_SYSTEMS,
        homeostasis_response,
        oxygen_saturation,
        poiseuille_flow,
    )

    logger.info("Running physiology analysis...")
    _flow = poiseuille_flow(radius_m=0.001, length_m=0.1, pressure_difference_Pa=100.0)
    _sat = oxygen_saturation(pO2_mmHg=95.0)
    _hom = homeostasis_response(set_point=37.0, measured_value=39.0, gain=0.5, tolerance=0.5)
    _require_nonempty("ORGAN_SYSTEMS", ORGAN_SYSTEMS)
    logger.info("Physiology analysis complete.")
    results.append(DomainSmokeResult("physiology", {"organ_systems": len(ORGAN_SYSTEMS)}))

    from biology.microbiology.microbiology import REFERENCE_ORGANISMS, bacterial_growth_curve, mic_fold_dilution

    logger.info("Running microbiology analysis...")
    _gc = bacterial_growth_curve(N0=1e6, doubling_time_hr=0.75, t_end_hr=6.0)
    _mic = mic_fold_dilution(starting_concentration_ug_mL=128.0, dilution_factor=2, n_tubes=8)
    _require_nonempty("REFERENCE_ORGANISMS", REFERENCE_ORGANISMS)
    logger.info("Microbiology analysis complete.")
    results.append(DomainSmokeResult("microbiology", {"reference_organisms": len(REFERENCE_ORGANISMS)}))

    from biology.botany.botany import PHOTOSYNTHESIS_PATHWAYS, photosynthesis_rate, transpiration_flux, water_potential

    logger.info("Running botany analysis...")
    _psi = water_potential(solute_concentration_M=0.2, turgor_pressure_MPa=0.5)
    _E = transpiration_flux(
        stomatal_conductance_mol_m2_s=0.2,
        internal_vapor_conc_mol_m3=0.5,
        external_vapor_conc_mol_m3=0.4,
    )
    _A = photosynthesis_rate(photon_flux_µmol_m2_s=800.0)
    _require_nonempty("PHOTOSYNTHESIS_PATHWAYS", PHOTOSYNTHESIS_PATHWAYS)
    logger.info("Botany analysis complete.")
    results.append(DomainSmokeResult("botany", {"pathways": len(PHOTOSYNTHESIS_PATHWAYS)}))

    from biology.neuroscience.neuroscience import action_potential_hh

    logger.info("Running neuroscience analysis...")
    hh = action_potential_hh(stimulus_current_µA=10.0)
    peak = max(hh.voltage_mV)
    logger.info("HH simulation: peak=%.2f mV, fired=%s", peak, hh.fired)
    results.append(DomainSmokeResult("neuroscience", {"hh_peak_mV": peak, "hh_fired": hh.fired}))

    return SmokeReport(tuple(results))


__all__ = ["DomainSmokeResult", "SmokeReport", "run_domain_smoke"]
