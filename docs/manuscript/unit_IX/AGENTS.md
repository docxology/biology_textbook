# Unit IX — Zoology and Systems Physiology: AGENTS.md

## Source Module

`src/biology/physiology/physiology.py`:
- `poiseuille_flow()` — blood flow: Q = πr⁴ΔP / (8ηL)
- `oxygen_saturation()` — Hill equation SO₂ at given PO₂
- `oxygen_dissociation_curve()` — O₂-Hb curve over PO₂ range
- `homeostasis_response()` — negative feedback control simulation
- `ORGAN_SYSTEMS` — organ system inventory

`src/biology/neuroscience/neuroscience.py`:
- `action_potential_hh()` — conductance-based neuron model
- `cable_voltage_attenuation()` — passive dendrite/axon cable attenuation
- `synaptic_current()` — EPSP/IPSP driving force and peak current
- `hebbian_weight_update()` — simple activity-dependent weight change

## Chapters

[README.md](README.md) lists chapter filenames/titles; [config.yaml](../config.yaml) owns order.

## Key Equations

- Cardiac output: CO = HR × SV
- Poiseuille: Q = πr⁴ΔP / (8ηL)
- Hill O₂-Hb: SO₂ = PO₂ⁿ / (P₅₀ⁿ + PO₂ⁿ); n ≈ 2.7, P₅₀ ≈ 26 mmHg
- Hodgkin-Huxley: I = C_m(dV/dt) + g_Na m³h(V − E_Na) + g_K n⁴(V − E_K) + g_L(V − E_L)

## Figures and Diagrams

- `plot_oxygen_dissociation()` varies supplied P₅₀ at Hill n=2.7 and labels 40/100 mmHg guides; it is not a calibrated fever/HbF model. `plot_action_potential()` is a separate neural teaching model. See [visual conventions](../../visualization_guide.md).
- `src/mermaid/biology_diagrams.py` — `nervous_system_reflex_diagram()`, `immune_response_diagram()`

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
