import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from Addstu import Ui_Addstu_window
from Addstu_detail_dialog import Addstu_detail_dialog

class Addstu_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Addstu_window()
        self.ui.setupUi(self)
        self.conn() #need cathch exeption
        Addstu_query = QSqlQuery()

        Addstu_query.exec_("Select Class_name from Class")
        model = QSqlQueryModel()
        model.setQuery(Addstu_query)
        self.ui.Class_listView.setModel(model)
        self.ui.Class_listView.clicked.connect(self.show_student)
        self.ui.Stu_listView.clicked.connect(self.select_student)
        self.ui.Remove_stu_btn.clicked.connect(self.remove_student)
        self.ui.Add_stu_btn.clicked.connect(self.add_student)
        
        self.ui.Remove_stu_btn.setEnabled(False)
        self.ui.Add_stu_btn.setEnabled(False)


    def add_student(self):
        self.ui.detail = Addstu_detail_dialog(self.class_name)
        self.ui.detail.show()

    def remove_student(self):
        Remove_query = QSqlQuery()
     
        if Remove_query.exec_("Update Student_Class Set Class_approval = -1 Where\
                            Student_id = (Select Student_id from Student Where Student_name = \
                            '%s') and Class_id = (Select Class_id from Class where \
                            Class_name = '%s')" % (self.stu_name, self.class_name)):
            QtGui.QMessageBox.information(
                self, 'Success', 'Remove student from class successfully')
     
    def select_student(self, index):
        self.ui.Remove_stu_btn.setEnabled(True)
        self.stu_name = index.data()
        
    def show_student(self, index):
        self.ui.Remove_stu_btn.setEnabled(False)
        self.ui.Add_stu_btn.setEnabled(True)
        Student_query = QSqlQuery()
        Student_query.exec_("Select S.Student_name from Student_Class as SC,Student as S where\
                            SC.Class_id = (Select Class_id from Class where Class_name = '%s') \
                            and SC.Student_id = S.Student_id and SC.Class_finished <> 1 and \
                            SC.Class_approval <> -1" % index.data())
        self.class_name = index.data()
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

app = QtGui.QApplication(sys.argv)
window = Addstu_window()
window.show()
sys.exit(app.exec_())

