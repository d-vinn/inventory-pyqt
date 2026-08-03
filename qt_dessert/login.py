from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from db_helper import DB, DB_CONFIG
from PyQt5.QtGui import QIcon

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("qt_dessert/setting.png"))
        self.setWindowTitle("LOGIN")
        self.setStyleSheet('background-color:white;')
        self.db = DB(**DB_CONFIG)

        self.username = QLineEdit()
        self.username.setFixedHeight(20)
        self.username.setFixedWidth(100)
        self.username.setPlaceholderText("input id")
        self.password = QLineEdit()
        self.password.setFixedWidth(100)
        self.password.setFixedHeight(20)
        self.password.setPlaceholderText("input password")
        self.password.setEchoMode(QLineEdit.Password)

        form = QFormLayout()
        form.addRow("ID", self.username)
        form.addRow("PW", self.password)

        self.btn_login = QPushButton("log in")
        self.btn_login.setStyleSheet('color:white; background:black')
        self.btn_login.clicked.connect(self.try_login)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.btn_login)
        self.setLayout(layout)

    def try_login(self):
        uid = self.username.text().strip()
        pw = self.password.text().strip()
        if not uid or not pw:
            QMessageBox.warning(self, "오류", "아이디와 비밀번호를 모두 입력하세요.")
            return

        ok = self.db.verify_user(uid, pw)
        if ok:
            self.accept()
        else:
            QMessageBox.critical(self, "실패", "아이디 또는 비밀번호가 올바르지 않습니다.")