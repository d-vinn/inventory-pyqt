from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtGui import QIcon

class modcount_dialog(QDialog):
    def __init__(self, parent=None):
          super().__init__(parent)
          self.setWindowTitle("수량 수정")
          self.setWindowIcon(QIcon("C:/pyqt_prac/qt_desert/setting.png"))
          self.setStyleSheet('background-color:white;')
          self.db = DB(**DB_CONFIG)

          self.input_name = QLineEdit()
          self.input_count = QLineEdit()

          form = QFormLayout()
          form.addRow("메뉴명", self.input_name)
          form.addRow("새로운 수량", self.input_count)

          self.btn_done = QPushButton("수정 완료")
          self.btn_done.setStyleSheet('background:black;color:white')
          self.btn_done.clicked.connect(self.mod_product)

          layout = QVBoxLayout()
          layout.addLayout(form)
          layout.addWidget(self.btn_done)
          self.setLayout(layout)

    def mod_product(self):
            name = self.input_name.text().strip()
            new_count = self.input_count.text().strip()
    
            if not name or not new_count:
                QMessageBox.warning(self, "오류", "전체 내용을 입력해주세요.")
                return
            
            ok = self.db.update_count(name, new_count)
    
            if ok:
                QMessageBox.information(self, "완료", "변경되었습니다.")
                self.input_name.clear()
                self.input_count.clear()
                self.close()
            else:
                QMessageBox.critical(self, "실패", "변경 중 오류가 발생하였습니다.")
