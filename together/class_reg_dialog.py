import sys
from PyQt4 import QtGui
from class_reg import Ui_class_search
from PyQt4.QtSql import *
from functools import partial

class class_reg_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_class_search()
        self.ui.setupUi(self)
        self.conn()
        Class_query = QSqlQuery()
        Class_query.exec_("select Class_name from Class")
        model = QSqlQueryModel()
        model.setQuery(Class_query)
        self.ui.class_listView.setModel(model)
        self.ui.class_listView.clicked.connect(self.show_student)
        self.ui.student_listView.clicked.connect(self.select_student)
        self.ui.approve_btn.setEnabled(False)
        self.ui.reject_btn.setEnabled(False)
        self.ui.approve_btn.clicked.connect(partial(self.update_satus, index = 1))
        self.ui.reject_btn.clicked.connect(partial(self.update_satus, index = -1))
        
    def update_satus(self, index):
        update_query = QSqlQuery()
        message = ''
        if index == 1:
            message = 'approve'
        else:
            message = 'reject'
        if update_query.exec("Update Student_Class Set Class_approval = %d Where\
                            Student_id = (Select Student_id from Student Where Student_name = \
                            '%s') and Class_id = (Select Class_id from Class where \
                            Class_name = '%s')" % (index, self.stu_name, self.class_name)):
            QtGui.QMessageBox.information(
                self, 'Success', '%s student successfully' % message)
        print (self.selected_row)
        self.ui.student_listView.setRowHidden(self.selected_row, True)

    def show_student(self, index):
        self.ui.approve_btn.setEnabled(False)
        self.ui.reject_btn.setEnabled(False)
        
        Student_query = QSqlQuery()
        Student_query.exec_("Select S.Student_name from Student_Class as SC,Student as S where\
                            SC.Class_id = (Select Class_id from Class where Class_name = '%s') \
                            and SC.Student_id = S.Student_id and SC.Class_finished <> 1 and \
                            SC.Class_approval = 0" % index.data())
        
        self.class_name = index.data()
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.student_listView.setModel(model)
        
    def select_student(self, index):
        self.ui.approve_btn.setEnabled(True)
        self.ui.reject_btn.setEnabled(True)
        self.stu_name = index.data()
        self.selected_row = index.row()

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()


