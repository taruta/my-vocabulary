from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout


class EditPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)
        self.foreign = QLineEdit()
        self.native = QLineEdit()
        self.part_of_speech = QLineEdit()
        self.transcription = QLineEdit()
        self.example = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(QLabel('Foreign'), 0, 0)
        layout.addWidget(QLabel('Native'), 1, 0)
        layout.addWidget(QLabel('Part of speech'), 2, 0)
        layout.addWidget(QLabel('Transcription'), 3, 0)
        layout.addWidget(QLabel('Example'), 4, 0)
        layout.addWidget(self.foreign, 0, 1)
        layout.addWidget(self.native, 1, 1)
        layout.addWidget(self.part_of_speech, 2, 1)
        layout.addWidget(self.transcription, 3, 1)
        layout.addWidget(self.example, 4, 1)
        self.setLayout(layout)

    def clear_all(self):
        self.foreign.setText('')
        self.native.setText('')
        self.transcription.setText('')
        self.example.setText('')
        self.part_of_speech.setText('')
