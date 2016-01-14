# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addstudetail.ui'
#
# Created: Sun Nov 29 15:57:54 2015
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

class Ui_Addstu_detail(object):
    def setupUi(self, Addstu_detail):
        Addstu_detail.setObjectName(_fromUtf8("Addstu_detail"))
        Addstu_detail.resize(282, 370)
        self.Addstu_detail_listView = QtGui.QListView(Addstu_detail)
        self.Addstu_detail_listView.setGeometry(QtCore.QRect(10, 40, 261, 261))
        self.Addstu_detail_listView.setObjectName(_fromUtf8("Addstu_detail_listView"))
        self.Addstu_detail_label = QtGui.QLabel(Addstu_detail)
        self.Addstu_detail_label.setGeometry(QtCore.QRect(30, 10, 221, 21))
        self.Addstu_detail_label.setObjectName(_fromUtf8("Addstu_detail_label"))
        self.Addstu_detail_btn = QtGui.QPushButton(Addstu_detail)
        self.Addstu_detail_btn.setGeometry(QtCore.QRect(80, 320, 101, 21))
        self.Addstu_detail_btn.setObjectName(_fromUtf8("Addstu_detail_btn"))

        self.retranslateUi(Addstu_detail)
        QtCore.QMetaObject.connectSlotsByName(Addstu_detail)

    def retranslateUi(self, Addstu_detail):
        Addstu_detail.setWindowTitle(_translate("Addstu_detail", "Dialog", None))
        self.Addstu_detail_label.setText(_translate("Addstu_detail", "Select student to add", None))
        self.Addstu_detail_btn.setText(_translate("Addstu_detail", "Add", None))

