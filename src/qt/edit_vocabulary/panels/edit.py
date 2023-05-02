from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
    QComboBox,
)

from src.enums import (
    PartOfSpeech,
    Topic,
)


class EditPanelWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setFixedSize(400, 200)
        self.foreign = QLineEdit()
        self.native = QLineEdit()
        self.part_of_speech = QComboBox()
        self.part_of_speech.addItems(
            (
                PartOfSpeech.NOUN.value,
                PartOfSpeech.VERB.value,
            )
        )
        self.transcription = QLineEdit()
        self.example = QLineEdit()
        self.topic = QComboBox()
        self.topic.addItems(
            (
                Topic.EMPTY.value,
                Topic.FAMILY.value,
            )
        )
        layout = QGridLayout()
        layout.addWidget(QLabel('Part of speech'), 0, 0)
        layout.addWidget(QLabel('Topic'), 1, 0)
        layout.addWidget(QLabel('Foreign'), 2, 0)
        layout.addWidget(QLabel('Native'), 3, 0)
        layout.addWidget(QLabel('Transcription'), 4, 0)
        layout.addWidget(QLabel('Example'), 5, 0)
        layout.addWidget(self.part_of_speech, 0, 1)
        layout.addWidget(self.topic, 1, 1)
        layout.addWidget(self.foreign, 2, 1)
        layout.addWidget(self.native, 3, 1)
        layout.addWidget(self.transcription, 4, 1)
        layout.addWidget(self.example, 5, 1)
        self.setLayout(layout)

    def cansel(self) -> None:
        self.foreign.clear()
        self.native.clear()
        self.transcription.clear()
        self.example.clear()
        self.part_of_speech.setCurrentText(PartOfSpeech.NOUN.value)
        self.topic.setCurrentText(Topic.EMPTY.value)
