"""Small file-writing helpers for manuscript maintenance scripts."""

from __future__ import annotations

import os
import stat
from pathlib import Path
from tempfile import NamedTemporaryFile


def require_independent_file_target(path: Path) -> Path:
    """Reject existing aliases/nonregular leaves without following or replacing them.

    The caller owns directory admission and publication. This is a pre-existing
    file-custody check, not protection against a concurrently hostile host.
    """
    try:
        info = path.lstat()
    except FileNotFoundError:
        return path
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"Output must be an independent regular file: {path}")
    return path


def write_text_atomic(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    """Replace via a same-directory temp, cleaning it after write/encoding/rename failure."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path: Path | None = None
    try:
        with NamedTemporaryFile(
            "w",
            encoding=encoding,
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            tmp_path = Path(handle.name)
            handle.write(text)
        os.replace(tmp_path, path)
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


__all__ = ["require_independent_file_target", "write_text_atomic"]
