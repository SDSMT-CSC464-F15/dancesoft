import sys
from PyQt4 import QtGui
from teacher_schedule import Ui_Teacher_schedule
from schedule_print import Print_window
from PyQt4.QtSql import *


class Teacher_schedule_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Teacher_schedule()
        self.ui.setupUi(self)
        self.conn()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher")
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        self.ui.schedule_btn.setEnabled(False)
        self.ui.Search_btn.clicked.connect(self.search_student)
        self.ui.schedule_btn.clicked.connect(self.print_schedule)
        self.ui.Teacher_listView.clicked.connect(self.select_teacher)
        
    def search_student(self):
        input_teacher_name = self.ui.Teacher_lineEdit.text()
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("select Teacher_name from Teacher where Teacher_name like '%%%s%%'" % input_teacher_name)
        model = QSqlQueryModel()
        model.setQuery(Teacher_query)
        self.ui.Teacher_listView.setModel(model)
        
    def print_schedule(self):
        self.ui.print = Print_window(self.ui.timeslicing, self.ui.msg)
        self.ui.print.show()

    class time:
        def __init__(self):
            self.day = ""
            self.start = ""
            self.end = ""
            self.class_name = ""
    
    def select_teacher(self, index):
        self.ui.Teacher_info = []
        self.ui.msg = []
        lookup = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thrusday':3, 'Friday':4, 'Saturday':5}
        

        
        self.ui.schedule_btn.setEnabled(True)
        Teacher_query = QSqlQuery()
        Teacher_query.exec_("SELECT C.Class_name, C.Class_time,\
                            C.Class_end_time, C.Class_day FROM Teacher as T, Teacher_Class\
                            as TC, Class as C WHERE T.Teacher_name = '%s' and\
                            T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id" % index.data())
        while Teacher_query.next():
            self.ui.Teacher_info.append(str(Teacher_query.value(3)) + ',' + str(Teacher_query.value(1).toString()) + ',' +
                                        str(Teacher_query.value(2).toString()) +',' + str(Teacher_query.value(0)) )

        timelist = [self.time() for i in range(len(self.ui.Teacher_info))]

        self.ui.timeslicing = []
        for i in range(len(self.ui.Teacher_info)):
            temp = self.ui.Teacher_info[i].split(',')
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

