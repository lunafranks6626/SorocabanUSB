from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class PaymanPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("Payload Manager")
        description = QLabel("Page for managing payloads both premade and user defined.")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()