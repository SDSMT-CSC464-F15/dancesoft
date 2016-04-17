# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAdminDialog.ui'
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

class Ui_addAdminDialog(object):
    def setupUi(self, addAdminDialog):
        addAdminDialog.setObjectName(_fromUtf8("addAdminDialog"))
        addAdminDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(addAdminDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(addAdminDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.teacherNameLabel = QtGui.QLabel(addAdminDialog)
        self.teacherNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.teacherNameLabel.setObjectName(_fromUtf8("teacherNameLabel"))
        self.teacherComboBox = QtGui.QComboBox(addAdminDialog)
        self.teacherComboBox.setGeometry(QtCore.QRect(100, 30, 231, 22))
        self.teacherComboBox.setObjectName(_fromUtf8("teacherComboBox"))

        self.retranslateUi(addAdminDialog)
        QtCore.QMetaObject.connectSlotsByName(addAdminDialog)

    def retranslateUi(self, addAdminDialog):
        addAdminDialog.setWindowTitle(_translate("addAdminDialog", "Add Admin", None))
        self.ok_btn.setText(_translate("addAdminDialog", "OK", None))
        self.cancel_btn.setText(_translate("addAdminDialog", "Cancel", None))
        self.teacherNameLabel.setText(_translate("addAdminDialog", "Teacher Name", None))

