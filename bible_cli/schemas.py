from dataclasses import dataclass

from bible_cli.database import Translation

type SuperScriptNumber = str
type RawNumber = str | int


@dataclass
class QueryData:
    query_string: str
    translation: Translation
    book_name: str
    chapter: int
    verse_start: int
    verse_end: int
