from PyQt5.QtWidgets import QDialog, QVBoxLayout, QComboBox, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtGui import QIcon

class modcount_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("수량 수정")
        self.setWindowIcon(QIcon("qt_dessert/setting.png"))
        self.setStyleSheet('background-color:white;')
        self.db = DB(**DB_CONFIG)

        self.combo_menu = QComboBox()
        names = [str(n)[2:-3] for n in self.db.watch_names()]
        self.combo_menu.addItem("선택하세요")
        self.combo_menu.addItems(names)
        self.combo_menu.currentTextChanged.connect(self.on_combo_changed)

        self.input_name = ''
        self.input_count = QLineEdit()

        form = QFormLayout()
        form.addRow("메뉴명", self.combo_menu)
        form.addRow("새로운 수량", self.input_count)

        self.btn_done = QPushButton("수정 완료")
        self.btn_done.setStyleSheet('background:black;color:white')
        self.btn_done.clicked.connect(self.mod_product)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_done)
        self.setLayout(layout)

    def on_combo_changed(self, text):
        if text != "선택하세요": 
            self.input_name = text

    def mod_product(self):
        name = self.input_name.strip()
        new_count = self.input_count.text().strip()

        if not name or not new_count:
            QMessageBox.warning(self, "오류", "전체 내용을 입력해주세요.")
            return
        
        ok = self.db.update_count(name, new_count)

        if ok:
            QMessageBox.information(self, "완료", "변경되었습니다.")
            self.input_name = ''
            self.input_count.clear()
            self.close()
        else:
            QMessageBox.critical(self, "실패", "변경 중 오류가 발생하였습니다.")
