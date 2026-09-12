from PySide6.QtWidgets import QApplication as QApp
from gui.main_window import MainWindow
import sys

def main():
    app = QApp(sys.argv)

    with open("resources/styles/main.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()