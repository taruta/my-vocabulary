from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit
from src.datamodels import Word
from ..words_list_model import WordsListModel
from ..list_view import WordsListView


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
        # self._native_list_filter.textChanged.connect(some)
        self._foreign_list_filter = QLineEdit()
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

    def delete(self):
        native = self._native_model.get(
            self._native_list.currentIndex()
        )
        foreign = self._foreign_model.get(
            self._foreign_list.currentIndex()
        )
        if native and foreign:
            del native.relations[foreign.name]
            del foreign.relations[native.name]

            if len(native.relations) == 0:
                self._native_model.delete(native)
                self._native_list.setCurrentIndex(
                    self._native_model.index(-1)
                )
            if len(foreign.relations) == 0:
                self._foreign_model.delete(foreign)
                self._foreign_list.setCurrentIndex(
                    self._foreign_model.index(-1)
                )

    def cancel(self):
        self._native_list.setCurrentIndex(
            self._native_model.index(-1)
        )
        self._foreign_list.setCurrentIndex(
            self._foreign_model.index(-1)
        )
        self._native_list_filter.setText('')
        self._foreign_list_filter.setText('')
