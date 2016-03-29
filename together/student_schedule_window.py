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
        #get student name for user choosing
        Student_query.exec_("select Student_name from Student ORDER BY Student_name")
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        #populate listview by student's name
        self.ui.Student_listView.setModel(model)
        #disable button when the focus is not on the list
        self.ui.schedule_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_student)
        self.ui.schedule_btn.clicked.connect(self.print_schedule)
        self.ui.Student_listView.clicked.connect(self.select_Student)
        self.ui.cancel_btn.clicked.connect(self.close)
        
    def search_student(self):
        #search student by name
        input_Student_name = self.ui.Student_lineEdit.text()
        Student_query = QSqlQuery()
        Student_query.exec_("Select Student_name From Student where Student_name like '%%%s%%' ORDER BY Student_name" % input_Student_name)
        model = QSqlQueryModel()
        model.setQuery(Student_query)
        self.ui.Student_listView.setModel(model)
        
    def print_schedule(self):
        #print student's schedule in a new window
        self.ui.print = Print_window(self.ui.timeslicing, self.ui.msg)
        self.ui.print.show()

    class time:
        def __init__(self):
            self.day = ""
            self.start = ""
            self.end = ""
            self.class_name = ""
        
    def select_Student(self, index):
        self.ui.Student_info = []
        self.ui.msg = []
        lookup = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thrusday':3, 'Friday':4, 'Saturday':5}

        
        self.ui.schedule_btn.setEnabled(True)
        Student_query = QSqlQuery()
        Student_query.exec_("SELECT C.Class_name, C.Class_time,\
                            C.Class_end_time, C.Class_day FROM Student as T, Student_Class\
                            as TC, Class as C WHERE T.Student_name = '%s' and\
                            T.Student_id = TC.Student_id and TC.Class_id = C.Class_id" % index.data())

        while Student_query.next():
            self.ui.Student_info.append(str(Student_query.value(3)) + ',' + str(Student_query.value(1).toString()) + ',' +
                                        str(Student_query.value(2).toString()) +',' + str(Student_query.value(0)) )

        timelist = [self.time() for i in range(len(self.ui.Student_info))]
        self.ui.timeslicing = []
        for i in range(len(self.ui.Student_info)):
            temp = self.ui.Student_info[i].split(',')
            timelist[i].day = temp[0]
            timelist[i].start = temp[1][0:5]
            timelist[i].end = temp[2][0:5]
            timelist[i].class_name = temp[3]
            if not temp[1][0:5] in self.ui.timeslicing:
                self.ui.timeslicing.append(temp[1][0:5])
            if not temp[2][0:5] in self.ui.timeslicing:
                self.ui.timeslicing.append(temp[2][0:5])

        self.ui.timeslicing.sort()
        time_length = len(self.ui.timeslicing)
        if time_length > 1:
            time_length -= 1

        self.ui.msg = [['' for i in range(time_length)] for j in range(6)]

        for i in range(len(timelist)):
            for j in range(self.ui.timeslicing.index(timelist[i].start), self.ui.timeslicing.index(timelist[i].end)):
                self.ui.msg[lookup[timelist[i].day]][j] = timelist[i].class_name


            
            
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

    
