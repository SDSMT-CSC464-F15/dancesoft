import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from removeStudentDialog import Ui_removeStudentDialog
from PyQt4.QtSql import *

class removeStudentData(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.removeStu = Ui_removeStudentDialog()
        self.removeStu.setupUi(self)

        self.model = QtGui.QStandardItemModel()

        self.conn()

        self.removeStu.sel_student = QSqlRelationalTableModel(db = self.db)
        self.removeStu.sel_student.setTable("Student")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        self.student_query = QSqlQuery()
        self.student_query.exec_("Select Student_name FROM Student")
        while self.student_query.next():
            record = self.student_query.record()
            item = QtGui.QStandardItem()
            self.name = str(record.value(0))
            item.setText(self.name)
            self.model.appendRow(item)

        self.removeStu.studentListView.setModel(self.model)
        self.removeStu.studentListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        
        self.removeStu.ok_btn.clicked.connect(self.submit)
        self.removeStu.cancel_btn.clicked.connect(self.close)

    def submit(self):
        studentList = []
        addressCounter = 0
        guardCounter = 0
        secondaryGuardCounter = 0
        #self.removeStu.studentListView.model().removeRow(refresh)

        for selected in self.removeStu.studentListView.selectedIndexes():
            studentList.append(str(selected.data()))
        for student in studentList:
            print(student)
            getId = QSqlQuery()
            getId.exec_("Select Student_id FROM Student WHERE \
                         Student_name = '%s'" % student)
            while getId.next():
                record = getId.record()
                self.id = int(record.value(0))

            getAddress = QSqlQuery()
            getAddress.exec_("Select Student_address from Student WHERE \
                Student_address = (Select Student_address from Student WHERE\
                Student_name = '%s')" % student)
            while getAddress.next():
                record = getAddress.record()
                addressId = int(record.value(0))
                addressCounter += 1

            getGuardian = QSqlQuery()
            getGuardian.exec_("Select Guardian_primary, Guardian_secondary from Student WHERE \
                Guardian_primary = (Select Guardian_primary from Student WHERE \
                Student_name = '%s') AND  (Guardian_secondary = (Select Guardian_secondary from Student WHERE \
                Student_name = '%s') OR Guardian_secondary IS NULL) " % (student, student))
            while getGuardian.next():
                record = getGuardian.record()
                guardId = int(record.value(0))
                guardIdSecondary = int(record.value(1))
                print(guardId)
                print(guardIdSecondary)
                guardCounter += 1
                if (guardIdSecondary != None):
                    secondaryGuardCounter += 1
            

            self.confirmMessage = "Are you sure you want to remove '%s' from the system? This will remove all relevant information, including payments and billing. This action can not be reversed." \
                                 %(student)
            self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if (self.confirmReply == QtGui.QMessageBox.Yes):
                self.confirm = QSqlQuery()
                self.confirm.exec_("DELETE from Student WHERE Student_name = '%s'" % student)
                self.confirm.exec_("DELETE from Student_Class WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Credits WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Discount WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Payment WHERE Student_id = %d" % self.id)
            
                if (addressCounter == 1):
                    self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)
                    
                if (guardCounter == 1):
                    addressCounter = 0
                    getAddress.exec_("Select Guardian_address from Guardian WHERE \
                       Guardian_address = (Select Guardian_address from Guardian WHERE\
                       Graudian_id = %d)" % guardId)
                    while getAddress.next():
                        record = getAddress.record()
                        addressId = int(record.value(0))
                        print(addressId)
                        addressCounter += 1

                    if (addressCounter == 1):
                        self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)
                        
                    self.confirm.exec_("DELETE from Guardian WHERE Guardian_id = %d" % guardId)

                if (secondaryGuardCounter == 1):
                    addressCounter = 0
                    getAddress.exec_("Select Guardian_address from Guardian WHERE \
                       Guardian_address = (Select Guardian_address from Guardian WHERE\
                       Graudian_id = %d)" % guardIdSecondary)
                    
                    while getAddress.next():
                        record = getAddress.record()
                        addressId = int(record.value(0))
                        addressCounter += 1

                    if (addressCounter == 1):
                        self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)

                    
                    self.confirm.exec_("DELETE from Guardian WHERE Guardian_id = %d" % guardIdSecondary)

                self.message = "Student removed"
                self.refreshModel()
            
                self.confirmReply = QtGui.QMessageBox.information(self, 'Message', 
                    self.message)

    def refreshModel(self):
        self.model.clear()
        self.student_query = QSqlQuery()
        self.student_query.exec_("Select Student_name FROM Student")
        while self.student_query.next():
            record = self.student_query.record()
            item = QtGui.QStandardItem()
            self.name = str(record.value(0))
            item.setText(self.name)
            self.model.appendRow(item)

        self.removeStu.studentListView.setModel(self.model)
        self.removeStu.studentListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        


    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = removeStudentData()
window.show()
sys.exit(app.exec_())
        
