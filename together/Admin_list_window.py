import sys
from PyQt4 import QtGui
from Admin_list import Ui_Admin_list
from Admin_info_Dialog import Admin_info_dialog
from addAdmin import addAdmin
from removeAdmin import removeAdmin
from PyQt4.QtSql import *

class Admin_list_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_list()
        self.ui.setupUi(self)
        self.conn()
        self.Admin_query = QSqlQuery()
        self.Admin_query.exec_("select Admin_name from Admin")
        model = QSqlQueryModel()
        model.setQuery(self.Admin_query)
        self.ui.Admin_listView.setModel(model)
        self.ui.Detail_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_Admin)
        self.ui.Detail_btn.clicked.connect(self.print_Detail)
        self.ui.Add_btn.clicked.connect(self.add_Admin)
        self.ui.Remove_btn.clicked.connect(self.remove_Admin)
        self.ui.Admin_listView.clicked.connect(self.select_Admin)

    def add_Admin(self):
        self.adminDialog = addAdmin()
        if self.adminDialog.exec_():
            model = QSqlQueryModel()
            model.setQuery(self.Admin_query)
            self.ui.Admin_listView.setModel(model)
        

    def remove_Admin(self):
        self.removeDialog = removeAdmin()
        if self.removeDialog.exec_():
            model = QSqlQueryModel()
            model.setQuery(self.Admin_query)
            self.ui.Admin_listView.setModel(model)
    
    def search_Admin(self):
        input_Admin_name = self.ui.Admin_lineEdit.text()
        Admin_query = QSqlQuery()
        Admin_query.exec_("select Admin_name from Admin where Admin_name like '%%%s%%'" % input_Admin_name)
        model = QSqlQueryModel()
        model.setQuery(Admin_query)
        self.ui.Admin_listView.setModel(model)
        
    def print_Detail(self):
        self.ui.detail = Admin_info_dialog(self.ui.name)
        self.ui.detail.show()
        
    def select_Admin(self, index):
        self.ui.name = index.data()
        self.ui.Detail_btn.setEnabled(True)
        
            
            
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

        
