import sys
from PyQt4 import QtGui
from Navi import Ui_Navi
from PyQt4.QtSql import *
from functools import partial

class Navi_dialog(QtGui.QDialog):
    def __init__(self, permit = None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Navi()
        self.ui.setupUi(self)
        self.ui.permission = permit
        self.ui.Admin_btn.clicked.connect(partial(self.is_valid, index = 0))
        self.ui.Teacher_btn.clicked.connect(partial(self.is_valid, index = 1))

    def is_valid(self, index):
        if index == 0:
            if self.ui.permission == 1:
                self.done(1)
            else:
                QtGui.QMessageBox.warning(
                self, 'Error', 'Access Denied!')
        elif index == 1:
            self.done(2)


