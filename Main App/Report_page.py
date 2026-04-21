from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QTableWidget, QTableWidgetItem, QHeaderView


class Rop_Page(QWidget):
    def __init__(self, main_window, Oc_page, Cos_page, Son_page):
        super().__init__()
        self.main_window = main_window
        self.Oc_page = Oc_page
        self.Cos_page = Cos_page
        self.Son_page = Son_page

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        title = QLabel("Report and stats")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title)

        but_occ = QPushButton("Occupancy")
        but_cos = QPushButton("Cost")
        but_Son = QPushButton("Upcoming release")
        but_back5 = QPushButton("Back")

        button_layout.addWidget(but_occ)
        button_layout.addWidget(but_cos)
        button_layout.addWidget(but_Son)
        button_layout.addStretch()
        button_layout.addWidget(but_back5)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.Oc_page.table)
        self.stack.addWidget(self.Cos_page.table)
        self.stack.addWidget(self.Son_page.table)
        layout.addLayout(button_layout)
        layout.addWidget(self.stack, stretch=1)

        self.setLayout(layout)

        but_occ.clicked.connect(lambda: self.show_table(0))
        but_cos.clicked.connect(lambda: self.show_table(1))
        but_Son.clicked.connect(lambda: self.show_table(2))
        but_back5.clicked.connect(self.main_window.show_home)

    def show_table(self, index):
        self.stack.setCurrentIndex(index)




