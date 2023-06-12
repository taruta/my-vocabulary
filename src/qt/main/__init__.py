import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from src.qt.main.widgets import MainPanelWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Menu')
        self.main_panel = MainPanelWidget(self)
        self.setCentralWidget(self.main_panel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
