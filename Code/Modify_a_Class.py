import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Modify_Class import Ui_Modify_Class
from PyQt4.QtSql import *

class mod_Class(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.MC = Ui_Modify_Class()
        self.MC.setupUi(self)
        self.setup_database()

        self.class_query = QSqlQuery()
        self.class_query.exec_("Select Class_name FROM Class")
        while self.class_query.next():
            record = self.class_query.record()
            self.class_name = str(record.value(0))
            self.MC.selectClassComboBox.addItem(self.class_name)

        self.location_query = QSqlQuery()
        self.location_query.exec_("SELECT DISTINCT Class_location FROM Class")
        while self.location_query.next():
            record = self.location_query.record()
            self.location = str(record.value(0))
            self.MC.Location_comboBox.addItem(self.location)

        self.MC.Select_class_btn.clicked.connect(self.current_class)

        self.MC.Submit_btn.clicked.connect(self.modify_class)
        self.MC.Back_btn.clicked.connect(self.back)
        
        
    def setup_database(self):

        self.conn() #need catch exception
        self.MC.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.MC.sel_teach.setTable("Class")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

    def current_class(self):
        self.MC.sel_class = QSqlRelationalTableModel(db = self.db)
        self.MC.sel_class.setTable("Class")

        selected_class = str(self.MC.selectClassComboBox.currentText())
        query = QSqlQuery()
        query.exec_("SELECT * FROM Class WHERE Class_name = '%s'" % selected_Class_name)
        while query.next():
            record = query.record()
            self.Class_id = str(record.value(0))
            self.MC.Name_lineEdit.setText(str(record.value(1)))
            self.MC.Cost_spinBox.setValue(str(record.value(2)))
            self.MC.Start_time_timeEdit.setValue(str(record.value(3)))
            self.MC.End_time_timeEdit.setValue(str(record.value(4)))
            self.MC.Day_ComboBox.findText(str(record.value(5)),QtCore.Qt.MatchFixedString)
            self.MC.Location_ComboBox.findText(str(record.value(6)),QtCore.Qt.MatchFixedString)
            self.MC.Cap_spinBox.setValue(str(record.value(7)))
            self.MC.Clothing_textEdit.setText(str(record.value(8)))
            self.MC.Description_textEdit.setText(str(record.value(9)))
            self.MC.Start_date_dateEdit.setValue(str(record.value(10)))
            self.MC.End_date_dateEdit.setValue(str(record.value(11)))
            self.MC.Age_spinBox.setValue(str(record.value(12)))
            self.MC.Age_limit_spinBox.setValue(str(record.value(13)))
        
        
    def modify_class(self):
        self.name = self.MC.Name_lineEdit.text()
        self.cost = self.MC.Cost_spinBox.value()
        self.start_time = self.MC.Start_time_timeEdit.time()
        self.start_time = self.start_time.toString("HH:mm:ss")
        self.end_time = self.MC.End_time_timeEdit.time()
        self.end_time = self.end_time.toString("HH:mm:ss")
        self.date = str(self.MC.Day_comboBox.currentText())
        self.location = str(self.MC.Location_comboBox.currentText())
        self.cap = self.MC.Cap_spinBox.value()
        self.clothing = self.MC.Clothing_textEdit.toPlainText()    
        self.descirption = self.MC.Description_textEdit.toPlainText()
        self.start = self.MC.Start_date_dateEdit.date()
        self.start = self.start.toPyDate()
        self.end = self.MC.End_date_dateEdit.date()
        self.end = self.end.toPyDate()

        if self.name == '':
            QtGui.QMessageBox.warning(
                self, 'Error', "Please fill in class name" )
        else:
            temp = "Update Class SET Class_name ='%s', Class_cost ='%s', Class_time ='%s',\
                   Class_end_time ='%s', Class_day ='%s', Class_location ='%s', \
                   Class_cap='%s', Class_clothing='%s', Class_description='%s', \
                   Class_start_date='%s', Class_end_date='%s'" 
                


            self.age = self.ui.Age_spinBox.value()
            if self.age != 0:
                temp += ", Class_age='%s'" % self.age
            self.age_limit = self.ui.Age_limit_spinBox.value()
            if self.age_limit != 0:
                temp += ", Class_age_end='%s'" % self.age_limit
                
            else:
                results_msg = "Pending Updates \n Name:'%s' \n Cost:'%s' \n Start Time:'%s' \n End Time:'%s' \n Day:'%s' \n Location:'%s' \n Student Cap:'%s' \
     \n Clothing Requirements:'%s' \n Class Descirption:'%s' \n Start Date:'%s' \n End Date:'%s' \n Age Requirement:'%s' \n Age Limit:'%s'" % (self.name, self.cost, \
                                self.start_time, self.end_time, self.date, self.location, self.cap, self.clothing, self.descirption, self.start, self.end, self.age, self.age_limit)
                reply = QtGui.QMessageBox.question(self, 'Message', 
                             results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.Update_query = QSqlQuery()
                    self.Update_query.exec_(temp \
                                    %(self.name, self.cost, self.start_time, self.end_time, self.date, self.location, \
                                       self.cap, self.clothing, self.descirption, self.start, self.end))
    

    def back(self):
        sys.exit()
        
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = mod_Class()
Current_Window.show()
sys.exit(app.exec_())
