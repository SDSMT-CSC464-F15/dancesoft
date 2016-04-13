import sys
from PyQt4 import QtGui, QtCore
from enter_hours import Ui_Enter_hours
from PyQt4.QtSql import *
from show_hours_dialog import show_hours_dialog


class Enter_hours_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Enter_hours()
        self.ui.setupUi(self)
        self.conn()

        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher")
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        self.ui.Search_btn.clicked.connect(self.search_teacher)
        self.ui.Hours_btn.setEnabled(False)
        self.ui.Hours_btn.clicked.connect(self.show_hours)
        self.ui.Teacher_listView.clicked.connect(self.select_teacher)

    def show_hours(self):
        self.ui.show = show_hours_dialog(self.ui.name)
        self.ui.show.show()

    def select_teacher(self, index):
        self.ui.name = index.data()
        self.ui.Hours_btn.setEnabled(True)
        
    def search_teacher(self):
        input_teacher_name = self.ui.Teacher_lineEdit.text()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher where Teacher_name like '%%%s%%'" % input_teacher_name)
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

