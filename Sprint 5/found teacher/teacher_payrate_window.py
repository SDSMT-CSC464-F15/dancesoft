import sys
from PyQt4 import QtGui
from teacher_payrate import Ui_Teacher_payrate
from PyQt4.QtSql import *
from teacher_payrate_dialog import Teacher_payrate_dialog

class Teacher_payrate_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_payrate()
        self.ui.setupUi(self)
        self.conn()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher")
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        self.ui.history_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_teacher)
        self.ui.history_btn.clicked.connect(self.print_history)
        self.ui.Teacher_listView.clicked.connect(self.select_teacher)
        
    def search_teacher(self):
        input_teacher_name = self.ui.Teacher_lineEdit.text()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher where Teacher_name like '%%%s%%'" % input_teacher_name)
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        
    def print_history(self):
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_id from Teacher where Teacher_name = '%s'" % self.ui.name)
        Teacher_query.next()
        self.ui.history = Teacher_payrate_dialog(int(Teacher_query.value(0)))
        self.ui.history.show()
        
    def select_teacher(self, index):
        self.ui.name = index.data()
        self.ui.history_btn.setEnabled(True)
        
            
            
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

        




app = QtGui.QApplication(sys.argv)
window = Teacher_payrate_window()
window.show()
sys.exit(app.exec_())
