from PyQt5.QtWidgets import QDialog, QComboBox, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtGui import QIcon

class modname_dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("메뉴명 수정")
        self.setWindowIcon(QIcon("qt_dessert/setting.png"))
        self.setStyleSheet('background-color:white;')
        self.db = DB(**DB_CONFIG)

        self.combo_menu = QComboBox()
        names = [str(n)[2:-3] for n in self.db.watch_names()]
        self.combo_menu.addItem("선택하세요")
        self.combo_menu.addItems(names)
        self.combo_menu.currentTextChanged.connect(self.on_combo_changed)

        self.input_name = ''
        self.input_new_name = QLineEdit()

        form = QFormLayout()
        form.addRow("기존 메뉴명", self.combo_menu)
        form.addRow("새로운 메뉴명", self.input_new_name)

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
        new_name = self.input_new_name.text().strip()

        if not name or not new_name:
            QMessageBox.warning(self, "오류", "전체를 입력해주세요.")
            return
        
        ok = self.db.update_name(name, new_name)

        if ok:
            QMessageBox.information(self, "완료", "변경되었습니다.")
            self.input_name = ''
            self.input_new_name.clear()
            self.close()
        else:
            QMessageBox.critical(self, "실패", "변경 중 오류가 발생하였습니다.")
