"""High-level scan orchestration."""

from __future__ import annotations

from pathlib import Path

from manga_scanner.loaders import (
    SUPPORTED_ARCHIVE_EXTENSIONS,
    SUPPORTED_IMAGE_EXTENSIONS,
    load_pages,
)
from manga_scanner.models import MangaScan, OcrEngine, PageScan
from manga_scanner.ocr import NullOcrEngine

NO_OCR_TEXT_WARNING = "No OCR text detected."
LONG_VERTICAL_WARNING = "Long vertical manhwa-style page."
VERTICAL_RATIO_THRESHOLD = 2.5


def scan_source(path: str | Path, ocr_engine: OcrEngine | None = None) -> MangaScan:
    """Scan a source and return OCR-ready Markdown data.

    Expected behavior:
    - Use ``load_pages`` to read the source.
    - Use ``NullOcrEngine`` when ``ocr_engine`` is ``None``.
    - Strip empty OCR blocks.
    - Add a warning when a page has no OCR text.
    - Add a warning for very tall manhwa-style pages.
    """

    source_path = Path(path)
    engine: OcrEngine = ocr_engine if ocr_engine is not None else NullOcrEngine()

    pages = load_pages(source_path)

    scanned_pages: list[PageScan] = []
    for page in pages:
        text_blocks = tuple(
            block.strip() for block in engine.recognize(page) if block.strip()
        )

        warnings: list[str] = []
        if not text_blocks:
            warnings.append(NO_OCR_TEXT_WARNING)
        if page.width > 0 and page.height / page.width >= VERTICAL_RATIO_THRESHOLD:
            warnings.append(LONG_VERTICAL_WARNING)

        scanned_pages.append(
            PageScan(
                page_number=page.page_number,
                source_name=page.source_name,
                width=page.width,
                height=page.height,
                text_blocks=text_blocks,
                warnings=tuple(warnings),
            )
        )

    return MangaScan(
        title=_source_title(source_path),
        source_path=source_path,
        source_type=_source_type(source_path),
        pages=tuple(scanned_pages),
    )


def _source_title(source_path: Path) -> str:
    """Folders use their name; files use their stem (extension removed)."""

    return source_path.name if source_path.is_dir() else source_path.stem


def _source_type(source_path: Path) -> str:
    if source_path.is_dir():
        return "folder"

    suffix = source_path.suffix.lower()
    if suffix in SUPPORTED_IMAGE_EXTENSIONS:
        return "image"
    if suffix in SUPPORTED_ARCHIVE_EXTENSIONS:
        return "archive"
    if suffix == ".pdf":
        return "pdf"
    return "unknown"
