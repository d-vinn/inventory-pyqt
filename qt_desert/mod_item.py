from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
from mod_name import modname_dialog
from mod_count import modcount_dialog
from mod_price import modprice_dialog

class mod_dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("메뉴 수정")
        self.db = DB(**DB_CONFIG)

        central = QWidget()
        self.setCentralWidget(central)
        vbox = QVBoxLayout(central)

        btn_box = QHBoxLayout()
        self.btn_name = QPushButton("메뉴명 수정")
        self.btn_name.clicked.connect(self.open_mod_name)
        self.btn_price = QPushButton("가격 수정")
        self.btn_price.clicked.connect(self.open_mod_price) 
        self.btn_count = QPushButton("수량 수정")
        self.btn_count.clicked.connect(self.open_mod_count)
        btn_box.addWidget(self.btn_name)
        btn_box.addWidget(self.btn_price)
        btn_box.addWidget(self.btn_count)

        vbox.addLayout(btn_box)

    def open_mod_name(self):
        self.namemod = modname_dialog()
        self.namemod.show()

    def open_mod_price(self):
        self.pricemod = modprice_dialog()
        self.pricemod.show()

    def open_mod_count(self):
        self.countmod = modcount_dialog()
        self.countmod.show()


        
