from PyQt4 import QtGui
from PyQt4.QtSql import *
import os, sys

class Login(QtGui.QDialog):
    
    def __init__(self):
        super(Login, self).__init__()
        self.user_access_level = -1
        print "isthis"
        self.initUI()

    def initUI(self):
        
        #set the window's size
        self.setWindowTitle('Login')
        self.resize(394, 171) 
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(9, 9, 379, 151)
       
        
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)

        #add frame of Dance Arts
        self.groupBox = QtGui.QGroupBox('Dance Arts', self.verticalLayoutWidget) 
        self.groupBox.setAutoFillBackground(True)

        #login button
        self.loginButton = QtGui.QPushButton('Login',self.groupBox)
        self.loginButton.setGeometry(200, 110, 75, 23)

        #cancel button (exit login page)
        self.cancelButton = QtGui.QPushButton('Cancel',self.groupBox)
        self.cancelButton.setGeometry(280, 110, 75, 23)
        
        #link two buttons to different functions 
        self.loginButton.clicked.connect(self.handleLogin)
        self.cancelButton.clicked.connect(sys.exit)

        #username input box
        self.textName = QtGui.QLineEdit(self.groupBox)
        self.textName.setGeometry(80, 50, 271, 20)
        
        #password input box with mask
        self.textPass = QtGui.QLineEdit(self.groupBox)
        self.textPass.setGeometry(80, 80, 271, 20)
        self.textPass.setAutoFillBackground(False)
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        
        #username label
        self.nameLabel = QtGui.QLabel('Username',self.groupBox)
        self.nameLabel.setGeometry(10, 50, 61, 20)
      
        #password label
        self.passLabel = QtGui.QLabel('Password', self.groupBox)
        self.passLabel.setGeometry(10, 80, 61, 16)

  
        self.verticalLayout.addWidget(self.groupBox)


    def handleLogin(self):
        # if cannot connect to database showing error window
        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')
        
        # create sql query to retrieve username, password, accesslevel
        query = QSqlQuery()
        query.exec_("SELECT User_name, User_password, Access_level FROM Account")

        # get username and password from gui
        input_name = self.textName.text()
        input_pass = self.textPass.text() 

        #this flag for detect weather the username and password are valid
        self.flag = False
        
        while query.next():
            # get username, password and accesslevel from database
            user_name = query.value(0).toString()
            user_password = query.value(1).toString()
            user_access_level = query.value(2).toInt()

            # campare above information to the user inputted information
            if (user_name == input_name and user_password == input_pass):
                # if valid user found, set flag true
                self.flag = True
                # save personal information once the valid information found 
                self.user_name = user_name
                self.user_password = user_password
                self.user_access_level = user_access_level[0]

                #test.....
                if self.user_access_level == 1:
                    QtGui.QMessageBox.warning(
                self, 'message', 'admin')
                
                elif self.user_access_level == 2:
                    
                    from Teacher import Teacher_window
                    self.tea = Teacher_window()
                    self.tea.show()
                    
                    

                '''
                self.accept()
                '''
                
                
        # if user not found, show error message.              
        if not self.flag:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Invalid user or password')

    # set up database connection 
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()


def main():
    import sys
    app = QtGui.QApplication(sys.argv)

    
    Login().exec_()

'''
    if Login().exec_() == QtGui.QDialog.Accepted:
        print ''
        from Teacher import Teacher_window
        window = Teacher_window()
        window.show()
        sys.exit(app.exec_())

'''       


if __name__ == '__main__':
    main()


'''
    if window.exec_() == QtGui.QDialog.Accepted:
        if window.user_access_level == 1:
            window = Window()
            window.show()
            sys.exit(app.exec_())
'''
