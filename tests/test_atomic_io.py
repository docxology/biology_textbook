"""Tests for shared maintenance-script file-writing helpers."""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "atomic_io.py"
spec = importlib.util.spec_from_file_location("atomic_io_for_test", SCRIPT)
assert spec is not None
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
write_text_atomic = module.write_text_atomic


def test_write_text_atomic_replaces_file_and_cleans_temp(tmp_path: Path) -> None:
    target = tmp_path / "nested" / "chapter.md"

    write_text_atomic(target, "first\n")
    write_text_atomic(target, "second\n")

    assert target.read_text(encoding="utf-8") == "second\n"
    assert not list(target.parent.glob(f".{target.name}.*.tmp"))


def test_script_consumer_encoding_failure_is_atomic(tmp_path: Path) -> None:
    target = tmp_path / "chapter.md"
    target.write_bytes(b"original\n")
    neighbor = tmp_path / "neighbor.md"
    neighbor.write_bytes(b"neighbor\n")
    before = set(tmp_path.iterdir())

    with pytest.raises(UnicodeEncodeError):
        write_text_atomic(target, "μ", encoding="ascii")

    assert target.read_bytes() == b"original\n"
    assert neighbor.read_bytes() == b"neighbor\n"
    assert set(tmp_path.iterdir()) == before
