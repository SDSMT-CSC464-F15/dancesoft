# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(400, 171)
        self.verticalLayoutWidget = QtGui.QWidget(Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(270, 100, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 271, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 70, 271, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.groupBox.setTitle(_translate("Login", "Dance Arts", None))
        self.pushButton.setText(_translate("Login", "Cancel", None))
        self.pushButton_2.setText(_translate("Login", "Login", None))
        self.label.setText(_translate("Login", "Username", None))
        self.label_2.setText(_translate("Login", "Password", None))

