import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Admin_Landing import Ui_Admin_Landing
from functools import partial
from PyQt4.QtSql import *
from Search_teacher_window import Search_teacher_window
from Select_teacher_dialog import  modify_Information
from Assign_class import assign_teacher
from Add_new_teacher import add_teacher

class Admin_window(QtGui.QMainWindow):
    def __init__(self, name):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        self.current_index = 0
        self.prev_index = 0

        self.ui.name = name
        self.ui.Employee_btn.clicked.connect(partial(self.change_window, index = 1))
        self.ui.Class_btn.clicked.connect(partial(self.change_window, index = 2))
        self.ui.Student_btn.clicked.connect(partial(self.change_window, index = 3))
        self.ui.Billing_btn.clicked.connect(partial(self.change_window, index = 4))
        
        self.ui.Employee_back_btn.clicked.connect(self.Back_btn)
        self.ui.Class_back_btn.clicked.connect(self.Back_btn)
        self.ui.Student_back_btn.clicked.connect(self.Back_btn)
        self.ui.Payroll_back_btn.clicked.connect(self.Back_btn)



        self.ui.Search_teacher_btn.clicked.connect(self.search_teacher)
        self.ui.Update_teacher_btn.clicked.connect(self.update_teacher)
        self.ui.Assign_teacher_btn.clicked.connect(self.assign_teacher)
        self.ui.New_teacher_btn.clicked.connect(self.add_teacher)

        self.ui.Quit_btn.clicked.connect(self.Quit)
        self.ui.Quit_btn_2.clicked.connect(self.Quit)
        self.ui.Quit_btn_3.clicked.connect(self.Quit)
        self.ui.Quit_btn_4.clicked.connect(self.Quit)
        self.ui.Quit_btn_5.clicked.connect(self.Quit)

    def add_teacher(self):
        self.ui.add_teacher = add_teacher()
        self.ui.add_teacher.show()
        
    def assign_teacher(self):
        self.ui.assign_teacher = assign_teacher()
        self.ui.assign_teacher.show()

    def update_teacher(self):
        self.ui.update_teacher = modify_Information()
        self.ui.update_teacher.show()
        
    def search_teacher(self):
        self.ui.search_teacher_w = Search_teacher_window()
        self.ui.search_teacher_w.show()
        
    def change_window(self, index):
        self.prev_index = self.current_index
        self.ui.stackedWidget.setCurrentIndex(index)
        self.current_index = index   
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
        

    def Back_btn(self):
        self.current_index = self.prev_index
        self.ui.stackedWidget.setCurrentIndex(self.current_index)
        
    def Quit(self):
        sys.exit()
        
        
        

