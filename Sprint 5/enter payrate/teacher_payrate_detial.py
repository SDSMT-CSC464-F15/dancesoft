# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_payrate_detail.ui'
#
# Created: Thu Mar 10 14:31:13 2016
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

class Ui_teacher_payrate_dialog(object):
    def setupUi(self, teacher_payrate_dialog):
        teacher_payrate_dialog.setObjectName(_fromUtf8("teacher_payrate_dialog"))
        teacher_payrate_dialog.resize(384, 189)
        self.Payname_label = QtGui.QLabel(teacher_payrate_dialog)
        self.Payname_label.setGeometry(QtCore.QRect(30, 20, 54, 16))
        self.Payname_label.setObjectName(_fromUtf8("Payname_label"))
        self.label_2 = QtGui.QLabel(teacher_payrate_dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 54, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Payname_lineEdit = QtGui.QLineEdit(teacher_payrate_dialog)
        self.Payname_lineEdit.setGeometry(QtCore.QRect(90, 20, 81, 20))
        self.Payname_lineEdit.setObjectName(_fromUtf8("Payname_lineEdit"))
        self.Payrate_lineEdit = QtGui.QLineEdit(teacher_payrate_dialog)
        self.Payrate_lineEdit.setGeometry(QtCore.QRect(240, 20, 81, 20))
        self.Payrate_lineEdit.setObjectName(_fromUtf8("Payrate_lineEdit"))
        self.Add_btn = QtGui.QPushButton(teacher_payrate_dialog)
        self.Add_btn.setGeometry(QtCore.QRect(70, 150, 75, 23))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.Update_btn = QtGui.QPushButton(teacher_payrate_dialog)
        self.Update_btn.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.Update_btn.setObjectName(_fromUtf8("Update_btn"))
        self.Payname_comboBox = QtGui.QComboBox(teacher_payrate_dialog)
        self.Payname_comboBox.setGeometry(QtCore.QRect(90, 80, 81, 22))
        self.Payname_comboBox.setObjectName(_fromUtf8("Payname_comboBox"))
        self.Payrate_update_lineEdit = QtGui.QLineEdit(teacher_payrate_dialog)
        self.Payrate_update_lineEdit.setGeometry(QtCore.QRect(240, 80, 81, 20))
        self.Payrate_update_lineEdit.setObjectName(_fromUtf8("Payrate_update_lineEdit"))

        self.retranslateUi(teacher_payrate_dialog)
        QtCore.QMetaObject.connectSlotsByName(teacher_payrate_dialog)

    def retranslateUi(self, teacher_payrate_dialog):
        teacher_payrate_dialog.setWindowTitle(_translate("teacher_payrate_dialog", "Dialog", None))
        self.Payname_label.setText(_translate("teacher_payrate_dialog", "Payname", None))
        self.label_2.setText(_translate("teacher_payrate_dialog", "Payrate", None))
        self.Add_btn.setText(_translate("teacher_payrate_dialog", "Add", None))
        self.Update_btn.setText(_translate("teacher_payrate_dialog", "Update", None))

