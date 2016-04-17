# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeTeacherDialog.ui'
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

class Ui_removeTeacherDialog(object):
    def setupUi(self, removeTeacherDialog):
        removeTeacherDialog.setObjectName(_fromUtf8("removeTeacherDialog"))
        removeTeacherDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(removeTeacherDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(removeTeacherDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.teacherNameLabel = QtGui.QLabel(removeTeacherDialog)
        self.teacherNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.teacherNameLabel.setObjectName(_fromUtf8("teacherNameLabel"))
        self.teacherComboBox = QtGui.QComboBox(removeTeacherDialog)
        self.teacherComboBox.setGeometry(QtCore.QRect(100, 30, 231, 22))
        self.teacherComboBox.setObjectName(_fromUtf8("teacherComboBox"))

        self.retranslateUi(removeTeacherDialog)
        QtCore.QMetaObject.connectSlotsByName(removeTeacherDialog)

    def retranslateUi(self, removeTeacherDialog):
        removeTeacherDialog.setWindowTitle(_translate("removeTeacherDialog", "Remove Teacher", None))
        self.ok_btn.setText(_translate("removeTeacherDialog", "OK", None))
        self.cancel_btn.setText(_translate("removeTeacherDialog", "Cancel", None))
        self.teacherNameLabel.setText(_translate("removeTeacherDialog", "Teacher Name", None))

