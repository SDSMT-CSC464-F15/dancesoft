import sys
from PyQt4 import QtGui, QtCore
from Search import Ui_Search_MainWindow
from PyQt4.QtSql import *

class Search_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Search_MainWindow()
        self.ui.setupUi(self)

        
        self.conn() #need catch exception
        
        self.ui.student = QSqlRelationalTableModel(db = self.db)
        self.ui.student.setTable("Student")


        #TODO deal with foreign key
        
        self.ui.student.setRelation(8, QSqlRelation("Guardian", "Guardian_id", "Guardian_name"))
        self.ui.student.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.ui.student.setHeaderData(2, QtCore.Qt.Horizontal, "Name")
        self.ui.student.setHeaderData(3, QtCore.Qt.Horizontal, "Gender")
        self.ui.student.setHeaderData(5, QtCore.Qt.Horizontal, "Date of Birth")
        self.ui.student.setHeaderData(6, QtCore.Qt.Horizontal, "Phone")
        self.ui.student.setHeaderData(8, QtCore.Qt.Horizontal, "Primary Guardian")
        
        
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

    def search(self):
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
            

        #get input data from user
        
        input_student_name = self.ui.Search_lineEdit.text()
        query = QSqlQuery()
        query.exec_("SELECT * FROM Student WHERE Student_name = '%s'" % input_student_name)

        print query.value(2).toString()
        self.ui.student.setQuery(query)       
        

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
