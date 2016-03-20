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

        self.Admin_id = 0
        self.Teacher_id = 0

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
            
        self.modify.Select_teacher_btn.clicked.connect(self.fillForm)

        self.modify.Submit_btn.clicked.connect(self.submitUpdates)

    def checkExistingAddress(self):
        temp_id = 0 
        existing_address_query =QSqlQuery()
        existing_address_query.exec_("SELECT * FROM Address WHERE Street = '%s'\
                            AND City = '%s' AND State = '%s' AND Zipcode = '%s'" % (self.address, self.city, self.state, self.zip))
        while existing_address_query.next():
            result = existing_address_query.record()
            temp_id =  int(result.value(0))

        return temp_id
            
    def clearForm(self):
        self.modify.nameLineEdit.setText("")
        self.modify.homePhoneLineEdit.setText("")
        self.modify.cellPhoneLineEdit.setText("")
        self.modify.workPhoneLineEdit.setText("")
        self.modify.addressLineEdit.setText("")
        self.modify.cityLineEdit.setText("")
        find = self.modify.stateComboBox.findText("South Dakota",QtCore.Qt.MatchFixedString)
        self.modify.zipLineEdit.setText("")
        if find >= 0:
            self.modify.stateComboBox.setCurrentIndex(find)
        self.modify.emailLineEdit.setText("")
        find = self.modify.genderComboBox.findText("Male",QtCore.Qt.MatchFixedString)
        if find >= 0:
            self.modify.genderComboBox.setCurrentIndex(find)
        self.modify.SSNLineEdit.setText("")
        self.modify.payRateDoubleSpinBox.setValue(0.00)
        self.modify.medicalTextEdit.setText("")
        self.modify.DOBDateEdit.setDate(QtCore.QDate.currentDate())
        

    def fillForm(self):

        self.clearForm()
        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        selected_teacher_name = str(self.modify.selectTeacherComboBox.currentText())
        query = QSqlQuery()
        address_query =QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_name = '%s'" % selected_teacher_name)
        address_query.exec_("SELECT Address_id, Street, City, State, Zipcode FROM Address, \
                             Teacher WHERE Teacher_address = Address_id AND Teacher_name = '%s'" % selected_teacher_name)
        while query.next():
            record = query.record()
            self.Teacher_id = int(record.value(0))
            self.modify.nameLineEdit.setText(str(record.value(1)))
            self.modify.homePhoneLineEdit.setText(str(record.value(2)))
            if not isinstance(record.value(3), QtCore.QPyNullVariant):
                self.modify.cellPhoneLineEdit.setText(str(record.value(3)))
            if not isinstance(record.value(4), QtCore.QPyNullVariant):
                self.modify.workPhoneLineEdit.setText(str(record.value(4)))
            while address_query.next():
                address_record =address_query.record()
                self.address_id = str(address_record.value(0))
                self.modify.addressLineEdit.setText(str(address_record.value(1)))
                self.modify.cityLineEdit.setText(str(address_record.value(2)))
                find = self.modify.stateComboBox.findText(str(address_record.value(3)),QtCore.Qt.MatchFixedString)
                self.modify.zipLineEdit.setText(str(address_record.value(4)))
                if find >= 0:
                    self.modify.stateComboBox.setCurrentIndex(find)
            self.modify.emailLineEdit.setText(str(record.value(6)))
            find = self.modify.genderComboBox.findText(str(record.value(7)),QtCore.Qt.MatchFixedString)
            if find >= 0:
                self.modify.genderComboBox.setCurrentIndex(find)
            self.modify.SSNLineEdit.setText(str(record.value(8)))
            self.modify.payRateDoubleSpinBox.setValue(float(record.value(9)))
            self.modify.medicalTextEdit.setText(str(record.value(10)))
            self.modify.DOBDateEdit.setDate(record.value(11))

        if self.Teacher_id != 0:
            query.exec("Select Admin_id From Account Where Teacher_id = %d" % self.Teacher_id)
            if query.next():
                record = query.record()
                self.Admin_id = int(record.value(0))
            

    def submitUpdates(self):
        self.name = self.modify.nameLineEdit.text()
        
        self.home = self.modify.homePhoneLineEdit.text()
        try:
            self.home = re.sub('[^0-9]+', '', self.home)
            self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                               % int(self.home[:-1])) + self.home[-1]
            
        except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                return
        
        self.cell = self.modify.cellPhoneLineEdit.text()
        try:
            if self.cell != '': 
                self.cell = re.sub('[^0-9]+', '', self.cell)
                self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                   % int(self.cell[:-1])) + self.cell[-1]
        except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                return
        
        self.work = self.modify.workPhoneLineEdit.text()
        try:
            if self.work != '':
                self.work = re.sub('[^0-9]+', '', self.work)
                self.work = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                   % int(self.work[:-1])) + self.work[-1]
        except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                return
        
        self.address = self.modify.addressLineEdit.text()
        self.address = self.address.upper()
        self.city = self.modify.cityLineEdit.text()
        self.city = self.city.upper()
        self.state = str(self.modify.stateComboBox.currentText())
        self.zip = self.modify.zipLineEdit.text()
        self.email = self.modify.emailLineEdit.text()
        self.email = self.email.lower()
        self.gender = str(self.modify.genderComboBox.currentText())
        self.ssn = self.modify.SSNLineEdit.text()
        self.pay = self.modify.payRateDoubleSpinBox.value()
        self.medical = self.modify.medicalTextEdit.toPlainText()
        self.DOB = self.modify.DOBDateEdit.date()
        self.DOB = self.DOB.toPyDate()

        if self.name == '':
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
        elif self.home == '' or len(self.home) < 10:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
            
        elif self.cell != '' and len(self.cell) < 10:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
            
        elif self.work != '' and len(self.work) < 10:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )

        elif self.address == '' or len(self.address) < 5:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
        elif self.city == '':
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )

        elif self.zip == '' or  re.match('^\d{5}(-\d{4})?$', self.zip) == None:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter a vaild zipcode")

        elif self.ssn == '' or  re.match('^\d{3}-\d{2}-\d{4}$', self.ssn) == None:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter a vaild SSN. SNN format: ###-##-####")

        else:
            self.address_question = "Would you like to add as a new address? \n (Click no to update current address)"
            self.address_reply = QtGui.QMessageBox.question(self, 'Address', 
                         self.address_question, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            
            self.address_exist = self.checkExistingAddress()
            
            results_msg = "Pending Upadates: \n Name:'%s' \n DOB:'%s' \n Home phone:'%s' \n Cell phone:'%s' \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                          \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Pay:'%s' \n Medical:'%s'" %( self.name, self.DOB, self.home, self.cell, self.work,\
                           self.address, self.city, self.state, self.email, self.gender, self.ssn, self.pay, self.medical)
            reply = QtGui.QMessageBox.question(self, 'Message', 
                         results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
           
            if reply == QtGui.QMessageBox.Yes:
                if self.address_reply == QtGui.QMessageBox.Yes:
                    if self.address_exist == 0:
                        self.address_query = QSqlQuery()
                        self.address_query.exec_("SELECT Address_id FROM Address ORDER BY Address_id DESC LIMIT 1")
                        while self.address_query.next():
                                self.record = self.address_query.record()
                                self.address_id = self.record.value(0)
                                self.address_id += 1
                        
                        self.update_query2 = QSqlQuery()
                        self.update_query2.exec_("Insert into Address (Address_id, Street,\
                                                City, State, zipcode) values('%d','%s','%s','%s','%s')" \
                                                %( int(self.address_id), self.address, self.city, self.state, self.zip))
                    else:
                         self.exist_msg = "Address already exist, setting teacher to existing address."
                         self.exist_reply = QtGui.QMessageBox.information(self, 'Already Exist', 
                         self.exist_msg, QtGui.QMessageBox.Ok)

                         self.address_id = self.address_exist
                
                elif self.address_reply == QtGui.QMessageBox.No:
                    self.update_query2 = QSqlQuery()
                    self.update_query2.exec_("Update Address SET Street ='%s', City ='%s',\
                                    State ='%s', Zipcode ='%s' WHERE Address_id ='%d'" %(self.address, \
                                    self.city, self.state, self.zip, int(self.address_id) ))
                
                update_query = QSqlQuery()
                update_query.exec_("Update Teacher SET Teacher_name ='%s', \
                                    Teacher_home_phone ='%s', Teacher_cell_phone ='%s',\
                                    Teacher_work_phone ='%s', Teacher_address = %d, Teacher_email ='%s',\
                                    Teacher_sex ='%s', Teacher_SSN ='%s', \
                                    Teacher_pay_rate ='%s', Teacher_medical_information ='%s',\
                                    Teacher_date_of_birth ='%s' WHERE \
                                    Teacher_id =%d" \
                                   %( self.name, self.home, self.cell, self.work, \
                                      int(self.address_id), self.email, self.gender,\
                                      self.ssn, self.pay, self.medical, self.DOB,\
                                      self.Teacher_id))
                
                if self.Admin_id != 0:
                    update_query.exec_("Update Admin SET Admin_name ='%s', \
                                    Admin_home_phone ='%s', Admin_cell_phone ='%s',\
                                    Admin_work_phone ='%s', Admin_address = %d, Admin_email ='%s',\
                                    Admin_sex ='%s', Admin_SSN ='%s', \
                                    Admin_pay_rate ='%s', Admin_medical_information ='%s',\
                                    Admin_date_of_birth ='%s' WHERE \
                                    Admin_id =%d" \
                                   %( self.name, self.home, self.cell, self.work, \
                                      int(self.address_id), self.email,self.gender,\
                                      self.ssn, self.pay, self.medical, self.DOB,\
                                      self.Admin_id))
                    

                
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
