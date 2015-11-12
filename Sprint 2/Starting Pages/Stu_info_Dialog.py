import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_info import Ui_stu_info_dialog
from PyQt4.QtSql import *
from functools import partial


class Stu_info_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_stu_info_dialog()
        self.ui.setupUi(self)


