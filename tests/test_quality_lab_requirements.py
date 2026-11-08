"""Default paper requirements and rendered instructor prose are distinct surfaces."""
from pathlib import Path

import pytest

from biology.maintenance.manuscript_walker import iter_prose_lines
from biology.quality import paths
from biology.quality.audits.content import audit_lab_defaults
from biology.quality.models import Finding


@pytest.mark.parametrize("heading, body, required", [
    ("Printed Evidence Packet", "Read the printed Biuret result and classify the unknown.", False),
    ("Paper-Based Materials", "Biuret reagent and a pipette.", True),
    ("Printed Evidence Packet", "Use a pipette to add the Biuret reagent.", True),
    ("Printed Evidence Packet", "Biuret readouts are synthetic. Use M1's named reference patterns to classify the unknown.", False),
    ("Printed Evidence Packet", "Use 0.5 mL Biuret reagent for each unknown.", True),
    ("Printed Evidence Packet", "Use e.g. Biuret reagent to assay each unknown.", True),
    ("Printed Evidence Packet", "Biuret reagent is provided. Use it to assay each unknown.", True),
])
def test_described_assay_is_not_a_required_physical_procedure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, heading: str, body: str, required: bool,
) -> None:
    lab = tmp_path / "labs" / "unit_test" / "lab_sample.md"
    lab.parent.mkdir(parents=True)
    lab.write_text(f"# Lab\n\n## {heading}\n\n{body}\n", encoding="utf-8")
    monkeypatch.setattr(paths, "MANUSCRIPT", tmp_path)
    monkeypatch.setattr(paths, "PROJECT", tmp_path)
    findings: list[Finding] = []
    audit_lab_defaults(findings)
    assert [(item.code, item.line) for item in findings] == (
        [("required-wet-lab-language", 5)] if required else []
    )

def test_printed_packet_exemption_ends_at_next_peer_section(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    lab = tmp_path / "labs/unit_test/lab_sample.md"
    lab.parent.mkdir(parents=True)
    lab.write_text(
        "# Lab\n\n## Printed Evidence Packet\n\nRecorded Biuret color: violet.\n\n"
        "## Paper-Based Materials\n\nBiuret reagent and a pipette.\n", encoding="utf-8",
    )
    monkeypatch.setattr(paths, "MANUSCRIPT", tmp_path)
    monkeypatch.setattr(paths, "PROJECT", tmp_path)
    findings: list[Finding] = []
    audit_lab_defaults(findings)
    assert [(item.code, item.line) for item in findings] == [("required-wet-lab-language", 9)]



def test_instructor_solutions_are_audited_but_examples_and_ordinary_comments_are_not(tmp_path: Path) -> None:
    path = tmp_path / "question.md"
    claim = "Only this instructor-only assertion should be reviewed."
    hidden = "Never treat this ordinary comment as published prose."
    example = "Always treat this as an illustrative Python string."
    path.write_text(
        "# Question\n\n<!-- " + hidden + " -->\n\n```python\ntext = '" + example + "'\n```\n\n"
        "<!-- SOLUTION\n" + claim + "\nSOLUTION -->\n", encoding="utf-8",
    )
    prose = dict(iter_prose_lines(path))
    assert prose[10] == claim
    assert hidden not in "\n".join(prose.values())
    assert example not in "\n".join(prose.values())
