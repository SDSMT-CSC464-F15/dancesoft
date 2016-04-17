# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Navi.ui'
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

class Ui_Navi(object):
    def setupUi(self, Navi):
        Navi.setObjectName(_fromUtf8("Navi"))
        Navi.resize(370, 165)
        self.Admin_btn = QtGui.QPushButton(Navi)
        self.Admin_btn.setGeometry(QtCore.QRect(100, 30, 161, 31))
        self.Admin_btn.setObjectName(_fromUtf8("Admin_btn"))
        self.Teacher_btn = QtGui.QPushButton(Navi)
        self.Teacher_btn.setGeometry(QtCore.QRect(100, 90, 161, 31))
        self.Teacher_btn.setObjectName(_fromUtf8("Teacher_btn"))

        self.retranslateUi(Navi)
        QtCore.QMetaObject.connectSlotsByName(Navi)

    def retranslateUi(self, Navi):
        Navi.setWindowTitle(_translate("Navi", "Landing Selection", None))
        self.Admin_btn.setText(_translate("Navi", "Administrator", None))
        self.Teacher_btn.setText(_translate("Navi", "Teacher", None))

