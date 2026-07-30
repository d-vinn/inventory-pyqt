from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG

class add_dialog(QDialog):
    def __init__(self, parent=None):
          super().__init__(parent)
          self.setWindowTitle("메뉴 추가")
          self.db = DB(**DB_CONFIG)

          self.input_name = QLineEdit()
          self.input_price = QLineEdit()
          self.input_count = QLineEdit()

          form = QFormLayout()
          form.addRow("메뉴명", self.input_name)
          form.addRow("가격", self.input_price)
          form.addRow("수량", self.input_count)

          self.btn_done = QPushButton("추가 완료")
          self.btn_done.clicked.connect(self.add_product)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addWidget(self.btn_done)
          self.setLayout(layout)

    def add_product(self):
        name = self.input_name.text().strip()
        price = self.input_price.text().strip()
        count = self.input_count.text().strip()

        if not name or not price or not count:
            QMessageBox.warning(self, "오류", "전체 내용을 입력해주세요.")
            return
        
        ok = self.db.insert_product(name, price, count)

        if ok:
            QMessageBox.information(self, "완료", "추가되었습니다.")
            self.input_name.clear()
            self.input_price.clear()
            self.input_count.clear()
            self.close()
        else:
            QMessageBox.critical(self, "실패", "추가 중 오류가 발생하였습니다.")
