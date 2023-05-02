from typing import Tuple

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLineEdit,
)

from src.datamodels import Word, Relation
from ..list_view import WordsListView
from ..words_list_model import WordsListModel


class WordsPanelWidget(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        self._model = WordsListModel(self, ())
        self.list = WordsListView(self)
        self.list.setModel(
            self._model,
        )
        self._words_filter = QLineEdit()
        self._words_filter.textChanged.connect(
            self._filter
        )
        layout = QGridLayout()
        layout.addWidget(self.list, 0, 0)
        layout.addWidget(self._words_filter, 1, 0)
        self.setLayout(layout)

    def get_current(self) -> Word:
        return self._model.get_current_word(
            self.list.currentIndex()
        )

    def add(self, word: Word):
        self._model.append(
            word=word,
        )

    def remove(self, word: Word):
        if not word.has_relations():
            self._model.delete(word)
            self.list.setCurrentIndex(
                self._model.index(-1)
            )

    def cancel(self):
        self.list.clearSelection()
        self.list.setCurrentIndex(
            self._model.index(-1)
        )
        self._words_filter.clear()
        self._model.reset()

    def filter_by_relations(self, relations: Tuple[Relation, ...]):
        words = []
        for relation in relations:
            words.append(relation.word)
        self._model.display_words(words)
        self.list.setCurrentIndex(
            self._model.index(-1)
        )

    def _filter(self):
        self._model.filter(
            self._words_filter.text()
        )
