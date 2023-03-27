from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QGridLayout,
    QComboBox,
)

from src.enums import PartOfSpeech


class EditPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)
        self.foreign = QLineEdit()
        self.native = QLineEdit()
        self.part_of_speech = QComboBox()
        self.part_of_speech.addItems(
            (
                PartOfSpeech.NOUN.value.capitalize(),
                PartOfSpeech.VERB.value.capitalize(),
            )
        )
        self.transcription = QLineEdit()
        self.example = QLineEdit()
        self.topic = QComboBox()
        self.topic.addItems(('Empty',))
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

    def clear_all(self):
        self.foreign.setText('')
        self.native.setText('')
        self.transcription.setText('')
        self.example.setText('')
