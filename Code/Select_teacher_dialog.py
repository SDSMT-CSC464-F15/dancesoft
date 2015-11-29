import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Update_Teacher import Ui_modify_teacher
from PyQt4.QtSql import *
import re

class modify_Information(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.modify = Ui_modify_teacher()
        self.modify.setupUi(self)

        self.conn()

        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        self.teach_query = QSqlQuery()
        self.teach_query.exec_("Select Teacher_name FROM Teacher")
        while self.teach_query.next():
            record = self.teach_query.record()
            self.name = str(record.value(0))
            self.modify.selectTeacherComboBox.addItem(self.name)
            
        self.modify.Select_teacher_btn.clicked.connect(self.fill_form)

        self.modify.Submit_btn.clicked.connect(self.submit_updates)

    def fill_form(self):
        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        selected_teacher_name = str(self.modify.selectTeacherComboBox.currentText())
        query = QSqlQuery()
        address_query =QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_name = '%s'" % selected_teacher_name)
        address_query.exec_("SELECT Address_id, Street, City, State FROM Address, Teacher WHERE Teacher_address = Address_id AND Teacher_name = '%s'" % selected_teacher_name)
        while query.next():
            record = query.record()
            self.Teacher_id = str(record.value(0))
            self.modify.nameLineEdit.setText(str(record.value(1)))
            self.modify.homePhoneLineEdit.setText(str(record.value(2)))
            self.modify.cellPhoneLineEdit.setText(str(record.value(3)))
            self.modify.workPhoneLineEdit.setText(str(record.value(4)))
            while address_query.next():
                address_record =address_query.record()
                self.address_id = str(address_record.value(0))
                self.modify.addressLineEdit.setText(str(address_record.value(1)))
                self.modify.cityLineEdit.setText(str(address_record.value(2)))
                find = self.modify.stateComboBox.findText(str(address_record.value(3)),QtCore.Qt.MatchFixedString)
                if find >= 0:
                    self.modify.stateComboBox.setCurrentIndex(find)
            self.modify.emailLineEdit.setText(str(record.value(6)))
            find = self.modify.genderComboBox.findText(str(record.value(7)),QtCore.Qt.MatchFixedString)
            if find >= 0:
                self.modify.genderComboBox.setCurrentIndex(find)
            self.modify.SSNLineEdit.setText(str(record.value(8)))
            self.modify.payRateDoubleSpinBox.setValue(float(record.value(9)))
            self.modify.textEdit.setText(str(record.value(10)))

    def submit_updates(self):
        self.name = self.modify.nameLineEdit.text()
        
        self.home = self.modify.homePhoneLineEdit.text()
        self.home = re.sub('[^0-9]+', '', self.home)
        self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.home[:-1])) + self.home[-1]
        
        self.cell = self.modify.cellPhoneLineEdit.text()
        self.cell = re.sub('[^0-9]+', '', self.cell)
        self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.cell[:-1])) + self.cell[-1]
        
        self.work = self.modify.workPhoneLineEdit.text()
        self.work = re.sub('[^0-9]+', '', self.work)
        self.work = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.work[:-1])) + self.work[-1]
        
        self.address = self.modify.addressLineEdit.text()
        self.city = self.modify.cityLineEdit.text()
        self.state = str(self.modify.stateComboBox.currentText())    
        self.email = self.modify.emailLineEdit.text()
        self.gender = str(self.modify.genderComboBox.currentText())
        self.ssn = self.modify.SSNLineEdit.text()
        self.pay = self.modify.payRateDoubleSpinBox.value()
        self.medical = self.modify.textEdit.toPlainText()

        if self.name == '':
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
        elif self.home == '' or self.home.len() < 10:w
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
            
        elif self.cell != '' and self.cell.len() < 10:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
            
        elif self.work != '' and self.work.len() < 10:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )

        elif self.address == '' || self.address.len() < 5:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
        elif self.city == '':
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )

        else:
            results_msg = "Pending Upadates: \n Name:'%s' \n Home phone:'%s' \n Cell phone:'%s' \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                          \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Pay:'%s' \n Medical:'%s'"
            reply = QtGui.QMessageBox.question(self, 'Message', 
                         results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == Yes:
                update_query = QSqlQuery()
                update_query.exec_("Update Teacher SET Teacher_name ='%s', \
                                    Teacher_home_phone ='%s', Teacher_cell_phone ='%s',\
                                    Teacher_work_phone ='%s', Teacher_email ='%s',\
                                    Teacher_sex ='%s', Teacher_SSN ='%s', \
                                    Teacher_pay_rate ='%s', Teacher_medical_information ='%s' WHERE \
                                    Teacher_id ='%s'" \
                                   %( self.name, self.home, self.cell, self.work, self.email, \
                                   self.gender, self.ssn, self.pay, self.medical, self.Teacher_id))

                update_query2 = QSqlQuery()
                update_query2.exec_("Update Address SET Street ='%s', City ='%s',\
                                    State ='%s' WHERE Address_id ='%u'" %(self.address, \
                                    self.city, self.state, int(self.address_id)))

        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = modify_Information()
Current_Window.show()
print("here")
sys.exit(app.exec_())
