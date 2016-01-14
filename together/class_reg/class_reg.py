# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class_reg.ui'
#
# Created: Wed Dec 30 14:05:08 2015
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

class Ui_class_search(object):
    def setupUi(self, class_search):
        class_search.setObjectName(_fromUtf8("class_search"))
        class_search.resize(491, 352)
        self.approve_btn = QtGui.QPushButton(class_search)
        self.approve_btn.setGeometry(QtCore.QRect(50, 310, 101, 23))
        self.approve_btn.setObjectName(_fromUtf8("approve_btn"))
        self.reject_btn = QtGui.QPushButton(class_search)
        self.reject_btn.setGeometry(QtCore.QRect(180, 310, 101, 23))
        self.reject_btn.setObjectName(_fromUtf8("reject_btn"))
        self.cancel_btn = QtGui.QPushButton(class_search)
        self.cancel_btn.setGeometry(QtCore.QRect(320, 310, 101, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.class_listView = QtGui.QListView(class_search)
        self.class_listView.setGeometry(QtCore.QRect(20, 40, 201, 241))
        self.class_listView.setObjectName(_fromUtf8("class_listView"))
        self.student_listView = QtGui.QListView(class_search)
        self.student_listView.setGeometry(QtCore.QRect(270, 40, 201, 241))
        self.student_listView.setObjectName(_fromUtf8("student_listView"))

        self.retranslateUi(class_search)
        QtCore.QMetaObject.connectSlotsByName(class_search)

    def retranslateUi(self, class_search):
        class_search.setWindowTitle(_translate("class_search", "Dialog", None))
        self.approve_btn.setText(_translate("class_search", "Approve", None))
        self.reject_btn.setText(_translate("class_search", "Reject", None))
        self.cancel_btn.setText(_translate("class_search", "Cancel", None))

