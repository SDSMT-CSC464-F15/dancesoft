import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_reg import Ui_Stu_reg_dialog
from Class_list_dialog import Class_list_dialog
from PyQt4.QtSql import *
from functools import partial


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
        guradian_query = QSqlQuery()
        guradian_query.exec_("select Guardian_name, Guardian_id from Guardian")
        while guradian_query.next():
            self.ui.Pguradian_detail_comboBox.addItem(guradian_query.value(0))
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

        if not isinstance(stu_query.value(10), QtCore.QPyNullVariant):
            self.ui.Econtact_detail_lineEdit.setText(stu_query.value(10))
            
        if not isinstance(stu_query.value(11), QtCore.QPyNullVariant):
            self.ui.Ephone_detail_lineEdit.setText(stu_query.value(11))
            
        if not isinstance(stu_query.value(12), QtCore.QPyNullVariant):
            self.ui.Medical_detail_textEdit.setText(stu_query.value(12))
            
        if not isinstance(stu_query.value(13), QtCore.QPyNullVariant):
            self.ui.Tuition_detail_lineEdit.setText(str(stu_query.value(13)))
        

    def show_list(self):
        self.ui.class_list = Class_list_dialog(self.id)
        self.ui.class_list.show()
        
    def update(self):
        self.StuID = self.ui.Id_detail_lineEdit.text()
        self.StuName = self.ui.Name_detail_lineEdit.text()      
        self.StuGender = self.ui.Gender_comboBox.currentText()   
        self.StuEmail = self.ui.Email_detail_lineEdit.text()
        self.StuBirth = self.ui.Birth_detail_dateEdit.date()  
        self.StuPhone = self.ui.Phone_detail_lineEdit.text()
        self.StuPG = self.ui.Pguradian_detail_comboBox.currentText()
        self.StuSG = self.ui.Sguardian_detail_comboBox.currentText()
        self.StuEcon = self.ui.Econtact_detail_lineEdit.text()
        self.StuEphone = self.ui.Ephone_detail_lineEdit.text()
        self.StuTuition = self.ui.Tuition_detail_lineEdit.text()
        self.StuAddress = self.ui.Address_detail_lineEdit.text()
        self.StuCity = self.ui.City_detail_lineEdit.text()    
        self.StuState = self.ui.State_detail_ComboBox.currentText()
        self.StuMedical = self.ui.Medical_detail_textEdit.toPlainText()
        self.StuZipcode = self.ui.Zipcode_detail_lineEdit.text()



        update_query = QSqlQuery()
        
        if update_query.exec_("Update Student, Address, Guardian Set Student.Student_name = '%s', Student.Student_sex = '%s', Student.Student_email = '%s', \
                           Student.Student_date_of_birth = '%s', Student.Student_home_phone = '%s', Student.Student_Emergency_contact = '%s', Student.Emergency_contact_phone = '%s', \
                           Student.Student_medical_information = '%s', Student.Tuition = '%s', \
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Address.Zipcode = '%s', Guardian.Guardian_name = '%s'\
                           Where Student.Student_id = '%d' and Student.Student_address = Address.Address_id and Student.Guardian_primary = Guardian.Guardian_id"\
                           %(self.StuName,  self.StuGender, self.StuEmail, self.StuBirth.toString("yyyy-MM-dd"), self.StuPhone,  self.StuEcon, self.StuEphone,\
                           self.StuMedical, self.StuTuition, self.StuAddress, self.StuCity, self.StuState, self.StuZipcode, self.StuPG, int(self.StuID)))\
            and update_query.exec_("Update Student, Guardian Set Guardian.Guardian_name = '%s '\
                                    Where Student.Student_id = '%d' and Student.Guardian_secondary = Guardian.Guardian_id" \
                                   %(self.StuSG, int(self.StuID))):
            QtGui.QMessageBox.information(
                self, 'Success', 'Update record successfully')
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
    
