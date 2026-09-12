from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class FlashPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel ("Flasher Page")
        description = QLabel("Page for flashing USB Army Knife firmware")

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()