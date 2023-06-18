from typing import Optional

from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
)

from src.datamodels import (
    Word,
)
from .widgets import WordsPanelWidget


class ListsPanelWidget(QWidget):
    def __init__(
            self,
            parent: QWidget
    ):
        super().__init__(parent=parent)
        self.foreign_panel = WordsPanelWidget(self)
        self.native_panel = WordsPanelWidget(self)
        layout = QGridLayout()
        layout.addWidget(QLabel('Foreign'), 0, 0)
        layout.addWidget(QLabel('Native'), 0, 1)
        layout.addWidget(self.foreign_panel, 1, 0)
        layout.addWidget(self.native_panel, 1, 1)
        self.setLayout(layout)
        self.native_panel.list.clicked.connect(
            self.parent().select
        )
        self.native_panel.list.clicked.connect(
            self._filter_by_native
        )
        self.foreign_panel.list.clicked.connect(
            self.parent().select
        )
        self.foreign_panel.list.clicked.connect(
            self._filter_by_foreign
        )

    def remove(
            self,
            native: Optional[Word],
            foreign: Optional[Word],
    ) -> None:
        if native and not native.has_relations():
            self.native_panel.remove(native)
        if foreign and not foreign.has_relations():
            self.foreign_panel.remove(foreign)
        self.parent().cancel()

    def cancel(self) -> None:
        self.native_panel.cancel()
        self.foreign_panel.cancel()

    def add_native(self, word: Word) -> None:
        self.native_panel.add(word)

    def add_foreign(self, word: Word) -> None:
        self.foreign_panel.add(word)

    def get_current_native(self) -> Word:
        return self.native_panel.get_current()

    def get_current_foreign(self) -> Word:
        return self.foreign_panel.get_current()

    def _filter_by_native(self):
        native = self.native_panel.get_current()
        foreign = self.foreign_panel.get_current()
        if not foreign or foreign.name not in native.relations:
            self.foreign_panel.filter_by_relations(
               tuple(relation for relation in native.relations.values())
            )

    def _filter_by_foreign(self):
        native = self.native_panel.get_current()
        foreign = self.foreign_panel.get_current()
        if not native or native.name not in foreign.relations:
            self.native_panel.filter_by_relations(
                tuple(relation for relation in foreign.relations.values())
            )


__all__ = (
    'ListsPanelWidget',
)
