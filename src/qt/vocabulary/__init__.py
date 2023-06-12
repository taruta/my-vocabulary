import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from .widgets import WordEditorPanelWidget


class WordsEditorWindow(QMainWindow):
    def __init__(
            self,
            main_panel: WordEditorPanelWidget,
    ) -> None:
        super().__init__()
        self.setWindowTitle('Words Editor')
        self.main_panel = main_panel
        self.setCentralWidget(self.main_panel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordsEditorWindow(
        main_panel=WordEditorPanelWidget(),
    )
    window.show()
    app.exec()
