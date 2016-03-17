import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Class_list import Ui_Class_list_Dialog
from PyQt4.QtSql import *
from functools import partial


class Class_list_dialog(QtGui.QDialog):
    def __init__(self, ID = 1):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Class_list_Dialog()
        self.ui.setupUi(self)
        self.conn()
        class_query = QSqlQuery()
        
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()


app = QtGui.QApplication(sys.argv)
window = Class_list_dialog()
window.show()
sys.exit(app.exec_())
