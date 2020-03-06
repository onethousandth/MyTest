
import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)


class example(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        qbtn = QPushButton("Quit", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Quit Button")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
