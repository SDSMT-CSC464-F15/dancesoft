import sys
from PyQt4 import QtGui
from partial_pay import Ui_Partial_pay
from PyQt4.QtSql import *

class partial_pay_dialog(QtGui.QDialog):
    def __init__(self, student_list):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Partial_pay()
        self.ui.setupUi(self)
        self.ui.list = student_list
        semester_query = QSqlQuery()
        semester_query.exec_("Select Term from System") 
        while semester_query.next():
            self.ui.Semester_comboBox.addItem(semester_query.value(0).replace('_', ' Term'))

        self.ui.Type_comboBox.addItem("default")
        self.ui.Type_comboBox.addItem("cash")
        self.ui.Type_comboBox.addItem("check")
        self.ui.Type_comboBox.addItem("other")
        self.ui.Confirm_btn.clicked.connect(self.pay)
        self.ui.Cancel_btn.clicked.connect(self.close)
        
    def pay(self):
        if self.ui.Amount_lineEdit.text() == '':
            QtGui.QMessageBox.information(
                self, 'fail', 'Please enter a number!')
        else:
            pay = QSqlQuery()
            for i in self.ui.list:
                 pay.exec_("INSERT INTO Payment VALUES \
                 (NULL, '%s', %d, '%s', NOW(), '%s')" % ( i, int(self.ui.Amount_lineEdit.text()),\
                  self.ui.Semester_comboBox.currentText().replace(' Term', '_'), self.ui.Type_comboBox.currentText()))
            QtGui.QMessageBox.information(
                self, 'success', 'Success!')
            self.close()
        
