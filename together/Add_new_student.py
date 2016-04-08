import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Add_student import Ui_add_student
from PyQt4.QtSql import *
import re

class add_Student(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.student = Ui_add_student()
        self.student.setupUi(self)

        self.conn()

        self.student.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.student.sel_teach.setTable("Student")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
            
        self.fillGuardian()
        self.student.Submit_btn.clicked.connect(self.insert_student)

    def fillGuardian(self):
        self.guardQuery = QSqlQuery()
        self.guardQuery.exec_("Select Guardian_name from Guardian")

        while self.guardQuery.next():
            record = self.guardQuery.record()
            guard = str(record.value(0))
            self.student.primaryComboBox.addItem(guard)
            self.student.secondaryComboBox.addItem(guard)

    def addGuardian(self):
        self.student.guardianDialog =  addGuadianDialog()
        if self.student.guardianDialog.exec_():
            self.closeFlag = self.student.guardianDialog.getClose()
            if self.closeFlag == 0:
                if not isinstance(self.ui.locationDialog.getLocation(), QtCore.QPyNullVariant):
                    return self.student.guardianDialog.getName()


    def check_existing_address(self):
        temp_id = 0
        existing_address_query =QSqlQuery()
        existing_address_query.exec_("SELECT * FROM Address WHERE Street = '%s'\
                            AND City = '%s' AND State = '%s' AND Zipcode = '%s'" % (self.address, self.city, self.state, self.zip))
        while existing_address_query.next():
            result = existing_address_query.record()
            temp_id =  int(result.value(0))

        return temp_id

    def insert_student(self):
            self.name = self.student.nameLineEdit.text()
            
            self.home = self.student.homePhoneLineEdit.text()
            try:
                if self.home != '':
                    self.home = re.sub('[^0-9]+', '', self.home)
                    self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.home[:-1])) + self.home[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                return
     
            self.cell = self.student.cellPhoneLineEdit.text()
            try:
                if self.cell != '':
                    self.cell = re.sub('[^0-9]+', '', self.cell)
                    self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.cell[:-1])) + self.cell[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild cell phone number.\nPhone number format: ###-###-####" )
                return
         
            self.emergencyPhone = self.student.ePhoneLineEdit.text()
            try:
                if self.emergencyPhone != '':
                    self.emergencyPhone = re.sub('[^0-9]+', '', self.emergencyPhone)
                    self.emergencyPhone = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" \
                                       % int(self.emergencyPhone[:-1])) + self.emegencyPhone[-1]
            except ValueError:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild emergency contact number.\nPhone number format: ###-###-####" )
                return
          
            self.address = self.student.addressLineEdit.text()
            self.address = self.address.upper()
            self.city = self.student.cityLineEdit.text()
            self.city = self.city.upper()
            self.state = self.student.stateComboBox.currentText()
            self.zip = self.student.zipcodeLineEdit.text()
            self.email = self.student.emailLineEdit.text()
            self.email = self.email.lower()
            self.gender = self.student.genderComboBox.currentText()
            self.primaryGuard = self.student.primaryComboBox.currentText()
            if self.primaryGuard == "Add New":
                self.primaryGuard = self.addGuardian()
                if self.closeFlag != 0:
                    return
                if self.primaryGuard == "Add New" or self.primaryGuard == '':
                    return
                
            self.secondaryGuard = self.student.secondaryComboBox.currentText()
            if self.secondaryGuard == "Add New":
                self.secondaryGuard = self.addGuardian()
                if self.closeFlag != 0:
                    return
                if self.secondaryGuard == "Add New" or self.secondaryGuard == '':
                    return
                
            self.emergency = self.student.emergencyLineEdit.text()
            self.medical = self.student.medicalTextEdit.toPlainText()
            self.DOB = self.student.DOBDateEdit.date()
            self.DOB = self.DOB.toPyDate()

            self.guardianQuery = QSqlQuery()
            self.guardianQuery.exec_("Select Guardian_id from Guardian where Guardian_name = '%s' or Guardian_name = '%s'" %(self.primaryGuard, self.secondaryGuard))

            if self.guardianQuery.next():
                record = self.guardianQuery.record()
                primary_id = int(record.value(0))
                secondary_id = int(record.value(1))
                if primary_id == None:
                    primary_id = 0
                if secondary_id == None:
                    secondary_id = 0
            
                    

            if self.name == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street" )
            
            elif self.home == '' or len(self.home) < 10 or len(self.home) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.cell != '' and len(self.cell) < 10 or len(self.cell) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild cell phone number.\nPhone number format: ###-###-####" )
                
            elif self.emergencyPhone != '' and len(self.emergencyPhone) < 10 or len(self.emergencyPhone) > 12:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild emergency phone.\nPhone number format: ###-###-####" )

            elif self.address == '' or len(self.address) < 5:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street" )
                
            elif self.city == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Zipcode, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street" )
                
            elif self.zip == '' or  re.match('^\d{5}(-\d{4})?$', self.zip) == None:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter a vaild zipcode")
                
            else:
                self.address_exist = self.check_existing_address()
                results_msg = "Pending Insert: \n Name:'%s' \n DOB:'%s' \n Home phone:'%s' \n Cell phone:'%s'\
                \n Emergency contact:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                \n Zipcode: '%s' \n Email:'%s' \n Gender:'%s' \n Primary Guardian:'%s' \n Secondary Guardian:'%s' \n Medical:'%s'" \
                          %( self.name, str(self.DOB), self.home, self.cell, self.emergency,\
                             self.address, self.city, self.state, self.zip, \
                             self.email, self.gender, self.primaryGuard, self.secondaryGuard, self.medical)
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
                        self.exist_msg = "Address already exist, setting student to existing address."
                        self.exist_reply = QtGui.QMessageBox.information(self, 'Already Exist', 
                        self.exist_msg, QtGui.QMessageBox.Ok)

                        self.address_id = self.address_exist
                         
                    self.id_query =QSqlQuery()
                    self.id_query.exec_("SELECT Student_id FROM Student ORDER BY Student_id DESC LIMIT 1")
                    while self.id_query.next():
                        self.record = self.id_query.record()
                        self.student_id = self.record.value(0)
                        self.student_id += 1

                    
                    Insert_Student_query = QSqlQuery()
                    Insert_Student_query.exec_("Insert into Student (Student_id, Student_address, Student_name,\
                    Student_sex, Student_email, Student_date_of_birth, Student_home_phone, Student_cell_phone,\
                    Guardian_primary, Guardian_secondary, Student_Emergency_contact, Emergency_contact_phone, \
                    Student_medical_information, )\
                    values(%d,'%s', '%s', '%s','%s',%d,'%s','%s', '%s', '%s', '%s','%s')"
                    %(int(self.student_id), int(self.address_id), self.name, self.gender, self.email,\
                      self.DOB, self.home, self.cell, self.primary_id, self.secondary_id, self.emergency,\
                      self.emergencyPhone, self.medical))

        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = add_Student()
window.show()
sys.exit(app.exec_())


