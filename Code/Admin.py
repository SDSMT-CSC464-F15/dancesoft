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
from Search_class_window import Search_class_window
from Add_a_Class import add_Class
from Search_window import Search_window
from Addstu_window_admin import Addstu_window
from class_reg_dialog import class_reg_dialog

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
        self.ui.Logout_btn.clicked.connect(self.logout)

        self.ui.Search_teacher_btn.clicked.connect(self.search_teacher)
        self.ui.Update_teacher_btn.clicked.connect(self.update_teacher)
        self.ui.Assign_teacher_btn.clicked.connect(self.assign_teacher)
        self.ui.New_teacher_btn.clicked.connect(self.add_teacher)

        self.ui.View_class_btn.clicked.connect(self.view_class)
        self.ui.Add_Class_btn.clicked.connect(self.new_class)
        self.ui.Class_tuition_btn.clicked.connect(self.class_tuition)
        
        self.ui.Search_student_btn.clicked.connect(self.search_student)
        self.ui.Add_student_btn.clicked.connect(self.add_student)
        self.ui.Registration_btn.clicked.connect(self.register)

        self.ui.Quit_btn.clicked.connect(self.Quit)
        self.ui.Quit_btn_2.clicked.connect(self.Quit)
        self.ui.Quit_btn_3.clicked.connect(self.Quit)
        self.ui.Quit_btn_4.clicked.connect(self.Quit)
        self.ui.Quit_btn_5.clicked.connect(self.Quit)
        self.num = True
    def logout(self):
        self.num = False
        self.close()

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

    def view_class(self):
        self.ui.see_class = Search_class_window()
        self.ui.see_class.show()

    def new_class(self):
        self.ui.add_class = add_Class()
        self.ui.add_class.show()
        
    def class_tuition(self):
        print("In Progress")

    def search_student(self):
        self.ui.search_student_window = Search_window()
        self.ui.search_student_window.show()

    def add_student(self):
        self.ui.place_student = Addstu_window()
        self.ui.place_student.show()

    def register(self):
        self.ui.registration = class_reg_dialog()
        self.ui.registration.show()
        
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
        
        
        
        
        

