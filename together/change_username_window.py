import sys
from PyQt4 import QtGui
from change_username import Ui_change_username
from PyQt4.QtSql import *


class username_window(QtGui.QDialog):
    def __init__(self, name):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_change_username()
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
        self.input_newName = self.ui.newUserLineEdit.text()
        self.input_confirm = self.ui.confirmLineEdit.text()

        self.checkQuery = QSqlQuery()
        self.checkQuery.exec_("Select User_password From Account Where User_name = '%s'"\
                              % (self.name))
        if self.checkQuery.next():
            record = self.checkQuery.record()
            self.confirm = str(record.value(0))
            

        #check for password confirmation
        if self.confirm != self.input_confirm:
            QtGui.QMessageBox.warning(
                self, 'Error', "Incorrect Password")
            self.ui.userLineEdit.clear()
            self.ui.passwordLineEdit.clear()
            self.ui.confirmLineEdit.clear()

        elif self.input_newName == "":
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter a new username")
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
            change_query.exec_("Update Account SET User_name ='%s' WHERE User_name = '%s'" \
                               %(self.input_newName, self.input_name))
            self.default_msg = "Username Changed"
            self.default_reply = QtGui.QMessageBox.information(self, 'Change Username', 
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


