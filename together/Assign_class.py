import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from assign_teacher import Ui_Assign_teacher_window
from PyQt4.QtSql import *

class assign_teacher(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.assign = Ui_Assign_teacher_window()
        self.assign.setupUi(self)
        self.dialogbox_Flag = False

        self.conn()

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
            
        self.assign.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.assign.sel_teach.setTable("Class")

        self.class_query = QSqlQuery()
        self.class_query.exec_("Select Class_name, Class_id FROM Class ORDER BY Class_name")
        self.class_result = QSqlQueryModel()
        self.class_result.setQuery(self.class_query)
        self.assign.Class_listView.setModel(self.class_result)

        self.assign.Class_listView.clicked.connect(self.teacher_assignment)
        self.assign.Assign_teacher_back_btn.clicked.connect(self.close)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
    
    def teacher_assignment(self, class_index):
        row = class_index.row()
        self.class_result.record(row).field(1).value()
        
        self.current_teacher = ''
        self.selected_class = class_index.data()

        self.current_teacher_query = QSqlQuery()
        self.current_teacher_query.exec("SELECT Teacher_name FROM Teacher \
                        WHERE Teacher_id = (SELECT DISTINCT Teacher_Class.Teacher_id\
                        FROM Teacher, Teacher_Class WHERE Teacher_Class.Class_id = \
                        (select Class_id from Class where Class_id = '%s')) ORDER BY Teacher_id" % (self.class_result.record(row).field(1).value()))
        
        self.current_teacher_query.next()
        self.current_teacher = self.current_teacher_query.value(0)
        if self.current_teacher != None:
            confirm_msg = "This class is currently assigned to '%s' do you want to change teachers" %(self.current_teacher)
            
            reply = QtGui.QMessageBox.question(self, 'Reassign Class', 
                    confirm_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.teacher_query = QSqlQuery()
                self.teacher_query.exec_( "SELECT Teacher_name from Teacher WHERE Teacher_name \
                      not in (SELECT NC.Teacher_name from (SELECT T.Teacher_name, C.Class_time, C.Class_end_time, C.Class_day \
                      from Teacher as T, Teacher_Class as TC, Class as C WHERE TC.Teacher_id = T.Teacher_id and \
                      TC.Class_id = C.Class_id) as NC, (SELECT C.Class_time, C.Class_end_time, C.Class_day FROM Class \
                      as C WHERE C.Class_id = %d) as C WHERE (not (NC.Class_time >= C.Class_end_time or \
                      C.Class_time >= NC.Class_end_time )) and NC.Class_day <> C.Class_day ) ORDER BY Teacher_id" % (self.class_result.record(row).field(1).value()))
                self.dialogbox_Flag = False
                self.teacher_result = QSqlQueryModel()
                self.teacher_result.setQuery(self.teacher_query)
                self.assign.Teacher_listView.setModel(self.teacher_result)
                self.assign.Teacher_listView.clicked.connect(self.Update_assign_teacher)
                

        else:
        
            self.teacher_query = QSqlQuery()
            self.teacher_query.exec_( "SELECT Teacher_name from Teacher WHERE Teacher_name \
                          not in (SELECT NC.Teacher_name from (SELECT T.Teacher_name, C.Class_time, C.Class_end_time, C.Class_day \
                          from Teacher as T, Teacher_Class as TC, Class as C WHERE TC.Teacher_id = T.Teacher_id and \
                          TC.Class_id = C.Class_id) as NC, (SELECT C.Class_time, C.Class_end_time, C.Class_day FROM Class \
                          as C WHERE C.Class_id = %d) as C WHERE (not (NC.Class_time >= C.Class_end_time or \
                          C.Class_time >= NC.Class_end_time)) and NC.Class_day <> C.Class_day ) ORDER BY Teacher_id" % (self.class_result.record(row).field(1).value() ))
            
            self.teacher_result = QSqlQueryModel()
            self.teacher_result.setQuery(self.teacher_query)
            self.assign.Teacher_listView.setModel(self.teacher_result)
            self.assign.Teacher_listView.clicked.connect(self.assign_teacher)
            self.dialogbox_Flag = False

    def assign_teacher(self, teacher_index):
        if self.dialogbox_Flag == False:
            confirm_msg = "Are you sure you want to assign '%s' to teach '%s'"\
                          %(teacher_index.data(), self.selected_class)
            
            reply = QtGui.QMessageBox.question(self, 'Confirm', 
                    confirm_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                    get_data_query = QSqlQuery()
                    get_data_query.exec("Select Teacher_id, Class_id, Current_term FROM \
                                         Teacher, Class, System WHERE Teacher_name \
                                         = '%s' AND Class_name = '%s' AND System_id = 1;" % (teacher_index.data(), self.selected_class) )
                    
                    if get_data_query.next():
                        record = get_data_query.record()
                        self.teacher_rec = int(record.value(0))
                        self.class_rec = int(record.value(1))
                        self.current_term = str(record.value(2))
                    
                        #assign teacher query
                        assign_teach_query = QSqlQuery()
                        assign_teach_query.exec("INSERT INTO Teacher_Class Values(%d,%d,'%s')"\
                                                %(self.teacher_rec, self.class_rec, self.current_term))
            self.dialogbox_Flag = True

    def Update_assign_teacher(self, teacher_index):
        if self.dialogbox_Flag == False:
            
            confirm_msg = "Are you sure you want to assign '%s' to teach '%s'" %(teacher_index.data(), self.selected_class)
            
            
            reply = QtGui.QMessageBox.question(self, 'Confirm', 
                    confirm_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                    get_data_query = QSqlQuery()
                    get_data_query.exec("Select Teacher_id, Class_id FROM Teacher, Class WHERE Teacher_name = '%s' AND Class_name = '%s'" % (teacher_index.data(), self.selected_class) )
                    
                    if get_data_query.next():
                        record = get_data_query.record()
                        self.teacher_rec = int(record.value(0))
                        self.class_rec = int(record.value(1))
                    
                        #assign teacher query
                        assign_teach_query = QSqlQuery()
                        assign_teach_query.exec("Update Teacher_Class SET Teacher_id = %d WHERE Class_id = %d" %(self.teacher_rec, self.class_rec))
            self.dialogbox_Flag = True
