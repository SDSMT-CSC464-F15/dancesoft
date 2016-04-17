import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from removeTeacherDialog import Ui_removeTeacherDialog
from PyQt4.QtSql import *

class removeTeacher(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.removeTeach = Ui_removeTeacherDialog()
        self.removeTeach.setupUi(self)

        self.conn()

        self.removeTeach.sel_teach = QSqlRelationalTableModel(db = self.db)
        self.removeTeach.sel_teach.setTable("Teacher")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        self.idList = []

        self.teach_query = QSqlQuery()
        self.teach_query.exec_("Select Teacher_name, Teacher_id FROM Teacher")
        while self.teach_query.next():
            record = self.teach_query.record()
            self.name = str(record.value(0))
            self.id = str(record.value(1))
            self.idList.append(self.id)
            self.removeTeach.teacherComboBox.addItem(self.name)
            
        self.removeTeach.ok_btn.clicked.connect(self.submit)

        self.removeTeach.cancel_btn.clicked.connect(self.close)

    def submit(self):
        self.addressCounter = 0
        self.selectedTeacher = self.removeTeach.teacherComboBox.currentIndex()
        self.selectedTeacherId = self.idList[self.selectedTeacher]
        

        self.getAddress = QSqlQuery()
        self.getAddress.exec_("Select Teacher_address from Teacher WHERE \
            Teacher_address = (Select Teacher_address from Teacher WHERE\
            Teacher_id = '%s')" % self.selectedTeacherId)
        while self.getAddress.next():
            record = self.getAddress.record()
            self.addressId = int(record.value(0))
            self.addressCounter += 1
            

        self.confirmMessage = "Are you sure you want to remove '%s' from the system? This will remove all relevant information and can not be reversed." \
                                 %(self.removeTeach.teacherComboBox.currentText())
        self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if (self.confirmReply == QtGui.QMessageBox.Yes):
            self.confirm_query = QSqlQuery()
            self.teach_query.exec_("DELETE from Teacher WHERE Teacher_id = '%s'" % self.selectedTeacherId)
            self.teach_query.exec_("Delete From Admin WHERE Admin_id = \
                        (select Admin_id from Account where Teacher_id = '%s')" % self.selectedTeacherId)
            self.teach_query.exec_("DELETE from Account WHERE Teacher_id = '%s'" % self.selectedTeacherId)
            self.teach_query.exec_("DELETE from Teacher_Payrate WHERE Teacher_id = '%s'" % self.selectedTeacherId)
            self.teach_query.exec_("UPDATE Teacher_Class SET Teacher_id = 0 WHERE Teacher_id = '%s'" % self.selectedTeacherId)
            
            if (self.addressCounter == 1):
                self.teach_query.exec_("DELETE from Address WHERE Address_id = %d" % self.addressId)

            self.message = "Teacher removed, classes taught by this teacher will need to be reasigned"
            
            self.confirmReply = QtGui.QMessageBox.information(self, 'Message', 
                self.message)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()
        
