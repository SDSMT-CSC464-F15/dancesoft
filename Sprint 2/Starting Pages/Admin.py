;import sys
from PyQt4 import QtGui
from Admin_Landing import Ui_Admin_Landing

class Admin_Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        
import sys
app = QtGui.QApplication(sys.argv)
Current_Window = Admin_Window()
Current_Window.show()
sys.exit(app.exec_())
