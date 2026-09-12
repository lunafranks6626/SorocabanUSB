from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SetupPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("Setup Page")
        description = QLabel("This is a setup page ig")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()