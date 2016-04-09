import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_reg import Ui_Stu_reg_dialog
from Class_list_dialog import Class_list_dialog
from PyQt4.QtSql import *
from functools import partial
import re

class Stu_reg_dialog(QtGui.QDialog):
    def __init__(self, name):
        self.name = name
        
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Stu_reg_dialog()
        self.ui.setupUi(self)
        self.ui.Update_detail_btn.clicked.connect(self.update)
        self.ui.Id_detail_lineEdit.setEnabled(False)


        #show detial
        stu_query = QSqlQuery()
        stu_query.exec_("select * from Student where Student_name = '%s'" % self.name)
        stu_query.next()

        self.ui.List_detail_btn.clicked.connect(self.show_list)


        #insert to combobox
        self.g_dict = {}
        guradian_query = QSqlQuery()
        guradian_query.exec_("select Guardian_name, Guardian_id from Guardian")

        while guradian_query.next():
            self.ui.Pguradian_detail_comboBox.addItem(guradian_query.value(0))
            self.g_dict[guradian_query.value(0)] = guradian_query.value(1)
            self.ui.Sguardian_detail_comboBox.addItem(guradian_query.value(0))


        if not isinstance(stu_query.value(1), QtCore.QPyNullVariant):
            StuAddress = stu_query.value(1)
            address_query = QSqlQuery()
            address_query.exec_("select Street, City, State, Zipcode from Address where Address_id = %d" % StuAddress)
            address_query.next()

            #address
            self.ui.Address_detail_lineEdit.setText(address_query.value(0))

            #city
            self.ui.City_detail_lineEdit.setText(address_query.value(1))

            #state
            index = self.ui.State_detail_ComboBox.findText(address_query.value(2))
            self.ui.State_detail_ComboBox.setCurrentIndex(index)

            #zipcode
            self.ui.Zipcode_detail_lineEdit.setText(str(address_query.value(3)))
            
        
        if not isinstance(stu_query.value(8), QtCore.QPyNullVariant):
            StuPG = stu_query.value(8)
            guardian_query = QSqlQuery()
            guardian_query.exec_("select Guardian_name from Guardian where Guardian_id = %d"% StuPG)
            guardian_query.next()
            text = guardian_query.value(0)
            index = self.ui.Pguradian_detail_comboBox.findText(guardian_query.value(0))
            self.ui.Pguradian_detail_comboBox.setCurrentIndex(index)

            
        if not isinstance(stu_query.value(9), QtCore.QPyNullVariant):
            StuSG = stu_query.value(9)
            guardian_query = QSqlQuery()
            guardian_query.exec_("select Guardian_name from Guardian where Guardian_id = %d"% StuSG)
            guardian_query.next()
            text = guardian_query.value(0) 
            index = self.ui.Sguardian_detail_comboBox.findText(guardian_query.value(0))
            self.ui.Sguardian_detail_comboBox.setCurrentIndex(index)
        
        if not isinstance(stu_query.value(0), QtCore.QPyNullVariant):
            self.id = stu_query.value(0)
            self.ui.Id_detail_lineEdit.setText(str(stu_query.value(0)))
            
        if not isinstance(stu_query.value(2), QtCore.QPyNullVariant):
            self.ui.Name_detail_lineEdit.setText(stu_query.value(2))
            self.orinName = stu_query.value(2)

        #gender
        if not isinstance(stu_query.value(3), QtCore.QPyNullVariant):
            index = self.ui.Gender_comboBox.findText(stu_query.value(3))
            self.ui.Gender_comboBox.setCurrentIndex(index)
    
        if not isinstance(stu_query.value(4), QtCore.QPyNullVariant):
            self.ui.Email_detail_lineEdit.setText(stu_query.value(4))
        if not isinstance(stu_query.value(5), QtCore.QPyNullVariant):
            self.ui.Birth_detail_dateEdit.setDate(stu_query.value(5)) 

        if not isinstance(stu_query.value(6), QtCore.QPyNullVariant):
            self.ui.Phone_detail_lineEdit.setText(stu_query.value(6))
            
        if not isinstance(stu_query.value(7), QtCore.QPyNullVariant):
            self.ui.Cphone_detail_lineEdit.setText(stu_query.value(7))

        if not isinstance(stu_query.value(10), QtCore.QPyNullVariant):
            self.ui.Econtact_detail_lineEdit.setText(stu_query.value(10))
            
        if not isinstance(stu_query.value(11), QtCore.QPyNullVariant):
            self.ui.Ephone_detail_lineEdit.setText(stu_query.value(11))
            
        if not isinstance(stu_query.value(12), QtCore.QPyNullVariant):
            self.ui.Medical_detail_textEdit.setText(stu_query.value(12))
            
        

    def show_list(self):
        self.ui.class_list = Class_list_dialog(self.id)
        self.ui.class_list.show()
        
    def update(self):
        self.StuID = self.ui.Id_detail_lineEdit.text()
        self.StuName = self.ui.Name_detail_lineEdit.text()      
        self.StuGender = self.ui.Gender_comboBox.currentText()   
        self.StuEmail = self.ui.Email_detail_lineEdit.text()
        self.StuBirth = self.ui.Birth_detail_dateEdit.date()
        self.StuBirth = self.StuBirth.toPyDate()
        
        self.StuPhone = self.ui.Phone_detail_lineEdit.text()
        self.StuCphone = self.ui.Cphone_detail_lineEdit.text()
        
        self.StuEcon = self.ui.Econtact_detail_lineEdit.text()
        self.StuEphone = self.ui.Ephone_detail_lineEdit.text()
        self.StuAddress = self.ui.Address_detail_lineEdit.text()
        self.StuAddress = self.StuAddress.upper()
        self.StuCity = self.ui.City_detail_lineEdit.text()
        self.StuCity =  self.StuCity.upper()
        self.StuState = self.ui.State_detail_ComboBox.currentText()
        self.StuMedical = self.ui.Medical_detail_textEdit.toPlainText()
        self.StuZipcode = self.ui.Zipcode_detail_lineEdit.text()


        self.StuPG = self.g_dict[self.ui.Pguradian_detail_comboBox.currentText()]
        self.StuSG = self.g_dict[self.ui.Sguardian_detail_comboBox.currentText()]

        name_query = QSqlQuery()
        name_query.exec_("select Student_name from Student")
        

        #needs error checking
        #if name empty
        if self.StuName == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "student name cannot be empty!" )
            return
        elif self.StuName != "" and self.orinName != self.StuName:
            while name_query.next():
                if (name_query.value(0) == self.StuName):
                    QtGui.QMessageBox.warning(
                    self, 'Error', "student name cannot be same!" )
                    return 

        #email
        if self.StuEmail != "" and \
        re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', self.StuEmail ) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid email address!" )
            return
        
        #check if the home phone is valid
        if self.StuPhone == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "home phone cannot be empty!" )
            return
        elif self.StuPhone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.StuPhone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid home phone number in XXX-XXX-XXXX format!")
            return

        #check if the cell phone is valid
        if self.StuCphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.StuCphone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid cell phone number in XXX-XXX-XXXX format!")
            return

        #check emer phone is valid
        if self.StuEphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.StuEphone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter an valid emergency phone number in XXX-XXX-XXXX format!")
            return

        #check address
        if self.StuAddress == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "Adress cannot be empty!")
            return
        #check city
        if self.StuCity == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "City cannot be empty!")
            return
        #ckeck zipcode
        if self.StuZipcode == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "Zipcode cannot be empty!")
            return 
        elif self.StuZipcode != "" and not self.StuZipcode.isdigit():
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid zipcode!")
            return 

        update_query = QSqlQuery()
        
        if update_query.exec_("Update Student, Address Set Student.Student_name = '%s', Student.Student_sex = '%s', Student.Student_email = '%s', \
                           Student.Student_date_of_birth = '%s', Student.Student_home_phone = '%s', Student.Student_cell_phone = '%s', Student.Student_Emergency_contact = '%s', Student.Emergency_contact_phone = '%s', \
                           Student.Student_medical_information = '%s', Student.Guardian_primary = %d, Student.Guardian_secondary = %d,\
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Address.Zipcode = '%s'\
                           Where Student.Student_id = '%d' and Student.Student_address = Address.Address_id"\
                           %(self.StuName,  self.StuGender, self.StuEmail, self.StuBirth, self.StuPhone, self.StuCphone, self.StuEcon, self.StuEphone,\
                           self.StuMedical, self.StuPG, self.StuSG,self.StuAddress, self.StuCity, self.StuState, self.StuZipcode, int(self.StuID))):
            QtGui.QMessageBox.information(
                self, 'Success', 'Update record successfully')
        else:
                       QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
    
