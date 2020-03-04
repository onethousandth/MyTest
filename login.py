import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QApplication


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        userLabel = QLabel("user:")
        userLabel.setFixedWidth(50)
        passWordLabel =QLabel("password:")
        passWordLabel.setFixedWidth(50)

        self.userLineEdit = QLineEdit()
        self.passWordLineEdit = QLineEdit()
        self.passWordLineEdit.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton("登录：")

        hboxLayout_1 = QHBoxLayout()
        hboxLayout_1.addWidget(userLabel)
        hboxLayout_1.addWidget(self.userLineEdit)
        hboxLayout_2 = QHBoxLayout()
        hboxLayout_2.addWidget(passWordLabel)
        hboxLayout_2.addWidget(self.passWordLineEdit)

        mainLayout = QVBoxLayout(self)
        mainLayout.addLayout(hboxLayout_1)
        mainLayout.addLayout(hboxLayout_2)
        mainLayout.addWidget(loginBtn)

        self.setWindowTitle("登录界面")
        self.show()

        loginBtn.clicked.connect(self.loginSlot)

    def loginSlot(self):
        user = self.userLineEdit.text()
        print(user)
        psw = self.passWordLineEdit.text()
        print(psw)

        if user == "admin" and psw == "root":
            print("登录")
        else:
            print("用户名或密码错误")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWidget()

    sys.exit(app.exec_())
