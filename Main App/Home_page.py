from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton

class Hom_page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(40, 40, 40, 40)

        title = QLabel("Housing system")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        subtitle = QLabel("Options:")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(subtitle, 1, 0, 1, 3)

        but_residents = QPushButton("Residents")
        but_residents.clicked.connect(self.main_window.show_residents)
        layout.addWidget(but_residents, 2, 0, 1, 3)

        but_housing = QPushButton("Housing Unit")
        but_housing.clicked.connect(self.main_window.show_housing)
        layout.addWidget(but_housing, 3, 0, 1, 3)

        but_allocation = QPushButton("Allocation")
        but_allocation.clicked.connect(self.main_window.show_allocation)
        layout.addWidget(but_allocation, 4, 0, 1, 3)

        but_report = QPushButton("Report")
        but_report.clicked.connect(self.main_window.show_report)
        layout.addWidget(but_report, 5, 0, 1, 3)

        but_logout = QPushButton("Logout")
        but_logout.clicked.connect(self.main_window.show_login)
        but_logout.setStyleSheet("background-color: #f00000; color: white;")
        layout.addWidget(but_logout, 6, 0, 1, 3)

        self.setLayout(layout)

