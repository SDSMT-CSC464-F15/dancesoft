import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_add_reg import Ui_Stu_reg_dialog
from Class_list_dialog import Class_list_dialog
from PyQt4.QtSql import *
from functools import partial
from modify_new_guardian import add_new_guardian
import re



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

        index = self.ui.State_detail_ComboBox.findText("South Dakota")
        self.ui.State_detail_ComboBox.setCurrentIndex(index)

        
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
        #can not be empty
        self.ui.StuName = self.ui.Name_detail_lineEdit.text()      
        self.ui.StuGender = self.ui.Gender_comboBox.currentText()
        #can not be empty
        self.ui.StuEmail = self.ui.Email_detail_lineEdit.text()
        self.ui.StuBirth = self.ui.Birth_detail_dateEdit.date()
        #can not be empty
        self.ui.StuPhone = self.ui.Phone_detail_lineEdit.text()
        self.ui.StuCphone = self.ui.Cphone_detail_lineEdit.text()
        self.ui.StuEcon = self.ui.Econtact_detail_lineEdit.text()
        self.ui.StuEphone = self.ui.Ephone_detail_lineEdit.text()
        #can not be empty
        self.ui.StuAddress = self.ui.Address_detail_lineEdit.text()
        self.ui.StuAddress.upper()
        #can not be empty
        self.ui.StuCity = self.ui.City_detail_lineEdit.text()
        self.ui.StuCity.upper()
        #can not be empty
        self.ui.StuState = self.ui.State_detail_ComboBox.currentText()
        #can not be empty
        self.ui.StuZip = self.ui.Zipcode_detail_lineEdit.text()
        self.ui.StuMedical = self.ui.Medical_detail_textEdit.toPlainText()


        #needs error checking
        #if name empty
        if self.ui.StuName == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "student name cannot be empty!" )
            return

        #email
        if self.ui.StuEmail != "" and \
        re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', self.ui.StuEmail ) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid email address!" )
            return
        
        #check if the home phone is valid
        if self.ui.StuPhone == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "home phone cannot be empty!" )
            return
        elif self.ui.StuPhone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.ui.StuPhone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid home phone number in XXX-XXX-XXXX format!")
            return

        #check if the cell phone is valid
        if self.ui.StuCphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.ui.StuCphone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid cell phone number in XXX-XXX-XXXX format!")
            return

        #check emer phone is valid
        if self.ui.StuEphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.ui.StuEphone) == None:
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter an valid emergency phone number in XXX-XXX-XXXX format!")
            return

        #check address
        if self.ui.StuAddress == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "Adress cannot be empty!")
            return
        #check city
        if self.ui.StuCity == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "City cannot be empty!")
            return
        #ckeck zipcode
        if self.ui.StuZip == "":
            QtGui.QMessageBox.warning(
                    self, 'Error', "Zipcode cannot be empty!")
            return 
        elif self.ui.StuZip != "" and not self.ui.StuZip.isdigit():
            QtGui.QMessageBox.warning(
                    self, 'Error', "please enter a valid zipcode!")
            return 
        

        

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
           , %d, %d, '%s', '%s', '%s', 0.0)" % \
            (int(self.ui.StuID), address_id, self.ui.StuName, self.ui.StuGender, self.ui.StuEmail, self.ui.StuBirth.toString("yyyy-MM-dd"), self.ui.StuPhone, self.ui.StuCphone, self.ui.p_id, \
            self.ui.s_id, self.ui.StuEcon, self.ui.StuEphone, self.ui.StuMedical)):

            QtGui.QMessageBox.information(
                self, 'Success', 'Update record successfully')
            self.ui.Id_detail_lineEdit.setText(str(int(self.ui.StuID)+1))
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
        
    def set_guradian(self, num):   
        self.g_name = self.gur.ui.nameLineEdit.text()
        self.g_hphone = self.gur.ui.homePhoneLineEdit.text()
        self.g_cphone = self.gur.ui.cellPhoneLineEdit.text()
        self.g_wphone = self.gur.ui.workPhoneLineEdit.text()
        self.g_address = self.gur.ui.addressLineEdit.text()
        self.g_address = self.g_address.upper()  
        self.g_city = self.gur.ui.cityLineEdit.text()
        self.g_city = self.g_city.upper()  
        self.g_state = self.gur.ui.stateComboBox.currentText()
        self.g_zipcode = self.gur.ui.zipcodeLineEdit.text()
        self.g_email = self.gur.ui.emailLineEdit.text()
        

        #needs error checking
        if self.g_name == "":
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "student name cannot be empty!" )
            return
        
        #check if the home phone is valid
        if self.g_hphone == "":
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "home phone cannot be empty!" )
            return
        elif self.g_hphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.g_hphone) == None:
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "please enter a valid home phone number in XXX-XXX-XXXX format!")
            return

        #check if the cell phone is valid
        if self.g_cphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.g_cphone) == None:
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "please enter a valid cell phone number!")
            return

        #check work phone is valid
        if self.g_wphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.g_wphone) == None:
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "please enter a valid work phone number!")
            return

        #check address
        if self.g_address == "":
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "Adress cannot be empty!")
            return
        #check city
        if self.g_city == "":
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "City cannot be empty!")
            return
        #ckeck zipcode
        if self.g_zipcode == "":
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "Zipcode cannot be empty!")
            return 
        elif self.g_zipcode != "" and not self.g_zipcode.isdigit():
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "please enter a valid zipcode!")
            return 
        #email
        if self.g_email != "" and \
        re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', self.g_email ) == None:
            QtGui.QMessageBox.warning(
                    self.gur, 'Error', "please enter a valid email address!" )
            return


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
                QtGui.QMessageBox.warning(
                self.gur, 'Error', 'Update record unsuccessfully')

                
                
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
            else:
                QtGui.QMessageBox.warning(
                self.gur, 'Error', 'Update record unsuccessfully')
                
                
                
    def add_guradian(self, num):
        self.gur = add_new_guardian()
        self.gur.show()

        self.gur.ui.Submit_btn.clicked.connect(partial(self.set_guradian, num))

        index = self.gur.ui.stateComboBox.findText("South Dakota")
        self.gur.ui.stateComboBox.setCurrentIndex(index)

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
        
   
    
