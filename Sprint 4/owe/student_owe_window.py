import sys
from PyQt4 import QtGui, QtCore
from student_owe import Ui_Student_payment
from PyQt4.QtSql import *
from fee_print import Print_window

class Student_payment_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Student_payment()
        self.ui.setupUi(self)
        self.conn()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Student_name from Student")
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Student_listView.setModel(model)
        self.ui.Statement_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_student)
        self.ui.Statement_btn.clicked.connect(self.print_history)
        self.ui.Student_listView.clicked.connect(self.select_student)

        Term_query = QSqlQuery()
        Term_query.exec_("select Current_term from System where System_id = '1'")
        Term_query.next()
        self.ui.cur_term = Term_query.value(0)

        self.ui.rates = []
        self.ui.time = []
        Rate_query = QSqlQuery()
        Rate_query.exec_("select Tuition_Rate, Tuition_Time from Tuition_Rates ")
        while Rate_query.next():
            self.ui.rates.append(float(Rate_query.value(0)))
            self.ui.time.append(float(Rate_query.value(1)))
        
    def get_rate(self, minitue):
        for i in range(len(self.ui.time)):
            if (minitue <= self.ui.time[i]):
                return self.ui.rates[i]
        return self.ui.rates[-1]
        
    def search_student(self):
        input_student_name = self.ui.Teacher_lineEdit.text()
        Student_query = QSqlQuery()
        Student_query.exec_("select Student_name from Student where Student_name like '%%%s%%'" % input_student_name)
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        
    def print_history(self):
        self.ui.Statement_btn.setEnabled(True)
        Hours_query = QSqlQuery()
        Hours_query.exec_("select sum(TIME_TO_SEC(TIMEDIFF(C.Class_end_time, C.Class_time))) from Student as S, Student_Class as SC, Class as C\
                           where S.Student_id = SC.Student_id and SC.Class_id = C.Class_id and S.Student_name = '%s'\
                           and SC.Student_semester_taken = '%s'" % (self.ui.name, self.ui.cur_term))
        Hours_query.next()
        minutes = 0
        if not isinstance(Hours_query.value(0), QtCore.QPyNullVariant):
            minutes = int(Hours_query.value(0)) / 60


        Money = 0.0
        Money_query = QSqlQuery()
        Money_query.exec_("select sum(P.Amount_paid) from Student as S, Payment as P where S.Student_id = P.Student_id and \
                           S.Student_name = '%s' and P.Semester_paid = '%s'" % (self.ui.name, self.ui.cur_term))

        Money_query.next()
        if not isinstance(Money_query.value(0), QtCore.QPyNullVariant):
            Money = float(Money_query.value(0))

        self.ui.print = Print_window(self.ui.cur_term, Money, self.get_rate(minutes))
        self.ui.print.show() 
        
        '''
        self.ui.history = Teacher_history_dialog(self.ui.name)
        self.ui.history.show()
        '''
        
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
window = Student_payment_window()
window.show()
sys.exit(app.exec_())
