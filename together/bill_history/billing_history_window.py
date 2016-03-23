import sys
from PyQt4 import QtGui, QtCore
from billing_history import Ui_Billing_history
from PyQt4.QtSql import *
from billing_print import Print_window

class Billing_history_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Billing_history()
        self.ui.setupUi(self)
        self.conn()
        Student_query = QSqlQuery()
        Student_query.exec_("select Student_name from Student")
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        self.ui.Statement_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_student)
        self.ui.Statement_btn.clicked.connect(self.print_history)
        self.ui.Student_listView.clicked.connect(self.select_student)

        Term_query = QSqlQuery()
        Term_query.exec_("select Current_term from System where System_id = '1'")
        Term_query.next()
        self.ui.cur_term = Term_query.value(0)
        
    def search_student(self):
        input_student_name = self.ui.Teacher_lineEdit.text()
        Student_query = QSqlQuery()
        Student_query.exec_("select Student_name from Student where Student_name like '%%%s%%'" % input_student_name)
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        
    def print_history(self):
        self.ui.Statement_btn.setEnabled(True)
        
        History_query = QSqlQuery()
        
        HistoryList = []
        History_query.exec_("select P.Payment_id, P.Amount_paid, P.Date_paid from Student as S, Payment as P where S.Student_id = P.Student_id and \
                           S.Student_name = '%s' and P.Semester_paid = '%s'" % (self.ui.name, self.ui.cur_term))
        cnt = 0
        while History_query.next():
            HistoryList.append([])
            HistoryList[cnt].append(History_query.value(0))
            HistoryList[cnt].append(self.ui.name)
            HistoryList[cnt].append(self.ui.cur_term.replace("_", " Term "))
            HistoryList[cnt].append(History_query.value(1))
            HistoryList[cnt].append(History_query.value(2).toString())
            cnt += 1

        print (HistoryList)
        
        self.ui.print = Print_window(HistoryList)
        self.ui.print.show() 
        

        
    def select_student(self, index):
        #TODO
        #total hours
        self.ui.name = index.data()
        self.ui.Statement_btn.setEnabled(True)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

        
app = QtGui.QApplication(sys.argv)
window = Billing_history_window()
window.show()
sys.exit(app.exec_())
