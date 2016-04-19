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
        
        self.hours_dict = {}
        pay_query = QSqlQuery()
        pay_query.exec_("select Payname, Hours, Payrate from Teacher_Payrate as TP, Payrate as P where \
                             TP.Payrate_id = P.Payrate_id and TP.Teacher_id = \
                             (select Teacher_id from Teacher where Teacher_name = '%s')" % teacher_name)

        sum = 0.0
        while pay_query.next():
            self.ui.Hour_comboBox.addItem(pay_query.value(0))
            self.hours_dict[pay_query.value(0)] = float(pay_query.value(1))
            sum += (pay_query.value(1) * pay_query.value(2))

        if self.ui.Hour_comboBox.currentText() != '':
            self.ui.other_lineEdit.setText(str(self.hours_dict[str(self.ui.Hour_comboBox.currentText())]))  


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

        self.ui.course_lineEdit.setText(str(hours))
        self.ui.course_lineEdit.setDisabled(True)
        self.ui.Wage_lineEdit.setDisabled(True)
        self.ui.Wage_lineEdit.setText(str('%.2f' % sum))
        self.ui.update_btn.clicked.connect(self.update_hours)
        self.ui.cancel_btn.clicked.connect(self.close)

        self.ui.Hour_comboBox.currentIndexChanged.connect(self.update_text)

    def update_text(self):
        if self.ui.Hour_comboBox.currentText() != '':
            self.ui.other_lineEdit.setText(str(self.hours_dict[str(self.ui.Hour_comboBox.currentText())]))  

    def update_hours(self):
        if self.ui.Hour_comboBox.currentText() != '':
            update_query = QSqlQuery()
            if update_query.exec_("update Teacher_Payrate as TP, Payrate as P set TP.Hours = %f where \
                                   TP.Teacher_id = (select Teacher_id from Teacher where Teacher_name = '%s')\
                                   and TP.Payrate_id = P.Payrate_id and P.Payname = '%s'" % \
                                   (float(self.ui.other_lineEdit.text()), self.teacher_name,\
                                    self.ui.Hour_comboBox.currentText())):
                pay_query = QSqlQuery()
                pay_query.exec_("select Payname, Hours, Payrate from Teacher_Payrate as TP, Payrate as P where \
                             TP.Payrate_id = P.Payrate_id and TP.Teacher_id = \
                             (select Teacher_id from Teacher where Teacher_name = '%s')" % self.teacher_name)

                sum = 0.0
                while pay_query.next():
                    sum += (pay_query.value(1) * pay_query.value(2))
                self.ui.Wage_lineEdit.setText(str('%.2f' % sum))
                
                self.hours_dict[str(self.ui.Hour_comboBox.currentText())] = float(self.ui.other_lineEdit.text())
                QtGui.QMessageBox.information(self, 'success', 'Success!')
            else:
                QtGui.QMessageBox.information(self, 'fail', 'Fail!')
            
                
