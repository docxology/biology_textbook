"""Small file-writing helpers for manuscript maintenance scripts."""

from __future__ import annotations

import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def write_text_atomic(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    """Write text through a same-directory temporary file, then replace atomically."""
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
            handle.write(text)
            tmp_path = Path(handle.name)
        os.replace(tmp_path, path)
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()


__all__ = ["write_text_atomic"]
