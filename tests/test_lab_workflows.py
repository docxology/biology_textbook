"""Tests for lab computational workflow normalisation."""

from __future__ import annotations

from biology.maintenance.lab_workflows import WORKFLOWS, normalise_lab


def test_workflow_catalog_is_non_empty() -> None:
    assert len(WORKFLOWS) >= 10
    assert all(workflow.relative_path.startswith("labs/") for workflow in WORKFLOWS)


def test_catalog_lab_files_exist() -> None:
    missing = [workflow.relative_path for workflow in WORKFLOWS if not workflow.path.exists()]
    assert not missing, f"Missing lab files: {missing[:3]}"


def test_normalise_lab_replaces_stale_notebook_block(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr("biology.maintenance.lab_workflows.MANUSCRIPT", tmp_path)
    lab_rel = "labs/unit_demo/lab_demo.md"
    lab_path = tmp_path / lab_rel
    lab_path.parent.mkdir(parents=True)
    lab_path.write_text(
        "\n".join(
            [
                "# Demo",
                "",
                "| Computer with Python/Jupyter Notebook | 1 |",
                "",
                "### Part 2: Computational extension",
                "",
                "*Complete this section using the provided Jupyter Notebook: demo.ipynb*",
                "",
                "- Investigate the Jupyter notebook `demo.ipynb` for the full workflow.",
                "",
                "### Part 3: Wrap-up",
                "",
                "Reference module: src/biology/genetics.py",
                "",
                "Done.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    from biology.maintenance.lab_workflows import LabWorkflow, normalise_lab

    workflow = LabWorkflow(
        lab_rel,
        "src/biology/genetics/genetics.py",
        "*Optional computational check*\n\n```python\nprint(1)\n```\n\n",
    )
    assert normalise_lab(workflow, dry_run=False)
    updated = lab_path.read_text(encoding="utf-8")
    assert "Optional computational check" in updated
    assert "Jupyter Notebook" not in updated
    assert "genetics/genetics.py" in updated
    assert "Calculator or optional Python REPL" in updated


def test_normalise_lab_is_idempotent_on_catalog() -> None:
    changed = [workflow.relative_path for workflow in WORKFLOWS if normalise_lab(workflow, dry_run=True)]
    assert not changed, f"Unexpected stale notebook sections: {changed[:3]}"
