import sys
from PyQt4 import QtGui
from Teacher_Landing import Ui_Teacher_Landing

class Teacher_window(QtGui.QMainWindow):
    def __init__(self):
        print "isthis"
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_Landing()
        self.ui.setupUi(self)
        

