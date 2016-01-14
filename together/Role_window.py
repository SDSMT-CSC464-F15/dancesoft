import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from Role import Ui_Role_window
from Role_print import Print_window


class Role_window(QtGui.QMainWindow):
    def __init__(self, name):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Role_window()
        self.ui.setupUi(self)
        self.conn() #need cathch exeption
        Class_query = QSqlQuery()
        Class_query.exec_("Select Class_name from Class as C, Teacher_Class as\
                           TC, Teacher as T where T.Teacher_id = TC.Teacher_id and \
                           T.Teacher_id = (select Teacher_id from Account where User_name = \
                           '%s') and TC.Class_id = C.Class_id" % name)

        
        model = QSqlQueryModel()
        model.setQuery(Class_query)
        self.ui.Role_listView.setModel(model)
        self.ui.Role_listView.clicked.connect(self.show_class) 
        self.ui.Role_print_btn.clicked.connect(self.print_student)
        self.ui.Role_print_btn.setEnabled(False)

    def print_student(self):
        self.ui.print = Print_window(self.ui.Student_info)
        self.ui.print.show()

    def show_class(self, index):
        self.ui.Student_info = []
        self.ui.Role_print_btn.setEnabled(True)
        Student_query = QSqlQuery()
        Student_query.exec_("Select S.Student_name, S.Student_id, S.Student_home_phone, S.Student_Emergency_contact, S.Emergency_contact_phone from Student_Class as SC,Student as S where\
                            SC.Class_id = (Select Class_id from Class where Class_name = '%s') \
                            and SC.Student_id = S.Student_id and SC.Class_finished <> 1 and \
                            SC.Class_approval <> -1" % index.data())
        while Student_query.next():
            self.ui.Student_info.append(str(Student_query.value(1)) + ',' + str(Student_query.value(0)) + ',' + str(Student_query.value(2)) +',' + str(Student_query.value(3)) +',' + str(Student_query.value(4)))
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Stu_listView.setModel(model)
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
        

