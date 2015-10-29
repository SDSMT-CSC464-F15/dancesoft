import sys
from PyQt4 import QtGui
from Teacher_Landing import Ui_Teacher_Landing

class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_Landing()
        self.ui.setupUi(self)
        
import sys
app = QtGui.QApplication(sys.argv)
test = Window()
test.show()
sys.exit(app.exec_())
