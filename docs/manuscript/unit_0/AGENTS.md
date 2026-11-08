# Unit 0: Systems Science for Biology — AGENTS.md

## Unit 0 Authoring Contract
Unit 0 is a foundational prologue to the textbook, introducing the conceptual, mathematical, historical, and philosophical frameworks that underpin all subsequent units. It situates biology within systems science, complexity theory, active inference, and source-critical history/philosophy of biology.

## Chapters

See [README.md](README.md#chapters) for the local chapter map; [config.yaml](../config.yaml) owns titles and order.

## Key Concepts
- Systems science: hierarchy, feedback, emergence, self-organization
- Complex adaptive systems: agents, attractors, phase transitions
- Active inference: free energy principle, Bayesian brain, perception–action loops
- History and philosophy: evidence practices, mechanism/function, species and individuality, values in science
- Connections to all subsequent units (cells as systems, ecosystems as CAS)

## Source Code Modules
- Repository-root `src/biology/foundations/`: active-inference teaching profiles, prediction-error precision curves, network degree distributions and biology milestones. [API reference](../../api_reference.md#biologyfoundations) curates callable details.

## Diagrams
- Mermaid diagrams: feedback loops, CAS agent diagrams, active inference belief-update cycle, Unit 0 roadmap

## Notes for Agents
- All chapters follow the standard textbook chapter template (learning objectives, body, summary, discussion questions, further reading).
- Equations must use LaTeX `equation` environment blocks with `\label{eq:...}` tags.
- Chapter numbering is assigned from config at render time; never calculate or type an offset.

## Shared source contract

Follow [manuscript instructions](../AGENTS.md) for H1s, stable IDs, metadata badges, references and authored assessments; see [writing examples](../../manuscript_guide.md). Implementation paths above are repository-root paths.
