from PySide6.QtCore import Qt
from PySide6.QtWidgets import ( QWidget, QLabel, QPushButton, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView )


class Liv_page(QWidget):
    def __init__(self, main_window, res_page, hou_page):
        super().__init__()
        self.main_window = main_window
        self.res_page = res_page
        self.hou_page = hou_page

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Allocated residents")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.resident_label = QLabel("no residents selected")
        self.house_label = QLabel("no house selected")

        but_back4 = QPushButton("Back")
        but_back4.clicked.connect(self.main_window.show_allocation)
        layout.addWidget(but_back4, 3, 0)

        layout.addWidget(self.resident_label, 1, 0)
        layout.addWidget(self.house_label, 2, 0)

        self.setLayout(layout)

    def load_resinfo(self, data):
        self.resident_label.setText(f"Resident:{data}")

    def load_houinfo(self, data):
        self.house_label.setText(f"House:{data}")


