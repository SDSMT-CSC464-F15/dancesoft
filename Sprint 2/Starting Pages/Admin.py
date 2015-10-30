import sys
from PyQt4 import QtGui
from Admin_Landing import Ui_Admin_Landing

class Admin_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        

