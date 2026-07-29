from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG

class modprice_dialog(QDialog):
    def __init__(self, parent=None):
          super().__init__(parent)
          self.setWindowTitle("가격 수정")
          self.db = DB(**DB_CONFIG)

          self.input_name = QLineEdit()
          self.input_price = QLineEdit()

          form = QFormLayout()
          form.addRow("메뉴명", self.input_name)
          form.addRow("새로운 가격", self.input_price)

          self.btn_done = QPushButton("수정 완료")
          self.btn_done.clicked.connect(self.mod_product)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addWidget(self.btn_done)
          self.setLayout(layout)

    def mod_product(self):
            name = self.input_name.text().strip()
            new_price = self.input_price.text().strip()
    
            if not name or not new_price:
                QMessageBox.warning(self, "오류", "전체 내용을 입력해주세요.")
                return
            
            ok = self.db.update_price(name, new_price)
    
            if ok:
                QMessageBox.information(self, "완료", "변경되었습니다.")
                self.input_name.clear()
                self.input_price.clear()
            else:
                QMessageBox.critical(self, "실패", "변경 중 오류가 발생하였습니다.")
