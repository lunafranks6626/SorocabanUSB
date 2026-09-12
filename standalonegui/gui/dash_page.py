from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class DashPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("Dashboard")
        description = QLabel("like a dashboard lol")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()