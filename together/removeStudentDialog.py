# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeStudentDialog.ui'
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

class Ui_removeStudentDialog(object):
    def setupUi(self, removeStudentDialog):
        removeStudentDialog.setObjectName(_fromUtf8("removeStudentDialog"))
        removeStudentDialog.resize(398, 203)
        self.ok_btn = QtGui.QPushButton(removeStudentDialog)
        self.ok_btn.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(removeStudentDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(310, 160, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.studentNameLabel = QtGui.QLabel(removeStudentDialog)
        self.studentNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.studentNameLabel.setObjectName(_fromUtf8("studentNameLabel"))
        self.studentListView = QtGui.QListView(removeStudentDialog)
        self.studentListView.setGeometry(QtCore.QRect(70, 30, 141, 151))
        self.studentListView.setObjectName(_fromUtf8("studentListView"))

        self.retranslateUi(removeStudentDialog)
        QtCore.QMetaObject.connectSlotsByName(removeStudentDialog)

    def retranslateUi(self, removeStudentDialog):
        removeStudentDialog.setWindowTitle(_translate("removeStudentDialog", "Dialog", None))
        self.ok_btn.setText(_translate("removeStudentDialog", "OK", None))
        self.cancel_btn.setText(_translate("removeStudentDialog", "Cancel", None))
        self.studentNameLabel.setText(_translate("removeStudentDialog", "Students", None))

