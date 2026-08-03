'''from PyQt5.QtWidgets import QSpinBox, QMessageBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
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



        
'''
from PyQt5.QtWidgets import QSpinBox, QMessageBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QHeaderView  #ch (QHeaderView 추가)
from PyQt5.QtCore import Qt  #ch
from db_helper import DB, DB_CONFIG
from show_order import ShowOrder
from PyQt5.QtGui import QIcon

class ShowMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문")
        self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/roll-cake.png"))
        self.setStyleSheet('background-color:black;color:white')
        
        self.setFixedSize(300, 500) 

        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        
        bigvbox = QVBoxLayout(central)
        bigvbox.setContentsMargins(15, 15, 15, 15)

        self.name_col = self.db.watch_names()
        
        self.order_widgets = {}

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["메뉴명", "가격", "잔여 수량"])
        self.table.setEditTriggers(self.table.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet('color:black;background-color:white')
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.table.cellClicked.connect(self.on_table_cell_clicked)

        bigvbox.addWidget(self.table)  

        self.ordervbox = QVBoxLayout()
        bigvbox.addStretch(1) 
        bigvbox.addLayout(self.ordervbox)

        self.btn_order = QPushButton("주문 완료")
        self.btn_order.setStyleSheet('''
            QPushButton {
                color: black;
                background-color: white;
                border-radius: 12px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        ''') 
        self.btn_order.clicked.connect(self.check_val)
        bigvbox.addWidget(self.btn_order)

        self.load_product()

    def on_table_cell_clicked(self, row, column):
        menu_name = self.table.item(row, 0).text() 
        
        if row in self.order_widgets:
            spinbox = self.order_widgets[row]['spinbox']
            spinbox.setValue(spinbox.value() + 1)
        else:
            a = QHBoxLayout()
            label = QLabel(menu_name)
            label.setStyleSheet('color:white; font-size:14px;')
            
            spinbox = QSpinBox()
            spinbox.setStyleSheet('color:black; background-color:white;')
            spinbox.setMinimum(0)
            spinbox.setValue(1) 
            
            a.addWidget(label)
            a.addWidget(spinbox)
            
            self.ordervbox.addLayout(a)
            
            self.order_widgets[row] = {
                'layout': a,
                'label': label,
                'spinbox': spinbox
            }
            
            spinbox.valueChanged.connect(lambda val, r=row: self.on_spinbox_changed(r, val)) 

    def on_spinbox_changed(self, row, value):
        if value == 0:
            if row in self.order_widgets:
                target = self.order_widgets.pop(row)
                target['label'].deleteLater()
                target['spinbox'].deleteLater()
                target['layout'].deleteLater()

    def check_val(self):
        self.valuelist = [0] * len(self.name_col) 
        
        for row, widgets in self.order_widgets.items():
            self.valuelist[row] = widgets['spinbox'].value()
            
        self.check_count()

    def check_count(self):
        counts = self.db.watch_counts()
        for i in range(len(counts)):
            if self.valuelist[i] > int(str(counts[i])[1:-2]):
                message_box = QMessageBox()
                message_box.setWindowTitle("Information")
                menu_name = self.table.item(i, 0).text() 
                message_box.setText(f"'{menu_name}' 수량이 초과되었습니다.")
                message_box.setIcon(QMessageBox.Icon.Information)
                message_box.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/warning.png"))
                message_box.exec()
                return
        if sum(self.valuelist) == 0:
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
            self.table.setItem(r, 1, QTableWidgetItem(str(price))) 
            self.table.setItem(r, 2, QTableWidgetItem(str(count)))