import sys
from PyQt4 import QtGui
from teacher_history_detail import Ui_Teacher_history_dialog
from PyQt4.QtSql import *

class Teacher_history_dialog(QtGui.QDialog):
    def __init__(self, name):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Teacher_history_dialog()
        self.ui.setupUi(self)
        History_query = QSqlQuery()
        History_query.exec_("Select Class_name from Class as C, Teacher_Class as\
                           TC, Teacher as T where T.Teacher_id = TC.Teacher_id and \
                           T.Teacher_id = (select Teacher_id from Teacher where Teacher_name = \
                           '%s') and TC.Class_id = C.Class_id" % name)
        model = QSqlQueryModel()
        model.setQuery(History_query)
        self.ui.history_listView.setModel(model)
        self.ui.history_pushButton.clicked.connect(self.close)


