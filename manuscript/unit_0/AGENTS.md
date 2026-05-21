# Unit 0: Systems Science and the Biology of Complexity — AGENTS.md

## Overview
Unit 0 is a foundational prologue to the textbook, introducing the conceptual and mathematical frameworks that underpin all subsequent units. It situates biology within systems science, complexity theory, and active inference.

## Chapters

| File | Chapter Title |
| ---- | ------------- |
| `systems_science.md` | Systems Science and the Logic of Emergence |
| `complex_adaptive_systems.md` | Complex Adaptive Systems |
| `active_inference.md` | Active Inference and the Free Energy Principle |

## Key Concepts
- Systems science: hierarchy, feedback, emergence, self-organisation
- Complex adaptive systems: agents, attractors, phase transitions
- Active inference: free energy principle, Bayesian brain, perception–action loops
- Connections to all subsequent units (cells as systems, ecosystems as CAS)

## Source Code Modules
- `src/biology/` (shared framework; unit-specific models appear in later units)

## Diagrams
- Mermaid diagrams: feedback loops, CAS agent diagrams, active inference belief-update cycle

## Notes for Agents
- All chapters follow the standard textbook chapter template (learning objectives, body, summary, discussion questions, further reading).
- Equations must use LaTeX `equation` environment blocks with `\label{eq:...}` tags.
- Unit 0 chapters are before Unit I; chapter numbering must account for this offset.

## Chapter Metadata Convention

All chapter files in this unit carry (inserted automatically by the scripts):

- `\label{sec:unit_0_<stem>}` on the line after the H1 — cross-reference with `\cref{sec:unit_0_<stem>}`
- `<!-- chapter-metadata-badge -->` blockquote with difficulty (Level 1/3–3/3), reading time, lecture time, and prerequisites (data in `../../src/biology/chapter_metadata.py`)

See [../AGENTS.md](../AGENTS.md) and [../../docs/manuscript_guide.md](../../docs/manuscript_guide.md) for the full set of invariants.
