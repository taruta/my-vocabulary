from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout


class BottomPanelWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.save_btn = QPushButton('Save')
        self.save_btn.clicked.connect(
            self.parent().save,
        )
        self.delete_btn = QPushButton('Delete')
        self.delete_btn.clicked.connect(
            self.parent().delete,
        )
        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.clicked.connect(
            self.parent().cancel,
        )
        self.layout = QGridLayout()
        self.layout.addWidget(self.save_btn, 0, 0)
        self.layout.addWidget(self.delete_btn, 0, 1)
        self.layout.addWidget(self.cancel_btn, 0, 2)
        self.setLayout(self.layout)
