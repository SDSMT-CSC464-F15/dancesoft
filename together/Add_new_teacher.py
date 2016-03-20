import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Add_teacher import Ui_add_teacher
from PyQt4.QtSql import *
import re

class add_teacher(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.teacher = Ui_add_teacher()
        self.teacher.setupUi(self)

        self.conn()

        self.teacher.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.teacher.sel_teach.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')


        self.teacher.Submit_btn.clicked.connect(self.insert_teacher)

    def check_existing_address(self):
        temp_id = 0
        existing_address_query =QSqlQuery()
        existing_address_query.exec_("SELECT * FROM Address WHERE Street = '%s'\
                            AND City = '%s' AND State = '%s' AND Zipcode = '%s'" % (self.address, self.city, self.state, self.zip))
        while existing_address_query.next():
            result = existing_address_query.record()
            temp_id =  int(result.value(0))

        return temp_id

    def insert_teacher(self):
            self.name = self.teacher.nameLineEdit.text()
            
            self.home = self.teacher.homePhoneLineEdit.text()
            try:
                if self.home != '':
                    self.home = re.sub('[^0-9]+', '', self.home)
                    self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.home[:-1])) + self.home[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                return
     
            self.cell = self.teacher.cellPhoneLineEdit.text()
            try:
                if self.cell != '':
                    self.cell = re.sub('[^0-9]+', '', self.cell)
                    self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.cell[:-1])) + self.cell[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild cell phone number.\nPhone number format: ###-###-####" )
                return
         
            self.work = self.teacher.workPhoneLineEdit.text()
            try:
                if self.work != '':
                    self.work = re.sub('[^0-9]+', '', self.work)
                    self.work = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.work[:-1])) + self.work[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild work phone.\nPhone number format: ###-###-####" )
                return
          
            self.address = self.teacher.addressLineEdit.text()
            self.address = self.address.upper()
            self.city = self.teacher.cityLineEdit.text()
            self.city = self.city.upper()
            self.state = self.teacher.stateComboBox.currentText()
            self.zip = self.teacher.zipcodeLineEdit.text()
            self.email = self.teacher.emailLineEdit.text()
            self.email = self.email.lower()
            self.gender = self.teacher.genderComboBox.currentText()
            self.SSN = self.teacher.SSNLineEdit.text()
            self.pay = self.teacher.payRateDoubleSpinBox.value()
            self.medical = self.teacher.medicalTextEdit.toPlainText()
            self.DOB = self.teacher.DOBDateEdit.date()
            self.DOB = self.DOB.toPyDate()

            if self.name == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
            elif self.home == '' or len(self.home) < 10 or len(self.home) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.cell != '' and len(self.cell) < 10 or len(self.cell) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild cell phone number.\nPhone number format: ###-###-####" )
                
            elif self.work != '' and len(self.work) < 10 or len(self.work) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild work phone.\nPhone number format: ###-###-####" )

            elif self.address == '' or len(self.address) < 5:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
                
            elif self.city == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
                
            elif self.zip == '' or  re.match('^\d{5}(-\d{4})?$', self.zip) == None:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter a vaild zipcode")

            elif self.SSN == '' or  re.match('^\d{3}-\d{2}-\d{4}$', self.SSN) == None:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter a vaild SSN. SNN format: ###-##-####")
            else:
                self.address_exist = self.check_existing_address()
                results_msg = "Pending Insert: \n Name:'%s' \n DOB:'%s' \n Home phone:'%s' \n Cell phone:'%s'\
                \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                \n Zipcode: '%s' \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Pay:'%s' \n Medical:'%s'" \
                          %( self.name, str(self.DOB), self.home, self.cell, self.work,\
                             self.address, self.city, self.state, self.zip, \
                             self.email, self.gender, self.SSN, str(self.pay), self.medical)
                reply = QtGui.QMessageBox.question(self, 'Message', 
                             results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    if self.address_exist == 0:
                        self.id_query =QSqlQuery()
                        self.id_query.exec_("SELECT Address_id FROM Address ORDER BY Address_id DESC LIMIT 1")
                        while self.id_query.next():
                            self.record = self.id_query.record()
                            self.address_id = self.record.value(0)
                            self.address_id += 1

                        
                        self.Insert_Address_query = QSqlQuery()
                        self.Insert_Address_query.exec_("Insert into Address (Address_id, Street,\
                                            City, State, zipcode) values('%u','%s','%s','%s','%s')" \
                                            %( int(self.address_id), self.address, self.city, self.state, self.zip))

                    else:
                        self.exist_msg = "Address already exist, setting teacher to existing address."
                        self.exist_reply = QtGui.QMessageBox.information(self, 'Already Exist', 
                        self.exist_msg, QtGui.QMessageBox.Ok)

                        self.address_id = self.address_exist
                         
                    self.id_query =QSqlQuery()
                    self.id_query.exec_("SELECT Teacher_id FROM Teacher ORDER BY Teacher_id DESC LIMIT 1")
                    while self.id_query.next():
                        self.record = self.id_query.record()
                        self.Teacher_id = self.record.value(0)
                        self.Teacher_id += 1

                    
                    Insert_Teacher_query = QSqlQuery()
                    Insert_Teacher_query.exec_("Insert into Teacher (Teacher_id,Teacher_name,\
                    Teacher_home_phone, Teacher_cell_phone, Teacher_work_phone,\
                    Teacher_address, Teacher_email, Teacher_sex, Teacher_SSN, \
                    Teacher_pay_rate, Teacher_medical_information, Teacher_date_of_birth)\
                    values(%d,'%s', '%s', '%s','%s',%d,'%s','%s', '%s', '%s', '%s','%s')"
                    %(int(self.Teacher_id), self.name, self.home, self.cell, self.work,\
                      int(self.address_id), self.email, self.gender, self.SSN, self.pay,\
                      self.medical, self.DOB))

                    self.create_account()

    def create_account(self):
        id_query =QSqlQuery()
        id_query.exec_("SELECT User_id FROM Account ORDER BY User_id DESC LIMIT 1")
        while id_query.next():
            result = id_query.record()
            user_id = result.value(0)
            user_id += 1

            username = self.name
            pword = "rcdancearts"
            access = 2
            stu_id = 0
            teach_id = int(self.Teacher_id)

            new_query = QSqlQuery()
            new_query.exec_("Insert into Account (User_id, User_name, User_password,\
               Access_level, Student_id, Teacher_id, Admin_id) values(%d,'%s','%s',%d,\
               %d,%d,%d)" % (int(user_id), username, pword, access, stu_id, \
                             teach_id, 0))

        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

