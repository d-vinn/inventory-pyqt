from PyQt5.QtWidgets import QSpinBox, QTableWidgetItem, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QVBoxLayout
from db_helper import DB, DB_CONFIG
import time, sys
from PyQt5.QtCore import Qt

class ShowEnd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT Dessert 주문 완료")
        self.db = DB(**DB_CONFIG)

        label1 = QLabel('주문이 완료되었습니다. 감사합니다.', self)
        label1.setAlignment(Qt.AlignCenter)


        
