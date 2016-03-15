import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Clothing_Requirements import Ui_Clothing_Requirements
from PyQt4.QtSql import *

class clothing_requirements(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Clothing_Requirements()
        self.ui.setupUi(self)
        self.setup_database()

        self.ui.submit.clicked.connect(self.modify_information)
        self.ui.cancel.clicked.connect(self.modify_information)

        
        
    def setup_database(self):

        
        
        self.conn() #need catch exception

        self.ui.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.ui.sel_teach.setTable("Class")

        self.id = 1

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        query = QSqlQuery()
        query.exec_("Select Class_clothing FROM Class WHERE Class_id = '%s'" % self.id)
        while query.next():
            record = query.record()
            self.ui.clothing_entry_field.setText(str(record.value(0).toString()))
        
        
    def modify_information(self):

        self.updates = self.ui.clothing_entry_field.toPlainText()
        
        update_query = QSqlQuery()
        update_query.exec_("Update Class SET Class_clothing ='%s' WHERE Class_id = '%s'"\
                           % (self.updates, self.id))
        quit()
        
        
        
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

def quit():
    sys.exit(app.exec_())
    

app = QtGui.QApplication(sys.argv)
Current_Window = clothing_requirements()
Current_Window.show()
sys.exit(app.exec_())

