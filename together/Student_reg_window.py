import sys
from PyQt4 import QtGui
from Stu_reg_window import Ui_Stu_reg
from Stu_add_reg_dialog import Stu_add_reg_dialog
from PyQt4.QtSql import *
from Stu_reg_dialog import Stu_reg_dialog 

class Stu_reg_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Stu_reg()
        self.ui.setupUi(self)
        self.conn()
        Stu_query = QSqlQuery()
        Stu_query.exec_("select Student_name from Student")
        model = QSqlQueryModel()
        model.setQuery(Stu_query)
        self.ui.Stu_listView.setModel(model)
        self.ui.Update_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_Stu)
        self.ui.Update_btn.clicked.connect(self.stu_info)
        self.ui.Stu_listView.clicked.connect(self.select_Stu)
        self.ui.Add_btn.clicked.connect(self.stu_add)

    def stu_add(self):
        self.ui.stu_add = Stu_add_reg_dialog()
        self.ui.stu_add.show()
    def search_Stu(self):
        input_Stu_name = self.ui.Stu_lineEdit.text()
        Stu_query = QSqlQuery()
        Stu_query.exec_("select Stu_name from Stu where Stu_name like '%%%s%%'" % input_Stu_name)
        model = QSqlQueryModel()
        model.setQuery(Stu_query)
        self.ui.Stu_listView.setModel(model)
        
    def stu_info(self):
        self.ui.stu_info = Stu_reg_dialog(self.ui.name)
        self.ui.stu_info.show()
        
    def select_Stu(self, index):
        self.ui.name = index.data()
        self.ui.Update_btn.setEnabled(True)
                    
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
