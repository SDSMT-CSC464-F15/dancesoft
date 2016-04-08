import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from removeClassDialog import Ui_removeClassDialog
from PyQt4.QtSql import *

class removeClass(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.removeClass = Ui_removeClassDialog()
        self.removeClass.setupUi(self)

        self.conn()

        self.removeClass.sel_class = QSqlRelationalTableModel(db = self.db)
        self.removeClass.sel_class.setTable("Class")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        self.idList = []

        self.class_query = QSqlQuery()
        self.class_query.exec_("Select Class_id, Class_name FROM Class")
        while self.class_query.next():
            record = self.class_query.record()
            self.id = str(record.value(0))
            self.name = str(record.value(1))
            self.idList.append(self.id)
            self.removeClass.classComboBox.addItem(self.name)
            
        self.removeClass.ok_btn.clicked.connect(self.submit)

        self.removeClass.cancel_btn.clicked.connect(self.close)

    def submit(self):
        self.selectedClass = self.removeClass.classComboBox.currentIndex()
        self.selectedClass = self.idList[self.selectedClass]
        self.name = self.removeClass.classComboBox.currentText()
        print(self.selectedClass, self.name)
        
        self.confirmMessage = "Are you sure you want to remove '%s' from the system? This will remove all relevant information and can not be reversed." \
                                 %(self.name)
        self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if (self.confirmReply == QtGui.QMessageBox.Yes):
            self.confirm_query = QSqlQuery()
            self.class_query.exec_("DELETE from Class WHERE Class_id = '%s'" % self.selectedClass)
            self.teachClass_query = QSqlQuery()
            self.teachClass_query.exec_("DELETE from Teacher_Class WHERE Class_id = '%s'" % self.selectedClass)
            

            self.message = "Class Removed"
            
            self.confirmReply = QtGui.QMessageBox.information(self, 'Class Removed', 
                self.message)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = removeClass()
window.show()
sys.exit(app.exec_())
        
