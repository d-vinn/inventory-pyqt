from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG

class del_dialog(QDialog):
    def __init__(self, parent=None):
          super().__init__(parent)
          self.setWindowTitle("메뉴 삭제")
          self.db = DB(**DB_CONFIG)

          self.input_name = QLineEdit()

          form = QFormLayout()
          form.addRow("메뉴명", self.input_name)

          self.btn_done = QPushButton("삭제 완료")
          self.btn_done.clicked.connect(self.del_product)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addWidget(self.btn_done)
          self.setLayout(layout)

    def del_product(self):
            name = self.input_name.text().strip()
    
            if not name:
                QMessageBox.warning(self, "오류", "메뉴명을 입력해주세요.")
                return
            
            ok = self.db.delete_product(name)
    
            if ok:
                QMessageBox.information(self, "완료", "삭제되었습니다.")
                self.input_name.clear()
                self.close()
            else:
                QMessageBox.critical(self, "실패", "삭제 중 오류가 발생하였습니다.")
