import sys
from PyQt4 import QtGui, QtCore
from Search_class import Ui_Search_MainWindow
from PyQt4.QtSql import *
from Advsearch_class_Dialog import Advsearch_Dialog
from Class_info_Dialog import Class_info_dialog

class Search_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)

        
        self.conn() #need catch exception
        
       
        #TODO deal with foreign key
        self.ui.Class = QSqlRelationalTableModel(db = self.db)
        self.ui.Class.setTable("Class")
        
        self.ui.Class.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.Class.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.ui.Class.setHeaderData(2, QtCore.Qt.Horizontal, "Cost")
        self.ui.Class.setHeaderData(3, QtCore.Qt.Horizontal, "Start Time")
        self.ui.Class.setHeaderData(4, QtCore.Qt.Horizontal, "End Time")
        self.ui.Class.setHeaderData(6, QtCore.Qt.Horizontal, "Location")
        self.ui.Class.setHeaderData(7, QtCore.Qt.Horizontal, "Capacity")
        self.ui.Class.setFilter('')
        self.ui.Class.select()
        
        

        #display window
        self.ui.Class_view.setModel(self.ui.Class)
        self.ui.Class_view.hideColumn(5)
        self.ui.Class_view.hideColumn(8)
        self.ui.Class_view.hideColumn(9)
        self.ui.Class_view.hideColumn(10)
        self.ui.Class_view.hideColumn(11)
        self.ui.Class_view.hideColumn(12)
        self.ui.Class_view.hideColumn(13)


        self.ui.Search_btn.clicked.connect(self.search)
        self.ui.Adv_search_btn.clicked.connect(self.advsearch_show)
        self.ui.Reset_search_btn.clicked.connect(self.reset_table)
        self.ui.Detail_btn.clicked.connect(self.detail_show)
        self.ui.Back_btn.clicked.connect(self.close)


    def Classinfo_update(self):
        #TODO check input validity
        #TODO Solve foreign key!!!!!!!!!!!!!!!
        
        self.detail.ClassID = self.detail.ui.Id_detail_lineEdit.text()
        self.detail.ClassName = self.detail.ui.Name_detail_lineEdit.text()      
        self.detail.ClassGender = self.detail.ui.Gender_detail_lineEdit.text()   
        self.detail.ClassEmail = self.detail.ui.Email_detail_lineEdit.text()
        self.detail.ClassBirth = self.detail.ui.Birth_detail_dateEdit.date()  
        self.detail.ClassPhone = self.detail.ui.Phone_detail_lineEdit.text()
        self.detail.ClassPG = self.detail.ui.Pguradian_detail_lineEdit.text()  
        self.detail.ClassSG = self.detail.ui.Sguardian_detail_lineEdit.text()
        self.detail.ClassEcon = self.detail.ui.Econtact_detail_lineEdit.text()
        self.detail.ClassEphone = self.detail.ui.Ephone_detail_lineEdit.text()
        self.detail.ClassTuition = self.detail.ui.Tuition_detail_lineEdit.text()
        self.detail.ClassAddress = self.detail.ui.Address_detail_lineEdit.text()
        self.detail.ClassCity = self.detail.ui.City_detail_lineEdit.text()    
        self.detail.ClassState = self.detail.ui.State_detail_lineEdit.text()
        self.detail.ClassMedical = self.detail.ui.Medical_detail_textEdit.toPlainText()


        update_query = QSqlQuery()

        '''
        if update_query.exec_("Update Class, Address, Guardian Set Class.Class_name = '%s', Class.Class_sex = '%s', Class.Class_email = '%s', \
                           Class.Class_date_of_birth = '%s', Class.Class_home_phone = '%s', Class.Class_Emergency_contact = '%s', Class.Emergency_contact_phone = '%s', \
                           Class.Class_medical_information = '%s', Class.Tuition = '%s', \
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Guardian.Guardian_name = '%s'\
                           Where Class.Class_id = '%d' and Class.Class_address = Address.Address_id and Class.Guardian_primary = Guardian.Guardian_id"\
                           %(self.detail.ClassName,  self.detail.ClassGender, self.detail.ClassEmail, self.detail.ClassBirth.toString("yyyy-MM-dd"), self.detail.ClassPhone,  self.detail.ClassEcon, self.detail.ClassEphone,\
                           self.detail.ClassMedical, self.detail.ClassTuition, self.detail.ClassAddress, self.detail.ClassCity, self.detail.ClassState, self.detail.ClassPG, int(self.detail.ClassID)))\
            and update_query.exec_("Update Class, Guardian Set Guardian.Guardian_name = '%s '\
                                    Where Class.Class_id = '%d' and Class.Guardian_secondary = Guardian.Guardian_id" \
                                   %(self.detail.ClassSG, int(self.detail.ClassID))):
            QtGui.QMessageBox.information(
                self.detail, 'Success', 'Update record successfully')
            self.reset_table()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        '''
        
    def detail_show(self):
        curIndex = self.ui.Class_view.currentIndex().row()
        if curIndex == -1:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Please select a row')
            return curIndex
        
       
        self.detail = Class_info_dialog()
        self.detail.show()
        
        self.detail.record = self.ui.Class.record(curIndex)

        #check weather the data exists in database

        #ClassID
        if not isinstance(self.detail.record.field(0).value(), QtCore.QPyNullVariant):
            self.detail.ui.Id_detail_lineEdit.setText(str(self.detail.record.field(0).value()))
        #ClassName
        if not isinstance(self.detail.record.field(1).value(), QtCore.QPyNullVariant):
            self.detail.ui.Name_detail_lineEdit.setText(self.detail.record.field(1).value())
        #ClassCost
        if not isinstance(self.detail.record.field(2).value(), QtCore.QPyNullVariant):
            self.detail.ui.Cost_detail_lineEdit.setText(str(self.detail.record.field(2).value()))
            
        #ClassTimeStart
        if not isinstance(self.detail.record.field(3).value(), QtCore.QPyNullVariant):
            self.detail.ui.Time_start_detail_timeEdit.setTime(self.detail.record.field(3).value())
        #need detail
            
        #ClassTimeEnd
        if not isinstance(self.detail.record.field(4).value(), QtCore.QPyNullVariant):
            self.detail.ui.Time_end_detail_timeEdit.setTime(self.detail.record.field(4).value())
            
        #ClassDay
        if not isinstance(self.detail.record.field(5).value(), QtCore.QPyNullVariant):
            self.detail.ui.Day_detail_lineEdit.setText(self.detail.record.field(5).value())
            
        #ClassLocation
        if not isinstance(self.detail.record.field(6).value(), QtCore.QPyNullVariant):
            self.detail.ui.Location_detail_lineEdit.setText(self.detail.record.field(6).value())
            
        #ClassCapacity
        if not isinstance(self.detail.record.field(7).value(), QtCore.QPyNullVariant):
            self.detail.ui.Capacity_detail_lineEdit.setText(str(self.detail.record.field(7).value()))

        #ClassClothing    
        if not isinstance(self.detail.record.field(8).value(), QtCore.QPyNullVariant):
            self.detail.ui.Clothing_detail_lineEdit.setText(self.detail.record.field(8).value())
            
        #ClassDateStart
        if not isinstance(self.detail.record.field(10).value(), QtCore.QPyNullVariant):
            self.detail.ui.Date_start_detail_dateEdit.setDate(self.detail.record.field(10).value())
        #ClassDateEnd
        if not isinstance(self.detail.record.field(11).value(), QtCore.QPyNullVariant):
            self.detail.ui.Date_end_detail_dateEdit.setDate(self.detail.record.field(11).value())

        #ClassAgeStart
        if not isinstance(self.detail.record.field(12).value(), QtCore.QPyNullVariant):
            self.detail.ui.Age_start_detail_lineEdit.setText(str(self.detail.record.field(12).value()))
        #ClassAgeEnd
        if not isinstance(self.detail.record.field(13).value(), QtCore.QPyNullVariant):
            self.detail.ui.Age_end_detail_lineEdit.setText(str(self.detail.record.field(13).value()))
        #ClassDescription
        if not isinstance(self.detail.record.field(9).value(), QtCore.QPyNullVariant):
            self.detail.ui.Description_detail_textEdit.setText(self.detail.record.field(9).value())

        self.detail.ui.Close_detail_btn.clicked.connect(self.detail.close)
        self.detail.ui.Update_detail_btn.clicked.connect(self.Classinfo_update)
            
    def advsearch_show(self):
        self.adv = Advsearch_Dialog()
        self.adv.show()
        self.adv.ui.Seacch_adv_btn.clicked.connect(self.advsearch_query)
        self.adv.ui.Cancel_adv_btn.clicked.connect(self.adv.close)
        
    def advsearch_query(self):
        #self.reset_table()
        self.adv.ui.Id_adv_label.hide()
        self.adv.ui.Name_adv_label.hide()
        self.adv.ui.Cost_adv_label.hide()
        self.adv.ui.Location_adv_label.hide()
        
        Class_ID = self.adv.ui.ID_adv_ledit.text()
        Class_name = self.adv.ui.Name_adv_ledit.text()
        Class_cost_start = self.adv.ui.Cost_start_adv_ledit.text()
        Class_cost_end = self.adv.ui.Cost_end_adv_ledit.text()
        Class_location= self.adv.ui.Location_adv_ledit.text()
        Class_time_start = self.adv.ui.Start_timeEdit.time()
        Class_time_end = self.adv.ui.End_timeEdit.time()
        
        whereClause = ''
        
        flag = True
        
          
        if self.adv.ui.ID_cbox.isChecked() and Class_ID == '':
            self.adv.ui.Id_adv_label.show()
            flag = False 
        elif Class_ID != '':
            if self.adv.ui.ID_Exact_cbox.isChecked():
                whereClause += ("Class_id = %s"%Class_ID)
            else:
                whereClause += ("Class_id like %%%s%%"%Class_ID)
            
        if self.adv.ui.Name_cobx.isChecked() and Class_name == '':
            self.adv.ui.Name_adv_label.show()
            flag = False
        elif Class_name != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Name_Exact_cobx.isChecked():
                whereClause += ("Class_name = '%s'"%Class_name)
            else:
                whereClause += ("Class_name like '%%%s%%'"%Class_name)
            
        if self.adv.ui.Cost_cbox.isChecked() and (Class_cost_start == '' or Class_cost_end == ''):
            self.adv.ui.Cost_adv_label.show()
            flag = False
        elif Class_cost_start != '' and Class_cost_end != '':
            if whereClause != '':
                whereClause += ' and '
            whereClause += ("Class_cost between %s and %s"% (Class_cost_start, Class_cost_end))
            
        if self.adv.ui.Location_cbox.isChecked() and Class_location == '':
            self.adv.ui.Location_adv_label.show()
            flag = False
        elif Class_location != '':
            if whereClause != '':
                whereClause += ' and '
            if self.adv.ui.Location_Exact_cbox.isChecked():
                whereClause += ("Class_location = '%s'" % Class_location)
            else:
                whereClause += ("Class_location like '%%%s%%'" % Class_location)

        if not self.adv.ui.Time_cbox.isChecked():
            flag = False
        else:
            if whereClause != '':
                whereClause += ' and '
            whereClause += ("Class_time >= '%s' and Class_end_time <= '%s'"% (Class_time_start.toString(), Class_time_end.toString()))

        self.ui.Class.setFilter(whereClause)
        if flag:
            self.adv.close()    
        
        
        
    def reset_table(self):
        self.ui.Class.setFilter('')
        
    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')          
        #get input data from user
        #refreash rows
        self.reset_table()
        input_Class_name = self.ui.Search_lineEdit.text()

        
        if input_Class_name != '':
            if self.ui.Exact_search_cbox.isChecked():
                self.ui.Class.setFilter("Class_name = '%s'" % input_Class_name)
            else:
                self.ui.Class.setFilter("Class_name like '%%%s%%'" % input_Class_name)
           
            
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
window = Search_window()
window.show()
sys.exit(app.exec_())
