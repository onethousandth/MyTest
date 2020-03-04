# -*- coding:utf-8 -*-
#
#

__author__ = "aayxiao"

from LoginTest import Ui_Form
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()

    sys.exit(app.exec_())
