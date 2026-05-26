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

1. `circulation_respiration_homeostasis.md` — Circulation and Respiration
2. `nervous_system.md` — Nervous System and Neural Signaling
3. `action_potential_synapses.md` — Action Potentials and Synaptic Transmission
4. `endocrine_signaling.md` — Endocrine Signaling and Homeostasis
5. `immune_system_defense.md` — Immune System Architecture

## Key Equations

- Cardiac output: CO = HR × SV
- Poiseuille: Q = πr⁴ΔP / (8ηL)
- Hill O₂-Hb: SO₂ = PO₂ⁿ / (P₅₀ⁿ + PO₂ⁿ); n ≈ 2.7, P₅₀ ≈ 26 mmHg
- Hodgkin-Huxley: I = C_m(dV/dt) + g_Na m³h(V − E_Na) + g_K n⁴(V − E_K) + g_L(V − E_L)

## Figures and Diagrams

- `src/visualization/plots.py` — `plot_oxygen_dissociation()`, `plot_action_potential()`
- `src/mermaid/biology_diagrams.py` — `nervous_system_reflex_diagram()`, `immune_response_diagram()`

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_IX_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_IX_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
