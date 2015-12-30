import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Add_admin import Ui_add_admin
from PyQt4.QtSql import *
import re

class add_admin(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.admin = Ui_add_admin()
        self.admin.setupUi(self)

        self.conn()

        self.admin.sel_admin = QSqlRelationalTableModel(db = self.db)
        self.admin.sel_admin.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
            
        self.admin.selectComboBox.addItem("New Admin")
        self.teach_query = QSqlQuery()
        self.teach_query.exec_("Select Teacher_name FROM Teacher, Account where \
                                Account.Teacher_id = Teacher.Teacher_id AND \
                                Account.Admin_id = 0 ")
        while self.teach_query.next():
            record = self.teach_query.record()
            self.name = str(record.value(0))
            self.admin.selectComboBox.addItem(self.name)

        self.admin.Select_btn.clicked.connect(self.fill_existing)
        self.admin.Submit_btn.clicked.connect(self.insert_admin)

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

    def fill_existing(self):
        self.admin.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.admin.sel_teach.setTable("Teacher")

        selected_teacher_name = str(self.admin.selectComboBox.currentText())
        query = QSqlQuery()
        address_query =QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_name = '%s'" % selected_teacher_name)
        address_query.exec_("SELECT Address_id, Street, City, State, Zipcode FROM Address, \
                             Teacher WHERE Teacher_address = Address_id AND Teacher_name = '%s'" % selected_teacher_name)
        while query.next():
            record = query.record()
            self.Teacher_id = str(record.value(0))
            self.admin.nameLineEdit.setText(str(record.value(1)))
            self.admin.homePhoneLineEdit.setText(str(record.value(2)))
            self.admin.cellPhoneLineEdit.setText(str(record.value(3)))
            self.admin.workPhoneLineEdit.setText(str(record.value(4)))
            while address_query.next():
                address_record =address_query.record()
                self.address_id = str(address_record.value(0))
                self.admin.addressLineEdit.setText(str(address_record.value(1)))
                self.admin.cityLineEdit.setText(str(address_record.value(2)))
                find = self.admin.stateComboBox.findText(str(address_record.value(3)),QtCore.Qt.MatchFixedString)
                self.admin.zipcodeLineEdit.setText(str(address_record.value(4)))
                if find >= 0:
                    self.admin.stateComboBox.setCurrentIndex(find)
            self.admin.emailLineEdit.setText(str(record.value(6)))
            find = self.admin.genderComboBox.findText(str(record.value(7)),QtCore.Qt.MatchFixedString)
            if find >= 0:
                self.admin.genderComboBox.setCurrentIndex(find)
            self.admin.SSNLineEdit.setText(str(record.value(8)))
            self.admin.payRateDoubleSpinBox.setValue(float(record.value(9)))
            self.admin.medicalTextEdit.setText(str(record.value(10)))
            self.admin.DOBDateEdit.setDate(record.value(11))
        

    def insert_admin(self):
            self.name = self.admin.nameLineEdit.text()
            self.home = self.admin.homePhoneLineEdit.text()
            self.home = re.sub('[^0-9]+', '', self.home)
            self.home = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.home[:-1])) + self.home[-1]
 
            self.cell = self.admin.cellPhoneLineEdit.text()
            if self.cell != '':
                self.cell = re.sub('[^0-9]+', '', self.cell)
                self.cell = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.cell[:-1])) + self.cell[-1]
     
            self.work = self.admin.workPhoneLineEdit.text()
            if self.work != '':
                self.work = re.sub('[^0-9]+', '', self.work)
                self.work = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(self.work[:-1])) + self.work[-1]
      
            self.address = self.admin.addressLineEdit.text()
            self.city = self.admin.cityLineEdit.text()
            self.state = self.admin.stateComboBox.currentText()
            self.zip = self.admin.zipcodeLineEdit.text()
            self.email = self.admin.emailLineEdit.text()
            self.gender = self.admin.genderComboBox.currentText()
            self.SSN = self.admin.SSNLineEdit.text()
            self.pay = self.admin.payRateDoubleSpinBox.value()
            self.medical = self.admin.medicalTextEdit.toPlainText()
            self.DOB = self.admin.DOBDateEdit.date()
            self.DOB = self.DOB.toPyDate()
            print(self.home, ' ', len(self.home))
            print("test:",  re.match('^\d{5}(-\d{4})?$', self.zip))

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
                        self.exist_msg = "Address already exist, setting Admin to existing address."
                        self.exist_reply = QtGui.QMessageBox.information(self, 'Already Exist', 
                        self.exist_msg, QtGui.QMessageBox.Ok)

                        self.address_id = self.address_exist
                         
                    self.id_query =QSqlQuery()
                    self.id_query.exec_("SELECT Admin_id FROM Admin ORDER BY Admin_id DESC LIMIT 1")
                    while self.id_query.next():
                        self.record = self.id_query.record()
                        self.admin_id = self.record.value(0)
                        self.admin_id += 1

                    
                    Insert_Admin_query = QSqlQuery()
                    Insert_Admin_query.exec_("Insert into Admin (Admin_id,Admin_name,\
                    Admin_home_phone, Admin_cell_phone, Admin_work_phone,\
                    Admin_address, Admin_email, Admin_sex, Admin_SSN, \
                    Admin_pay_rate, Admin_medical_information, Admin_date_of_birth)\
                    values(%d,'%s', '%s', '%s','%s',%d,'%s','%s', '%s', '%s', '%s','%s')"
                    %(int(self.admin_id), self.name, self.home, self.cell, self.work,\
                      int(self.address_id), self.email, self.gender, self.SSN, self.pay,\
                      self.medical, self.DOB))

                    self.create_account()

    def create_account(self):
        if str(self.admin.selectComboBox.currentText()) == "New Admin":
            id_query =QSqlQuery()
            id_query.exec_("SELECT User_id FROM Account ORDER BY User_id DESC LIMIT 1")
            while id_query.next():
                result = id_query.record()
                print("record: ",result.value(0))
                user_id = result.value(0)
                user_id += 1
                print("User id: ",user_id)

            username = self.admin.nameLineEdit.text()
            pword = "rcdancearts"
            access = 1
            stu_id = 0
            teach_id = 0

            print("test: ",int(user_id), username, pword, access, stu_id, \
                             teach_id, int(self.admin_id)) 

            new_query = QSqlQuery()
            new_query.exec_("Insert into Account (User_id, User_name, User_password,\
               Access_level, Student_id, Teacher_id, Admin_id) values(%d,'%s','%s',%d,\
               %d,%d,%d)" % (int(user_id), username, pword, access, stu_id, \
                             teach_id, int(self.admin_id)))

        else:
            update_query = QSqlQuery()
            update_query.exec_("Update Account SET Access_level=1, Admin_id=%d \
                WHERE Teacher_id = (SELECT Teacher_id FROM Teacher WHERE Teacher_name ='%s')"\
                %(int(self.admin_id), self.name))
            print(self.admin_id, self.name)

        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = add_admin()
Current_Window.show()
sys.exit(app.exec_())
