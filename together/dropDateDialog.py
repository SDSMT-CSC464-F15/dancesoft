# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dropDateDialog.ui'
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

class Ui_dropDateDialog(object):
    def setupUi(self, dropDateDialog):
        dropDateDialog.setObjectName(_fromUtf8("dropDateDialog"))
        dropDateDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(dropDateDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(dropDateDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.dropDateLabel = QtGui.QLabel(dropDateDialog)
        self.dropDateLabel.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.dropDateLabel.setObjectName(_fromUtf8("dropDateLabel"))
        self.dropDateEdit = QtGui.QDateEdit(dropDateDialog)
        self.dropDateEdit.setGeometry(QtCore.QRect(130, 30, 201, 22))
        self.dropDateEdit.setObjectName(_fromUtf8("dropDateEdit"))

        self.retranslateUi(dropDateDialog)
        QtCore.QMetaObject.connectSlotsByName(dropDateDialog)

    def retranslateUi(self, dropDateDialog):
        dropDateDialog.setWindowTitle(_translate("dropDateDialog", "Drop Date", None))
        self.ok_btn.setText(_translate("dropDateDialog", "OK", None))
        self.cancel_btn.setText(_translate("dropDateDialog", "Cancel", None))
        self.dropDateLabel.setText(_translate("dropDateDialog", "Enter Drop Date", None))

