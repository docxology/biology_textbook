"""Tests for ``biology.quality.publication_gate``."""

from __future__ import annotations

from pathlib import Path

from biology.quality.publication_gate import (
    CommandStep,
    PythonStep,
    build_command_steps,
    build_python_steps,
)


def test_default_steps_include_practical_checks() -> None:
    names = {step.name for step in build_command_steps(full=False)}
    assert "quality-audit" in names
    assert "current-claims" in names
    assert "diagrams-strict" in names
    assert "root-wip-resolver-smoke" in names
    assert "project-tests-gate" not in names
    assert "root-render" not in names


def test_full_steps_add_root_orchestration() -> None:
    names = {step.name for step in build_command_steps(full=True)}
    assert {"project-tests-gate", "root-setup", "root-render", "root-validate-output", "root-pdf-log"} <= names


def test_check_modes_used_for_mutating_sync_scripts() -> None:
    commands = {step.name: step.command for step in build_command_steps(full=False)}
    assert "--check" in commands["assessment-sync"]
    assert "--check" in commands["mermaid-alt-sync"]


def test_artifact_paths_are_outside_project_output(tmp_path: Path) -> None:
    commands = {step.name: step.command for step in build_command_steps(full=False, artifact_dir=tmp_path)}
    project_output = str(Path(__file__).resolve().parent.parent / "output")
    assert "--output" in commands["visual-contracts"]
    assert "--output-dir" in commands["figures-strict"]
    assert "--output-dir" in commands["diagrams-strict"]
    for command in commands.values():
        assert not any(part.startswith(project_output) for part in command)


def test_project_tests_gate_uses_uv_pytest_with_coverage_floor() -> None:
    commands = {step.name: step.command for step in build_command_steps(full=True)}
    gate = commands["project-tests-gate"]
    assert gate[:3] == ("uv", "run", "pytest")
    assert "--cov-fail-under=90" in gate


def test_python_steps_are_in_process_checks() -> None:
    steps = build_python_steps(full=False)
    names = {step.name for step in steps}
    assert names == {
        "recursive-markdown",
        "recursive-prerender",
        "artifact-counts",
        "tracked-artifact-hygiene",
    }
    assert all(isinstance(step, PythonStep) for step in steps)


def test_command_steps_are_typed() -> None:
    for step in build_command_steps(full=True):
        assert isinstance(step, CommandStep)
        assert isinstance(step.command, tuple)
