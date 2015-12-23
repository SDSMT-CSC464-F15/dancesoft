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

    def insert_teacher(self):
            self.name = self.teacher.nameLineEdit.text()
            self.home = self.teacher.homePhoneLineEdit.text()
            self.home = re.sub('[^0-9]+', '', self.home)
            self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.home[:-1])) + self.home[-1]
 
            self.cell = self.teacher.cellPhoneLineEdit.text()
            self.cell = re.sub('[^0-9]+', '', self.cell)
            self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.cell[:-1])) + self.cell[-1]
     
            self.work = self.teacher.workPhoneLineEdit.text()
            self.work = re.sub('[^0-9]+', '', self.work)
            self.work = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.work[:-1])) + self.work[-1]
      
            self.address = self.teacher.addressLineEdit.text()
            self.city = self.teacher.cityLineEdit.text()
            self.state = self.teacher.stateComboBox.currentText()
            self.zip = self.teacher.zipcodeLineEdit.text()
            self.email = self.teacher.emailLineEdit.text()
            self.gender = self.teacher.genderComboBox.currentText()
            self.SSN = self.teacher.SSNLineEdit.text()
            self.pay = self.teacher.payRateDoubleSpinBox.value()
            self.medical = self.teacher.medicalTextEdit.toPlainText()
            self.DOB = self.teacher.DOBDateEdit.date()
            self.DOB = self.DOB.toPyDate()
            print(self.home, ' ', len(self.home))

            if self.name == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
            elif self.home == '' or len(self.home) < 10 or len(self.home) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.cell != '' and len(self.cell) < 10 or len(self.cell) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.work != '' and len(self.work) < 10 or len(self.work) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )

            elif self.address == '' or len(self.address) < 5:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
                
            elif self.city == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
                
            elif self.zip == '' or len(self.zip) < 5:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            else:
                print(self.name, self.DOB, self.home, self.cell, self.work,\
                           self.address, self.city, self.state, self.zip, self.email, self.gender, self.SSN, self.pay, self.medical)
                results_msg = "Pending Insert: \n Name:'%s' \n DOB:'%s' \n Home phone:'%s' \n \
                            Cell phone:'%s' \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                          \n Zipcode: '%s' \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Pay:'%s' \n Medical:'%s'" \
                          %( self.name, str(self.DOB), self.home, self.cell, self.work,\
                             self.address, self.city, self.state, self.zip, \
                             self.email, self.gender, self.SSN, str(self.pay), self.medical)
                reply = QtGui.QMessageBox.question(self, 'Message', 
                             results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
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

                    self.id_query =QSqlQuery()
                    self.id_query.exec_("SELECT Teacher_id FROM Teacher ORDER BY Teacher_id DESC LIMIT 1")
                    while self.id_query.next():
                        self.record = self.id_query.record()
                        self.Teacher_id = self.record.value(0)
                        self.Teacher_id += 1
                        print(self.Teacher_id)

                    
                    Insert_Teacher_query = QSqlQuery()
                    Insert_Teacher_query.exec_("Insert into Teacher (Teacher_id,Teacher_name,\
                    Teacher_home_phone, Teacher_cell_phone, Teacher_work_phone,\
                    Teacher_address, Teacher_email, Teacher_sex, Teacher_SSN, \
                    Teacher_pay_rate, Teacher_medical_information, Teacher_date_of_birth)\
                    values(%d,'%s', '%s', '%s','%s',%d,'%s','%s', '%s', '%s', '%s','%s')"
                    %(int(self.Teacher_id), self.name, self.home, self.cell, self.work,\
                      int(self.address_id), self.email, self.gender, self.SSN, self.pay,\
                      self.medical, self.DOB))

        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = add_teacher()
Current_Window.show()
sys.exit(app.exec_())
