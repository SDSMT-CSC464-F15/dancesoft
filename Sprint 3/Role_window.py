import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from Role import Ui_Role_window


class Role_window(QtGui.QMainWindow):
    def __init__(self, Id = 1):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Role_window()
        self.ui.setupUi(self)
        self.conn() #need cathch exeption
        Class_query = QSqlQuery()
        Class_query.exec_("Select C.Class_name from Teacher_Class as T, Class as C where \
                           T.Class_id = C.Class_id and T.Teacher_id = '%s'" % Id)

         
        self.ui.Role_listView.setModel(QSqlQueryModel().setQuery(Class_query))

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
        

app = QtGui.QApplication(sys.argv)
window = Role_window()
window.show()
sys.exit(app.exec_())


