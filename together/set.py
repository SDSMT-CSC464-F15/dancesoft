# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set.ui'
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

class Ui_Semester_set_Dialog(object):
    def setupUi(self, Semester_set_Dialog):
        Semester_set_Dialog.setObjectName(_fromUtf8("Semester_set_Dialog"))
        Semester_set_Dialog.resize(400, 215)
        self.Set_btn = QtGui.QPushButton(Semester_set_Dialog)
        self.Set_btn.setGeometry(QtCore.QRect(30, 130, 81, 23))
        self.Set_btn.setObjectName(_fromUtf8("Set_btn"))
        self.Add_btn = QtGui.QPushButton(Semester_set_Dialog)
        self.Add_btn.setGeometry(QtCore.QRect(250, 130, 81, 23))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.Year_spinBox = QtGui.QSpinBox(Semester_set_Dialog)
        self.Year_spinBox.setGeometry(QtCore.QRect(250, 40, 101, 22))
        self.Year_spinBox.setObjectName(_fromUtf8("Year_spinBox"))
        self.Term_comboBox = QtGui.QComboBox(Semester_set_Dialog)
        self.Term_comboBox.setGeometry(QtCore.QRect(250, 80, 101, 22))
        self.Term_comboBox.setObjectName(_fromUtf8("Term_comboBox"))
        self.Term_comboBox.addItem(_fromUtf8(""))
        self.Term_comboBox.addItem(_fromUtf8(""))
        self.Term_comboBox.addItem(_fromUtf8(""))
        self.Semester_comboBox = QtGui.QComboBox(Semester_set_Dialog)
        self.Semester_comboBox.setGeometry(QtCore.QRect(30, 40, 101, 22))
        self.Semester_comboBox.setObjectName(_fromUtf8("Semester_comboBox"))
        self.Set_label = QtGui.QLabel(Semester_set_Dialog)
        self.Set_label.setGeometry(QtCore.QRect(30, 10, 151, 16))
        self.Set_label.setObjectName(_fromUtf8("Set_label"))
        self.Add_label = QtGui.QLabel(Semester_set_Dialog)
        self.Add_label.setGeometry(QtCore.QRect(250, 10, 151, 16))
        self.Add_label.setObjectName(_fromUtf8("Add_label"))

        self.retranslateUi(Semester_set_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Semester_set_Dialog)

    def retranslateUi(self, Semester_set_Dialog):
        Semester_set_Dialog.setWindowTitle(_translate("Semester_set_Dialog", "Set Semester", None))
        self.Set_btn.setText(_translate("Semester_set_Dialog", "Set", None))
        self.Add_btn.setText(_translate("Semester_set_Dialog", "Add", None))
        self.Term_comboBox.setItemText(0, _translate("Semester_set_Dialog", "Term1", None))
        self.Term_comboBox.setItemText(1, _translate("Semester_set_Dialog", "Term2", None))
        self.Term_comboBox.setItemText(2, _translate("Semester_set_Dialog", "Term3", None))
        self.Set_label.setText(_translate("Semester_set_Dialog", "Set current semester:", None))
        self.Add_label.setText(_translate("Semester_set_Dialog", "Add new semester:", None))

