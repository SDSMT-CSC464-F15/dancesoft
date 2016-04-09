import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QAbstractItemView
from Search import Ui_Search_MainWindow
from PyQt4.QtSql import *
from Advsearch_Dialog import Advsearch_Dialog
from Stu_info_Dialog import Stu_info_dialog
import re



class Search_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)

        
        self.conn() #need catch exception
        
             
        #TODO deal with foreign key
        self.ui.student = QSqlRelationalTableModel(db = self.db)
        self.ui.student.setTable("Student")
    
        self.ui.student.setRelation(8, QSqlRelation("Guardian", "Guardian_id", "Guardian_name"))
        self.ui.student.setRelation(9, QSqlRelation("Guardian", "Guardian_id", "Guardian_name"))

        
        self.ui.student.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.student.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
        self.ui.student.setHeaderData(3, QtCore.Qt.Horizontal, "Gender")
        self.ui.student.setHeaderData(5, QtCore.Qt.Horizontal, "Date of Birth")
        self.ui.student.setHeaderData(6, QtCore.Qt.Horizontal, "Phone")
        self.ui.student.setHeaderData(8, QtCore.Qt.Horizontal, "Primary Guardian")
        self.ui.student.setFilter('')
        self.ui.student.select()
        
        

        #display window
        self.ui.Student_view.setModel(self.ui.student)      
        self.ui.Student_view.hideColumn(1)
        self.ui.Student_view.hideColumn(4)
        self.ui.Student_view.hideColumn(7)
        self.ui.Student_view.hideColumn(9)
        self.ui.Student_view.hideColumn(10)
        self.ui.Student_view.hideColumn(11)
        self.ui.Student_view.hideColumn(12)
        self.ui.Student_view.hideColumn(13)
        self.ui.Student_view.setEditTriggers(QAbstractItemView.NoEditTriggers)


        self.ui.Search_btn.clicked.connect(self.search)
        self.ui.Adv_search_btn.clicked.connect(self.advsearch_show)
        self.ui.Reset_search_btn.clicked.connect(self.reset_table)
        self.ui.Detail_btn.clicked.connect(self.detail_show)
        self.ui.Back_btn.clicked.connect(self.close)

        self.ui.Student_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.Student_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        


    def stuinfo_update(self):
        #TODO check input validity
        
        self.detail.StuID = self.detail.ui.Id_detail_lineEdit.text()
        self.detail.StuName = self.detail.ui.Name_detail_lineEdit.text()      
        self.detail.StuGender = self.detail.ui.Gender_comboBox.currentText()   
        self.detail.StuEmail = self.detail.ui.Email_detail_lineEdit.text()
        self.detail.StuBirth = self.detail.ui.Birth_detail_dateEdit.date()
        self.detail.StuBirth = self.detail.StuBirth.toPyDate()
        self.detail.StuPhone = self.detail.ui.Phone_detail_lineEdit.text()
        self.detail.StuPG = self.detail.ui.Pguradian_detail_lineEdit.text()  
        self.detail.StuSG = self.detail.ui.Sguardian_detail_lineEdit.text()
        self.detail.StuEcon = self.detail.ui.Econtact_detail_lineEdit.text()
        self.detail.StuEphone = self.detail.ui.Ephone_detail_lineEdit.text()
        self.detail.StuTuition = self.detail.ui.Tuition_detail_lineEdit.text()
        self.detail.StuAddress = self.detail.ui.Address_detail_lineEdit.text()
        self.detail.StuAddress = self.detail.StuAddress.upper()
        self.detail.StuCity = self.detail.ui.City_detail_lineEdit.text()
        self.detail.StuCity = self.detail.StuCity.upper()
        self.detail.StuState = self.detail.ui.State_detail_ComboBox.currentText()
        self.detail.StuZip = self.detail.ui.Zipcode_detail_lineEdit.text()
        self.detail.StuMedical = self.detail.ui.Medical_detail_textEdit.toPlainText()

        #check is name empty
        if self.detail.StuName == "":
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "student name cannot be empty!" )
            return    
        #check is email empty
        if self.detail.StuEmail == "":
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "email cannot be empty!" )
            return
        elif self.detail.StuEmail != "" and \
        re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', self.detail.StuEmail) == None:
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "please enter a valid email address!" )
            return
        
        #check if the phone is valid
        if self.detail.StuPhone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.detail.StuPhone) == None:
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "please enter a valid phone number!")
            return
        
        #check if eme phone is valid
        if self.detail.StuEphone != "" and re.match('^[2-9]\d{2}-\d{3}-\d{4}$', self.detail.StuEphone) == None:
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "please enter a valid phone number!")
            return


        #check if zipcode is valid 
        if self.detail.StuZip != "" and not self.detail.StuZip.isdigit():
            QtGui.QMessageBox.warning(
                    self.detail, 'Error', "please enter a valid zipcode!")
            return



        update_query = QSqlQuery()
        
        if update_query.exec_("Update Student, Address, Guardian Set Student.Student_name = '%s', Student.Student_sex = '%s', Student.Student_email = '%s', \
                           Student.Student_date_of_birth = '%s', Student.Student_home_phone = '%s', Student.Student_Emergency_contact = '%s', Student.Emergency_contact_phone = '%s', \
                           Student.Student_medical_information = '%s', Student.Tuition = '%s', \
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Address.Zipcode = '%d', Guardian.Guardian_name = '%s'\
                           Where Student.Student_id = '%d' and Student.Student_address = Address.Address_id and Student.Guardian_primary = Guardian.Guardian_id"\
                           %(self.detail.StuName,  self.detail.StuGender, self.detail.StuEmail, self.detail.StuBirth, self.detail.StuPhone,  self.detail.StuEcon, self.detail.StuEphone,\
                           self.detail.StuMedical, self.detail.StuTuition, self.detail.StuAddress, self.detail.StuCity, self.detail.StuState, int(self.detail.StuZip), self.detail.StuPG, int(self.detail.StuID)))\
            and update_query.exec_("Update Student, Guardian Set Guardian.Guardian_name = '%s '\
                                    Where Student.Student_id = '%d' and Student.Guardian_secondary = Guardian.Guardian_id" \
                                   %(self.detail.StuSG, int(self.detail.StuID))):
            QtGui.QMessageBox.information(
                self.detail, 'Success', 'Update record successfully')
            self.reset_table()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
    def detail_show(self):
        curIndex = self.ui.Student_view.currentIndex().row()
        if curIndex == -1:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please select a row')
            return curIndex
        
       
        self.detail = Stu_info_dialog()
        self.detail.show()
        
        self.detail.record = self.ui.student.record(curIndex)

        address = QSqlQuery()
        self.detail.Address_id = self.detail.record.field(1).value()
        address.exec_("select * from Address where Address_id = %d" % self.detail.Address_id)
        address.next()
        self.detail.record_A = address.record()
        self.detail.ui.Id_detail_lineEdit.setDisabled(True)
  
        
        #check weather the data exists in database

        #StuID
        if not isinstance(self.detail.record.field(0).value(), QtCore.QPyNullVariant):
            self.detail.ui.Id_detail_lineEdit.setText(str(self.detail.record.field(0).value()))
        #StuName
        if not isinstance(self.detail.record.field(2).value(), QtCore.QPyNullVariant):
            self.detail.ui.Name_detail_lineEdit.setText(self.detail.record.field(2).value())
        #StuGender
        if not isinstance(self.detail.record.field(3).value(), QtCore.QPyNullVariant):
            self.detail.ui.Gender_comboBox.addItem("Male")
            self.detail.ui.Gender_comboBox.addItem("Female")
            if self.detail.record.field(3).value() == "Male":
                self.detail.ui.Gender_comboBox.setCurrentIndex(0)
            else:
                self.detail.ui.Gender_comboBox.setCurrentIndex(1)
                
        #StuEmail
        if not isinstance(self.detail.record.field(4).value(), QtCore.QPyNullVariant):
            self.detail.ui.Email_detail_lineEdit.setText(self.detail.record.field(4).value())
        #need detail
        #StuBirth
        if not isinstance(self.detail.record.field(6).value(), QtCore.QPyNullVariant):
            self.detail.ui.Birth_detail_dateEdit.setDate(self.detail.record.field(5).value())
        #StuPhone
        if not isinstance(self.detail.record.field(7).value(), QtCore.QPyNullVariant):
            self.detail.ui.Phone_detail_lineEdit.setText(self.detail.record.field(6).value())
        #StuPG
        if not isinstance(self.detail.record.field(8).value(), QtCore.QPyNullVariant):
            self.detail.ui.Pguradian_detail_lineEdit.setText(self.detail.record.field(8).value())
        #StuSG
        if not isinstance(self.detail.record.field(9).value(), QtCore.QPyNullVariant):
            self.detail.ui.Sguardian_detail_lineEdit.setText(self.detail.record.field(9).value())

        #StuEcon     
        if not isinstance(self.detail.record.field(10).value(), QtCore.QPyNullVariant):
            self.detail.ui.Econtact_detail_lineEdit.setText(self.detail.record.field(10).value())
        #StuEphone
        if not isinstance(self.detail.record.field(11).value(), QtCore.QPyNullVariant):
            self.detail.ui.Ephone_detail_lineEdit.setText(self.detail.record.field(11).value())
        #StuTuition
        if not isinstance(self.detail.record.field(13).value(), QtCore.QPyNullVariant):
            self.detail.ui.Tuition_detail_lineEdit.setText(str(self.detail.record.field(13).value()))
        #medical
        if not isinstance(self.detail.record.field(12).value(), QtCore.QPyNullVariant):
            self.detail.ui.Medical_detail_textEdit.setText(self.detail.record.field(12).value())

        #address
        if not isinstance(self.detail.record.field(1).value(), QtCore.QPyNullVariant):
            self.detail.ui.Address_detail_lineEdit.setText(self.detail.record_A.field(1).value())

        if not isinstance(self.detail.record_A.field(2).value(), QtCore.QPyNullVariant):
            self.detail.ui.City_detail_lineEdit.setText(self.detail.record_A.field(2).value())
        if not isinstance(self.detail.record_A.field(3).value(), QtCore.QPyNullVariant):
            index = self.detail.ui.State_detail_ComboBox.findText(self.detail.record_A.field(3).value())
            self.detail.ui.State_detail_ComboBox.setCurrentIndex(index)

        if not isinstance(self.detail.record_A.field(4).value(), QtCore.QPyNullVariant):
            self.detail.ui.Zipcode_detail_lineEdit.setText(str(self.detail.record_A.field(4).value()))
            
        self.detail.ui.Close_detail_btn.clicked.connect(self.detail.close)
        self.detail.ui.Update_detail_btn.clicked.connect(self.stuinfo_update)
            
    def advsearch_show(self):
        self.adv = Advsearch_Dialog()
        self.adv.show()
        self.adv.ui.Seacch_adv_btn.clicked.connect(self.advsearch_query)
        self.adv.ui.Cancel_adv_btn.clicked.connect(self.adv.close)
        
    def advsearch_query(self):
        #self.reset_table()
        self.adv.ui.Id_adv_label.hide()
        self.adv.ui.Name_adv_label.hide()
        self.adv.ui.Phone_adv_label.hide()
        self.adv.ui.Guardian_adv_label.hide()
        
        Stu_ID = self.adv.ui.ID_adv_ledit.text()
        Stu_name = self.adv.ui.Name_adv_ledit.text()
        Stu_phone = self.adv.ui.Phone_adv_ledit.text()
        Stu_guardian = self.adv.ui.Guardian_adv_ledit.text()

        Stu_datebirth = self.adv.ui.Start_dateedit.date()
        Stu_end_datebirth = self.adv.ui.End_dateedit.date()

        whereClause = ''
        
        flag = True
        
          
        if self.adv.ui.ID_cbox.isChecked() and Stu_ID == '':
            self.adv.ui.Id_adv_label.show()
            flag = False 
        elif Stu_ID != '':
            if Stu_ID.isdigit():
                whereClause += ("Student_id = %s"%Stu_ID)
            else:
                QtGui.QMessageBox.warning(
                    self.adv, 'Error', "please enter valid id!" )
                return
            
            
        if self.adv.ui.Name_cobx.isChecked() and Stu_name == '':
            self.adv.ui.Name_adv_label.show()
            flag = False
        elif Stu_name != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Name_Exact_cobx.isChecked():
                whereClause += ("Student_name = '%s'"%Stu_name)
            else:
                whereClause += ("Student_name like '%%%s%%'"%Stu_name)
            
        if self.adv.ui.Phone_cbox.isChecked() and Stu_phone == '':
            self.adv.ui.Phone_adv_label.show()
            flag = False
        elif Stu_phone != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Phone_Exact_cbox.isChecked():
                whereClause += ("Student_home_phone = '%s'"%Stu_phone)
            else:
                whereClause += ("Student_home_phone like '%%%s%%'"%Stu_phone)
            
        if self.adv.ui.Guardian_cbox.isChecked() and Stu_guardian == '':
            self.adv.ui.Guardian_adv_label.show()
            flag = False
        elif Stu_guardian != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Guardian_Exact_cbox.isChecked():
                whereClause += ("relTblAl_8.Guardian_name = '%s'" % Stu_guardian)
            else:
                whereClause += ("relTblAl_8.Guardian_name like '%%%s%%'" % Stu_guardian)



        if self.adv.ui.Birth_cbox.isChecked():
            if whereClause != '':
                whereClause += ' and '
            whereClause += ("Student_date_of_birth >= '%s' and Student_date_of_birth <= '%s'"% \
                            (Stu_datebirth.toString("yyyy-MM-dd"), Stu_end_datebirth.toString("yyyy-MM-dd")))


        self.ui.student.setFilter(whereClause)

        if flag:
            self.adv.close()    
        
        
        
    def reset_table(self):
        self.ui.student.setFilter('')
        
    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')          
        #get input data from user
        #refreash rows
        self.reset_table()
        input_student_name = self.ui.Search_lineEdit.text()

        
        if input_student_name != '':
            if self.ui.Exact_search_cbox.isChecked():
                self.ui.student.setFilter("Student_name = '%s'" % input_student_name)
            else:
                self.ui.student.setFilter("Student_name like '%%%s%%'" % input_student_name)
           
            
        if self.ui.Search_lineEdit.text() == '':
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please input keyword you want to search by') 

        
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
    
