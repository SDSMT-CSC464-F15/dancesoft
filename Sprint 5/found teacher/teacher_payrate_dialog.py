import sys
from PyQt4 import QtGui
from teacher_payrate_detial import Ui_teacher_payrate_dialog
from PyQt4.QtSql import *

class Teacher_payrate_dialog(QtGui.QDialog):
    def __init__(self, id):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_teacher_payrate_dialog()
        self.ui.setupUi(self)
        self.id_number = id;

        #store payrate
        self.payrate_dict = {}
        
        self.ui.Add_btn.clicked.connect(self.insert)
        payrate_query = QSqlQuery()
        payrate_query.exec_("select Payname, Payrate from Teacher_Payrate as TP, Payrate as P where \
                             TP.Payrate_id = P.Payrate_id and TP.Teacher_id = %d" % id)
        
        while payrate_query.next():
            self.ui.Payname_comboBox.addItem(payrate_query.value(0))
            self.payrate_dict[payrate_query.value(0)] = float(payrate_query.value(1))

        if self.ui.Payname_comboBox.currentText() != '':
            self.ui.Payrate_update_lineEdit.setText(str(self.payrate_dict[str(self.ui.Payname_comboBox.currentText())]))  
        self.ui.Update_btn.clicked.connect(self.update)
        self.ui.Payname_comboBox.currentIndexChanged.connect(self.update_text)


    def update_text(self):
        if self.ui.Payname_comboBox.currentText() != '':
            self.ui.Payrate_update_lineEdit.setText(str(self.payrate_dict[str(self.ui.Payname_comboBox.currentText())]))  

    def update(self):
        if self.ui.Payname_comboBox.currentText() != '':
            update_query = QSqlQuery()
            if update_query.exec_("update Teacher_Payrate as TP, Payrate as P set P.Payrate = %f where\
                                TP.Teacher_id = %d and TP.Payrate_id = P.Payrate_id and P.Payname = '%s'" % \
                               (float(self.ui.Payrate_update_lineEdit.text()), self.id_number,\
                                self.ui.Payname_comboBox.currentText())):
                
                self.payrate_dict[str(self.ui.Payname_comboBox.currentText())] = float(self.ui.Payrate_update_lineEdit.text())
                QtGui.QMessageBox.information(self, 'success', 'Success!')
            else:
                QtGui.QMessageBox.information(self, 'fail', 'Fail!')
                
    def insert(self):
        payname = self.ui.Payname_lineEdit.text()
        payrate = self.ui.Payrate_lineEdit.text()
        if payname == '':
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please input payname')
            return
        if payrate == '':
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please input payrate')
            return
        
        insert_query = QSqlQuery()
        if insert_query.exec("insert into Payrate (Payname, Payrate)\
                           values ('%s', %f)" % (payname, float(payrate))): 
            insert_query.exec("SELECT LAST_INSERT_ID()")
            insert_query.next()
            payrate_id = insert_query.value(0)
            if insert_query.exec("insert into Teacher_Payrate values ('%s', '%s')" %(self.id_number, payrate_id)):
                QtGui.QMessageBox.information(self, 'success', 'Success!')
            else:
                QtGui.QMessageBox.information(self, 'fail', 'Fail!')
        else:
            QtGui.QMessageBox.information(self, 'fail', 'Fail!')
    

