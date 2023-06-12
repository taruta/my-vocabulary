from enum import Enum


class PartOfSpeech(Enum):
    NOUN = 'Noun'
    VERB = 'Verb'
    ADJECTIVE = 'Adjective'


class Topic(Enum):
    EMPTY = 'Empty'
    FAMILY = 'Family'


__all__ = (
    'PartOfSpeech',
    'Topic',
)

