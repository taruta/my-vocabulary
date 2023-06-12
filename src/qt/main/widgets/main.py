from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
    QPushButton,
)
from src.qt.vocabulary import WordsEditorWindow
from src.qt.vocabulary.panels import WordEditorPanelWidget


class MainPanelWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self._window = WordsEditorWindow(
            main_panel=WordEditorPanelWidget(),
        )
        self._window.destroyed.connect(
            self._destroyed
        )
        self.layout = QGridLayout()
        self._vocabulary_btn = QPushButton(
            parent=self,
            text='Vocabulary',
        )
        self._vocabulary_btn.clicked.connect(
            self._show_word_editor
        )
        self.layout.addWidget(self._vocabulary_btn)
        self.setLayout(self.layout)

    def _show_word_editor(self, checked: bool):
        self.parent().hide()
        self._window.show()

    def _destroyed(self):
        self.parent().show()
