# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Class_list.ui'
#
# Created: Sun Mar 20 11:51:49 2016
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
        Class_list_Dialog.resize(891, 599)
        self.Class_drop_tableView = QtGui.QTableView(Class_list_Dialog)
        self.Class_drop_tableView.setGeometry(QtCore.QRect(20, 40, 411, 501))
        self.Class_drop_tableView.setObjectName(_fromUtf8("Class_drop_tableView"))
        self.Add_btn = QtGui.QPushButton(Class_list_Dialog)
        self.Add_btn.setGeometry(QtCore.QRect(640, 560, 81, 21))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.Drop_btn = QtGui.QPushButton(Class_list_Dialog)
        self.Drop_btn.setGeometry(QtCore.QRect(150, 560, 81, 21))
        self.Drop_btn.setObjectName(_fromUtf8("Drop_btn"))
        self.Class_add_tableView = QtGui.QTableView(Class_list_Dialog)
        self.Class_add_tableView.setGeometry(QtCore.QRect(460, 40, 411, 501))
        self.Class_add_tableView.setObjectName(_fromUtf8("Class_add_tableView"))
        self.Reg_label = QtGui.QLabel(Class_list_Dialog)
        self.Reg_label.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.Reg_label.setObjectName(_fromUtf8("Reg_label"))
        self.Avail_label = QtGui.QLabel(Class_list_Dialog)
        self.Avail_label.setGeometry(QtCore.QRect(470, 10, 151, 21))
        self.Avail_label.setObjectName(_fromUtf8("Avail_label"))

        self.retranslateUi(Class_list_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Class_list_Dialog)

    def retranslateUi(self, Class_list_Dialog):
        Class_list_Dialog.setWindowTitle(_translate("Class_list_Dialog", "Dialog", None))
        self.Add_btn.setText(_translate("Class_list_Dialog", "Add", None))
        self.Drop_btn.setText(_translate("Class_list_Dialog", "Drop", None))
        self.Reg_label.setText(_translate("Class_list_Dialog", "Class registered", None))
        self.Avail_label.setText(_translate("Class_list_Dialog", "Available classes", None))

