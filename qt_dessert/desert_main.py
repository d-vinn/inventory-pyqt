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
        self.setWindowIcon(QIcon("qt_desert/coffee-shop.png"))
        self.setStyleSheet('background-color:white;')

        self.setFixedSize(300, 500)  #ch

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)
        vbox.setContentsMargins(20, 20, 20, 40) 

        top_box = QHBoxLayout()
        self.btn_set = QPushButton("설정")
        btn_style = """
            QPushButton {
                border: none;
                background-color: rgb(220,220,220);
                color: white;
                border-radius: 8px;
                padding: 3px 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgb(150, 150, 150);
            }
        """
        self.btn_set.setStyleSheet(btn_style)
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
        explanation.setStyleSheet('color:rgb(150,150,150); font-size: 11px;')  
        explanation.setAlignment(Qt.AlignCenter)
        vbox.addWidget(explanation)  

        vbox.addSpacing(15)  

        self.btn_start = QPushButton("주문 시작하기")
        btn_st = """
            QPushButton {
                border: solid black;
                background-color: black;
                color: white;
                border-radius: 12px;
                padding: 6px 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                color: black;
                background-color: white;
                border: 1px solid black;
            }
        """  
        self.btn_start.setStyleSheet(btn_st)  
        self.btn_start.setFixedHeight(45)
        self.btn_start.setFixedWidth(200) 
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