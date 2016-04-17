# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_history_detail.ui'
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

class Ui_Teacher_history_dialog(object):
    def setupUi(self, Teacher_history_dialog):
        Teacher_history_dialog.setObjectName(_fromUtf8("Teacher_history_dialog"))
        Teacher_history_dialog.resize(280, 381)
        self.history_listView = QtGui.QListView(Teacher_history_dialog)
        self.history_listView.setGeometry(QtCore.QRect(20, 20, 241, 321))
        self.history_listView.setObjectName(_fromUtf8("history_listView"))
        self.history_pushButton = QtGui.QPushButton(Teacher_history_dialog)
        self.history_pushButton.setGeometry(QtCore.QRect(190, 350, 75, 23))
        self.history_pushButton.setObjectName(_fromUtf8("history_pushButton"))

        self.retranslateUi(Teacher_history_dialog)
        QtCore.QMetaObject.connectSlotsByName(Teacher_history_dialog)

    def retranslateUi(self, Teacher_history_dialog):
        Teacher_history_dialog.setWindowTitle(_translate("Teacher_history_dialog", "Teacher History", None))
        self.history_pushButton.setText(_translate("Teacher_history_dialog", "Close", None))

