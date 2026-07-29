#데이터 목록 보여줌, 옆에 수량 표시 기능 있음, 
# 상단에 추가/삭제/수정(재고나 상품명 변경) 버튼 있음

from PyQt5.QtWidgets import QSpinBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG

class ShowEnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문 확인")
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        bigvbox = QVBoxLayout(central)

        self.btn_order = QPushButton("주문이 맞게 들어갔습니다.")
        self.btn_order.clicked.connect(self.dd)
        bigvbox.addWidget(self.btn_order)


    def show_order(self):
        self.orderwin = ShowEnd()
        self.orderwin.show()

        
