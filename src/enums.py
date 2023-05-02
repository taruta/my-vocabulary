from enum import Enum


class PartOfSpeech(Enum):
    NOUN = 'Noun'
    VERB = 'Verb'


class Topic(Enum):
    EMPTY = 'Empty'
    FAMILY = 'Family'


__all__ = (
    'PartOfSpeech',
    'Topic',
)

