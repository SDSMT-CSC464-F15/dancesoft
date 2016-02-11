import sys
from PyQt4 import QtGui, QtCore
from enter_fullpayment import Ui_Enter_fullpayment
from PyQt4.QtSql import *


class Enter_fullpayment_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Enter_fullpayment()
        self.ui.setupUi(self)
        self.conn()


        Term_query = QSqlQuery()
        Term_query.exec_("select Current_term from System where System_id = '1'")
        Term_query.next()
        self.ui.cur_term = Term_query.value(0)

        #get somone who actually the class and the amount of money they should pay
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select S.Student_name, sum(TIME_TO_SEC(TIMEDIFF(C.Class_end_time, C.Class_time))) / 60, S.Student_id from Student as S, Student_Class as SC, Class as C where S.Student_id = SC.Student_id and SC.Class_id = C.Class_id and SC.Student_semester_taken = '%s' GROUP BY S.Student_name" % self.ui.cur_term)

        self.stuid_dict = {}
        self.owe_dict = {}
        
        self.ui.rates = []
        self.ui.time = []
        Rate_query = QSqlQuery()
        Rate_query.exec_("select Tuition_Rate, Tuition_Time from Tuition_Rates ")
        while Rate_query.next():
            self.ui.rates.append(float(Rate_query.value(0)))
            self.ui.time.append(float(Rate_query.value(1)))

        while Teacher_query.next():
            self.owe_dict.update({Teacher_query.value(0):self.get_rate(float(Teacher_query.value(1)))})
            self.stuid_dict.update({Teacher_query.value(0):Teacher_query.value(2)})

        #print (self.stuid_dict)
        paid_dict = {}
        Money_query = QSqlQuery()
        Money_query.exec_("select S.student_name, sum(P.Amount_paid) from Student as S, Payment as P where S.Student_id = P.Student_id and P.Semester_paid = '%s' GROUP BY S.Student_name" % self.ui.cur_term)
        
        while Money_query.next():
            paid_dict.update({Money_query.value(0):float(Money_query.value(1))})
        model = QtGui.QStandardItemModel()
        
        for i in self.owe_dict:
            if i in paid_dict:
                self.owe_dict[i] -= paid_dict[i]
            if (self.owe_dict[i] > 0):
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
                
        self.ui.Student_listView.setModel(model)
        self.ui.Student_listView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ui.Student_listView.clicked.connect(self.select_student)
        self.ui.Statement_btn.clicked.connect(self.clear_money)
        
                                                 
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
 
    def clear_money(self):
        pay = QSqlQuery()
        delete_list = []
        for i in self.ui.Student_listView.selectedIndexes():
            #print (self.stuid_dict[i.data()])
            #print (i.data(), self.stuid_dict[i.data()], self.owe_dict[i.data()])
            delete_list.append(i.row())
            pay.exec_("INSERT INTO Payment VALUES (NULL, '%s', %d, '%s', NOW(), 'default')" % ( self.stuid_dict[i.data()], self.owe_dict[i.data()], self.ui.cur_term))
            #self.ui.Student_listView.model().removeRow(i.row())
        delete_list = sorted(delete_list, reverse = True)
        for i in delete_list:
            self.ui.Student_listView.model().removeRow(i)
            
    def select_student(self):
        self.ui.Statement_btn.setEnabled(True)
        
          

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()





app = QtGui.QApplication(sys.argv)
window = Enter_fullpayment_window()
window.show()
sys.exit(app.exec_())
