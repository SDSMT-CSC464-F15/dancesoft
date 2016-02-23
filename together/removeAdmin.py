import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from removeAdminDialog import Ui_removeAdminDialog
from PyQt4.QtSql import *

class removeAdmin(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.removeAd = Ui_removeAdminDialog()
        self.removeAd.setupUi(self)

        self.conn()

        self.removeAd.sel_ad = QSqlRelationalTableModel(db = self.db)
        self.removeAd.sel_ad.setTable("Admin")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        self.ad_query = QSqlQuery()
        self.ad_query.exec_("Select Admin_name FROM Admin")
        while self.ad_query.next():
            record = self.ad_query.record()
            self.name = str(record.value(0))
            self.removeAd.adminComboBox.addItem(self.name)
            
        self.removeAd.ok_btn.clicked.connect(self.submit)

        self.removeAd.cancel_btn.clicked.connect(self.close)

    def submit(self):
        self.addressCounter = 0
        self.selectedAd = self.removeAd.adminComboBox.currentText()

        self.getId = QSqlQuery()
        self.getId.exec_("Select Admin_id FROM Admin WHERE \
                         Admin_name = '%s'" % self.selectedAd)
        while self.getId.next():
            record = self.getId.record()
            self.id = int(record.value(0))

        self.getAddress = QSqlQuery()
        self.getAddress.exec_("Select Admin_address from Admin WHERE \
            Admin_address = (Select Admin_address from Admin WHERE\
            Admin_name = '%s')" % self.selectedAd)
        while self.getAddress.next():
            record = self.getAddress.record()
            self.addressId = int(record.value(0))
            self.addressCounter += 1
            

        self.confirmMessage = "Are you sure you want to remove '%s' from the system? This can not be reversed." \
                                 %(self.selectedAd)
        self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        self.checkMessage = "Remove all admin information? Click no to just remove admin permissions"
        self.checkReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.checkMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if (self.confirmReply == QtGui.QMessageBox.Yes):
            self.confirm_query = QSqlQuery()          
            self.ad_query.exec_("DELETE from Admin WHERE Admin_name = '%s'" % self.selectedAd)
            self.ad_query.exec_("DELETE from Account WHERE Admin_id = %d" % self.id)
            
            if (self.addressCounter == 1 and self.checkReply == QtGui.QMessageBox.Yes):
                self.ad_query.exec_("DELETE from Address WHERE Address_id = %d" % self.addressId)

            self.message = "Admin Removed"
            
            self.confirmReply = QtGui.QMessageBox.information(self, 'Message', 
                self.message)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = removeAdmin()
window.show()
sys.exit(app.exec_())
        
