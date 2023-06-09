from typing import (
    Optional,
    Dict,
)

from pydantic import BaseModel

from src.enums import PartOfSpeech


class Relation(BaseModel):
    word: "Word"
    part_of_speech: PartOfSpeech
    example: Optional[str]


class Word(BaseModel):
    id: Optional[int]
    name: str
    transcription: Optional[str]
    relations: Dict[str, "Relation"] = {}
    topic: Optional[str]

    def has_relations(self) -> bool:
        if len(self.relations) > 0:
            return True
        return False

    def remove_relation(self, name: str):
        if self.relations.get(name):
            del self.relations[name]


class NativeWord(Word):
    pass


class ForeignWord(Word):
    pass


Relation.update_forward_refs()
