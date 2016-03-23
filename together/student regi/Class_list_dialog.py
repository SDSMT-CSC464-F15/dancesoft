import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Class_list import Ui_Class_list_Dialog
from PyQt4.QtSql import *
from functools import partial
from PyQt4.QtGui import QAbstractItemView



class Class_list_dialog(QtGui.QDialog):
    def __init__(self, ID):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Class_list_Dialog()
        self.ui.setupUi(self)
        self.id = ID
        class_query = QSqlQuery()
        class_query.exec_("SELECT T.Teacher_name, C.Class_id, C.Class_name, C.Class_time, C.Class_end_time, \
                            C.Class_location FROM Teacher as T, Teacher_Class as TC, \
                           Class as C WHERE T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id \
                           and TC.Class_semester_taught = (SELECT Current_term FROM System WHERE System_id = 1) and\
                           C.Class_id in(SELECT C.Class_id FROM Class as C, Student_Class as SC WHERE C.Class_id = \
                           SC.Class_id and SC.Student_semester_taken = (SELECT Current_term FROM System WHERE System_id\
                           = 1) and SC.Student_id = %d) order by C.Class_id" % ID) 

        self.class_model = QSqlQueryModel()
        self.class_model.setQuery(class_query)
        self.ui.Class_drop_tableView.setModel(self.class_model)


        class_query.exec_("SELECT T.Teacher_name, C.Class_id, C.Class_name, C.Class_time, C.Class_end_time, \
                            C.Class_location FROM Teacher as T, Teacher_Class as TC, \
                           Class as C WHERE T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id \
                           and TC.Class_semester_taught = (SELECT Current_term FROM System WHERE System_id = 1) and\
                           C.Class_id not in(SELECT C.Class_id FROM Class as C, Student_Class as SC WHERE C.Class_id = \
                           SC.Class_id and SC.Student_semester_taken = (SELECT Current_term FROM System WHERE System_id\
                           = 1) and SC.Student_id = %d) order by C.Class_id" % ID)
        

        self.class_drop_model = QSqlQueryModel()
        self.class_drop_model.setQuery(class_query)
        self.ui.Class_add_tableView.setModel(self.class_drop_model)

        self.ui.Add_btn.clicked.connect(self.add)
        self.ui.Drop_btn.clicked.connect(self.drop)
        self.ui.Class_add_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.Class_drop_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)


        


    def add(self):
        data_list = [i.data() for i in self.ui.Class_add_tableView.selectedIndexes() if isinstance(i.data(),int)]
        class_add = QSqlQuery()
        for i in data_list:
            class_add.exec_("INSERT into Student_Class values(%d, %d, 0, 0, CURDATE(), \
                            (SELECT Current_term FROM System WHERE System_id = 1))" % (self.id, i))
        self.refresh()

    def drop(self):
        data_list = [i.data() for i in self.ui.Class_drop_tableView.selectedIndexes() if isinstance(i.data(),int)]
        class_drop = QSqlQuery()
        for i in data_list:
            class_drop.exec_("delete from Student_Class where Student_id = %d and Class_id = %d and \
                          Student_semester_taken = (SELECT Current_term FROM System WHERE System_id\
                           = 1)" % (self.id, i))
        self.refresh()

    def refresh(self):
        class_query = QSqlQuery()
        class_query.exec_("SELECT T.Teacher_name, C.Class_id, C.Class_name, C.Class_time, C.Class_end_time, \
                            C.Class_location FROM Teacher as T, Teacher_Class as TC, \
                           Class as C WHERE T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id \
                           and TC.Class_semester_taught = (SELECT Current_term FROM System WHERE System_id = 1) and\
                           C.Class_id in(SELECT C.Class_id FROM Class as C, Student_Class as SC WHERE C.Class_id = \
                           SC.Class_id and SC.Student_semester_taken = (SELECT Current_term FROM System WHERE System_id\
                           = 1) and SC.Student_id = %d) order by C.Class_id" % self.id)

        self.class_model.setQuery(class_query)

        class_query.exec_("SELECT T.Teacher_name, C.Class_id, C.Class_name, C.Class_time, C.Class_end_time, \
                            C.Class_location FROM Teacher as T, Teacher_Class as TC, \
                           Class as C WHERE T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id \
                           and TC.Class_semester_taught = (SELECT Current_term FROM System WHERE System_id = 1) and\
                           C.Class_id not in(SELECT C.Class_id FROM Class as C, Student_Class as SC WHERE C.Class_id = \
                           SC.Class_id and SC.Student_semester_taken = (SELECT Current_term FROM System WHERE System_id\
                           = 1) and SC.Student_id = %d) order by C.Class_id" % self.id)

        self.class_drop_model.setQuery(class_query)
