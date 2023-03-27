from typing import (
    Any,
    Optional,
    Tuple,
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
            self._words[word.name] = exists_word
        else:
            self._words[word.name] = word
        self._reset()

    def delete(self, word: Word) -> None:
        del self._words[word.name]
        self._reset()

    def change(self, word: Word) -> None:
        pass

    def filter(self, mask: str):
        if mask:
            self._current = []
            for name, word in self._words.items():
                if name.startswith(mask.lower()):
                    self._current.append(word)
            self.layoutChanged.emit()
        else:
            self._reset()

    def _reset(self) -> None:
        self._current = []
        for key, word in self._words.items():
            self._current.append(word)
        self.layoutChanged.emit()
