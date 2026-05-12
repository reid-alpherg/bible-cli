from enum import StrEnum
from pathlib import Path

from sqlalchemy import ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

DATA_DIR = Path(__file__).parent / "data_source"


class Translation(StrEnum):
    ACF = "ACF.sqlite"
    ARA = "ARA.sqlite"
    ARC = "ARC.sqlite"
    AS21 = "AS21.sqlite"
    JFAA = "JFAA.sqlite"
    KJA = "KJA.sqlite"
    KJF = "KJF.sqlite"
    NAA = "NAA.sqlite"
    NBV = "NBV.sqlite"
    NTLH = "NTLH.sqlite"
    NVI = "NVI.sqlite"
    NVT = "NVT.sqlite"
    TB = "TB.sqlite"


class Base(DeclarativeBase):
    pass


# Models
class Testament(Base):
    __tablename__ = "testament"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    books: Mapped[list["Book"]] = relationship("Book", back_populates="testament")


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_reference_id: Mapped[int] = mapped_column(Integer)
    testament_reference_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("testament.id")
    )
    name: Mapped[str] = mapped_column(String)
    testament: Mapped["Testament"] = relationship("Testament", back_populates="books")
    verses: Mapped[list["Verse"]] = relationship("Verse", back_populates="book")


class Verse(Base):
    __tablename__ = "verse"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("book.id"))
    chapter: Mapped[int] = mapped_column(Integer)
    verse: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(Text)
    book: Mapped["Book"] = relationship("Book", back_populates="verses")


class Metadata(Base):
    __tablename__ = "metadata"
    key: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(String)


def get_engine(translation: Translation = Translation.ACF):
    db_path = DATA_DIR / translation.value
    return create_engine(f"sqlite:///{db_path}", future=True)


def get_session(translation: Translation = Translation.ACF) -> Session:
    engine = get_engine(translation)
    return Session(engine)
