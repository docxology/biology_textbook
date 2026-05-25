"""Shared physical and chemical constants for biology domain modules."""

from __future__ import annotations

FARADAY_CONSTANT = 96485.0  # C mol⁻¹
FARADAY = FARADAY_CONSTANT  # biochemistry alias
GAS_CONSTANT = 8.314  # J mol⁻¹ K⁻¹
AVOGADRO = 6.022e23  # mol⁻¹
BOLTZMANN = 1.381e-23  # J K⁻¹

__all__ = [
    "AVOGADRO",
    "BOLTZMANN",
    "FARADAY",
    "FARADAY_CONSTANT",
    "GAS_CONSTANT",
]
