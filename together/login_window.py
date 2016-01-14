import sys
from PyQt4 import QtGui
from login import Ui_Login
from PyQt4.QtSql import *
from Navi_dialog import Navi_dialog
from Admin import Admin_window
from Teacher import Teacher_window


name = '' #keep track of user name

class Login_Window(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.user_access_level = -1
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.handleLogin)
        self.ui.pushButton.clicked.connect(self.close)

    def handleLogin(self):
        # if cannot connect to database showing error window
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
        
        # create sql query to retrieve username, password, accesslevel
        query = QSqlQuery()
        query.exec_("SELECT User_name, User_password, Access_level FROM Account")

        # get username and password from gui
        input_name = self.ui.lineEdit.text()
        input_pass = self.ui.lineEdit_2.text() 

        #this flag for detect weather the username and password are valid
        self.flag = False
        
        while query.next():
            # get username, password and accesslevel from database
            user_name = str(query.value(0))
            user_password = str(query.value(1))
            user_access_level = int(query.value(2))
            
            # campare above information to the user inputted information
            if (user_name == input_name and user_password == input_pass):
                # if valid user found, set flag true
                self.flag = True
                
                global name
                name = user_name
                
                # save personal information once the valid information found 
                self.user_access_level = user_access_level
                #test.....
                if self.user_access_level == 1:   
                    self.done(self.user_access_level)
                
                elif self.user_access_level == 2:           
                    self.done(self.user_access_level)
                
                
        # if user not found, show error message.              
        if not self.flag:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Invalid user or password')
            self.ui.lineEdit_2.clear()

    # set up database connection 
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

def main():
    app = QtGui.QApplication(sys.argv)
    sign = Login_Window().exec_()

    flag = 0

    if sign == 1:
        flag = Navi_dialog(sign).exec_()

    
    global name

    if flag == 1:
        window = Admin_window(name)
        window.show()
        sys.exit(app.exec_())
    elif flag == 2:
        window = Teacher_window(name)
        window.show()
        sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()



