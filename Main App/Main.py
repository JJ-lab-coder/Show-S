import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import Qt

from Login_page import Log_Page
from Home_page import Hom_page
from Residents_page import Res_page
from Housing_page import Hou_page
from Allocation_page import Allo_page
from Live_page import Liv_page
from Report_page import Rop_Page
from Occupancy_page import Oc_page
from Cost_page import Cos_page
from Soon_release_page import Son_page



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Allocation System")

        menubar = self.menuBar()

        fileMenu = menubar.addMenu("File")
        editMenu = menubar.addMenu("Edit")
        helpMenu = menubar.addMenu("Help")
        aboutAction = helpMenu.addAction("About")
        settingsAction = menubar.addMenu("Settings")

        submenu = menubar.addMenu("App Pages")
        homeAction = submenu.addAction("Home")
        residentsAction = submenu.addAction("Residents")
        allocationAction = submenu.addAction("Allocation")
        reportAction = submenu.addAction("Report")
        exitAction = submenu.addAction("Exit")

        exitAction.triggered.connect(self.close)
        homeAction.triggered.connect(self.show_home)
        residentsAction.triggered.connect(self.show_residents)
        allocationAction.triggered.connect(self.show_allocation)
        reportAction.triggered.connect(self.show_report)
        aboutAction.triggered.connect(lambda : print("this is an allocation app"))



        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.Login_page = Log_Page(self)
        self.Home_page = Hom_page(self)
        self.Residents_page = Res_page(self)
        self.Housing_page = Hou_page(self)
        self.Liv_page = Liv_page(self, self.Housing_page, self.Residents_page)
        self.Allo_page = Allo_page(self, self.Residents_page, self.Housing_page, self.Liv_page)
        self.Oc_Page = Oc_page(self)
        self.Cos_page = Cos_page(self)
        self.Son_page = Son_page(self)


        self.Rop_Page = Rop_Page(self, self.Oc_Page, self.Cos_page, self.Son_page)


        self.stacked_widget.addWidget(self.Login_page)
        self.stacked_widget.addWidget(self.Home_page)
        self.stacked_widget.addWidget(self.Residents_page)
        self.stacked_widget.addWidget(self.Housing_page)
        self.stacked_widget.addWidget(self.Allo_page)
        self.stacked_widget.addWidget(self.Liv_page)
        self.stacked_widget.addWidget(self.Oc_Page)
        self.stacked_widget.addWidget(self.Cos_page)
        self.stacked_widget.addWidget(self.Son_page)


        self.stacked_widget.addWidget(self.Rop_Page)

        self.show_login()

    def show_login(self):
        self.stacked_widget.setCurrentWidget(self.Login_page)

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.Home_page)

    def show_residents(self):
        self.stacked_widget.setCurrentWidget(self.Residents_page)

    def show_housing(self):
        self.stacked_widget.setCurrentWidget(self.Housing_page)

    def show_allocation(self):
        self.stacked_widget.setCurrentWidget(self.Allo_page)

    def show_live(self):
        self.stacked_widget.setCurrentWidget(self.Liv_page)

    def show_report(self):
        self.stacked_widget.setCurrentWidget(self.Rop_Page)

    def show_occupancy(self):
        self.stacked_widget.setCurrentWidget(self.Oc_Page)

    def show_cost(self):
        self.stacked_widget.setCurrentWidget(self.Cos_page)

    def show_soon(self):
        self.stacked_widget.setCurrentWidget(self.Son_page)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()