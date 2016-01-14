import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Update_My_Teacher_Info import Ui_modify_my_teacher
from PyQt4.QtSql import *
import re

class modify_My_Information(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.modify = Ui_modify_my_teacher()
        self.modify.setupUi(self)

        self.name = "jwitmore"

        self.conn()

        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
        self.fill_form()

        self.modify.Submit_btn.clicked.connect(self.submit_updates)

    def check_existing_address(self):
        temp_id = 0 
        existing_address_query =QSqlQuery()
        existing_address_query.exec_("SELECT * FROM Address WHERE Street = '%s'\
                            AND City = '%s' AND State = '%s' AND Zipcode = '%s'" % (self.address, self.city, self.state, self.zip))
        while existing_address_query.next():
            result = existing_address_query.record()
            temp_id =  int(result.value(0))
        print("check ", temp_id)

        return temp_id
            
        
        

    def fill_form(self):
        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        query = QSqlQuery()
        address_query =QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_id = \
                    (select Teacher_id from Account where User_name = \
                    '%s')" % self.name)
        address_query.exec_("SELECT Address_id, Street, City, State, Zipcode FROM Address, \
                             Teacher WHERE Teacher_address = Address_id AND Teacher_id = \
                            (select Teacher_id from Account where User_name = '%s')" % self.name)
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
                self.modify.zipLineEdit.setText(str(address_record.value(4)))
                if find >= 0:
                    self.modify.stateComboBox.setCurrentIndex(find)
            self.modify.emailLineEdit.setText(str(record.value(6)))
            find = self.modify.genderComboBox.findText(str(record.value(7)),QtCore.Qt.MatchFixedString)
            if find >= 0:
                self.modify.genderComboBox.setCurrentIndex(find)
            self.modify.SSNLineEdit.setText(str(record.value(8)))
            self.modify.medicalTextEdit.setText(str(record.value(10)))
            self.modify.DOBDateEdit.setDate(record.value(11))

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
        self.zip = self.modify.zipLineEdit.text()
        self.email = self.modify.emailLineEdit.text()
        self.gender = str(self.modify.genderComboBox.currentText())
        self.ssn = self.modify.SSNLineEdit.text()
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
            
            self.address_exist = self.check_existing_address()
            
            results_msg = "Pending Upadates: \n Name:'%s' \n DOB:'%s' \n Home phone:'%s' \n Cell phone:'%s' \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                          \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Medical:'%s'" %( self.name, self.DOB, self.home, self.cell, self.work,\
                           self.address, self.city, self.state, self.email, self.gender, self.ssn, self.medical)
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
                         print(self.address_id)
                
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
                                    Teacher_medical_information ='%s',\
                                    Teacher_date_of_birth ='%s' WHERE \
                                    Teacher_id ='%s'" \
                                   %( self.name, self.home, self.cell, self.work, int(self.address_id), self.email, \
                                   self.gender, self.ssn, self.medical, self.DOB,\
                                      self.Teacher_id))

                
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = modify_My_Information()
Current_Window.show()
sys.exit(app.exec_())
