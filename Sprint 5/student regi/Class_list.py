# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Class_list.ui'
#
# Created: Thu Mar 17 10:20:02 2016
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Class_list_Dialog(object):
    def setupUi(self, Class_list_Dialog):
        Class_list_Dialog.setObjectName(_fromUtf8("Class_list_Dialog"))
        Class_list_Dialog.resize(357, 420)
        self.Class_tableView = QtGui.QTableView(Class_list_Dialog)
        self.Class_tableView.setGeometry(QtCore.QRect(30, 20, 301, 341))
        self.Class_tableView.setObjectName(_fromUtf8("Class_tableView"))
        self.Add_btn = QtGui.QPushButton(Class_list_Dialog)
        self.Add_btn.setGeometry(QtCore.QRect(40, 380, 81, 21))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.Drop_btn = QtGui.QPushButton(Class_list_Dialog)
        self.Drop_btn.setGeometry(QtCore.QRect(234, 380, 81, 21))
        self.Drop_btn.setObjectName(_fromUtf8("Drop_btn"))

        self.retranslateUi(Class_list_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Class_list_Dialog)

    def retranslateUi(self, Class_list_Dialog):
        Class_list_Dialog.setWindowTitle(_translate("Class_list_Dialog", "Dialog", None))
        self.Add_btn.setText(_translate("Class_list_Dialog", "Add", None))
        self.Drop_btn.setText(_translate("Class_list_Dialog", "Drop", None))

