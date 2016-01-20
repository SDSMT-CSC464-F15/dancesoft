import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from teacher_history import Ui_teacher_history

class teacher_history_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_teacher_history()
        self.ui.setupUi(self)
        self.conn()
        History_query = QSqlQuery()
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
    
app = QtGui.QApplication(sys.argv)
window = teacher_history_window()
window.show()
sys.exit(app.exec_())
