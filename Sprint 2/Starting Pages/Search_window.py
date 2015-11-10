import sys
from PyQt4 import QtGui, QtCore
from Search import Ui_Search_MainWindow
from PyQt4.QtSql import *
from Advsearch_Dialog import Advsearch_Dialog

class Search_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)

        
        self.conn() #need catch exception
        
       
        #TODO deal with foreign key
        self.ui.student = QSqlRelationalTableModel(db = self.db)
        self.ui.student.setTable("Student")
        self.ui.student.setRelation(8, QSqlRelation("Guardian", "Guardian_id", "Guardian_name"))
        self.ui.student.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.student.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
        self.ui.student.setHeaderData(3, QtCore.Qt.Horizontal, "Gender")
        self.ui.student.setHeaderData(5, QtCore.Qt.Horizontal, "Date of Birth")
        self.ui.student.setHeaderData(6, QtCore.Qt.Horizontal, "Phone")
        self.ui.student.setHeaderData(8, QtCore.Qt.Horizontal, "Primary Guardian")
        self.ui.student.setFilter('')
        self.ui.student.select()
        
        

        #display window
        self.ui.Student_view.setModel(self.ui.student)      
        self.ui.Student_view.hideColumn(1)
        self.ui.Student_view.hideColumn(4)
        self.ui.Student_view.hideColumn(7)
        self.ui.Student_view.hideColumn(9)
        self.ui.Student_view.hideColumn(10)
        self.ui.Student_view.hideColumn(11)
        self.ui.Student_view.hideColumn(12)
        self.ui.Student_view.hideColumn(13)

        self.ui.Search_btn.clicked.connect(self.search)
        self.ui.Adv_search_btn.clicked.connect(self.advsearch_show)
        self.ui.Reset_search_btn.clicked.connect(self.reset_table)

    def advsearch_show(self):
        self.adv = Advsearch_Dialog()
        self.adv.show()
        self.adv.ui.Seacch_adv_btn.clicked.connect(self.advsearch_query)
        self.adv.ui.Cancel_adv_btn.clicked.connect(self.adv.close)
        
    def advsearch_query(self):
        #self.reset_table()
        self.adv.ui.Id_adv_label.hide()
        self.adv.ui.Name_adv_label.hide()
        self.adv.ui.Phone_adv_label.hide()
        self.adv.ui.Guardian_adv_label.hide()
        
        Stu_ID = self.adv.ui.ID_adv_ledit.text()
        Stu_name = self.adv.ui.Name_adv_ledit.text()
        Stu_phone = self.adv.ui.Phone_adv_ledit.text()
        Stu_guardian = self.adv.ui.Guardian_adv_ledit.text()

        self.ui.student.setFilter("Student_name = '*'")

        
        flag = True
        
        '''     
        if self.adv.ui.ID_cbox.isChecked() and Stu_ID == '':
            self.adv.ui.Id_adv_label.show()
            flag = False 
        elif Stu_ID != '':
            self.ui.student.setFilter("Student_id = %s"%Stu_ID)
            
        if self.adv.ui.Name_cobx.isChecked() and Stu_name == '':
            self.adv.ui.Name_adv_label.show()
            flag = False
        elif Stu_name != '':
            self.ui.student.setFilter("Student_name = '%s'"%Stu_name)
            
        if self.adv.ui.Phone_cbox.isChecked() and Stu_phone == '':
            self.adv.ui.Phone_adv_label.show()
            flag = False
        elif Stu_phone != '':
            self.ui.student.setFilter("Student_home_phone = '%s'"%Stu_phone)
            
        if self.adv.ui.Guardian_cbox.isChecked() and Stu_guardian == '':
            self.adv.ui.Guardian_adv_label.show()
            flag = False
        elif Stu_guardian != '':
            self.ui.student.setFilter("relTblAl_8.Guardian_name = '%s'" % Stu_guardian)

        if flag:
            self.adv.close()    
        '''
        
        
    def reset_table(self):
        self.ui.student.setFilter('')
        
    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')          
        #get input data from user
        #refreash rows
        self.reset_table()
        input_student_name = self.ui.Search_lineEdit.text()
        if input_student_name != '':
            self.ui.student.setFilter("Student_name = '%s'" % input_student_name)

        
        

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()


app = QtGui.QApplication(sys.argv)
window = Search_window()
window.show()
sys.exit(app.exec_())
