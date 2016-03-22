import sys
from PyQt4 import QtGui
from Teacher_Landing import Ui_Teacher_Landing
from functools import partial
from Search_window import Search_window
from student_schedule_window import Student_schedule_window
from Addstu_window import Addstu_window
from teacher_schedule_window import Teacher_schedule_window
from Search_class_window import Search_class_window
from Role_window import Role_window
from change_username_window import username_window
from change_password_window import password_window
from My_Information import modify_My_Information


class Teacher_window(QtGui.QMainWindow):
    def __init__(self, name):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_Landing()
        self.ui.setupUi(self)
        self.ui.name = name
        self.ui.Quit_btn.clicked.connect(self.close)
        self.ui.Student_btn.clicked.connect(partial(self.change_window, index = 1))
        self.ui.Class_btn.clicked.connect(partial(self.change_window, index = 2))
        self.ui.Personal_btn.clicked.connect(partial(self.change_window, index = 3))
        self.ui.Student_back_btn.clicked.connect(partial(self.change_window, index = 0))
        self.ui.Class_back_btn.clicked.connect(partial(self.change_window, index = 0))
        self.ui.Personal_back_btn.clicked.connect(partial(self.change_window, index = 0))
        self.ui.Logout_btn.clicked.connect(self.logout)
        
        self.ui.Search_student_btn.clicked.connect(self.search_student)
        self.ui.See_student_schedule_btn.clicked.connect(self.See_student_schedule)
        self.ui.Add_class_btn.clicked.connect(self.Add_student_class)
        self.ui.See_class_schedule_btn.clicked.connect(self.See_teacher_schedule)
        self.ui.See_class_info_btn.clicked.connect(self.search_class)
        self.ui.See_class_role_btn.clicked.connect(self.roll_sheet)
        self.ui.Modify_personal_info.clicked.connect(self.update_teacher)
        self.ui.Reset_password.clicked.connect(self.reset_password)      
        self.ui.Student_quit_btn.clicked.connect(self.close)
        self.ui.Class_quit_btn.clicked.connect(self.close)
        self.ui.Personal_quit_btn.clicked.connect(self.close)
        self.num = True
    def logout(self):
        self.num = False
        self.close()

    def reset_user(self):
        self.ui.reset_user = username_window(self.ui.name)
        if self.ui.reset_user.exec():
            self.ui.name = self.ui.reset_user.getName()
            name = self.ui.name
            

    def reset_password(self):
        self.ui.reset_password = password_window(self.ui.name)
        self.ui.reset_password.show()

    def update_teacher(self):
        self.ui.my_info = modify_My_Information(self.ui.name)
        self.ui.my_info.show()
        
    def roll_sheet(self):
        self.ui.roll_sheet = Role_window(self.ui.name)
        self.ui.roll_sheet.show()

    def search_class(self):
        self.ui.search_class = Search_class_window()
        self.ui.search_class.show()


    def See_teacher_schedule(self):
        self.ui.See_teacher_schedule = Teacher_schedule_window()
        self.ui.See_teacher_schedule.show()

    def Add_student_class(self):
        self.ui.Add_student_class = Addstu_window(self.ui.name)
        self.ui.Add_student_class.show()
        
    def See_student_schedule(self):
        self.ui.See_student_schedule = Student_schedule_window()
        self.ui.See_student_schedule.show()
        
    def search_student(self):
        self.ui.search_student = Search_window()
        self.ui.search_student.show()

        
    def change_window(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        

