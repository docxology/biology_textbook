"""Reviewed mappings are source-owned; sync must preserve or fail without writes."""

from pathlib import Path

import pytest
import yaml

from biology.assessment import chapter_learning_objectives, parse_question_bank
from biology.assessment_sync import (
    sync_all_assessment_metadata,
    sync_lab_alignment,
    sync_question_bank,
    write_or_record,
)


def _bank_text() -> str:
    # Deliberately not ordinal tiers or round-robin objective IDs.
    mappings = {
        1: ("LO3", "Evaluate", "Synthesis", 11),
        2: ("LO1", "Apply", "Application", 3),
        3: ("LO2", "Understand", "Recall", 2),
    }
    lines = ["# Questions {#sec:q_unit_I_atoms_molecules .unnumbered}", ""]
    for number in range(1, 31):
        lo, bloom, difficulty, minutes = mappings.get(number, mappings[2])
        if lo == "LO3":
            prompt = "Assess the claim that doubling any integer always gives an odd integer."
            answer = "False: twice an integer n is 2n, which is even by definition; n=1 gives the counterexample 2."
        elif lo == "LO2":
            prompt = "Explain why doubling an integer gives an even result."
            answer = "The result has the form 2n for an integer n, the definition of an even integer."
        else:
            prompt = f"Calculate twice {number}."
            answer = f"2 × {number} = {2 * number}."
        lines.extend([
            f"<!-- assess: minutes={minutes}; format=short-answer; LO={lo}; difficulty={difficulty}; bloom={bloom} -->",
            f"{number}. {prompt}", "<!-- SOLUTION",
            f"**Answer (Q{number}, {difficulty}).** {answer}", "SOLUTION -->", "",
        ])
    return "\n".join(lines)


def _lab_text() -> str:
    return """# Lab
<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}
- **Outcome 1 (LO1):** Calculate doubled values from the printed integer table.
- **Outcome 2 (LO2):** Explain parity using the representation 2n.
- **Outcome 3 (LO3):** Test the universal odd-result claim using a counterexample.
- **Evidence:** Credit a correctly calculated table row supporting the conclusion.
- **Controls:** Credit comparison of the same integer before and after doubling.
- **Uncertainty:** Distinguish exact integer arithmetic from measurement uncertainty.
- **Mechanism:** Credit the factor-of-two argument, not an unsupported parity guess.
- **Transfer:** Apply the proof to a previously unseen integer.
<!-- lab-alignment-end -->
"""


