import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Add_Class import Ui_Add_Class
from PyQt4.QtSql import *

class add_Class(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Add_Class()
        self.ui.setupUi(self)
        self.setup_database()

        self.location_query = QSqlQuery()
        self.location_query.exec_("SELECT DISTINCT Class_location FROM Class")
        while self.location_query.next():
            record = self.location_query.record()
            self.location = str(record.value(0))
            self.ui.Location_comboBox.addItem(self.location)

        self.ui.Submit_btn.clicked.connect(self.add_class)
        self.ui.Back_btn.clicked.connect(self.back)
        
        
    def setup_database(self):

        self.conn() #need catch exception
        self.ui.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.ui.sel_teach.setTable("Class")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        
        
    def add_class(self):
        self.name = self.ui.Name_lineEdit.text()
        self.cost = self.ui.Cost_spinBox.value()
        self.start_time = self.ui.Start_time_timeEdit.time()
        self.start_time = self.start_time.toString("HH:mm:ss")
        self.end_time = self.ui.End_time_timeEdit.time()
        self.end_time = self.end_time.toString("HH:mm:ss")
        print(self.start_time, ' ', self.end_time)
        self.date = str(self.ui.Day_comboBox.currentText())
        self.location = str(self.ui.Location_comboBox.currentText())
        self.cap = self.ui.Cap_spinBox.value()
        self.clothing = self.ui.Clothing_textEdit.toPlainText()    
        self.descirption = self.ui.Description_textEdit.toPlainText()
        
        self.start = self.ui.Start_date_dateEdit.date()
        self.start = self.start.toPyDate()
        self.end = self.ui.End_date_dateEdit.date()
        self.end = self.end.toPyDate()

        temp = "INSERT INTO Class %s VALUES( '%s','%s','%s','%s','%s','%s','%s',\
                        '%s','%s','%s','%s','%s'"
        attributes = "(Class_id, Class_name, Class_cost, Class_time, Class_end_time, Class_day, Class_location, Class_cap, Class_clothing, Class_description, Class_start_date, Class_end_date"


        self.age = self.ui.Age_spinBox.value()
        if self.age != 0:
            temp += ",'%d'" % self.age
            attributes += ', Class_age'
        self.age_limit = self.ui.Age_limit_spinBox.value()
        if self.age_limit != 0:
            temp += ",'%d'" % self.age_limit
            attributes += ', Class_age_end'
        
        attributes += ')'
        temp += ')'

        id_query =QSqlQuery()
        id_query.exec_("SELECT Class_id FROM Class ORDER BY Class_id DESC LIMIT 1")
        while id_query.next():
            record = id_query.record()
            self.id = record.value(0)
            self.id += 1
            self.id = str(self.id)
            
        else:
            results_msg = "Add this class: \n Name:'%s' \n Cost:'%s' \n Start Time:'%s' \n End Time:'%s' \n Day:'%s' \n Location:'%s' \n Student Cap:'%s' \
 \n Clothing Requirements:'%s' \n Class Descirption:'%s' \n Start Date:'%s' \n End Date:'%s' \n Age Requirement:'%s' \n Age Limit:'%s'" % (self.name, self.cost, \
                            self.start_time, self.end_time, self.date, self.location, self.cap, self.clothing, self.descirption, self.start, self.end, self.age, self.age_limit)
            reply = QtGui.QMessageBox.question(self, 'Message', 
                         results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                add_query = QSqlQuery()
                add_query.exec_(temp \
                                %(attributes, self.id, self.name, self.cost, self.start_time, self.end_time, self.date, self.location, \
                                   self.cap, self.clothing, self.descirption, self.start, self.end))
            
                sys.exit()
    

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
Current_Window = add_Class()
Current_Window.show()
sys.exit(app.exec_())
