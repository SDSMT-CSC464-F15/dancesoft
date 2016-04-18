import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Addstu_detail import Ui_Addstu_detail
from PyQt4.QtSql import *


class Addstu_detail_dialog(QtGui.QDialog):
    def __init__(self, Class_name = None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Addstu_detail()
        self.ui.setupUi(self)
        Stu_query = QSqlQuery()
        self.class_name = Class_name
        #dislplay students those who have class need to be approved
        Stu_query.exec_("Select S.Student_name from Student_Class as SC,Student as S where\
                            SC.Class_id = (Select Class_id from Class where Class_name = '%s') \
                            and SC.Student_id = S.Student_id and SC.Class_finished <> 1 and \
                            SC.Class_approval <> 1" % self.class_name)
        model = QSqlQueryModel()
        model.setQuery(Stu_query)
        #populate list view
        self.ui.Addstu_detail_listView.setModel(model)
        self.ui.Addstu_detail_listView.clicked.connect(self.add_student)
        self.ui.Addstu_detail_btn.setEnabled(False)
        self.ui.Addstu_detail_btn.clicked.connect(self.set_student)

    def set_student(self):
        Add_query = QSqlQuery()
        
        if Add_query.exec_("Update Student_Class Set Class_approval = 1 Where\
                            Student_id = (Select Student_id from Student Where Student_name = \
                            '%s') and Class_id = (Select Class_id from Class where \
                            Class_name = '%s')" % (self.stu_name, self.class_name)):
            QtGui.QMessageBox.information(
                self, 'Success', 'Add student to class successfully')


    def add_student(self, index):
        self.ui.Addstu_detail_btn.setEnabled(True)
        self.stu_name = index.data()
        
