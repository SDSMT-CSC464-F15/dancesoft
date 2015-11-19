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
        self.time = self.ui.Time_timeEdit.time()
        self.time = self.time.toString("h:mm ap")
        self.date = str(self.ui.Day_comboBox.currentText())
        self.location = self.ui.Location_lineEdit.text()
        self.cap = self.ui.Cap_spinBox.value()
        self.clothing = self.ui.Clothing_textEdit.toPlainText()    
        self.descirption = self.ui.Description_textEdit.toPlainText()
        
        self.start = self.ui.Start_date_dateEdit.date()
        self.start = self.start.toPyDate()
        self.end = self.ui.End_date_dateEdit.date()
        self.end = self.end.toPyDate()

        self.age = self.ui.Age_spinBox.value()
        self.age_limit = self.ui.Age_limit_spinBox.value()

        id_query =QSqlQuery()
        id_query.exec_("SELECT Class_id FROM Class ORDER BY Class_id DESC LIMIT 1")
        while id_query.next():
            record = id_query.record()
            self.id = str(record.value(0))
            
        
        add_query = QSqlQuery()
        add_query.exec_("INSERT INTO Class VALUES( %s,%s,%s,%s,%s,%s,\
                        %s,%s,%s,%s,%s,%s,%s)", \
                        (self.id, self.name, self.cost, self.time, self.date, self.location, \
                           self.cap, self.clothing, self.descirption, self.start, self.end, \
                           self.age, self.age_limit))
    

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
