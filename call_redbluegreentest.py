# -*- conding:utf-8 -*-
#
#

__author__ = "addyxiao"


import sys
from redbluegreen import Ui_Form
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
