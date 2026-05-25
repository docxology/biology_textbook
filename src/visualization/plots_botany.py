"""Domain matplotlib figure generators."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from visualization._scaffold import (
    GRAY,
    SERIES2,
    SERIES3,
    _save_figure,
)


def plot_light_response_curve(
    output_dir: Path,
) -> Path:
    """Plot photosynthesis light-response curves for C3, C4, and CAM plants.

    Args:
        output_dir: Directory to save PNG.

    Returns:
        Path to saved PNG.
    """
    from biology.botany import light_response_curve

    fig, ax = plt.subplots(figsize=(9, 5))

    pathways: list[tuple[str, float, float, float, str, str]] = [
        ("C3", 20.0, 500.0, 1.5, SERIES3[0], "-"),
        ("C4", 35.0, 1500.0, 2.0, SERIES3[1], "--"),
        ("CAM", 15.0, 800.0, 1.0, SERIES3[2], "-."),
    ]
    for label, amax, light_sat, rd, color, ls in pathways:
        curve = light_response_curve(amax, light_sat, rd, n_points=80, max_par=2100.0)
        pars = [x for x, _ in curve]
        rates = [y for _, y in curve]
        ax.plot(pars, rates, color=color, linewidth=2.5, linestyle=ls, label=label)

    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_xlabel("Photon Flux Density, PAR (µmol m⁻² s⁻¹)", fontsize=14)
    ax.set_ylabel("Net Photosynthesis A_net (µmol CO₂ m⁻² s⁻¹)", fontsize=14)
    ax.set_title("Photosynthesis Light-Response Curves: C3, C4, CAM", fontsize=15)
    ax.legend(fontsize=12)
    ax.tick_params(labelsize=12)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "light_response_curves.png")


def plot_photosynthesis_rate(
    output_dir: Path,
) -> Path:
    """Plot net photosynthesis versus PAR using the hyperbolic rate model."""
    from biology.botany import photosynthesis_rate

    par = np.linspace(0.0, 2000.0, 120)
    configs = [
        ("C3-like", 18.0, 700.0, 1.8, SERIES3[0], "-"),
        ("C4-like", 28.0, 1200.0, 2.2, SERIES3[1], "--"),
    ]
    fig, ax = plt.subplots(figsize=(9, 5))
    for label, amax, sat, rd, color, linestyle in configs:
        rates = [photosynthesis_rate(float(i), amax, sat, rd) for i in par]
        ax.plot(par, rates, color=color, linewidth=2.2, linestyle=linestyle, label=label)
    ax.axhline(0, color=GRAY, linestyle=":", linewidth=1.0)
    ax.set_xlabel("PAR (µmol m⁻² s⁻¹)", fontsize=13)
    ax.set_ylabel("Net photosynthesis (µmol CO₂ m⁻² s⁻¹)", fontsize=13)
    ax.set_title("Net Photosynthesis Light-Response Curves", fontsize=15)
    ax.legend(fontsize=10, frameon=False)
    ax.tick_params(labelsize=11)
    fig.tight_layout()
    return _save_figure(fig, output_dir, "photosynthesis_rate.png")


def plot_water_potential_transpiration(
    output_dir: Path,
) -> Path:
    """Plot plant water potential components and transpiration flux."""
    from biology.botany import transpiration_flux, water_potential

    solutes = np.linspace(0.05, 0.60, 90)
    psi_s = []
    psi_total = []
    for concentration in solutes:
        result = water_potential(float(concentration), turgor_pressure_MPa=0.5)
        psi_s.append(result.osmotic_potential_MPa)
        psi_total.append(result.water_potential_MPa)

    external_vapor = np.linspace(0.30, 0.50, 90)
    conductances = [0.10, 0.20, 0.35]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5))
    ax1.plot(solutes, psi_s, color=SERIES2[0], linewidth=2.2, label="solute potential psi_s")
    ax1.plot(solutes, psi_total, color=SERIES2[1], linestyle="--", linewidth=2.2, label="total psi at psi_p=0.5 MPa")
    ax1.axhline(0, color=GRAY, linewidth=0.9, linestyle=":")
    ax1.set_xlabel("Solute concentration (mol L^-1)", fontsize=12)
    ax1.set_ylabel("Water potential (MPa)", fontsize=12)
    ax1.set_title("Water Potential Components", fontsize=13)
    ax1.legend(fontsize=9, frameon=False)

    for conductance, color, linestyle in zip(conductances, SERIES3, ("-", "--", "-.")):
        flux = [
            transpiration_flux(
                stomatal_conductance_mol_m2_s=conductance,
                internal_vapor_conc_mol_m3=0.52,
                external_vapor_conc_mol_m3=float(external),
            ).flux_mmol_m2_s
            for external in external_vapor
        ]
        ax2.plot(external_vapor, flux, color=color, linestyle=linestyle, linewidth=2.2, label=f"g = {conductance:g}")
    ax2.set_xlabel("External water vapor concentration (mol m^-3)", fontsize=12)
    ax2.set_ylabel("Transpiration flux (mmol m^-2 s^-1)", fontsize=12)
    ax2.set_title("Fick-Law Transpiration Gradient", fontsize=13)
    ax2.legend(title="Conductance", fontsize=9, title_fontsize=9, frameon=False)

    for ax in (ax1, ax2):
        ax.tick_params(labelsize=10)
    fig.suptitle("Plant Water Potential and Transpiration", fontsize=15, fontweight="bold")
    fig.tight_layout()
    return _save_figure(fig, output_dir, "water_potential_transpiration.png")


# ---------------------------------------------------------------------------
# Ecology — logistic growth, species–area, biome NPP
# ---------------------------------------------------------------------------

