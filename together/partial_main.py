# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'partial_main.ui'
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

class Ui_Enter_partialpayment(object):
    def setupUi(self, Enter_partialpayment):
        Enter_partialpayment.setObjectName(_fromUtf8("Enter_partialpayment"))
        Enter_partialpayment.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Enter_partialpayment)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Student_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Student_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Student_lineEdit.setObjectName(_fromUtf8("Student_lineEdit"))
        self.Student_listView = QtGui.QListView(self.centralwidget)
        self.Student_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Student_listView.setObjectName(_fromUtf8("Student_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        Enter_partialpayment.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Enter_partialpayment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Enter_partialpayment.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Enter_partialpayment)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Enter_partialpayment.setStatusBar(self.statusbar)

        self.retranslateUi(Enter_partialpayment)
        QtCore.QMetaObject.connectSlotsByName(Enter_partialpayment)

    def retranslateUi(self, Enter_partialpayment):
        Enter_partialpayment.setWindowTitle(_translate("Enter_partialpayment", "Enter Partial Payment", None))
        self.Search_btn.setText(_translate("Enter_partialpayment", "search", None))
        self.Add_btn.setText(_translate("Enter_partialpayment", "Add", None))

