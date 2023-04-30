from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from src.datamodels import (
    Word,
    Relation,
)
from .edit import EditPanelWidget
from .lists import ListsPanelWidget


class UpperPanelWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.edit_panel = EditPanelWidget(self)
        self.lists_panel = ListsPanelWidget(
            self,
            self.edit_panel,
        )
        layout = QGridLayout()
        layout.addWidget(self.edit_panel, 0, 0)
        layout.addWidget(self.lists_panel, 0, 1)
        self.setLayout(layout)

    def save(self):
        native_word = None
        if self.edit_panel.native.text():
            native_word = Word(
                name=self.edit_panel.native.text(),
            )
        foreign_word = None
        if self.edit_panel.foreign.text():
            foreign_word = Word(
                name=self.edit_panel.foreign.text(),
                transcription=self.edit_panel.transcription.text(),
                example=self.edit_panel.example.text(),
            )
        if native_word and foreign_word:
            part_of_speech = \
                self.edit_panel.part_of_speech.currentText().lower()
            native_word.relations[foreign_word.name] = Relation(
                word=foreign_word,
                part_of_speech=part_of_speech,
            )
            foreign_word.relations[native_word.name] = Relation(
                word=native_word,
                part_of_speech=part_of_speech,
            )
        if native_word:
            self.lists_panel.native_panel.add(
                word=native_word,
            )
        if foreign_word:
            self.lists_panel.foreign_panel.add(
                word=foreign_word,
            )
        self.edit_panel.clean()

    def delete(self):
        self.lists_panel.remove()

    def cancel(self):
        self.edit_panel.clean()
        self.lists_panel.cancel()
