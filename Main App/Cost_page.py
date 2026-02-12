from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QTableWidgetItem, QHeaderView, QTableWidget

import random

class Cos_page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Cost")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Capacity", "Occupied", "Cost pcm£"])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table, 1, 0, 1, 3)

        self.setLayout(layout)

        self.load_Cos(10)

    def load_Cos(self, count):
        Cos = self.random_Cos(count)
        self.table.setRowCount(len(Cos))

        for row, Pi in enumerate(Cos):
            for col, value in enumerate(Pi):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def random_Cos(self, count):
        Cos_name = ["Matyas Sykora", "tiril Berge", "Lucie Lefebvre", "Willo johnston", "Penelope Black"]

        Cos = []

        for i in range(count):
            Name = random.choice(Cos_name)
            Capacity = random.randint(18, 30)
            Occupied = random.randint(5, 18)
            Cost_pcm = random.randint(1, 100)
            Cos.append([Name, Capacity, Occupied, Cost_pcm])

        print(f"Generated {len(Cos)} Cos")
        print(Cos)
        return Cos