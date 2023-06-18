from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class Words(Base):
    __tablename__ = 'words'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    transcription: Mapped[str] = mapped_column(String(128))


class Relations(Base):
    __tablename__ = 'relations'
    id: Mapped[int] = mapped_column(primary_key=True)
    part_of_speech: Mapped[str] = mapped_column(String(32))
    example: Mapped[str] = mapped_column(String(256))
