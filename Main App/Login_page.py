from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QLineEdit, QLabel, QWidget, QLineEdit


class Log_Page(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        layout = QGridLayout()
        layout.setSpacing(10)

        title = QLabel("Login in")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        user = QLabel("Username")
        layout.addWidget(user, 1, 0)

        pas = QLabel("Password")
        layout.addWidget(pas, 2, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 1, 1, 1, 2)

        self.input2 = QLineEdit()
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input2, 2, 1, 1, 2)

        button1 = QPushButton("Login")
        button1.clicked.connect(self.login)
        layout.addWidget(button1, 3, 1)

        self.setLayout(layout)

    def login(self):
        if self.input1.text() == "" and self.input2.text() == "":
            print("Login successful")
            self.main_window.show_home()



