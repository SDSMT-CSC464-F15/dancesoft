# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set.ui'
#
# Created: Thu Feb 18 09:19:19 2016
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

class Ui_Semester_set_Dialog(object):
    def setupUi(self, Semester_set_Dialog):
        Semester_set_Dialog.setObjectName(_fromUtf8("Semester_set_Dialog"))
        Semester_set_Dialog.resize(400, 215)
        self.Set_btn = QtGui.QPushButton(Semester_set_Dialog)
        self.Set_btn.setGeometry(QtCore.QRect(60, 130, 75, 23))
        self.Set_btn.setObjectName(_fromUtf8("Set_btn"))
        self.Semester_comboBox = QtGui.QComboBox(Semester_set_Dialog)
        self.Semester_comboBox.setGeometry(QtCore.QRect(60, 40, 69, 22))
        self.Semester_comboBox.setObjectName(_fromUtf8("Semester_comboBox"))
        self.Semester_lineEdit = QtGui.QLineEdit(Semester_set_Dialog)
        self.Semester_lineEdit.setGeometry(QtCore.QRect(180, 40, 101, 20))
        self.Semester_lineEdit.setObjectName(_fromUtf8("Semester_lineEdit"))
        self.Add_btn = QtGui.QPushButton(Semester_set_Dialog)
        self.Add_btn.setGeometry(QtCore.QRect(200, 130, 75, 23))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))

        self.retranslateUi(Semester_set_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Semester_set_Dialog)

    def retranslateUi(self, Semester_set_Dialog):
        Semester_set_Dialog.setWindowTitle(_translate("Semester_set_Dialog", "Dialog", None))
        self.Set_btn.setText(_translate("Semester_set_Dialog", "Set", None))
        self.Add_btn.setText(_translate("Semester_set_Dialog", "Add", None))

