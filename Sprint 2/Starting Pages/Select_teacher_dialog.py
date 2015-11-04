import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Select_Teacher import Select_teacher
from Update_Teacher import modify_teacher
from PyQt4.QtSql import *

class select_Teacher(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Select_teacher()
        self.ui.setupUi(self)
        self.setup_database()

        self.ui.pushButton.clicked.connect(self.modify_information)

        
        
    def setup_database(self):

        
        
        self.conn() #need catch exception

        self.ui.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.ui.sel_teach.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        query = QSqlQuery()
        query.exec_("Select Teacher_name FROM Teacher")
        while query.next():
            record = query.record()
            self.name = str(record.value(0).toString())
            self.ui.selectTeacherComboBox.addItem(self.name)
        
        
    def modify_information(self):

        self.Current_Window2 = modify_information()
        
        
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

class modify_Information(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.modify = modify_teacher()
        self.modify.setupUi(self)

        self.conn()

        self.modify.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.modify.sel_teach.setTable("Teacher")

        selected_teacher_name = "Jamie Witmore"
        query = QSqlQuery()
        address_query =QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_name = '%s'" % selected_teacher_name)
        address_query.exec_("SELECT Address_id, Street, City, State FROM Address, Teacher WHERE Teacher_address = Address_id AND Teacher_name = '%s'" % selected_teacher_name)
        while query.next():
            record = query.record()
            self.Teacher_id = str(record.value(0).toString())
            self.modify.nameLineEdit.setText(str(record.value(1).toString()))
            self.modify.homePhoneLineEdit.setText(str(record.value(2).toString()))
            self.modify.cellPhoneLineEdit.setText(str(record.value(3).toString()))
            self.modify.workPhoneLineEdit.setText(str(record.value(4).toString()))
            while address_query.next():
                address_record =address_query.record()
                self.address_id = str(address_record.value(0).toString())
                self.modify.addressLineEdit.setText(str(address_record.value(1).toString()))
                self.modify.cityLineEdit.setText(str(address_record.value(2).toString()))
                find = self.modify.stateComboBox.findText(str(address_record.value(3).toString()),QtCore.Qt.MatchFixedString)
                if find >= 0:
                    self.modify.stateComboBox.setCurrentIndex(find)
            self.modify.emailLineEdit.setText(str(record.value(6).toString()))
            find = self.modify.genderComboBox.findText(str(record.value(7).toString()),QtCore.Qt.MatchFixedString)
            if find >= 0:
                self.modify.genderComboBox.setCurrentIndex(find)
            self.modify.SSNLineEdit.setText(str(record.value(8).toString()))
            print(float(record.value(9).toString()))
            self.modify.payRateDoubleSpinBox.setValue(float(record.value(9).toString()))
            self.modify.textEdit.setText(str(record.value(10).toString()))

        self.modify.pushButton.clicked.connect(self.submit_updates)

    def submit_updates(self):
        self.name = self.modify.nameLineEdit.text()
        self.home = self.modify.homePhoneLineEdit.text()
        self.cell = self.modify.cellPhoneLineEdit.text()
        self.work = self.modify.workPhoneLineEdit.text()
        self.address = self.modify.addressLineEdit.text()
        self.city = self.modify.cityLineEdit.text()
        self.state = str(self.modify.stateComboBox.currentText())    
        self.email = self.modify.emailLineEdit.text()
        self.gender = str(self.modify.genderComboBox.currentText())
        self.ssn = self.modify.SSNLineEdit.text()
        self.pay = self.modify.payRateDoubleSpinBox.value()
        self.medical = self.modify.textEdit.toPlainText()

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
