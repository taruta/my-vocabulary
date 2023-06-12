from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QLabel,
)

from ..edit import EditPanelWidget
from .widgets import WordsPanelWidget


class ListsPanelWidget(QWidget):
    def __init__(
            self,
            parent: QWidget,
            edit_panel: EditPanelWidget
    ):
        super().__init__(parent=parent)
        self._edit_panel = edit_panel
        self.foreign_panel = WordsPanelWidget(self)
        self.native_panel = WordsPanelWidget(self)
        layout = QGridLayout()
        layout.addWidget(QLabel('Foreign'), 0, 0)
        layout.addWidget(QLabel('Native'), 0, 1)
        layout.addWidget(self.foreign_panel, 1, 0)
        layout.addWidget(self.native_panel, 1, 1)
        self.setLayout(layout)
        self.native_panel.list.clicked.connect(
            self._select
        )
        self.native_panel.list.clicked.connect(
            self._filter_by_native
        )
        self.foreign_panel.list.clicked.connect(
            self._select
        )
        self.foreign_panel.list.clicked.connect(
            self._filter_by_foreign
        )

    def remove(self) -> None:
        native = self.native_panel.get_current()
        foreign = self.foreign_panel.get_current()
        if native and foreign and \
                native.relations.get(foreign.name) and \
                foreign.relations.get(native.name):
            native.remove_relation(foreign.name)
            foreign.remove_relation(native.name)
        if native and not native.has_relations():
            self.native_panel.remove(native)
            self._edit_panel.native.clear()
        if foreign and not foreign.has_relations():
            self.foreign_panel.remove(foreign)
            self._edit_panel.foreign.clear()

    def cancel(self) -> None:
        self.native_panel.cancel()
        self.foreign_panel.cancel()

    def _select(self) -> None:
        native = self.native_panel.get_current()
        foreign = self.foreign_panel.get_current()
        if native:
            self._edit_panel.native.setText(native.name)
        if foreign:
            self._edit_panel.foreign.setText(foreign.name)
        if native and foreign:
            native_rel = native.relations.get(foreign.name)
            foreign_rel = foreign.relations.get(native.name)
            if native_rel and foreign_rel:
                self._edit_panel.transcription.setText(
                    foreign.transcription
                )
                self._edit_panel.example.setText(
                    foreign.example
                )
                self._edit_panel.topic.setCurrentText(
                    foreign.topic
                )
                self._edit_panel.part_of_speech.setCurrentText(
                    foreign_rel.part_of_speech.value
                )
        else:
            self._edit_panel.transcription.clear()
            self._edit_panel.example.clear()

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
