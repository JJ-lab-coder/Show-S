from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView,
                               QAbstractItemView)


class Allo_page(QWidget):
    def __init__(self, main_window, res_page, hou_page, liv_page):
        super().__init__()
        self.main_window = main_window
        self.res_page = res_page
        self.hou_page = hou_page
        self.liv_page = liv_page

        self.picked_res = None
        self.picked_hou = None

        layout = QGridLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Allocation System")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size:24px; font-weight:bold;")
        layout.addWidget(title, 0, 0, 1, 3)

        self.res_table = QTableWidget()
        self.res_table.setColumnCount(3)
        self.res_table.setHorizontalHeaderLabels(["Name", "category", "Case ID"])
        self.res_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.res_table, 1, 0)

        self.res_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.res_table.cellClicked.connect(self.clicked_res)

        self.house_table = QTableWidget()
        self.house_table.setColumnCount(3)
        self.house_table.setHorizontalHeaderLabels(["Pio", "category", "Capacity"])
        self.house_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.house_table, 1, 1)

        self.house_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.house_table.cellClicked.connect(self.clicked_hou)

        but_allocate = QPushButton("Allocate")
        but_allocate.clicked.connect(self.main_window.show_live)
        layout.addWidget(but_allocate, 2, 0)

        but_back3 = QPushButton("Back")
        but_back3.clicked.connect(self.main_window.show_home)
        layout.addWidget(but_back3, 2, 1)

        self.setLayout(layout)

        self.load_res2()
        self.load_hou2()

    def load_res2(self):
        source = self.res_page.table
        row_count = source.rowCount()
        self.res_table.setRowCount(row_count)

        for row in range(row_count):
            name = source.item(row, 0)
            category = source.item(row, 3)
            case_id = source.item(row, 2)

            self.res_table.setItem(row, 0, QTableWidgetItem(name))
            self.res_table.setItem(row, 1, QTableWidgetItem(category))
            self.res_table.setItem(row, 2, QTableWidgetItem(case_id))

    def load_hou2(self):
        source = self.hou_page.table
        row_count = source.rowCount()
        self.house_table.setRowCount(row_count)

        for row in range(row_count):
            name = source.item(row, 0)
            category = source.item(row, 3)
            capacity = source.item(row, 2)
            self.house_table.setItem(row, 0, QTableWidgetItem(name))
            self.house_table.setItem(row, 1, QTableWidgetItem(category))
            self.house_table.setItem(row, 2, QTableWidgetItem(capacity))

    def clicked_res(self, row, column):
        row_data = []

        for col in range(self.res_table.columnCount()):
            item = self.res_table.item(row, col)
            if item:
                row_data.append(item.text())

        self.picked_res = row_data
        self.liv_page.load_resinfo(row_data)


    def clicked_hou(self, row, column):
        row_data = []

        for col in range(self.house_table.columnCount()):
            item = self.house_table.item(row, col)
            if item:
                row_data.append(item.text())

        self.picked_hou = row_data
        self.liv_page.load_houinfo(row_data)
