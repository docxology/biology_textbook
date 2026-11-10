"""Publication dependency, failure and source-custody regressions."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from biology.quality.publication_gate import (
    CommandStep,
    _run_step_batches,
    run_command_step,
)


@pytest.mark.parametrize("workers", [1, 2])
def test_failed_prerequisite_blocks_transitive_consumers_but_not_peers(tmp_path: Path, workers: int) -> None:
    failed_output = tmp_path / "failed-output"
    dependent_output = tmp_path / "dependent-output"
    peer_output = tmp_path / "peer-output"
    steps = [
        CommandStep("consumer", (sys.executable, "-c", f"from pathlib import Path; Path({str(dependent_output)!r}).touch()"), tmp_path, depends_on=frozenset({"producer"})),
        CommandStep("producer", (sys.executable, "-c", f"from pathlib import Path; Path({str(failed_output)!r}).touch(); raise SystemExit(3)"), tmp_path),
        CommandStep("peer", (sys.executable, "-c", f"from pathlib import Path; Path({str(peer_output)!r}).touch()"), tmp_path),
        CommandStep("grandchild", (sys.executable, "-c", "raise SystemExit(99)"), tmp_path, depends_on=frozenset({"consumer"})),
    ]
    assert _run_step_batches(steps, run_command_step, max_workers=workers) == 3
    assert failed_output.is_file()
    assert peer_output.is_file()
    assert not dependent_output.exists()


@pytest.mark.parametrize("workers", [1, 2])
def test_out_of_order_graph_consumes_successful_producer_output(tmp_path: Path, workers: int) -> None:
    data = tmp_path / "result.txt"
    steps = [
        CommandStep("consumer", (sys.executable, "-c", f"from pathlib import Path; assert Path({str(data)!r}).read_text() == 'validated'"), tmp_path, depends_on=frozenset({"producer"})),
        CommandStep("producer", (sys.executable, "-c", f"from pathlib import Path; Path({str(data)!r}).write_text('validated')"), tmp_path),
    ]
    assert _run_step_batches(steps, run_command_step, max_workers=workers) == 0


def test_unavailable_command_is_an_explicit_failed_step(tmp_path: Path) -> None:
    assert run_command_step(CommandStep("missing", (str(tmp_path / "absent-executable"),), tmp_path)) == 1


def test_unknown_dependency_refuses_before_executing_command(tmp_path: Path) -> None:
    marker = tmp_path / "must-not-run"
    step = CommandStep("invalid", (sys.executable, "-c", f"from pathlib import Path; Path({str(marker)!r}).touch()"), tmp_path, depends_on=frozenset({"absent"}))
    with pytest.raises(ValueError):
        _run_step_batches([step], run_command_step, max_workers=1)
    assert not marker.exists()


@pytest.mark.parametrize("workers", [1, 2])
def test_signal_failure_cannot_cancel_positive_failure_status(tmp_path: Path, workers: int) -> None:
    steps = [
        CommandStep("positive", (sys.executable, "-c", "raise SystemExit(15)"), tmp_path),
        CommandStep("signal", (sys.executable, "-c", "import os, signal; os.kill(os.getpid(), signal.SIGTERM)"), tmp_path),
    ]
    assert _run_step_batches(steps, run_command_step, max_workers=workers) == 2


def test_command_step_prevents_renderer_bytecode_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("PYTHONDONTWRITEBYTECODE", "")
    (tmp_path / "fixture_renderer.py").write_text("value = 42\n")
    code = "import sys, fixture_renderer; assert sys.dont_write_bytecode; assert fixture_renderer.value == 42"
    step = CommandStep("renderer-import", (sys.executable, "-c", code), tmp_path)
    assert run_command_step(step) == 0
    assert not (tmp_path / "__pycache__").exists()



def test_tracked_artifact_hygiene_ignores_an_unrelated_index(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Real source binding and hygiene must inspect the same project index."""
    import hashlib
    import subprocess

    from biology.pipeline.release_assets import source_state
    from biology.quality import publication_gate as gate

    project, unrelated = tmp_path / "project", tmp_path / "unrelated"
    project.mkdir()
    unrelated.mkdir()
    def git(root: Path, *args: str) -> str:
        return subprocess.run(
            ["git", "-c", "core.fsmonitor=false", "-C", str(root), *args],
            check=True, capture_output=True, text=True, stdin=subprocess.DEVNULL,
            timeout=30,
        ).stdout.strip()
    for root in (project, unrelated):
        git(root, "init", "--initial-branch=main")
    artifact = project / "output" / "forbidden.txt"
    artifact.parent.mkdir()
    artifact.write_text("Tracked generated-artifact fixture\n")
    git(project, "add", ".")
    git(project, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "-m", "tracked output fixture")
    git(unrelated, "read-tree", "--empty")
    before = {path.relative_to(unrelated): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in unrelated.rglob("*") if path.is_file()}
    monkeypatch.setattr(gate, "PROJECT", project)
    ordinary = gate.check_tracked_artifact_hygiene()
    assert any("output/forbidden.txt" in issue for issue in ordinary)
    expected_state = source_state(project)
    monkeypatch.setenv("GIT_INDEX_FILE", str(unrelated / ".git" / "index"))
    assert source_state(project) == expected_state
    assert gate.check_tracked_artifact_hygiene() == ordinary
    assert {path.relative_to(unrelated): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in unrelated.rglob("*") if path.is_file()} == before



@pytest.mark.parametrize("relative", ["output/α-generated.txt", "  cached.pyc"])
def test_tracked_artifact_hygiene_preserves_machine_path_names(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, relative: str,
) -> None:
    """Git quoting and significant path whitespace cannot hide tracked artifacts."""
    import subprocess

    from biology.quality import publication_gate as gate

    root = tmp_path / "project"
    root.mkdir()
    def git(*args: str) -> None:
        subprocess.run(
            ["git", "-c", "core.fsmonitor=false", "-C", str(root), *args],
            check=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=30,
        )
    git("init", "--initial-branch=main")
    git("config", "--local", "core.quotePath", "true")
    artifact = root / relative
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_bytes(b"real tracked generated-artifact fixture")
    git("add", ".")
    monkeypatch.setattr(gate, "PROJECT", root)
    assert any(relative in issue for issue in gate.check_tracked_artifact_hygiene())
