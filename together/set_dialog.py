import sys
from PyQt4 import QtGui
from set import Ui_Semester_set_Dialog
from PyQt4.QtSql import *

class semester_set_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Semester_set_Dialog()
        self.ui.setupUi(self)
        self.conn()

        semester_query = QSqlQuery()
        semester_query.exec_("Select Term from System")
        while semester_query.next():
            self.ui.Semester_comboBox.addItem(semester_query.value(0).replace('_', ' Term'))

        self.ui.Set_btn.clicked.connect(self.set)

    def set(self):
        semester_query = QSqlQuery()
        if semester_query.exec_("Update System set Current_term = '%s' where System_id = 1" % \
                             self.ui.Semester_comboBox.currentText().replace(' Term', '_')):
            QtGui.QMessageBox.information(self, 'success', 'Success!')
        else:
            QtGui.QMessageBox.information(self, 'fail', 'Fail!')
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

