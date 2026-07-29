#데이터 목록 보여줌, 옆에 수량 표시 기능 있음, 
# 상단에 추가/삭제/수정(재고나 상품명 변경) 버튼 있음

from PyQt5.QtWidgets import QSpinBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
from show_order import ShowOrder

class ShowMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문")
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        bigvbox = QVBoxLayout(central)
        hbox = QHBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["메뉴명", "가격", "잔여 수량"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)
        
        hbox.addWidget(self.table)

        ordervbox = QVBoxLayout()
        name_col = self.db.watch_names()
        spinboxlist = []
        for i in range(len(name_col)):
            a = QHBoxLayout()
            a.addWidget(QLabel(str(name_col[i])[2:-3]))
            spinboxlist.append(QSpinBox())
            a.addWidget(spinboxlist[i])
            ordervbox.addLayout(a)

        hbox.addLayout(ordervbox)

        bigvbox.addLayout(hbox)
        self.btn_order = QPushButton("주문 완료")
        self.btn_order.clicked.connect(self.show_order)
        bigvbox.addWidget(self.btn_order)


        self.load_product()

        self.valuelist = []
        for j in spinboxlist:
            self.valuelist.append(j.value())

    def returnval(self):
        return self.valuelist

    def show_order(self):
        self.orderwin = ShowOrder(self.valuelist)
        self.orderwin.show()

    def load_product(self):
        rows = self.db.watch_products()
        self.table.setRowCount(len(rows))
        for r, (name, price, count) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(price))
            self.table.setItem(r, 2, QTableWidgetItem(str(count)))
        self.table.resizeColumnsToContents()



        
