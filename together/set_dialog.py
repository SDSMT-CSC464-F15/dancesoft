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
        self.list = []

        semester_query = QSqlQuery()
        semester_query.exec_("Select Term from System")
        
        while semester_query.next():
            temp = semester_query.value(0).replace('_', ' Term')
            self.list.append(temp)
            self.ui.Semester_comboBox.addItem(temp)
        
        semester_query.exec_("Select Current_term from System where System_id = 1")
        semester_query.next()
        index = self.ui.Semester_comboBox.findText(semester_query.value(0).replace('_', ' Term'))

        self.ui.Semester_comboBox.setCurrentIndex(index)
        self.ui.Year_spinBox.setMaximum(3000)
        self.ui.Year_spinBox.setMinimum(1970)
        self.ui.Year_spinBox.setValue(int(semester_query.value(0)[0:4]))
        self.ui.Set_btn.clicked.connect(self.set)
        self.ui.Add_btn.clicked.connect(self.add)
        
    def add(self):
        year = self.ui.Year_spinBox.value()
        term = self.ui.Term_comboBox.currentText()
        new = str(year) + ' ' + term
        if new in self.list:
            QtGui.QMessageBox.warning(self, 'error', 'semester already existed!')
        else:
            self.list.append(new)
            self.ui.Semester_comboBox.addItem(new)
            semester_query = QSqlQuery()
            semester_query.exec_("Select System_id from System order by System_id desc")
            semester_query.next()
            s_id = semester_query.value(0)+1
            if semester_query.exec_("insert into System \
            (System_id, Term) values (%d, '%s')" % \
            (s_id, new.replace(' Term', '_'))):
                QtGui.QMessageBox.information(self, 'success', 'add semester success!')
            else:
                QtGui.QMessageBox.warning(self, 'error', 'add semester failed!')

        
    def set(self):
        semester_query = QSqlQuery()
        if semester_query.exec_("Update System set Current_term = '%s' where System_id = 1" % \
                             self.ui.Semester_comboBox.currentText().replace(' Term', '_')):
            QtGui.QMessageBox.information(self, 'success', 'Success!')
        else:
            QtGui.QMessageBox.warning(self, 'fail', 'Fail!')
            
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

