from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
)

from src.datamodels import Word
from ..list_view import WordsListView
from ..words_list_model import WordsListModel


class ListsPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._foreign_model = WordsListModel(self, ())
        self._foreign_list = WordsListView(self)
        self._foreign_list.setModel(
            self._foreign_model,
        )
        self._native_model = WordsListModel(self, ())
        self._native_list = WordsListView(self)
        self._native_list.setModel(
            self._native_model,
        )
        self._native_list_filter = QLineEdit()
        self._native_list_filter.textChanged.connect(
            self._filter_native
        )
        self._foreign_list_filter = QLineEdit()
        self._foreign_list_filter.textChanged.connect(
            self._filter_foreign
        )
        layout = QGridLayout()
        layout.addWidget(QLabel('Foreign'), 0, 0)
        layout.addWidget(QLabel('Native'), 0, 1)
        layout.addWidget(self._foreign_list, 1, 0)
        layout.addWidget(self._native_list, 1, 1)
        layout.addWidget(self._foreign_list_filter, 2, 0)
        layout.addWidget(self._native_list_filter, 2, 1)
        self.setLayout(layout)

    def add_native(self, word: Word):
        self._native_model.append(
            word=word,
        )

    def add_foreign(self, word: Word):
        self._foreign_model.append(
            word=word,
        )

    def remove(self):
        native = self._native_model.get_current_word(
            self._native_list.currentIndex()
        )
        foreign = self._foreign_model.get_current_word(
            self._foreign_list.currentIndex()
        )
        if native and foreign and \
                native.relations.get(foreign.name) and \
                foreign.relations.get(native.name):
            native.remove_relation(foreign.name)
            foreign.remove_relation(native.name)
        if native and native.has_relations():
            self._remove_native(native)
        if foreign and foreign.has_relations():
            self._remove_foreign(foreign)

    def cancel(self):
        self._native_list.setCurrentIndex(
            self._native_model.index(-1)
        )
        self._foreign_list.setCurrentIndex(
            self._foreign_model.index(-1)
        )
        self._native_list_filter.setText('')
        self._foreign_list_filter.setText('')

    def _filter_foreign(self):
        self._foreign_model.filter(
            self._foreign_list_filter.text()
        )

    def _filter_native(self):
        self._native_model.filter(
            self._native_list_filter.text()
        )

    def _remove_native(self, word: Word):
        if not word.has_relations():
            self._native_model.delete(word)
            self._native_list.setCurrentIndex(
                self._native_model.index(-1)
            )

    def _remove_foreign(self, word: Word):
        if not word.has_relations():
            self._foreign_model.delete(word)
            self._foreign_list.setCurrentIndex(
                self._foreign_model.index(-1)
            )
