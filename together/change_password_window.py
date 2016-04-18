#change admin password
import sys
from PyQt4 import QtGui
from change_password import Ui_change_password
from PyQt4.QtSql import *


class password_window(QtGui.QDialog):
    def __init__(self, name):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_change_password()
        self.ui.setupUi(self)
        self.name = name;
        self.ui.change_btn.clicked.connect(self.update)
        self.ui.cancel_btn.clicked.connect(self.close)

    def update(self):
        # if cannot connect to database showing error window
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        # get username and password from gui
        self.input_name = self.ui.userLineEdit.text()
        self.input_pass = self.ui.passwordLineEdit.text()
        self.input_confirm = self.ui.confirmLineEdit.text()

        #check for password confirmation
        if self.input_pass != self.input_confirm:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter the same password")
            self.ui.userLineEdit.clear()
            self.ui.passwordLineEdit.clear()
            self.ui.confirmLineEdit.clear()

        elif self.input_pass == "":
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter a new password")
            self.ui.userLineEdit.clear()
            self.ui.passwordLineEdit.clear()
            self.ui.confirmLineEdit.clear()
        
        elif self.input_name != self.name:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter your username")
            self.ui.userLineEdit.clear()
            self.ui.passwordLineEdit.clear()
            self.ui.confirmLineEdit.clear()

        else: # make changes
            change_query = QSqlQuery()
            change_query.exec_("Update Account SET User_password='%s' WHERE User_name = '%s'" \
                               %(self.input_confirm, self.input_name))
            self.default_msg = "Password Changed"
            self.default_reply = QtGui.QMessageBox.information(self, 'Change Password', 
                        self.default_msg, QtGui.QMessageBox.Ok)
            self.close();
            

    # set up database connection 
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()


