import sys
from PyQt4 import QtGui, QtCore
from Search_teacher import Ui_Search_MainWindow
from PyQt4.QtSql import *
from Advsearch_teacher_Dialog import Advsearch_Dialog
from Teacher_info_Dialog import Teacher_info_dialog

class Search_teacher_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)

        
        self.conn() #need catch exception
        
       
        #TODO deal with foreign key
        self.ui.Teacher = QSqlRelationalTableModel(db = self.db)
        self.ui.Teacher.setTable("Teacher")

        
        self.ui.Teacher.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.Teacher.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.ui.Teacher.setHeaderData(7, QtCore.Qt.Horizontal, "Gender")
        self.ui.Teacher.setHeaderData(11, QtCore.Qt.Horizontal, "Date of Birth")
        self.ui.Teacher.setHeaderData(2, QtCore.Qt.Horizontal, "Home Phone")
        self.ui.Teacher.setHeaderData(3, QtCore.Qt.Horizontal, "Cell Phone")
        self.ui.Teacher.setHeaderData(4, QtCore.Qt.Horizontal, "Work Phone")
        self.ui.Teacher.setFilter('')
        self.ui.Teacher.select()
        
        

        #display window
        self.ui.Teacher_view.setModel(self.ui.Teacher)
        self.ui.Teacher_view.hideColumn(5)
        self.ui.Teacher_view.hideColumn(6)
        self.ui.Teacher_view.hideColumn(8)
        self.ui.Teacher_view.hideColumn(9)
        self.ui.Teacher_view.hideColumn(10)


        self.ui.Search_btn.clicked.connect(self.search)
        self.ui.Adv_search_btn.clicked.connect(self.advsearch_show)
        self.ui.Reset_search_btn.clicked.connect(self.reset_table)
        self.ui.Detail_btn.clicked.connect(self.detail_show)
        self.ui.Back_btn.clicked.connect(self.close)


    def Teacherinfo_update(self):
        #TODO check input validity
        #TODO Solve foreign key!!!!!!!!!!!!!!!
        
        self.detail.TeacherID = self.detail.ui.Id_detail_lineEdit.text()
        self.detail.TeacherName = self.detail.ui.Name_detail_lineEdit.text()      
        self.detail.TeacherGender = self.detail.ui.Gender_detail_lineEdit.text()   
        self.detail.TeacherEmail = self.detail.ui.Email_detail_lineEdit.text()
        self.detail.TeacherBirth = self.detail.ui.Birth_detail_dateEdit.date()  
        self.detail.TeacherPhone = self.detail.ui.Phone_detail_lineEdit.text()
        self.detail.TeacherPG = self.detail.ui.Pguradian_detail_lineEdit.text()  
        self.detail.TeacherSG = self.detail.ui.Sguardian_detail_lineEdit.text()
        self.detail.TeacherEcon = self.detail.ui.Econtact_detail_lineEdit.text()
        self.detail.TeacherEphone = self.detail.ui.Ephone_detail_lineEdit.text()
        self.detail.TeacherTuition = self.detail.ui.Tuition_detail_lineEdit.text()
        self.detail.TeacherAddress = self.detail.ui.Address_detail_lineEdit.text()
        self.detail.TeacherCity = self.detail.ui.City_detail_lineEdit.text()    
        self.detail.TeacherState = self.detail.ui.State_detail_lineEdit.text()
        self.detail.TeacherMedical = self.detail.ui.Medical_detail_textEdit.toPlainText()


        update_query = QSqlQuery()
        
        if update_query.exec_("Update Teacher, Address, Guardian Set Teacher.Teacher_name = '%s', Teacher.Teacher_sex = '%s', Teacher.Teacher_email = '%s', \
                           Teacher.Teacher_date_of_birth = '%s', Teacher.Teacher_home_phone = '%s', Teacher.Teacher_Emergency_contact = '%s', Teacher.Emergency_contact_phone = '%s', \
                           Teacher.Teacher_medical_information = '%s', Teacher.Tuition = '%s', \
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Guardian.Guardian_name = '%s'\
                           Where Teacher.Teacher_id = '%d' and Teacher.Teacher_address = Address.Address_id and Teacher.Guardian_primary = Guardian.Guardian_id"\
                           %(self.detail.TeacherName,  self.detail.TeacherGender, self.detail.TeacherEmail, self.detail.TeacherBirth.toString("yyyy-MM-dd"), self.detail.TeacherPhone,  self.detail.TeacherEcon, self.detail.TeacherEphone,\
                           self.detail.TeacherMedical, self.detail.TeacherTuition, self.detail.TeacherAddress, self.detail.TeacherCity, self.detail.TeacherState, self.detail.TeacherPG, int(self.detail.TeacherID)))\
            and update_query.exec_("Update Teacher, Guardian Set Guardian.Guardian_name = '%s '\
                                    Where Teacher.Teacher_id = '%d' and Teacher.Guardian_secondary = Guardian.Guardian_id" \
                                   %(self.detail.TeacherSG, int(self.detail.TeacherID))):
            QtGui.QMessageBox.information(
                self.detail, 'Success', 'Update record successfully')
            self.reset_table()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
    def detail_show(self):
        curIndex = self.ui.Teacher_view.currentIndex().row()
        if curIndex == -1:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please select a row')
            return curIndex
        
       
        self.detail = Teacher_info_dialog()
        
        self.detail.show()
        
        self.detail.record = self.ui.Teacher.record(curIndex)

        address = QSqlQuery()
        self.detail.Address_id = self.detail.record.field(5).value()
        address.exec_("select * from Address where Address_id = %d" % self.detail.Address_id)
        address.next()
        self.detail.record_A = address.record()
    
  
        
        #check weather the data exists in database

        #TeacherID
        if not isinstance(self.detail.record.field(0).value(), QtCore.QPyNullVariant):
            self.detail.ui.Id_detail_lineEdit.setText(str(self.detail.record.field(0).value()))
        #TeacherName
        if not isinstance(self.detail.record.field(1).value(), QtCore.QPyNullVariant):
            self.detail.ui.Name_detail_lineEdit.setText(self.detail.record.field(1).value())
        #TeacherGender
        if not isinstance(self.detail.record.field(7).value(), QtCore.QPyNullVariant):
            self.detail.ui.Gender_detail_lineEdit.setText(self.detail.record.field(7).value())
        #TeacherEmail
        if not isinstance(self.detail.record.field(6).value(), QtCore.QPyNullVariant):
            self.detail.ui.Email_detail_lineEdit.setText(self.detail.record.field(6).value())
        #need detail
        #TeacherBirth
        if not isinstance(self.detail.record.field(11).value(), QtCore.QPyNullVariant):
            self.detail.ui.Birth_detail_dateEdit.setDate(self.detail.record.field(11).value())
        #TeacherHomePhone
        if not isinstance(self.detail.record.field(2).value(), QtCore.QPyNullVariant):
            self.detail.ui.Homephone_detail_lineEdit.setText(self.detail.record.field(2).value())
        #TeacherCellPhone
        if not isinstance(self.detail.record.field(3).value(), QtCore.QPyNullVariant):
            self.detail.ui.Cellphone_detail_lineEdit.setText(self.detail.record.field(3).value())
        #TeacherWorkPhone
        if not isinstance(self.detail.record.field(4).value(), QtCore.QPyNullVariant):
            self.detail.ui.Workphone_detail_lineEdit.setText(self.detail.record.field(4).value())

        #TeacherSNN  
        if not isinstance(self.detail.record.field(8).value(), QtCore.QPyNullVariant):
            self.detail.ui.SSN_detail_lineEdit.setText(self.detail.record.field(8).value())
        #TeacherPayRate
        if not isinstance(self.detail.record.field(9).value(), QtCore.QPyNullVariant):
            self.detail.ui.Payrate_detail_lineEdit.setText(str(self.detail.record.field(9).value()))
        #Teacher address
        if not isinstance(self.detail.record_A.field(4).value(), QtCore.QPyNullVariant):
            self.detail.ui.Zipcode_detail_lineEdit.setText(str(self.detail.record_A.field(4).value()))

        if not isinstance(self.detail.record.field(1).value(), QtCore.QPyNullVariant):
            self.detail.ui.Address_detail_lineEdit.setText(self.detail.record_A.field(1).value())

        if not isinstance(self.detail.record_A.field(2).value(), QtCore.QPyNullVariant):
            self.detail.ui.City_detail_lineEdit.setText(self.detail.record_A.field(2).value())
        if not isinstance(self.detail.record_A.field(3).value(), QtCore.QPyNullVariant):
            self.detail.ui.State_detail_lineEdit.setText(self.detail.record_A.field(3).value())
        #TeacherMedical
        if not isinstance(self.detail.record.field(12).value(), QtCore.QPyNullVariant):
            self.detail.ui.Medical_detail_textEdit.setText(self.detail.record.field(12).value())
        

        self.detail.ui.Close_detail_btn.clicked.connect(self.detail.close)
        self.detail.ui.Update_detail_btn.clicked.connect(self.Teacherinfo_update)
            
    def advsearch_show(self):
        self.adv = Advsearch_Dialog()
        self.adv.show()
        self.adv.ui.Seacch_adv_btn.clicked.connect(self.advsearch_query)
        self.adv.ui.Cancel_adv_btn.clicked.connect(self.adv.close)
        
    def advsearch_query(self):
        #self.reset_table()
        self.adv.ui.Id_adv_label.hide()
        self.adv.ui.Name_adv_label.hide()
        self.adv.ui.Homephone_adv_label.hide()
        self.adv.ui.Cellphone_adv_label.hide()
        self.adv.ui.Workphone_adv_label.hide()

        
        
        Teacher_ID = self.adv.ui.ID_adv_ledit.text()
        Teacher_name = self.adv.ui.Name_adv_ledit.text()
        Teacher_homephone = self.adv.ui.Homephone_adv_ledit.text()
        Teacher_cellphone = self.adv.ui.Cellphone_adv_ledit.text()
        Teacher_workphone = self.adv.ui.Workphone_adv_ledit.text()
        whereClause = ''
        
        flag = True
        
          
        if self.adv.ui.ID_cbox.isChecked() and Teacher_ID == '':
            self.adv.ui.Id_adv_label.show()
            flag = False 
        elif Teacher_ID != '':
            whereClause += ("Teacher_id = %s"%Teacher_ID)

            
        if self.adv.ui.Name_cobx.isChecked() and Teacher_name == '':
            self.adv.ui.Name_adv_label.show()
            flag = False
        elif Teacher_name != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Name_Exact_cobx.isChecked():
                whereClause += ("Teacher_name = '%s'"%Teacher_name)
            else:
                whereClause += ("Teacher_name like '%%%s%%'"%Teacher_name)
            
        if self.adv.ui.Homephone_cbox.isChecked() and Teacher_homephone == '':
            self.adv.ui.Homephone_adv_label.show()
            flag = False
        elif Teacher_homephone != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Homephone_Exact_cbox.isChecked():
                whereClause += ("Teacher_home_phone = '%s'"%Teacher_homephone)
            else:
                whereClause += ("Teacher_home_phone like '%%%s%%'"%Teacher_homephone)
            
        if self.adv.ui.Cellphone_cbox.isChecked() and Teacher_cellphone == '':
            self.adv.ui.Cellphone_adv_label.show()
            flag = False
        elif Teacher_cellphone != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Cellphone_Exact_cbox.isChecked():
                whereClause += ("Teacher_cell_phone = '%s'" % Teacher_cellphone)
            else:
                whereClause += ("Teacher_cell_phone like '%%%s%%'" % Teacher_cellphone)
                
        if self.adv.ui.Workphone_cbox.isChecked() and Teacher_workphone == '':
            self.adv.ui.Workphone_adv_label.show()
            flag = False
        elif Teacher_workphone != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.WorkPhone_Exact_cbox.isChecked():
                whereClause += ("Teacher_work_phone = '%s'" % Teacher_workphone)
            else:
                whereClause += ("Teacher_work_phone like '%%%s%%'" % Teacher_workphone)

        self.ui.Teacher.setFilter(whereClause)

        if flag:
            self.adv.close()    
        
        
        
    def reset_table(self):
        self.ui.Teacher.setFilter('')
        
    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')          
        #get input data from user
        #refreash rows
        self.reset_table()
        input_Teacher_name = self.ui.Search_lineEdit.text()

        
        if input_Teacher_name != '':
            if self.ui.Exact_search_cbox.isChecked():
                self.ui.Teacher.setFilter("Teacher_name = '%s'" % input_Teacher_name)
            else:
                self.ui.Teacher.setFilter("Teacher_name like '%%%s%%'" % input_Teacher_name)
           
            
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

app = QtGui.QApplication(sys.argv)
window = Search_teacher_window()
window.show()
sys.exit(app.exec_())
