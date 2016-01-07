import sys
from PyQt4 import QtGui
from student_schedule import Ui_Student_schedule
from schedule_print import Print_window
from PyQt4.QtSql import *

class Student_schedule_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Student_schedule()
        self.ui.setupUi(self)
        self.conn()
        Student_query = QSqlQuery()
        Student_query.exec_("select Student_name from Student")
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        self.ui.schedule_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_student)
        self.ui.schedule_btn.clicked.connect(self.print_schedule)
        self.ui.Student_listView.clicked.connect(self.select_Student)
        
    def search_student(self):
        input_Student_name = self.ui.Student_lineEdit.text()
        Student_query = QSqlQuery()
        Student_query.exec_("select Student_name from Student where Student_name like '%%%s%%'" % input_Student_name)
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        
    def print_schedule(self):
        self.ui.print = Print_window(self.ui.msg)
        self.ui.print.show()
        
    def select_Student(self, index):
        self.ui.Student_info = []
        self.ui.msg = []
        lookup = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thrusday':3, 'Friday':4, 'Saturday':5}
        self.ui.msg = [['' for i in range(6)] for j in range(13)]
        
        self.ui.schedule_btn.setEnabled(True)
        Student_query = QSqlQuery()
        Student_query.exec_("SELECT C.Class_name, C.Class_time,\
                            C.Class_end_time, C.Class_day FROM Student as T, Student_Class\
                            as TC, Class as C WHERE T.Student_name = '%s' and\
                            T.Student_id = TC.Student_id and TC.Class_id = C.Class_id" % index.data())
        while Student_query.next():
            self.ui.Student_info.append(str(Student_query.value(3)) + ',' + str(Student_query.value(1).toString()) + ',' +
                                        str(Student_query.value(2).toString()) +',' + str(Student_query.value(0)) )

        for i in self.ui.Student_info:
            temp = i.split(',')
            start = int(temp[1][0:2])
            start -= 8
            end = int(temp[2][0:2])
            end -= 8
            if int(temp[2][3:5]) == 0:
                end -= 1;
            for j in range(start, end+1):
                self.ui.msg[j][lookup[temp[0]]] = temp[3]
        
            
            
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

        




app = QtGui.QApplication(sys.argv)
window = Student_schedule_window()
window.show()
sys.exit(app.exec_())
