import sys
from PyQt4 import QtGui
from change_password import Ui_change_password
from PyQt4.QtSql import *


class password_window(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.user_access_level = -1
        self.ui = Ui_change_password()
        self.ui.setupUi(self)
        self.ui.change_btn.clicked.connect(self.update)
        self.ui.cancel_btn.clicked.connect(self.close)

    def update(self):
        # if cannot connect to database showing error window
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        # get username and password from gui
        input_name = self.ui.userLineEdit.text()
        input_pass = self.ui.passwordLineEdit.text()
        input_confirm = self.ui.confirmLineEdit.text()

        if input_pass != input_confirm:
            QtGui.QMessageBox.warning(
                self, 'Error', "Please enter the same password")
            self.ui.userLineEdit.clear()
            self.ui.passwordLineEdit.clear()
            self.ui.confirmLineEdit.clear()

        else:
            change_query = QSqlQuery()
            change_query.exec_("Update Account SET User_name='%s', User_password='%s' WHERE User_name = '%s'" %(name))
            name = input_name

    # set up database connection 
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
Current_Window = password_window()
Current_Window.show()
sys.exit(app.exec_())



