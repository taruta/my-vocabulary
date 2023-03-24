from typing import Optional, Dict
from pydantic import BaseModel
from src.enums import PartOfSpeech


class Relation(BaseModel):
    word: "Word"
    part_of_speech: PartOfSpeech


class Word(BaseModel):
    id: Optional[int]
    name: str
    transcription: Optional[str]
    example: Optional[str]
    relations: Dict[str, "Relation"] = {}


Relation.update_forward_refs()
