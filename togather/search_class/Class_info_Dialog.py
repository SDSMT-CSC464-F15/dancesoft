import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Class_info import Ui_Class_info_dialog
from PyQt4.QtSql import *
from functools import partial


class Class_info_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Class_info_dialog()
        self.ui.setupUi(self)

