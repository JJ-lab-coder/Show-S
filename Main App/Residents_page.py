from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QTableWidget, QInputDialog, QLineEdit, QMessageBox, QMessageBox
import random
from datetime import date, timedelta


class Res_page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30,30,30,30)

        title = QLabel("Residents management")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["First name", "Surname", "Case number ID", "Category", "Release date", "Gender"])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table, 1, 0, 1, 3)

        but_back1 = QPushButton("Back")
        but_back1.clicked.connect(self.main_window.show_home)
        layout.addWidget(but_back1, 2, 2)

        self.setLayout(layout)

        self.load_res(10)

    def load_res(self, count):
        residents = self.radom_res(count)
        self.table.setRowCount(len(residents))

        for row, resident in enumerate(residents):
            for col, value in enumerate(resident):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def radom_res(self, count):
        first_name_list = ["caden", "Ailami", "Trevor", "Hixley", "Riggs", "Rowen", "Madden"]
        surname_list = ["Bradshaw", "Wyatt", "Jax", "Snow", "Bulter", "Fuller", "Zhang"]
        category_list = ["A", "B", "C", "D"]
        gender_list = ["Male", "Female"]

        residents =  []
        for i in range(count):
            first_name = random.choice(first_name_list)
            surname = random.choice(surname_list)
            case_numbers_ID = f"ID{1000 + i}"
            category = random.choice(category_list)
            gender = random.choice(gender_list)

            days = random.randint(30, 826)
            release_date = date.today() + timedelta(days=days)

            residents.append([first_name, surname, case_numbers_ID, category, release_date, gender])
        print(f"Generated {len(residents)} residents")
        print(residents)
        return residents