def _project(root: Path) -> tuple[Path, Path]:
    manuscript = root / "docs" / "manuscript"
    chapter = manuscript / "unit_I" / "atoms_molecules.md"
    bank = manuscript / "questions" / "unit_I" / "questions_atoms_molecules.md"
    lab = manuscript / "labs" / "unit_I" / "lab_atoms_molecules.md"
    for path in (chapter, bank, lab):
        path.parent.mkdir(parents=True, exist_ok=True)
    chapter.write_text("# Arithmetic\n## Learning Objectives\n1. Calculate doubled integers.\n2. Explain parity.\n3. Evaluate universal parity claims.\n", encoding="utf-8")
    bank.write_text(_bank_text(), encoding="utf-8")
    lab.write_text(_lab_text(), encoding="utf-8")
    config = {
        "units": [{"id": "unit_I", "directory": "unit_I", "chapters": [{"file": chapter.name, "title": "Arithmetic"}]}],
        "appendices": {
            "questions": [{"unit": "unit_I", "files": [{"file": bank.name}]}],
            "labs": [{"unit": "unit_I", "files": [{"file": lab.name}]}],
        },
    }
    (manuscript / "config.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
    return bank, lab


def test_reviewed_comments_and_lab_criteria_survive_byte_for_byte(tmp_path: Path) -> None:
    bank, lab = _project(tmp_path)
    before = {path: path.read_bytes() for path in (bank, lab)}
    assert sync_question_bank(bank, ("LO1", "LO2", "LO3")) == _bank_text()
    assert sync_lab_alignment(lab, "Arithmetic", ("LO1", "LO2", "LO3")) == _lab_text()
    for check, dry_run in ((False, False), (True, False), (False, True)):
        assert sync_all_assessment_metadata(tmp_path, check=check, dry_run=dry_run) == ([], 0)
    assert {path: path.read_bytes() for path in before} == before
    first = parse_question_bank(bank).items[0]
    assert (first.lo, first.bloom, first.difficulty, first.minutes) == ("LO3", "Evaluate", "Synthesis", 11)


@pytest.mark.parametrize("replacement", ["LO=LO99", "LO=LO0", "LO=", "LO=LO3; LO=LO1"])
def test_invalid_reviewed_mapping_is_not_replaced(tmp_path: Path, replacement: str) -> None:
    bank, _ = _project(tmp_path)
    bank.write_text(_bank_text().replace("LO=LO3", replacement, 1), encoding="utf-8")
    before = bank.read_bytes()
    with pytest.raises(ValueError):
        sync_question_bank(bank, ("LO1", "LO2", "LO3"))
    assert bank.read_bytes() == before


@pytest.mark.parametrize("check,dry_run", [(False, False), (True, False), (False, True)])
def test_missing_late_lab_alignment_cannot_publish_earlier_bank_changes(tmp_path: Path, check: bool, dry_run: bool) -> None:
    bank, lab = _project(tmp_path)
    lab.write_text("# Lab\nAuthoring incomplete.\n", encoding="utf-8")
    before = {path: path.read_bytes() for path in (bank, lab)}
    with pytest.raises(ValueError):
        sync_all_assessment_metadata(tmp_path, check=check, dry_run=dry_run)
    assert {path: path.read_bytes() for path in before} == before


def test_missing_question_metadata_requires_author_action(tmp_path: Path) -> None:
    bank, _ = _project(tmp_path)
    bank.write_text(_bank_text().replace("<!-- assess: minutes=11; format=short-answer; LO=LO3; difficulty=Synthesis; bloom=Evaluate -->\n", ""), encoding="utf-8")
    before = bank.read_bytes()
    with pytest.raises(ValueError, match="question 1"):
        sync_all_assessment_metadata(tmp_path)
    assert bank.read_bytes() == before


def test_unknown_lab_objective_fails_without_rewriting_rubric(tmp_path: Path) -> None:
    _, lab = _project(tmp_path)
    lab.write_text(_lab_text().replace("(LO3)", "(LO99)"), encoding="utf-8")
    before = lab.read_bytes()
    with pytest.raises(ValueError, match="LO99"):
        sync_lab_alignment(lab, "Arithmetic", ("LO1", "LO2", "LO3"))
    assert lab.read_bytes() == before


def test_empty_config_does_not_silently_skip_all_banks(tmp_path: Path) -> None:
    manuscript = tmp_path / "docs" / "manuscript"
    manuscript.mkdir(parents=True)
    (manuscript / "config.yaml").write_text("units: []\n", encoding="utf-8")
    with pytest.raises(ValueError):
        sync_all_assessment_metadata(tmp_path)


def test_objective_list_stops_before_numbered_h3_examples(tmp_path: Path) -> None:
    chapter = tmp_path / "chapter.md"
    chapter.write_text("## Learning Objectives\n\n1. Explain evidence.\n2. Analyze uncertainty.\n\n### Worked example\n\n1. First step.\n2. Second step.\n3. Third step.\n", encoding="utf-8")
    assert chapter_learning_objectives(chapter) == ("LO1", "LO2")


def test_write_or_record_respects_nonwriting_mode(tmp_path: Path) -> None:
    target = tmp_path / "file.md"
    target.write_text("original\n", encoding="utf-8")
    assert write_or_record(target, "reviewed\n", write=False) == [target]
    assert target.read_text(encoding="utf-8") == "original\n"


@pytest.mark.parametrize("bad_outcome", [
    "- **Outcome 3 (LO0):** Evaluate the claim.",
    "- **Outcome 3 (LO3):**",
    "- **Outcome 4 (LO3):** Evaluate the claim.",
])
def test_invalid_lab_outcome_schema_is_not_silently_preserved(tmp_path: Path, bad_outcome: str) -> None:
    _, lab = _project(tmp_path)
    original = _lab_text().replace(
        "- **Outcome 3 (LO3):** Test the universal odd-result claim using a counterexample.",
        bad_outcome,
    )
    lab.write_text(original, encoding="utf-8")
    with pytest.raises(ValueError):
        sync_lab_alignment(lab, "Arithmetic", ("LO1", "LO2", "LO3"))
    assert lab.read_text(encoding="utf-8") == original
