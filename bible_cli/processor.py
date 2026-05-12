from bible_cli.database import (
    Book,
    Translation,
    Verse,
    get_session
)
from bible_cli.constants import QUERY_PATTERN, DEFAULT_TRANSLATION
from bible_cli.utils import get_superscript_number
from bible_cli.types import QueryData

class QueryProcessor:
    def process_query(self, query: str) -> str | None:
        query_string = query.strip()
        q = self._parse_query(query_string)

        session = get_session(q.translation)

        verses = (
            session.query(Verse)
            .join(Verse.book)
            .filter(
                Book.name.ilike(q.book_name),
                Verse.chapter == q.chapter,
                Verse.verse.between(q.verse_start, q.verse_end),
            )
            .order_by(Verse.verse)
            .all()
        )

        if not verses:
            print(f"Nenhum versículo encontrado para: {q.query_string}")
            return None
        
        formatted_verses = (
            f'{get_superscript_number(verse.verse)}{verse.text}\n'
            for verse in verses
        )
        output = ''.join(formatted_verses)

        return output

    def _parse_query(self, raw_query) -> QueryData:
    
        query_string, raw_translation = (
            self._extract_query_string_and_translation(raw_query)
        )
        translation = self._get_translation(raw_translation)
        query_data = self._build_query_data(query_string, translation)
        
        return query_data

    def _build_query_data(self, query_string, translation):
        match = QUERY_PATTERN.match(query_string)  
        if not match:
            raise ValueError(
                "Consulta inválida. Use: [book] [chapter]:[verse/range] [version]"
            )

        book_name = match.group("book").strip()
        chapter = int(match.group("chapter"))
        verse_start = int(match.group("verse"))
        verse_end = int(match.group("end_verse") or verse_start)

        query_data = QueryData(
            query_string,
            translation,
            book_name,
            chapter,
            verse_start,
            verse_end
        )
        
        return query_data
    
    def _get_translation(self, translation_str: str) -> Translation:
        try:
            return Translation[translation_str.upper()]
        except KeyError:
            return DEFAULT_TRANSLATION

    def _is_valid_translation(self, translation_str: str) -> bool:
        return translation_str.upper() in Translation.__members__

    def _is_valid_query_range(self, split_query: list[str]):
        return len(split_query) > 1
    
    def _extract_query_string_and_translation(self, query_string: str) -> tuple[str, str]:
            split_query = query_string.split()
            if not self._is_valid_query_range(split_query):
                raise ValueError('Inválid query!')
        
            try:
                query_string = " ".join(split_query[:-1]).strip()
                raw_translation = split_query[-1]
                
                return query_string, raw_translation
            
            except IndexError:
                ValueError('Invalid query')