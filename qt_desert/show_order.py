#데이터 목록 보여줌, 옆에 수량 표시 기능 있음, 
# 상단에 추가/삭제/수정(재고나 상품명 변경) 버튼 있음

from PyQt5.QtWidgets import QSpinBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
#from show_end import ShowEnd

class ShowOrder(QMainWindow):
    def __init__(self, list):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문 확인")
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        bigvbox = QVBoxLayout(central)

        name_col = self.db.watch_names()

        for i in range(len(name_col)):
            #if list[i]>0:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(str(name_col[i])[2:-3]))
            hbox.addWidget(QLabel(str(list[i])))
            bigvbox.addLayout(hbox)

        bigvbox.addWidget(QLabel("주문 내역을 확인해주세요."))
        
        self.btn_order = QPushButton("주문이 맞게 들어갔습니다.")
        #self.btn_order.clicked.connect(self.show_end)
        bigvbox.addWidget(self.btn_order)

    '''def show_end(self):
        self.orderwin = ShowEnd()
        self.orderwin.show()'''



        
