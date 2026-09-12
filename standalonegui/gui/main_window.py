from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
)
from gui.dash_page import DashPage
from gui.setup_page import SetupPage
from gui.flash_page import FlashPage
from gui.c2_manpage import c2ManPage
from gui.payloads_man import PaymanPage
from gui.payload_chainman import ChainmanPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorocaban USB")
        self.resize(1000,650)

        # Main Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Vertical layout for main
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # Navbar setup

        nav_bar = QWidget()
        nav_layout = QHBoxLayout(nav_bar)

        nav_layout.setContentsMargins(10, 10 ,10 ,10 )

        self.dash_button = QPushButton("Dashboard")
        self.setup_button = QPushButton("Setup")
        self.flash_button = QPushButton("Device Flasher")
        self.c2man_button = QPushButton("C2 Manager")
        self.payman_button = QPushButton("Payloads Manager")
        self.chainman_button = QPushButton("Payload Chaining")

        nav_layout.addWidget(self.dash_button)
        nav_layout.addWidget(self.setup_button)
        nav_layout.addWidget(self.flash_button)
        nav_layout.addWidget(self.c2man_button)
        nav_layout.addWidget(self.payman_button)
        nav_layout.addWidget(self.chainman_button)

        nav_layout.addStretch()

        # Setting up pages:

        self.pages = QStackedWidget()

        self.dash_page = DashPage()
        self.setup_page = SetupPage()
        self.flash_page = FlashPage()
        self.c2man_page = c2ManPage()
        self.payman_page = PaymanPage()
        self.chainman_page = ChainmanPage()

        self.pages.addWidget(self.dash_page)
        self.pages.addWidget(self.setup_page)
        self.pages.addWidget(self.flash_page)
        self.pages.addWidget(self.c2man_page)
        self.pages.addWidget(self.payman_page)
        self.pages.addWidget(self.chainman_page)

        # connecting buttons to pages: (Note im highly aware how janky this is, gonna make a helper at a later date)
        # TODO: MAKE THE HELPER

        self.dash_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.dash_page)
        )

        self.setup_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.setup_page)
        )

        self.flash_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.flash_page)
        )

        self.c2man_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.c2man_page)
        )

        self.payman_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.payman_page)
        )

        self.chainman_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.chainman_page)
        )

        # insert the layouts

        main_layout.addWidget(nav_bar)
        main_layout.addWidget(self.pages)

        #start on dashboard

        self.pages.setCurrentWidget(self.dash_page)