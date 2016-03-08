import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from show_hours import Ui_Show_hours


class show_hours_dialog(QtGui.QDialog):
    def __init__(self, teacher_name):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Show_hours()
        self.ui.setupUi(self)
        self.teacher_name = teacher_name

        Term_query = QSqlQuery()
        Term_query.exec_("select Current_term from System where System_id = '1'")
        Term_query.next()
        self.ui.cur_term = Term_query.value(0)

        Hours_query = QSqlQuery()
        Hours_query.exec_("select sum(TIME_TO_SEC(TIMEDIFF(C.Class_end_time, C.Class_time))) from Teacher as T, Teacher_Class as TC, Class as C\
                           where T.Teacher_id = TC.Teacher_id and TC.Class_id = C.Class_id and T.Teacher_name = '%s'\
                           and TC.Class_semester_taught = '%s'" % (teacher_name, self.ui.cur_term))
        Hours_query.next()
        hours = 0.0
        if not isinstance(Hours_query.value(0), QtCore.QPyNullVariant):
            hours = int(Hours_query.value(0)) / 3600

        other_hours = 0.0
        other_hours_query = QSqlQuery()
        other_hours_query.exec_("select Teacher_hours from Teacher where Teacher_name = '%s'" % teacher_name)
        other_hours_query.next()
        
        if not isinstance(other_hours_query.value(0), QtCore.QPyNullVariant):
            other_hours = other_hours_query.value(0)
        self.ui.course_lineEdit.setText(str(hours))
        self.ui.course_lineEdit.setDisabled(True)
        self.ui.other_lineEdit.setText(str(other_hours))
        self.ui.update_btn.clicked.connect(self.update_hours)
        self.ui.cancel_btn.clicked.connect(self.close)

    def update_hours(self):
        update_hours = QSqlQuery()
        if update_hours.exec_("update Teacher set Teacher_hours = '%s' where\
                            Teacher_name = '%s'" % (self.ui.other_lineEdit.text(), self.teacher_name)):
            QtGui.QMessageBox.information(
                self, 'success', 'Success!')
        else:
            QtGui.QMessageBox.information(
                self, 'fail', 'Please enter a number!')
            
                
