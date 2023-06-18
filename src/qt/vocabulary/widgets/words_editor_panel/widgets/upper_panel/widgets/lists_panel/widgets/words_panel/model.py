from typing import (
    Any,
    Optional,
    Tuple,
    Union,
    Iterable,
)

from PyQt6.QtCore import (
    QAbstractListModel,
    QModelIndex,
    QVariant,
    Qt,
)

from src.datamodels import Word


class WordsListModel(QAbstractListModel):
    def __init__(self, parent, words: Tuple[Word, ...]) -> None:
        super().__init__(parent)
        self._current = [*words]
        self._words = {}
        for word in words:
            self._words[word.name] = word

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._current)

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            return QVariant(self._current[index.row()].name)
        return QVariant()

    def get_current_word(self, index: QModelIndex) -> Optional[Word]:
        if index.row() > -1:
            return self._current[index.row()]
        return None

    def append(self, word: Word) -> None:
        exists_word = self._words.get(word.name)
        if exists_word:
            for relation_name, relation in word.relations.items():
                exists_relation = exists_word.relations.get(relation_name)
                if not exists_relation:
                    exists_word.relations[relation_name] = relation
            # exists_word.example = word.example
            exists_word.transcription = word.transcription
            self._words[word.name] = exists_word
        else:
            self._words[word.name] = word
        self.reset()

    def delete(self, word: Word) -> None:
        del self._words[word.name]
        self.reset()

    def change(self, word: Word) -> None:
        pass

    def filter(self, mask: Union[str, Word]):
        if mask:
            self._current = []
            for name, word in self._words.items():
                if name.startswith(mask.lower()):
                    self._current.append(word)
            self.layoutChanged.emit()
        else:
            self.reset()

    def display_words(self, words: Iterable[Word]):
        self._current = []
        for word in words:
            if word.name in self._words:
                self._current.append(word)
        self.layoutChanged.emit()

    def reset(self) -> None:
        self._current = []
        for key, word in self._words.items():
            self._current.append(word)
        self.layoutChanged.emit()
