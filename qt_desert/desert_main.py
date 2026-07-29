from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from settings import Set

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
        #self.btn_start.clicked.connect()

        form_box = QVBoxLayout()
        form_box.addWidget(self.btn_set)
        form_box.addWidget(QLabel("이름"))
        form_box.addWidget(self.btn_start)

        vbox.addLayout(form_box)

    def open_settings(self):
        self.set_win = Set()
        self.set_win.show()



        
