from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
import sys
from src.qt.edit_vocabulary.panels import (
    MainPanelWidget,
    BottomPanelWidget,
    UpperPanelWidget,
)


class MainWindow(QMainWindow):
    def __init__(
            self,
            main_panel: MainPanelWidget,
    ) -> None:
        super().__init__()
        self.setWindowTitle('Words Editor')
        self.main_panel = main_panel
        self.setCentralWidget(self.main_panel)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(
        main_panel=MainPanelWidget(),
    )
    window.show()
    app.exec()

