from PySide6.QtWidgets import QApplication as QApp
from gui.main_window import MainWindow
import sys

def main():
    app = QApp(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()