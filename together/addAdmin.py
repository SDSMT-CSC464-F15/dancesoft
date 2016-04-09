import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from addAdminDialog import Ui_addAdminDialog

class addAdmin(QtGui.QDialog):    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.admin = Ui_addAdminDialog()
        self.admin.setupUi(self)

        self.idList = []
        
        self.teach_query = QSqlQuery()
        self.teach_query.exec_("Select Teacher_name, Teacher_id FROM Teacher")
        while self.teach_query.next():
            record = self.teach_query.record()
            self.name = str(record.value(0))
            self.id = str(record.value(1))
            self.idList.append(self.id)
            self.admin.teacherComboBox.addItem(self.name)
            
        self.admin.ok_btn.clicked.connect(self.submit)

        self.admin.cancel_btn.clicked.connect(self.close)

    def submit(self):
        self.selected = self.admin.teacherComboBox.currentIndex()
        self.selected = self.idList[self.selected]
        self.name = self.admin.teacherComboBox.currentText()

        self.check_query = QSqlQuery()
        self.check_query.exec_("Select Admin_name From Admin")
        while self.check_query.next():
            self.record = self.check_query.record()
            if self.name == str(self.record.value(0)):
                self.message = "%s is already an admin" % self.name
                self.confirmReply = QtGui.QMessageBox.information(self, 'Error', 
                    self.message)
                return

        self.confirmMessage = "Are you sure you want to make '%s' an admin" \
                                 %(self.name)
        self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if (self.confirmReply == QtGui.QMessageBox.Yes):
            self.id_query =QSqlQuery()
            self.id_query.exec_("SELECT Admin_id FROM Admin ORDER BY Admin_id DESC LIMIT 1")
            while self.id_query.next():
                self.record = self.id_query.record()
                self.Admin_id = self.record.value(0)
                self.Admin_id += 1

            
            self.confirm_query = QSqlQuery()
            self.confirm_query.exec_("SELECT * From Teacher Where Teacher_id = %d" % (int(self.selected)) )
            if self.confirm_query.next():
                self.record = self.confirm_query.record()
                self.name = str(self.record.value(1))
                self.home = str(self.record.value(2))
                self.cell = str(self.record.value(3))
                self.work = str(self.record.value(4))
                self.address_id = str(self.record.value(5))
                self.email = str(self.record.value(6))
                self.gender = str(self.record.value(7))
                self.number = str(self.record.value(8))
                self.pay = str(self.record.value(9))
                self.medical = str(self.record.value(10))
                self.DOB = str(self.record.value(11))

            self.confirm_query.exec_("Insert into Admin (Admin_id,Admin_name,\
                    Admin_home_phone, Admin_cell_phone, Admin_work_phone,\
                    Admin_address, Admin_email, Admin_sex, Admin_SSN, \
                    Admin_pay_rate, Admin_medical_information, Admin_date_of_birth)\
                    values(%d,'%s', '%s', '%s','%s',%d,'%s','%s', '%s', '%s', '%s','%s')"
                    %(int(self.Admin_id), self.name, self.home, self.cell, self.work,\
                      int(self.address_id), self.email, self.gender, self.number, self.pay,\
                      self.medical, self.DOB))

            self.confirm_query.exec_("Update Account SET Admin_id = %d Where Teacher_id = %d" % (int(self.Admin_id), int(self.selected)) )
            self.close()
        
