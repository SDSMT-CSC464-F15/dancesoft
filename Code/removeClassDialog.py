# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeClassDialog.ui'
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

class Ui_removeClassDialog(object):
    def setupUi(self, removeClassDialog):
        removeClassDialog.setObjectName(_fromUtf8("removeClassDialog"))
        removeClassDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(removeClassDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(removeClassDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.classNameLabel = QtGui.QLabel(removeClassDialog)
        self.classNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.classNameLabel.setObjectName(_fromUtf8("classNameLabel"))
        self.classComboBox = QtGui.QComboBox(removeClassDialog)
        self.classComboBox.setGeometry(QtCore.QRect(100, 30, 231, 22))
        self.classComboBox.setObjectName(_fromUtf8("classComboBox"))

        self.retranslateUi(removeClassDialog)
        QtCore.QMetaObject.connectSlotsByName(removeClassDialog)

    def retranslateUi(self, removeClassDialog):
        removeClassDialog.setWindowTitle(_translate("removeClassDialog", "Dialog", None))
        self.ok_btn.setText(_translate("removeClassDialog", "OK", None))
        self.cancel_btn.setText(_translate("removeClassDialog", "Cancel", None))
        self.classNameLabel.setText(_translate("removeClassDialog", "Class Name", None))

