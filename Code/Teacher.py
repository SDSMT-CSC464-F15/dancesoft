import sys
from PyQt4 import QtGui
from Teacher_Landing import Ui_Teacher_Landing
from functools import partial

class Teacher_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_Landing()
        self.ui.setupUi(self)

        self.ui.Quit_btn.clicked.connect(self.close)
        self.ui.Student_btn.clicked.connect(partial(self.change_window, index = 1))
        self.ui.Class_btn.clicked.connect(partial(self.change_window, index = 2))
        self.ui.Personal_btn.clicked.connect(partial(self.change_window, index = 3))
        self.ui.Student_back_btn.clicked.connect(partial(self.change_window, index = 0))
        self.ui.Class_back_btn.clicked.connect(partial(self.change_window, index = 0))
        self.ui.Personal_back_btn.clicked.connect(partial(self.change_window, index = 0))
        
        self.ui.Student_quit_btn.clicked.connect(self.close)
        self.ui.Class_quit_btn.clicked.connect(self.close)
        self.ui.Personal_quit_btn.clicked.connect(self.close)
        
    def change_window(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        
        
app = QtGui.QApplication(sys.argv)
window = Teacher_window()
window.show()
sys.exit(app.exec_())
