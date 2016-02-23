# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_fullpayment.ui'
#
# Created: Tue Feb 16 03:05:07 2016
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

class Ui_Enter_fullpayment(object):
    def setupUi(self, Enter_fullpayment):
        Enter_fullpayment.setObjectName(_fromUtf8("Enter_fullpayment"))
        Enter_fullpayment.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Enter_fullpayment)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Teacher_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Teacher_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Teacher_lineEdit.setObjectName(_fromUtf8("Teacher_lineEdit"))
        self.Student_listView = QtGui.QListView(self.centralwidget)
        self.Student_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Student_listView.setObjectName(_fromUtf8("Student_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Statement_btn = QtGui.QPushButton(self.centralwidget)
        self.Statement_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Statement_btn.setObjectName(_fromUtf8("Statement_btn"))
        Enter_fullpayment.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Enter_fullpayment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Enter_fullpayment.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Enter_fullpayment)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Enter_fullpayment.setStatusBar(self.statusbar)

        self.retranslateUi(Enter_fullpayment)
        QtCore.QMetaObject.connectSlotsByName(Enter_fullpayment)

    def retranslateUi(self, Enter_fullpayment):
        Enter_fullpayment.setWindowTitle(_translate("Enter_fullpayment", "MainWindow", None))
        self.Search_btn.setText(_translate("Enter_fullpayment", "search", None))
        self.Statement_btn.setText(_translate("Enter_fullpayment", "Clear", None))

