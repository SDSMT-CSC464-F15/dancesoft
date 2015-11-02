import sys
from PyQt4 import QtGui
from Admin_Landing import Ui_Admin_Landing
from functools import partial

class Admin_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        self.current_index = 0
        self.prev_index = 0
        self.ui.Employee_btn.clicked.connect(partial(self.change_window, index = 1))
        self.ui.Class_btn.clicked.connect(partial(self.change_window, index = 2))
        self.ui.Student_btn.clicked.connect(partial(self.change_window, index = 3))
        self.ui.Billing_btn.clicked.connect(partial(self.change_window, index = 4))
        
        self.ui.Employee_back_btn.clicked.connect(self.Back_btn)
        self.ui.Class_back_btn.clicked.connect(self.Back_btn)
        self.ui.Student_back_btn.clicked.connect(self.Back_btn)
        self.ui.Payroll_back_btn.clicked.connect(self.Back_btn)

        self.ui.Quit_btn.clicked.connect(self.Quit)
        self.ui.Quit_btn_2.clicked.connect(self.Quit)
        self.ui.Quit_btn_3.clicked.connect(self.Quit)
        self.ui.Quit_btn_4.clicked.connect(self.Quit)
        self.ui.Quit_btn_5.clicked.connect(self.Quit)
        
        
    def change_window(self, index):
        self.prev_index = self.current_index
        self.ui.stackedWidget.setCurrentIndex(index)
        self.current_index = index

    def Back_btn(self):
        self.current_index = self.prev_index
        self.ui.stackedWidget.setCurrentIndex(self.current_index)
        
    def Quit(self):
        sys.exit()
        
        
        

import sys
app = QtGui.QApplication(sys.argv)
Current_Window = Admin_window()
Current_Window.show()
sys.exit(app.exec_())
