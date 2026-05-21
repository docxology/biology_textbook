"""Neuroscience subpackage."""

from .neuroscience import (
    NeuronProperties,
    ActionPotentialResult,
    SynapticResult,
    CableResult,
    action_potential_hh,
    cable_voltage_attenuation,
    synaptic_current,
    hebbian_weight_update,
    BRAIN_REGIONS,
)

__all__ = [
    "NeuronProperties",
    "ActionPotentialResult",
    "SynapticResult",
    "CableResult",
    "action_potential_hh",
    "cable_voltage_attenuation",
    "synaptic_current",
    "hebbian_weight_update",
    "BRAIN_REGIONS",
]
