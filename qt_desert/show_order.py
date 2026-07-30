from PyQt5.QtWidgets import QSpinBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
from show_end import ShowEnd
from PyQt5.QtGui import QIcon

class ShowOrder(QMainWindow):
    def __init__(self, list):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문 확인")
        self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/roll-cake.png"))
        self.setStyleSheet('background-color:white;')
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        bigvbox = QVBoxLayout(central)

        name_col = self.db.watch_names()
        counts = self.db.watch_counts()
        self.db_update = []

        for i in range(len(name_col)):
            if list[i]>0:
                hbox = QHBoxLayout()
                hbox.addWidget(QLabel(str(name_col[i])[2:-3]))
                hbox.addWidget(QLabel(str(list[i])))
                bigvbox.addLayout(hbox)
                self.db_update.append((name_col[i], int(str(counts[i])[1:-2])-list[i]))

        bigvbox.addWidget(QLabel("주문 내역을 확인해주세요."))
        
        self.btn_order = QPushButton("주문이 맞게 들어갔습니다.")
        self.btn_order.clicked.connect(self.show_end)
        bigvbox.addWidget(self.btn_order)


    def show_end(self):
        for j in self.db_update:
            self.db.update_count(j[0], j[1])
        self.orderwin = ShowEnd()
        self.orderwin.show()



        
