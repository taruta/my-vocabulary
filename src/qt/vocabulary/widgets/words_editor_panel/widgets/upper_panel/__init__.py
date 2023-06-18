from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from src.datamodels import (
    Word,
    Relation,
)

from .widgets import (
    EditPanelWidget,
    ListsPanelWidget,
)


class UpperPanelWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._edit_panel = EditPanelWidget(self)
        self._lists_panel = ListsPanelWidget(self)
        layout = QGridLayout()
        layout.addWidget(self._edit_panel, 0, 0)
        layout.addWidget(self._lists_panel, 0, 1)
        self.setLayout(layout)

    def save(self) -> None:
        native_word = None
        if self._edit_panel.native.text():
            native_word = Word(
                name=self._edit_panel.native.text(),
            )
        foreign_word = None
        if self._edit_panel.foreign.text():
            foreign_word = Word(
                name=self._edit_panel.foreign.text(),
                transcription=self._edit_panel.transcription.text(),
                topic=self._edit_panel.topic.currentText(),
            )
        if native_word and foreign_word:
            part_of_speech = \
                self._edit_panel.part_of_speech.currentText()
            native_word.relations[foreign_word.name] = Relation(
                word=foreign_word,
                part_of_speech=part_of_speech,
            )
            foreign_word.relations[native_word.name] = Relation(
                word=native_word,
                part_of_speech=part_of_speech,
                example=self._edit_panel.example.text(),
            )
        if native_word:
            self._lists_panel.add_native(
                word=native_word,
            )
        if foreign_word:
            self._lists_panel.add_foreign(
                word=foreign_word,
            )
        self._edit_panel.cancel()

    def delete(self) -> None:
        native = self._lists_panel.get_current_native()
        foreign = self._lists_panel.get_current_foreign()
        if native and foreign:
            if native.relations.get(foreign.name):
                native.remove_relation(foreign.name)
            if foreign.relations.get(native.name):
                foreign.remove_relation(native.name)
        self._lists_panel.remove(
            native=native,
            foreign=foreign,
        )

    def cancel(self) -> None:
        self._edit_panel.cancel()
        self._lists_panel.cancel()

    def select(self) -> None:
        self._edit_panel.transcription.clear()
        self._edit_panel.example.clear()
        native = self._lists_panel.native_panel.get_current()
        foreign = self._lists_panel.foreign_panel.get_current()
        if native:
            self._edit_panel.native.setText(native.name)
        if foreign:
            self._edit_panel.foreign.setText(foreign.name)
            self._edit_panel.transcription.setText(foreign.transcription)
            self._edit_panel.topic.setCurrentText(foreign.topic)
        if native and foreign:
            native_rel = native.relations.get(foreign.name)
            foreign_rel = foreign.relations.get(native.name)
            if native_rel and foreign_rel:
                self._edit_panel.part_of_speech.setCurrentText(
                    foreign_rel.part_of_speech.value
                )
                self._edit_panel.example.setText(
                    foreign_rel.example,
                )

    def clear_native_line(self):
        self._edit_panel.native.clear()

    def clear_foreign_line(self):
        self._edit_panel.foreign.clear()



__all__ = (
    'UpperPanelWidget',
)
