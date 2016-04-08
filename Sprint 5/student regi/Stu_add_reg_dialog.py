import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_add_reg import Ui_Stu_reg_dialog
from Class_list_dialog import Class_list_dialog
from PyQt4.QtSql import *
from functools import partial
from modify_new_guardian import add_new_guardian



class Stu_add_reg_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Stu_reg_dialog()
        self.ui.setupUi(self)
        self.ui.Update_detail_btn.clicked.connect(self.update)
        self.ui.Id_detail_lineEdit.setDisabled(True)
        stu_query = QSqlQuery()
        stu_query.exec_("select Student_id from Student order by Student_id DESC")
        stu_query.next()
        self.id = stu_query.value(0)+1
        self.ui.Id_detail_lineEdit.setText(str(self.id))
        guradian_query = QSqlQuery()

        new_id = -1
        guradian_query.exec_("select Guardian_name, Guardian_id from Guardian")
        self.g_dict = {}

        
        while guradian_query.next():
            self.ui.Pguradian_detail_comboBox.addItem(guradian_query.value(0))
            self.g_dict[guradian_query.value(0)] = guradian_query.value(1)
            if guradian_query.value(1) > new_id:
                new_id = guradian_query.value(1)
            self.ui.Sguardian_detail_comboBox.addItem(guradian_query.value(0))

        self.highest = new_id+1
        
        self.ui.Add_first_btn.clicked.connect(partial(self.add_guradian, 0))
        self.ui.Add_second_btn.clicked.connect(partial(self.add_guradian, 1))
        self.ui.Update_detail_btn.clicked.connect(self.add_stu)
  
        self.ui.p_id = 0
        self.ui.s_id = 0

    def add_stu(self):
        self.ui.StuID = self.ui.Id_detail_lineEdit.text()
        self.ui.StuName = self.ui.Name_detail_lineEdit.text()      
        self.ui.StuGender = self.ui.Gender_comboBox.currentText()   
        self.ui.StuEmail = self.ui.Email_detail_lineEdit.text()
        self.ui.StuBirth = self.ui.Birth_detail_dateEdit.date()  
        self.ui.StuPhone = self.ui.Phone_detail_lineEdit.text()
        self.ui.StuEcon = self.ui.Econtact_detail_lineEdit.text()
        self.ui.StuEphone = self.ui.Ephone_detail_lineEdit.text()
        self.ui.StuTuition = self.ui.Tuition_detail_lineEdit.text()
        self.ui.StuAddress = self.ui.Address_detail_lineEdit.text()
        self.ui.StuAddress.upper()
        self.ui.StuCity = self.ui.City_detail_lineEdit.text()
        self.ui.StuCity.upper()
        self.ui.StuState = self.ui.State_detail_ComboBox.currentText()
        self.ui.StuZip = self.ui.Zipcode_detail_lineEdit.text()
        self.ui.StuMedical = self.ui.Medical_detail_textEdit.toPlainText()

        if self.ui.Pguradian_detail_comboBox.currentText() in self.g_dict:
            self.ui.p_id = self.g_dict[self.ui.Pguradian_detail_comboBox.currentText()]
        if self.ui.Sguardian_detail_comboBox.currentText() in self.g_dict:
            self.ui.s_id = self.g_dict[self.ui.Sguardian_detail_comboBox.currentText()]

        address_query = QSqlQuery()
        address_id = 0
        address_query.exec_("select Address_id from Address order by Address_id desc")
        address_query.next()
        address_id = address_query.value(0)+1

        add_query = QSqlQuery()
        if address_query.exec_("insert into Address values(%d, '%s', '%s', '%s', %d)" % (address_id, \
           self.ui.StuAddress,self.ui.StuCity, self.ui.StuState, int(self.ui.StuZip))) and \
           add_query.exec_("insert into Student values(%d, %d, '%s', '%s', '%s', '%s', '%s', '%s'\
           , %d, %d, '%s', '%s', '%s', %f)" % \
            (int(self.ui.StuID), address_id, self.ui.StuName, self.ui.StuGender, self.ui.StuEmail, self.ui.StuBirth.toString("yyyy-MM-dd"), self.ui.StuPhone, self.ui.StuPhone, self.ui.p_id, \
            self.ui.s_id, self.ui.StuEcon, self.ui.StuEphone, self.ui.StuMedical, float(self.ui.StuTuition))):

            QtGui.QMessageBox.information(
                self.gur, 'Success', 'Update record successfully')
        else:
            print ("insert into values(%d, %d, '%s', '%s', '%s', '%s', '%s', '%s'\
           , %d, %d, '%s', '%s', '%s', %f)" % \
            (int(self.ui.StuID), address_id, self.ui.StuName, self.ui.StuGender, self.ui.StuEmail, self.ui.StuBirth.toString("yyyy-MM-dd"), self.ui.StuPhone, self.ui.StuPhone, self.ui.p_id, \
            self.ui.s_id, self.ui.StuEcon, self.ui.StuEphone, self.ui.StuMedical, float(self.ui.StuTuition)))
        
    def set_guradian(self, num):
        
        self.g_name = self.gur.ui.nameLineEdit.text()
        self.g_hphone = self.gur.ui.homePhoneLineEdit.text()
        self.g_cphone = self.gur.ui.cellPhoneLineEdit.text()
        self.g_wphone = self.gur.ui.workPhoneLineEdit.text()
        self.g_address = self.gur.ui.addressLineEdit.text()
        self.g_city = self.gur.ui.cityLineEdit.text()
        self.g_state = self.gur.ui.stateComboBox.currentText()
        self.g_zipcode = self.gur.ui.zipcodeLineEdit.text()
        self.g_email = self.gur.ui.emailLineEdit.text()

        #needs error checking

        #update
        if self.g_id != self.highest:
            update_query = QSqlQuery()
            if update_query.exec_("Update Guardian, Address Set Guardian_name = '%s',\
                                   Guardian_home_phone = '%s', Guardian_cell_phone = '%s',\
                                  Guardian_work_phone = '%s', Street = '%s',\
                                  City = '%s', State = '%s', Zipcode = %d, Guardian_email = '%s' where\
                                  Guardian_address = Address_id and Guardian_id = %d" % \
                                  (self.g_name, self.g_hphone, self.g_cphone, self.g_wphone,\
                                   self.g_address, self.g_city, self.g_state, int(self.g_zipcode),\
                                   self.g_email, int(self.g_id))):

                QtGui.QMessageBox.information(
                self.gur, 'Success', 'Update record successfully')          
                   
                #update key
                for name, id_num in self.g_dict.items():
                    if id_num == self.g_id:
                        self.g_dict[self.g_name] = self.g_dict.pop(name)
                        index_p = self.ui.Pguradian_detail_comboBox.findText(name)
                        self.ui.Pguradian_detail_comboBox.setItemText(index_p, self.g_name)
                        
                        index_s = self.ui.Sguardian_detail_comboBox.findText(name)
                        self.ui.Sguardian_detail_comboBox.setItemText(index_s, self.g_name)
                        
                        #set comobobox list
                        if num == 0:
                            self.ui.p_id = self.g_id
                            self.ui.Pguradian_detail_comboBox.setCurrentIndex(index_p)
                        else:
                            self.ui.s_id = self.g_id
                            self.ui.Sguardian_detail_comboBox.setCurrentIndex(index_s)
                        break
                
                
        else:
            add_query = QSqlQuery()
            address_query = QSqlQuery()
            address_query.exec_("select Address_id from Address order by Address_id desc")
            address_query.next()
            address_id = address_query.value(0)+1

            if address_query.exec_("insert into Address values(%d, '%s', '%s', '%s', %d)" % (address_id, \
               self.g_address, self.g_city, self.g_state, int(self.g_zipcode))) and add_query.exec_\
               ("insert into Guardian values(%d, %d, '%s', '%s', '%s', '%s', '%s')" % (self.highest, address_id,\
                self.g_name, self.g_hphone, self.g_cphone, self.g_wphone, self.g_email)):
                
                QtGui.QMessageBox.information(
                self.gur, 'Success', 'Update record successfully')

                #add key
                self.g_dict[self.g_name] = self.highest
                #set comobobox list
                self.ui.Pguradian_detail_comboBox.addItem(self.g_name)
                self.ui.Sguardian_detail_comboBox.addItem(self.g_name)

                #set which one is the highest
                if num == 0:
                    self.ui.p_id = self.highest
                    index = self.ui.Pguradian_detail_comboBox.findText(self.g_name)
                    self.ui.Pguradian_detail_comboBox.setCurrentIndex(index)
                else:
                    self.ui.s_id = self.highest
                    index = self.ui.Sguardian_detail_comboBox.findText(self.g_name)
                    self.ui.Sguardian_detail_comboBox.setCurrentIndex(index)
                
                #update id
                self.highest += 1
                
                
                
    def add_guradian(self, num):
        self.gur = add_new_guardian()
        self.gur.show()

        self.gur.ui.Submit_btn.clicked.connect(partial(self.set_guradian, num))

        if num == 0:
            #get correspoding id
            self.g_id = self.highest
            if self.ui.Pguradian_detail_comboBox.currentText() in self.g_dict:
                self.g_id = self.g_dict[self.ui.Pguradian_detail_comboBox.currentText()]
                
            guradian_query = QSqlQuery()
            address_query = QSqlQuery()

            #if record exist
            if self.highest != self.g_id:
                guradian_query.exec_("select * from Guardian where Guardian_id = %d" % self.g_id)
                guradian_query.next()
                address_query.exec_("select * from Address where Address_id = %d" % guradian_query.value(1))
                address_query.next()
                #name
                if not isinstance(guradian_query.value(2), QtCore.QPyNullVariant):
                    self.gur.ui.nameLineEdit.setText(guradian_query.value(2))
                #home phone
                if not isinstance(guradian_query.value(3), QtCore.QPyNullVariant):
                    self.gur.ui.homePhoneLineEdit.setText(guradian_query.value(3))
                #cell phone
                if not isinstance(guradian_query.value(4), QtCore.QPyNullVariant):
                    self.gur.ui.cellPhoneLineEdit.setText(guradian_query.value(4))
                #work phone
                if not isinstance(guradian_query.value(5), QtCore.QPyNullVariant):
                    self.gur.ui.workPhoneLineEdit.setText(guradian_query.value(5))
                #address
                if not isinstance(address_query.value(1), QtCore.QPyNullVariant):
                    self.gur.ui.addressLineEdit.setText(address_query.value(1))
                #city
                if not isinstance(address_query.value(2), QtCore.QPyNullVariant):
                    self.gur.ui.cityLineEdit.setText(address_query.value(2))
                #state
                if not isinstance(address_query.value(3), QtCore.QPyNullVariant):
                    index = self.gur.ui.stateComboBox.findText(address_query.value(3))
                    self.gur.ui.stateComboBox.setCurrentIndex(index)
                #zipcode
                if not isinstance(address_query.value(4), QtCore.QPyNullVariant):
                    self.gur.ui.zipcodeLineEdit.setText(str(address_query.value(4)))
                #email
                if not isinstance(guradian_query.value(6), QtCore.QPyNullVariant):
                    self.gur.ui.emailLineEdit.setText(guradian_query.value(6))
        else:
            self.g_id = self.highest
            if self.ui.Sguardian_detail_comboBox.currentText() in self.g_dict:
                self.g_id = self.g_dict[self.ui.Sguardian_detail_comboBox.currentText()]

            guradian_query = QSqlQuery()
            address_query = QSqlQuery()

            #if record exist
            if self.highest != self.g_id:
                guradian_query.exec_("select * from Guardian where Guardian_id = %d" % self.g_id)
                guradian_query.next()
                address_query.exec_("select * from Address where Address_id = %d" % guradian_query.value(1))
                address_query.next()
                #name
                if not isinstance(guradian_query.value(2), QtCore.QPyNullVariant):
                    self.gur.ui.nameLineEdit.setText(guradian_query.value(2))
                #home phone
                if not isinstance(guradian_query.value(3), QtCore.QPyNullVariant):
                    self.gur.ui.homePhoneLineEdit.setText(guradian_query.value(3))
                #cell phone
                if not isinstance(guradian_query.value(4), QtCore.QPyNullVariant):
                    self.gur.ui.cellPhoneLineEdit.setText(guradian_query.value(4))
                #work phone
                if not isinstance(guradian_query.value(5), QtCore.QPyNullVariant):
                    self.gur.ui.cellPhoneLineEdit.setText(guradian_query.value(5))
                #address
                if not isinstance(address_query.value(1), QtCore.QPyNullVariant):
                    self.gur.ui.addressLineEdit.setText(address_query.value(1))
                #city
                if not isinstance(address_query.value(2), QtCore.QPyNullVariant):
                    self.gur.ui.cityLineEdit.setText(address_query.value(2))
                #state
                if not isinstance(address_query.value(3), QtCore.QPyNullVariant):
                    index = self.gur.ui.stateComboBox.findText(address_query.value(3))
                    self.gur.ui.stateComboBox.setCurrentIndex(index)
                #zipcode
                if not isinstance(address_query.value(4), QtCore.QPyNullVariant):
                    self.gur.ui.zipcodeLineEdit.setText(str(address_query.value(4)))
                #email
                if not isinstance(guradian_query.value(6), QtCore.QPyNullVariant):
                    self.gur.ui.emailLineEdit.setText(guradian_query.value(6))
        

    def show_list(self):
        self.ui.class_list = Class_list_dialog(self.id)
        self.ui.class_list.show()
        
   
    
