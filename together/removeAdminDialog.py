# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeAdminDialog.ui'
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

class Ui_removeAdminDialog(object):
    def setupUi(self, removeAdminDialog):
        removeAdminDialog.setObjectName(_fromUtf8("removeAdminDialog"))
        removeAdminDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(removeAdminDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(removeAdminDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.adminNameLabel = QtGui.QLabel(removeAdminDialog)
        self.adminNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.adminNameLabel.setObjectName(_fromUtf8("adminNameLabel"))
        self.adminComboBox = QtGui.QComboBox(removeAdminDialog)
        self.adminComboBox.setGeometry(QtCore.QRect(100, 30, 231, 22))
        self.adminComboBox.setObjectName(_fromUtf8("adminComboBox"))

        self.retranslateUi(removeAdminDialog)
        QtCore.QMetaObject.connectSlotsByName(removeAdminDialog)

    def retranslateUi(self, removeAdminDialog):
        removeAdminDialog.setWindowTitle(_translate("removeAdminDialog", "Remove Admin", None))
        self.ok_btn.setText(_translate("removeAdminDialog", "OK", None))
        self.cancel_btn.setText(_translate("removeAdminDialog", "Cancel", None))
        self.adminNameLabel.setText(_translate("removeAdminDialog", "Admin Name", None))

