# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clothing_Requirements.ui'
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

class Ui_Clothing_Requirements(object):
    def setupUi(self, Clothing_Requirements):
        Clothing_Requirements.setObjectName(_fromUtf8("Clothing_Requirements"))
        Clothing_Requirements.resize(551, 377)
        self.cancel = QtGui.QPushButton(Clothing_Requirements)
        self.cancel.setGeometry(QtCore.QRect(460, 340, 75, 23))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.submit = QtGui.QPushButton(Clothing_Requirements)
        self.submit.setGeometry(QtCore.QRect(370, 340, 75, 23))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.clothing_entry_field = QtGui.QTextEdit(Clothing_Requirements)
        self.clothing_entry_field.setGeometry(QtCore.QRect(10, 70, 531, 261))
        self.clothing_entry_field.setObjectName(_fromUtf8("clothin_entry_field"))
        self.clothing_text = QtGui.QLabel(Clothing_Requirements)
        self.clothing_text.setGeometry(QtCore.QRect(10, 10, 481, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(24)
        self.clothing_text.setFont(font)
        self.clothing_text.setObjectName(_fromUtf8("clothing_text"))

        self.retranslateUi(Clothing_Requirements)
        QtCore.QMetaObject.connectSlotsByName(Clothing_Requirements)

    def retranslateUi(self, Clothing_Requirements):
        Clothing_Requirements.setWindowTitle(_translate("Clothing_Requirements", "Clothing Requirements", None))
        self.cancel.setText(_translate("Clothing_Requirements", "Cancel", None))
        self.submit.setText(_translate("Clothing_Requirements", "Submit", None))
        self.clothing_text.setText(_translate("Clothing_Requirements", "Enter Clothing Requirements", None))

