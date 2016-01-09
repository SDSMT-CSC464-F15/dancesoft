# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password.ui'
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

class Ui_change_password(object):
    def setupUi(self, change_password):
        change_password.setObjectName(_fromUtf8("change_password"))
        change_password.resize(419, 199)
        self.verticalLayoutWidget = QtGui.QWidget(change_password)
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
        self.change_btn.setObjectName(_fromUtf8("change_btn"))
        self.usernameLabel = QtGui.QLabel(self.groupBox)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.passwordLabel = QtGui.QLabel(self.groupBox)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.userLineEdit = QtGui.QLineEdit(self.groupBox)
        self.userLineEdit.setGeometry(QtCore.QRect(130, 40, 241, 20))
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.passwordLineEdit = QtGui.QLineEdit(self.groupBox)
        self.passwordLineEdit.setGeometry(QtCore.QRect(130, 70, 241, 20))
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.confirmLabel = QtGui.QLabel(self.groupBox)
        self.confirmLabel.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.confirmLabel.setObjectName(_fromUtf8("confirmLabel"))
        self.confirmLineEdit = QtGui.QLineEdit(self.groupBox)
        self.confirmLineEdit.setGeometry(QtCore.QRect(130, 100, 241, 20))
        self.confirmLineEdit.setObjectName(_fromUtf8("confirmLineEdit"))
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(change_password)
        QtCore.QMetaObject.connectSlotsByName(change_password)

    def retranslateUi(self, change_password):
        change_password.setWindowTitle(_translate("change_password", "Login", None))
        self.groupBox.setTitle(_translate("change_password", "Dance Arts", None))
        self.cancel_btn.setText(_translate("change_password", "Cancel", None))
        self.change_btn.setText(_translate("change_password", "Change", None))
        self.usernameLabel.setText(_translate("change_password", "Username", None))
        self.passwordLabel.setText(_translate("change_password", "Password", None))
        self.confirmLabel.setText(_translate("change_password", "Confirm Password", None))

