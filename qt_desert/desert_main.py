from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from settings import Set
from show_menu import ShowMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert")

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        self.btn_set = QPushButton("설정")
        self.btn_set.clicked.connect(self.open_settings) #요기 이 페이지 연결법 찾아보기
        self.btn_start = QPushButton("주문 시작하기")
        self.btn_start.clicked.connect(self.open_show_menu)

        form_box = QVBoxLayout()
        form_box.addWidget(self.btn_set)
        form_box.addWidget(QLabel("안녕하세요, Qt 디저트 카페입니다."))
        form_box.addWidget(QLabel("주문을 원하시면 주문 시작하기 버튼을 눌러주세요."))
        form_box.addWidget(self.btn_start)

        vbox.addLayout(form_box)

    def open_settings(self):
        self.set_win = Set()
        self.set_win.show()

    def open_show_menu(self):
        self.show_win = ShowMenu()
        self.show_win.show()



        
