"""Curriculum metadata for the biology textbook."""

from __future__ import annotations

from biology.curriculum.models import CurriculumRecord
from biology.curriculum.unit_0 import RECORDS as UNIT_0_RECORDS
from biology.curriculum.unit_I import RECORDS as UNIT_I_RECORDS
from biology.curriculum.unit_II import RECORDS as UNIT_II_RECORDS
from biology.curriculum.unit_III import RECORDS as UNIT_III_RECORDS
from biology.curriculum.unit_IV import RECORDS as UNIT_IV_RECORDS
from biology.curriculum.unit_IX import RECORDS as UNIT_IX_RECORDS
from biology.curriculum.unit_V import RECORDS as UNIT_V_RECORDS
from biology.curriculum.unit_VI import RECORDS as UNIT_VI_RECORDS
from biology.curriculum.unit_VII import RECORDS as UNIT_VII_RECORDS
from biology.curriculum.unit_VIII import RECORDS as UNIT_VIII_RECORDS
from biology.curriculum.unit_X import RECORDS as UNIT_X_RECORDS

CURRICULUM: tuple[CurriculumRecord, ...] = (
    *UNIT_0_RECORDS,
    *UNIT_I_RECORDS,
    *UNIT_II_RECORDS,
    *UNIT_III_RECORDS,
    *UNIT_IV_RECORDS,
    *UNIT_V_RECORDS,
    *UNIT_VI_RECORDS,
    *UNIT_VII_RECORDS,
    *UNIT_VIII_RECORDS,
    *UNIT_IX_RECORDS,
    *UNIT_X_RECORDS,
)

CURRICULUM_BY_ID: dict[str, CurriculumRecord] = {record.chapter_id: record for record in CURRICULUM}


def by_id(chapter_id: str) -> CurriculumRecord | None:
    return CURRICULUM_BY_ID.get(chapter_id)


def require(chapter_id: str) -> CurriculumRecord:
    record = by_id(chapter_id)
    if record is None:
        raise KeyError(f"No curriculum record for {chapter_id}")
    return record


__all__ = ["CURRICULUM", "CURRICULUM_BY_ID", "CurriculumRecord", "by_id", "require"]
