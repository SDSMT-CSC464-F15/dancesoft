# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locationDialog.ui'
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

class Ui_locationDialog(object):
    def setupUi(self, locationDialog):
        locationDialog.setObjectName(_fromUtf8("locationDialog"))
        locationDialog.resize(357, 111)
        self.ok_btn = QtGui.QPushButton(locationDialog)
        self.ok_btn.setGeometry(QtCore.QRect(180, 70, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(locationDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.locationNameLabel = QtGui.QLabel(locationDialog)
        self.locationNameLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.locationNameLabel.setObjectName(_fromUtf8("locationNameLabel"))
        self.locationLineEdit = QtGui.QLineEdit(locationDialog)
        self.locationLineEdit.setGeometry(QtCore.QRect(100, 30, 231, 20))
        self.locationLineEdit.setObjectName(_fromUtf8("locationLineEdit"))

        self.retranslateUi(locationDialog)
        QtCore.QMetaObject.connectSlotsByName(locationDialog)

    def retranslateUi(self, locationDialog):
        locationDialog.setWindowTitle(_translate("locationDialog", "Dialog", None))
        self.ok_btn.setText(_translate("locationDialog", "OK", None))
        self.cancel_btn.setText(_translate("locationDialog", "Cancel", None))
        self.locationNameLabel.setText(_translate("locationDialog", "New Location", None))

