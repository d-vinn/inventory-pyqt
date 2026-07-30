from PyQt5.QtWidgets import QSpinBox, QMessageBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
from show_order import ShowOrder
from PyQt5.QtGui import QIcon

class ShowMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문")
        self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/roll-cake.png"))
        self.setStyleSheet('background-color:black;color:white')
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
        self.table.setStyleSheet('color:black;background-color:white')

        hbox.addWidget(self.table)

        ordervbox = QVBoxLayout()
        name_col = self.db.watch_names()
        self.spinboxlist = []
        for i in range(len(name_col)):
            a = QHBoxLayout()
            a.addWidget(QLabel(str(name_col[i])[2:-3]))
            self.spinboxlist.append(QSpinBox())
            a.addWidget(self.spinboxlist[i])
            ordervbox.addLayout(a)

        hbox.addLayout(ordervbox)

        bigvbox.addLayout(hbox)
        self.btn_order = QPushButton("주문 완료")
        self.btn_order.setStyleSheet('color:black;background-color:white')
        self.btn_order.clicked.connect(self.check_val)
        bigvbox.addWidget(self.btn_order)


        self.load_product()

    def check_val(self):
        self.valuelist = []
        for j in self.spinboxlist:
            self.valuelist.append(j.value())
        self.check_count()
                

    def check_count(self):
        counts = self.db.watch_counts()
        for i in range(len(counts)):
            if self.valuelist[i]>int(str(counts[i])[1:-2]):
                message_box = QMessageBox()
                message_box.setWindowTitle("Information")
                message_box.setText("수량이 초과되었습니다.")
                message_box.setIcon(QMessageBox.Icon.Information)
                message_box.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/warning.png"))
                message_box.exec()
                return
        if sum(self.valuelist)==0:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Information")
            msgbox.setText("선택한 항목이 없습니다.")
            msgbox.setIcon(QMessageBox.Icon.Information)
            msgbox.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/warning.png"))
            msgbox.exec()
            return
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



        
