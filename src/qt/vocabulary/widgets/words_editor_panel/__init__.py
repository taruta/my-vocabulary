from PyQt6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from .widgets import (
    BottomPanelWidget,
    UpperPanelWidget,
)


class WordEditorPanelWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._upper_panel = UpperPanelWidget(self)
        self._bottom_panel = BottomPanelWidget(self)
        self._layout = QGridLayout()
        self._layout.addWidget(self._upper_panel, 0, 0)
        self._layout.addWidget(self._bottom_panel, 1, 0)
        self.setLayout(self._layout)

    def save(self) -> None:
        self._upper_panel.save(),

    def delete(self) -> None:
        self._upper_panel.delete(),

    def cancel(self) -> None:
        self._upper_panel.cancel(),


__all__ = (
    'WordEditorPanelWidget',
)
