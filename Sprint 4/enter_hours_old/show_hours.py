# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_hours.ui'
#
# Created: Tue Feb 23 12:59:27 2016
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

class Ui_Show_hours(object):
    def setupUi(self, Show_hours):
        Show_hours.setObjectName(_fromUtf8("Show_hours"))
        Show_hours.resize(468, 276)
        self.course_label = QtGui.QLabel(Show_hours)
        self.course_label.setGeometry(QtCore.QRect(50, 40, 71, 16))
        self.course_label.setObjectName(_fromUtf8("course_label"))
        self.course_lineEdit = QtGui.QLineEdit(Show_hours)
        self.course_lineEdit.setGeometry(QtCore.QRect(50, 70, 113, 20))
        self.course_lineEdit.setObjectName(_fromUtf8("course_lineEdit"))
        self.other_label = QtGui.QLabel(Show_hours)
        self.other_label.setGeometry(QtCore.QRect(240, 40, 71, 16))
        self.other_label.setObjectName(_fromUtf8("other_label"))
        self.other_lineEdit = QtGui.QLineEdit(Show_hours)
        self.other_lineEdit.setGeometry(QtCore.QRect(240, 70, 113, 20))
        self.other_lineEdit.setObjectName(_fromUtf8("other_lineEdit"))
        self.update_btn = QtGui.QPushButton(Show_hours)
        self.update_btn.setGeometry(QtCore.QRect(60, 200, 75, 23))
        self.update_btn.setObjectName(_fromUtf8("update_btn"))
        self.cancel_btn = QtGui.QPushButton(Show_hours)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 200, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))

        self.retranslateUi(Show_hours)
        QtCore.QMetaObject.connectSlotsByName(Show_hours)

    def retranslateUi(self, Show_hours):
        Show_hours.setWindowTitle(_translate("Show_hours", "Dialog", None))
        self.course_label.setText(_translate("Show_hours", "Course Hours", None))
        self.other_label.setText(_translate("Show_hours", "Other Hours", None))
        self.update_btn.setText(_translate("Show_hours", "Update", None))
        self.cancel_btn.setText(_translate("Show_hours", "Cancel", None))

