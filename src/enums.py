from enum import Enum


class PartOfSpeech(Enum):
    NOUN = 'noun'
    VERB = 'verb'


class Topic(Enum):
    EMPTY = 'Empty'
    FAMILY = 'Family'


__all__ = (
    'PartOfSpeech',
    'Topic',
)

