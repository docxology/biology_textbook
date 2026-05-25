"""Enrichment data models."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from biology.enrichment.paths import MANUSCRIPT


@dataclass(frozen=True)
class ChapterRecord:
    unit_id: str
    unit_title: str
    file: str
    title: str

    @property
    def stem(self) -> str:
        return Path(self.file).stem

    @property
    def chapter_path(self) -> Path:
        return MANUSCRIPT / self.unit_id / self.file

    @property
    def lab_path(self) -> Path:
        return MANUSCRIPT / "labs" / self.unit_id / f"lab_{self.stem}.md"

    @property
    def question_path(self) -> Path:
        return MANUSCRIPT / "questions" / self.unit_id / f"questions_{self.stem}.md"

    @property
    def section_ref(self) -> str:
        return f"sec:{self.unit_id}_{self.stem}"
