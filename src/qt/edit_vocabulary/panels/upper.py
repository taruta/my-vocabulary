from PyQt6.QtWidgets import QWidget, QGridLayout
from .edit import EditPanelWidget
from .lists import ListsPanelWidget
from src.datamodels import Word, Relation


class UpperPanelWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.edit_panel = EditPanelWidget()
        self.lists_panel = ListsPanelWidget()
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
            native_word.relations[foreign_word.name] = Relation(
                word=foreign_word,
                part_of_speech=self.edit_panel.part_of_speech.text()
            )
            foreign_word.relations[native_word.name] = Relation(
                word=foreign_word,
                part_of_speech=self.edit_panel.part_of_speech.text()
            )
        if native_word:
            self.lists_panel.add_native(
                word=native_word,
            )
        if foreign_word:
            self.lists_panel.add_foreign(
                word=foreign_word,
            )

    def delete(self):
        self.lists_panel.delete()

    def cancel(self):
        self.edit_panel.clear_all()
        self.lists_panel.cancel()
