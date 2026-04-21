from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QTableWidgetItem, QTableWidgetItem, QHeaderView, QTableWidget

import random

class Hou_page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Housing Management")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Location", "Capacity", "Category", "Cost"])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table, 1, 0, 1, 3)

        but_back2 = QPushButton("Back")
        but_back2.clicked.connect(self.main_window.show_home)
        layout.addWidget(but_back2, 2, 2)

        self.setLayout(layout)

        self.load_Poi(10)

    def load_Poi(self, count):
        Pio = self.random_Pio(count)
        self.table.setRowCount(len(Pio))

        for row, Pi in enumerate(Pio):
            for col, value in enumerate(Pi):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def random_Pio(self, count):
        Pio_name = ["Matyas Sykora", "tiril Berge", "Lucie Lefebvre", "Willo johnston", "Penelope Black"]
        location = ["Forty-seven Lincoln Road, Enfield, EN1 1JS", "Thirty-seven Atherstone Avenue, Peterborough, PE3 9TU", "Sixteen Stad Gwastadgoed Isaf, Llwyngwril, LL37 2LA", "The Cottage, Two New Street Yard, Broughton-In-Furness, LA20 6JE", "Six Bentley Close, Howden, DN14 7XW"]
        category = ["A", "B", "C", "D"]

        Pio = []

        for i in range(count):
            Name = random.choice(Pio_name)
            Location = random.choice(location)
            Capacity = random.randint(5, 25)
            Category = random.choice(category)
            Cost = random.randint(75, 195)
            Pio.append([Name, Location, Capacity, Category, Cost])

        print(f"Generated {len(Pio)} Pio")
        print(Pio)
        return Pio