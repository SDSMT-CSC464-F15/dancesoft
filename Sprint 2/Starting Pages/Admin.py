import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Admin_Landing import Ui_Admin_Landing
from functools import partial
from PyQt4.QtSql import *

class Admin_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Admin_Landing()
        self.ui.setupUi(self)
        self.current_index = 0
        self.prev_index = 0

        
        self.ui.Employee_btn.clicked.connect(partial(self.change_window, index = 1))
        self.ui.Class_btn.clicked.connect(partial(self.change_window, index = 2))
        self.ui.Student_btn.clicked.connect(partial(self.change_window, index = 3))
        self.ui.Billing_btn.clicked.connect(partial(self.change_window, index = 4))
        
        self.ui.Employee_back_btn.clicked.connect(self.Back_btn)
        self.ui.Class_back_btn.clicked.connect(self.Back_btn)
        self.ui.Student_back_btn.clicked.connect(self.Back_btn)
        self.ui.Payroll_back_btn.clicked.connect(self.Back_btn)

        self.ui.Search_teacher_btn.clicked.connect(partial(self.change_window, index = 5))
        self.ui.Teacher_search_back_btn.clicked.connect(self.Back_btn)

        self.ui.Update_teacher_btn.clicked.connect(self.modify_teacher)

        self.ui.Quit_btn.clicked.connect(self.Quit)
        self.ui.Quit_btn_2.clicked.connect(self.Quit)
        self.ui.Quit_btn_3.clicked.connect(self.Quit)
        self.ui.Quit_btn_4.clicked.connect(self.Quit)
        self.ui.Quit_btn_5.clicked.connect(self.Quit)

        self.setup_database
        
        
    def change_window(self, index):
        self.prev_index = self.current_index
        self.ui.stackedWidget.setCurrentIndex(index)
        self.current_index = index
        if (self.current_index == 5):
            self.setup_database()


    def modify_teacher(self):
        self.select_teacher = Select_teacher()
        self.select_teacher.show()

    def setup_database(self):

        print("got Here")
        
        self.conn() #need catch exception
        
        self.ui.teacher = QSqlRelationalTableModel(db = self.db)
        self.ui.teacher.setTable("Teacher")

        #TODO deal with foreign key
        
       # self.ui.teacher.setRelation(8, QSqlRelation("Guardian", "Guardian_id", "Guardian_name"))
        self.ui.teacher.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.teacher.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.ui.teacher.setHeaderData(2, QtCore.Qt.Horizontal, "Home Phone")
        self.ui.teacher.setHeaderData(3, QtCore.Qt.Horizontal, "Cell Phone")
        self.ui.teacher.setHeaderData(4, QtCore.Qt.Horizontal, "Work Phone")
        self.ui.teacher.setHeaderData(6, QtCore.Qt.Horizontal, "Email")
        
        
        self.ui.teacher.select()
        

        #display window
        self.ui.Teacher_view.setModel(self.ui.teacher)      
        self.ui.Teacher_view.hideColumn(5)
        self.ui.Teacher_view.hideColumn(7)
        self.ui.Teacher_view.hideColumn(8)
        self.ui.Teacher_view.hideColumn(9)
        self.ui.Teacher_view.hideColumn(10)
        self.ui.Teacher_view.hideColumn(11)

        self.ui.Search_btn.clicked.connect(self.search)

    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
            

        #get input data from user
        
        input_teacher_name = self.ui.Search_lineEdit.text()
        query = QSqlQuery()
        query.exec_("SELECT * FROM Teacher WHERE Teacher_name = '%s'" % input_teacher_name)

        print query.value(2).toString()
        self.ui.teacher.setQuery(query)       
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
        

    def Back_btn(self):
        self.current_index = self.prev_index
        self.ui.stackedWidget.setCurrentIndex(self.current_index)
        
    def Quit(self):
        sys.exit()
        
        
        

import sys
app = QtGui.QApplication(sys.argv)
Current_Window = Admin_window()
Current_Window.show()
sys.exit(app.exec_())
