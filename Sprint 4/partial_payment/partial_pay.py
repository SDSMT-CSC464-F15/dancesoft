# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'partial_pay.ui'
#
# Created: Thu Feb 11 10:19:14 2016
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

class Ui_Partial_pay(object):
    def setupUi(self, Partial_pay):
        Partial_pay.setObjectName(_fromUtf8("Partial_pay"))
        Partial_pay.resize(400, 208)
        self.Amount_label = QtGui.QLabel(Partial_pay)
        self.Amount_label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.Amount_label.setObjectName(_fromUtf8("Amount_label"))
        self.Amount_lineEdit = QtGui.QLineEdit(Partial_pay)
        self.Amount_lineEdit.setGeometry(QtCore.QRect(110, 40, 161, 21))
        self.Amount_lineEdit.setObjectName(_fromUtf8("Amount_lineEdit"))
        self.Type_label = QtGui.QLabel(Partial_pay)
        self.Type_label.setGeometry(QtCore.QRect(40, 90, 71, 21))
        self.Type_label.setObjectName(_fromUtf8("Type_label"))
        self.Type_comboBox = QtGui.QComboBox(Partial_pay)
        self.Type_comboBox.setGeometry(QtCore.QRect(110, 90, 69, 22))
        self.Type_comboBox.setObjectName(_fromUtf8("Type_comboBox"))
        self.Semester_label = QtGui.QLabel(Partial_pay)
        self.Semester_label.setGeometry(QtCore.QRect(40, 140, 71, 21))
        self.Semester_label.setObjectName(_fromUtf8("Semester_label"))
        self.Semester_comboBox = QtGui.QComboBox(Partial_pay)
        self.Semester_comboBox.setGeometry(QtCore.QRect(110, 140, 69, 22))
        self.Semester_comboBox.setObjectName(_fromUtf8("Semester_comboBox"))

        self.retranslateUi(Partial_pay)
        QtCore.QMetaObject.connectSlotsByName(Partial_pay)

    def retranslateUi(self, Partial_pay):
        Partial_pay.setWindowTitle(_translate("Partial_pay", "Dialog", None))
        self.Amount_label.setText(_translate("Partial_pay", "Amount", None))
        self.Type_label.setText(_translate("Partial_pay", "Type", None))
        self.Semester_label.setText(_translate("Partial_pay", "Semester", None))

