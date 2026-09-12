from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class c2ManPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("C2 Manager Page")
        description = QLabel("Page for managing the C2 server backend")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()