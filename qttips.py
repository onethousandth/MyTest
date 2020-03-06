# -*- coding-utf-8 -*-
#
#

__author__ = "addyxiao"
__author_email__ = "addyxiao@msn.cn"

"""
PyQt5 Tips Test
a window and a button tips

author: AddyXiao
email:addyxiao@msn.cn
last edited: 2020-3-4

"""
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
import sys


class example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")

        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Tooltips")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())
