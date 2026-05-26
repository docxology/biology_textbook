"""Curriculum metadata models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CurriculumRecord:
    """Instructional metadata for one chapter and its companion materials."""

    chapter_id: str
    big_idea: str
    core_concepts: tuple[str, ...]
    quantitative_model: str
    data_skill: str
    lab_focus: str
    common_misconception: str
    assessment_focus: str
    transfer_task: str
    bridge_api: str

    @property
    def lab_label(self) -> str:
        return f"sec:lab_{self.chapter_id}"

    @property
    def question_label(self) -> str:
        return f"sec:q_{self.chapter_id}"
