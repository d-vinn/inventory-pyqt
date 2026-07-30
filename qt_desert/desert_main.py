from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from settings import Set
from show_menu import ShowMenu
from PyQt5.QtGui import QIcon
from login import LoginDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert")
        self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/coffee-shop.png"))
        self.setStyleSheet('background-color:white;')

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        self.btn_set = QPushButton("설정")
        self.btn_set.setStyleSheet('color:white; background-color:rgb(70,70,70); border-style: outset; border-width: 2px; border-radius: 15px; border-color: rgb(70,70,70);')
        self.btn_set.setFixedHeight(15)
        self.btn_set.setFixedWidth(30)
        self.btn_set.clicked.connect(self.open_settings)
        self.btn_start = QPushButton("주문 시작하기")
        self.btn_start.setStyleSheet('color:white; background-color:black')
        self.btn_start.clicked.connect(self.open_show_menu)

        form_box = QVBoxLayout()
        form_box.addWidget(self.btn_set)
        form_box.addWidget(QLabel("<H1>🥨QT Dessert🥨</H1>"))
        form_box.addWidget(QLabel("주문을 원하시면 주문 시작하기 버튼을 눌러주세요."))
        form_box.addWidget(self.btn_start)

        vbox.addLayout(form_box)
    
    def open_settings(self):
        login = LoginDialog()
        if login.exec_() == LoginDialog.Accepted:
            self.w = Set()
            self.w.show()
        else:
            sys.exit(0)

    def open_show_menu(self):
        self.show_win = ShowMenu()
        self.show_win.show()



        
