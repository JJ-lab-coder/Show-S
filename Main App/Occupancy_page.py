from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QTableWidgetItem, QHeaderView, QTableWidget

import random

class Oc_page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Occupancy")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Name", "Location", "Occupied", "Available", "Full%"])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table, 1, 0, 1, 3)

        self.setLayout(layout)

        self.load_Oc(10)

    def load_Oc(self, count):
        Oc = self.random_Oc(count)
        self.table.setRowCount(len(Oc))

        for row, Pi in enumerate(Oc):
            for col, value in enumerate(Pi):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

    def random_Oc(self, count):
        Oc_name = ["Matyas Sykora", "tiril Berge", "Lucie Lefebvre", "Willo johnston", "Penelope Black"]
        location = ["Forty-seven Lincoln Road, Enfield, EN1 1JS", "Thirty-seven Atherstone Avenue, Peterborough, PE3 9TU", "Sixteen Stad Gwastadgoed Isaf, Llwyngwril, LL37 2LA", "The Cottage, Two New Street Yard, Broughton-In-Furness, LA20 6JE", "Six Bentley Close, Howden, DN14 7XW"]


        Oc = []

        for i in range(count):
            Name = random.choice(Oc_name)
            Location = random.choice(location)
            Occupied = random.randint(5, 25)
            Available = random.randint(1, 7)
            Full = random.randint(1, 100)
            Oc.append([Name, Location, Occupied, Available, Full])

        print(f"Generated {len(Oc)} Oc")
        print(Oc)
        return Oc