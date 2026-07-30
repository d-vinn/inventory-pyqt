from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
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

        self.setFixedSize(450, 800)  #ch

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)
        vbox.setContentsMargins(20, 20, 20, 40) 

        top_box = QHBoxLayout()
        self.btn_set = QPushButton("설정")
        self.btn_set.setStyleSheet('color:white; background-color:rgb(180,180,180);border: none;')
        self.btn_set.setFixedHeight(20)
        self.btn_set.setFixedWidth(40)
        self.btn_set.clicked.connect(self.open_settings)

        top_box.addStretch(1)
        top_box.addWidget(self.btn_set)
        vbox.addLayout(top_box)

        vbox.addStretch(2) 

        main = QLabel("<H1>🥨QT Dessert🥨</H1>")
        main.setStyleSheet('color:black;')
        main.setAlignment(Qt.AlignCenter)
        vbox.addWidget(main)

        vbox.addStretch(3)

        explanation = QLabel("주문을 원하시면 주문 시작하기 버튼을 눌러주세요.")
        explanation.setStyleSheet('color:rgb(150,150,150); font-size: 13px;')  
        explanation.setAlignment(Qt.AlignCenter)
        vbox.addWidget(explanation)  

        vbox.addSpacing(15)  

        self.btn_start = QPushButton("주문 시작하기")
        self.btn_start.setStyleSheet('color:white; background-color:black; border: none; padding: 12px 0px; font-weight: bold;')  
        self.btn_start.setFixedHeight(45)
        self.btn_start.setFixedWidth(300) 
        self.btn_start.clicked.connect(self.open_show_menu)
        vbox.addWidget(self.btn_start, alignment=Qt.AlignCenter)

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