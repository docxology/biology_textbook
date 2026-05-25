"""Chapter record loading."""

from __future__ import annotations

from biology.enrichment.models import ChapterRecord
from biology.enrichment.paths import PROJECT


def load_book_toc():
    from biology.toc import load_toc

    return load_toc(PROJECT)


def chapter_records() -> list[ChapterRecord]:
    return [
        ChapterRecord(
            unit_id=chapter.unit_id,
            unit_title=chapter.unit_title,
            file=chapter.file,
            title=chapter.title,
        )
        for chapter in load_book_toc().chapters
    ]
