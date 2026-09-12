from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ChainmanPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("Payload Chaining Manager page")
        description = QLabel("Page for the creation of autoruns that chain payloads based on user defined attributes")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()