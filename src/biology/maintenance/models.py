"""Data models for textbook maintenance and quality auditing."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: Path
    line: int
    message: str

    def format(self) -> str:
        rel = self.path.relative_to(PROJECT)
        return f"{self.severity.upper()} {self.code} {rel}:{self.line}: {self.message}"


@dataclass(frozen=True)
class ManuscriptSurface:
    category: str
    path: Path


__all__ = ["Finding", "ManuscriptSurface", "PROJECT"]
