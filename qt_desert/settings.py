#데이터 목록 보여줌, 옆에 수량 표시 기능 있음, 
# 상단에 추가/삭제/수정(재고나 상품명 변경) 버튼 있음

from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
from add_item import add_dialog
from del_item import del_dialog
from mod_item import mod_dialog
from PyQt5.QtGui import QIcon

class Set(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert Settings")
        self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/setting.png"))
        self.setStyleSheet('background-color:black;')
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        btn_box = QHBoxLayout()
        self.btn_add = QPushButton("메뉴 추가")
        self.btn_add.setStyleSheet('border:None;background:white;height:18;width:20px;color:black;')
        self.btn_add.clicked.connect(self.open_add_item)
        self.btn_del = QPushButton("메뉴 삭제")
        self.btn_del.setStyleSheet('border:None;background:white;height:18;width:30px;color:black;')
        self.btn_del.clicked.connect(self.open_del_item) 
        self.btn_mod = QPushButton("수정")
        self.btn_mod.setStyleSheet('border:None;background:white;height:18;width:30px;color:black;')
        self.btn_mod.clicked.connect(self.open_mod_item)
        btn_box.addWidget(self.btn_add)
        btn_box.addWidget(self.btn_del)
        btn_box.addWidget(self.btn_mod)

        self.table = QTableWidget()
        self.table.setStyleSheet('background:white;color:black')
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["메뉴명", "가격", "잔여 수량"])
        self.table.setEditTriggers(self.table.NoEditTriggers)  # 표준 예시: 목록은 읽기 전용
        self.table.verticalHeader().setVisible(False)

        vbox.addLayout(btn_box)
        vbox.addWidget(self.table)

        self.load_product()

    def load_product(self):
        rows = self.db.watch_products()
        self.table.setRowCount(len(rows))
        for r, (name, price, count) in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(name))
            self.table.setItem(r, 1, QTableWidgetItem(price))
            self.table.setItem(r, 2, QTableWidgetItem(str(count)))
        self.table.resizeColumnsToContents()
        self.table.repaint()

    def open_add_item(self):
        self.add_win = add_dialog()
        self.add_win.show()

    def open_del_item(self):
        self.del_win = del_dialog()
        self.del_win.show()

    def open_mod_item(self):
        self.mod_win = mod_dialog()
        self.mod_win.show()


        
