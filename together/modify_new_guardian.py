import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtSql import *
from functools import partial
from Modify_guardian import Ui_add_teacher

class add_new_guardian(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_add_teacher()
        self.ui.setupUi(self)


app = QtGui.QApplication(sys.argv)
window = add_new_guardian()
window.show()
sys.exit(app.exec_())

