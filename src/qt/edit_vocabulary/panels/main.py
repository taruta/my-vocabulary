from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from .bottom import BottomPanelWidget
from .upper import UpperPanelWidget


class MainPanelWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        upper_panel = UpperPanelWidget(self)
        bottom_panel = BottomPanelWidget(
            self,
            panel=upper_panel
        )
        self.upper_panel = upper_panel
        self.bottom_panel = bottom_panel
        self.layout = QGridLayout()
        self.layout.addWidget(upper_panel, 0, 0)
        self.layout.addWidget(bottom_panel, 1, 0)
        self.setLayout(self.layout)
