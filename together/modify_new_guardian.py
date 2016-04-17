import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtSql import *
from functools import partial
from Modify_guardian import Ui_add_guardian

class add_new_guardian(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_add_guardian()
        self.ui.setupUi(self)

