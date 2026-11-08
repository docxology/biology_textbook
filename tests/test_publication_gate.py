"""Dependency failure and ordering regressions for publication gates."""

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
