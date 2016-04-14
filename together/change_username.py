# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_username.ui'
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

class Ui_change_username(object):
    def setupUi(self, change_username):
        change_username.setObjectName(_fromUtf8("change_username"))
        change_username.resize(423, 206)
        self.verticalLayoutWidget = QtGui.QWidget(change_username)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 401, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cancel_btn = QtGui.QPushButton(self.groupBox)
        self.cancel_btn.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.change_btn = QtGui.QPushButton(self.groupBox)
        self.change_btn.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.change_btn.setDefault(True)
        self.change_btn.setObjectName(_fromUtf8("change_btn"))
        self.usernameLabel = QtGui.QLabel(self.groupBox)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.newUserLabel = QtGui.QLabel(self.groupBox)
        self.newUserLabel.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.newUserLabel.setObjectName(_fromUtf8("newUserLabel"))
        self.userLineEdit = QtGui.QLineEdit(self.groupBox)
        self.userLineEdit.setGeometry(QtCore.QRect(100, 40, 271, 20))
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.newUserLineEdit = QtGui.QLineEdit(self.groupBox)
        self.newUserLineEdit.setGeometry(QtCore.QRect(100, 70, 271, 20))
        self.newUserLineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.newUserLineEdit.setObjectName(_fromUtf8("newUserLineEdit"))
        self.confirmLabel = QtGui.QLabel(self.groupBox)
        self.confirmLabel.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.confirmLabel.setObjectName(_fromUtf8("confirmLabel"))
        self.confirmLineEdit = QtGui.QLineEdit(self.groupBox)
        self.confirmLineEdit.setGeometry(QtCore.QRect(100, 100, 271, 20))
        self.confirmLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.confirmLineEdit.setObjectName(_fromUtf8("confirmLineEdit"))
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(change_username)
        QtCore.QMetaObject.connectSlotsByName(change_username)

    def retranslateUi(self, change_username):
        change_username.setWindowTitle(_translate("change_username", "Username", None))
        self.groupBox.setTitle(_translate("change_username", "Dance Arts", None))
        self.cancel_btn.setText(_translate("change_username", "Cancel", None))
        self.change_btn.setText(_translate("change_username", "Change", None))
        self.usernameLabel.setText(_translate("change_username", "Username", None))
        self.newUserLabel.setText(_translate("change_username", "New Username", None))
        self.confirmLabel.setText(_translate("change_username", "Password", None))

