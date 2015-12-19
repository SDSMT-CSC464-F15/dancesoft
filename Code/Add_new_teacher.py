import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Update_Teacher import Ui_add_teacher
from PyQt4.QtSql import *
from re import sub

class add_teacher(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.teacher = Ui_add_teacher()
        self.modify.setupUi(self)

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
            self.email = self.teacher.emailLineEdit.text()
            self.gender = self.teacher.genderComboBox.currentText()
            self.SSN = self.teacher.SSNLineEdit.text()
            self.pay = self.teacher.payRateDoubleSpinBox.value()
            self.medical = self.teacher.medicalTextEdit.toPlainText()
            self.DOB = self.teacher.DOBDateEdit.date()
            self.DOB = self.DOB.toPyDate()

            if self.name == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            
            elif self.home == '' or self.home.len() < 10:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.cell != '' and self.cell.len() < 10:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )
                
            elif self.work != '' and self.work.len() < 10:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please enter vaild phone number.\nPhone number format: ###-###-####" )

            elif self.address == '' or self.address.len() < 5:
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
                
            elif self.city == '':
                QtGui.QMessageBox.warning(
                    self, 'Error', "Please fill in required fields: Name, DOB, House Phone, Address, City, State, Gender, and Social security number(SSN).\
                    \nPhone number format: ###-###-#### \nAddress format: #'s Street \nSNN format: ###-##-####" )
            else:
                results_msg = "Pending Upadates: \n Name:'%s' \n DOB \n Home phone:'%s' \n Cell phone:'%s' \n Work phone:'%s' \n Address:'%s' \n City:'%s' \n State:'%s' \
                              \n Email:'%s' \n Gender:'%s' \n SSN:'%s' \n Pay:'%s' \n Medical:'%s'"
                reply = QtGui.QMessageBox.question(self, 'Message', 
                             results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    update_query = QSqlQuery()
                    update_query.exec_("Insert into Teacher values(Teacher_name ='%s', \
                                        Teacher_home_phone ='%s', Teacher_cell_phone ='%s',\
                                        Teacher_work_phone ='%s', Teacher_email ='%s',\
                                        Teacher_sex ='%s', Teacher_SSN ='%s', \
                                        Teacher_pay_rate ='%s', Teacher_medical_information ='%s',\
                                        Teacher_date_of_birth ='%s' WHERE \
                                        Teacher_id ='%s'" \
                                       %( self.name, self.home, self.cell, self.work, self.email, \
                                       self.gender, self.ssn, self.pay, self.medical, self.DOB,\
                                          self.Teacher_id))

                    update_query2 = QSqlQuery()
                    update_query2.exec_("Update Address SET Street ='%s', City ='%s',\
                                        State ='%s' WHERE Address_id ='%u'" %(self.address, \
                                        self.city, self.state, int(self.address_id))


        

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
