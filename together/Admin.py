#admin landing page
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
from billing_history_window import Billing_history_window
from teacher_history_window import Teacher_history_window
from set_dialog import semester_set_dialog
from partial_main_window import Enter_partialpayment_window
from enter_fullpayment_window import Enter_fullpayment_window
from student_owe_window import Student_payment_window
from Credits_Window import credit
from Admin_list_window import Admin_list_window
from enter_hours_window import Enter_hours_window
from teacher_payrate_window import Teacher_payrate_window
from tuition import tuition
from fees import fees
from Student_reg_window import Stu_reg_window
from removeTeacher import removeTeacher
from removeStudentData import removeStudentData
from removeClass import removeClass

class Admin_window(QtGui.QMainWindow):
    def __init__(self, name):
        QtGui.QMainWindow.__init__(self)
        #button for different functionalities
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        self.current_index = 0
        self.prev_index = 0

        #layout of page for scrolling back and forth
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
        self.ui.Remove_teacher_btn.clicked.connect(self.removeTeach)

        self.ui.View_class_btn.clicked.connect(self.view_class)
        self.ui.Add_Class_btn.clicked.connect(self.new_class)
        
        self.ui.Search_student_btn.clicked.connect(self.search_student)
        self.ui.Add_student_btn.clicked.connect(self.add_student)
        self.ui.Billing_history_btn.clicked.connect(self.billing)
        self.ui.Tuition_btn.clicked.connect(self.tuition)
        self.ui.Fee_btn.clicked.connect(self.fee)
        self.ui.Registration_btn.clicked.connect(self.registration)
        self.ui.Remove_student_btn.clicked.connect(self.removeStu)
        self.ui.Remove_class_btn.clicked.connect(self.removeClass)

        
        self.ui.Teaching_his_btn.clicked.connect(self.teaching_his)
        self.ui.Set_Semester_btn.clicked.connect(self.set_semester)
        self.ui.Enter_partial_payment_btn.clicked.connect(self.enter_partial_payment)
        self.ui.Enter_full_payment_btn.clicked.connect(self.enter_full_payment)
        self.ui.Student_balance_btn.clicked.connect(self.student_balance)
        self.ui.Show_admin_list_btn.clicked.connect(self.show_admin_list)
        self.ui.Enter_teacher_hour_btn.clicked.connect(self.enter_teacher_hour)
        self.ui.Enter_teacher_payrate_btn.clicked.connect(self.enter_teacher_payrate)
        self.ui.Registration_btn.clicked.connect(self.registration)
        self.ui.Credits_btn.clicked.connect(self.studentCredit)

        self.ui.Quit_btn.clicked.connect(self.Quit)
        self.ui.Quit_btn_2.clicked.connect(self.Quit)
        self.ui.Quit_btn_3.clicked.connect(self.Quit)
        self.ui.Quit_btn_4.clicked.connect(self.Quit)
        self.ui.Quit_btn_5.clicked.connect(self.Quit)
        self.num = True

    #log out button
    def logout(self):
        self.num = False
        self.close()

    #registration new student 
    def registration(self):
        self.ui.regi = Stu_reg_window()
        self.ui.regi.show()

    #enter teacher pay rate
    def enter_teacher_payrate(self):
        self.ui.enter_teacher_payrate = Teacher_payrate_window()
        self.ui.enter_teacher_payrate.show()

    #enter teacher hours
    def enter_teacher_hour(self):
        self.ui.enter_teacher_hour = Enter_hours_window()
        self.ui.enter_teacher_hour.show()

    #display the list of admin
    def show_admin_list(self):
        self.ui.show_admin_list = Admin_list_window()
        self.ui.show_admin_list.show()
        
    #check student balance
    def student_balance(self):
        self.ui.student_balance = Student_payment_window()
        self.ui.student_balance.show()

    #enter a full payment for the student
    def enter_full_payment(self):
        self.ui.enter_full_payment = Enter_fullpayment_window()
        self.ui.enter_full_payment.show()

    #enter partial payment for student
    def enter_partial_payment(self):
        self.ui.enter_partial_payment = Enter_partialpayment_window()
        self.ui.enter_partial_payment.show()

    #set current semester        
    def set_semester(self):
        self.ui.set_semester = semester_set_dialog()
        self.ui.set_semester.show()

    #display teacher history
    def teaching_his(self):
        self.ui.teaching_his = Teacher_history_window()
        self.ui.teaching_his.show()

    #display billing history
    def billing(self):
        self.ui.billing = Billing_history_window()
        self.ui.billing.show()

    #show fee
    def fee(self):
        self.ui.fee = fees()
        self.ui.fee.show()

    #sho tuition
    def tuition(self):
        self.ui.tuit = tuition()
        self.ui.tuit.show()

    #add new teacher
    def add_teacher(self):
        self.ui.add_teacher = add_teacher()
        self.ui.add_teacher.show()

    #remove teacher
    def removeTeach(self):
        self.ui.remTeach = removeTeacher()
        self.ui.remTeach.show()

    #assign teacher a class
    def assign_teacher(self):
        self.ui.assign_teacher = assign_teacher()
        self.ui.assign_teacher.show()

    #update teacher information
    def update_teacher(self):
        self.ui.update_teacher = modify_Information()
        self.ui.update_teacher.show()

    #search teacher and show their information
    def search_teacher(self):
        self.ui.search_teacher_w = Search_teacher_window()
        self.ui.search_teacher_w.show()

    #search class and show class infromation
    def view_class(self):
        self.ui.see_class = Search_class_window()
        self.ui.see_class.show()

    #add new class
    def new_class(self):
        self.ui.add_class = add_Class()
        self.ui.add_class.show()

    #search student and show student information
    def search_student(self):
        self.ui.search_student_window = Search_window()
        self.ui.search_student_window.show()

    #add new student
    def add_student(self):
        self.ui.place_student = Addstu_window()
        self.ui.place_student.show()

    #register a class
    def register(self):
        self.ui.registration = class_reg_dialog()
        self.ui.registration.show()

    #remove a student
    def removeStu(self):
        self.ui.remStu = removeStudentData()
        self.ui.remStu.show()

    #remove a class
    def removeClass(self):
        self.ui.remClass = removeClass()
        self.ui.remClass.show()

    #show student credit
    def studentCredit(self):
        self.ui.credit = credit()
        self.ui.credit.show()
        
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
        
        
        
        
        
