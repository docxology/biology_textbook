"""Curriculum record factory helper."""

from __future__ import annotations

from biology.curriculum.models import CurriculumRecord


def _r(
    chapter_id: str,
    big_idea: str,
    core_concepts: tuple[str, ...],
    quantitative_model: str,
    data_skill: str,
    lab_focus: str,
    common_misconception: str,
    assessment_focus: str,
    transfer_task: str,
    bridge_api: str,
) -> CurriculumRecord:
    return CurriculumRecord(
        chapter_id=chapter_id,
        big_idea=big_idea,
        core_concepts=core_concepts,
        quantitative_model=quantitative_model,
        data_skill=data_skill,
        lab_focus=lab_focus,
        common_misconception=common_misconception,
        assessment_focus=assessment_focus,
        transfer_task=transfer_task,
        bridge_api=bridge_api,
    )
