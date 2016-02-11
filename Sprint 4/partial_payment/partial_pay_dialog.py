import sys
from PyQt4 import QtGui
from partial_pay import Ui_Partial_pay
from PyQt4.QtSql import *

class partial_pay_dialog(QtGui.QDialog):
    def __init__(self, id = -1):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Partial_pay()
        self.ui.setupUi(self)
        
        self.conn()


    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
4
app = QtGui.QApplication(sys.argv)
window = partial_pay_dialog()
window.show()
sys.exit(app.exec_())
