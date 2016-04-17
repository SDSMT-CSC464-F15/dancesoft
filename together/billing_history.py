# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'billing_history.ui'
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

class Ui_Billing_history(object):
    def setupUi(self, Billing_history):
        Billing_history.setObjectName(_fromUtf8("Billing_history"))
        Billing_history.resize(351, 412)
        self.centralwidget = QtGui.QWidget(Billing_history)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.student_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.student_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.student_lineEdit.setObjectName(_fromUtf8("student_lineEdit"))
        self.Student_listView = QtGui.QListView(self.centralwidget)
        self.Student_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Student_listView.setObjectName(_fromUtf8("Student_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Statement_btn = QtGui.QPushButton(self.centralwidget)
        self.Statement_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Statement_btn.setObjectName(_fromUtf8("Statement_btn"))
        Billing_history.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Billing_history)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Billing_history.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Billing_history)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Billing_history.setStatusBar(self.statusbar)

        self.retranslateUi(Billing_history)
        QtCore.QMetaObject.connectSlotsByName(Billing_history)

    def retranslateUi(self, Billing_history):
        Billing_history.setWindowTitle(_translate("Billing_history", "Billing History", None))
        self.Search_btn.setText(_translate("Billing_history", "search", None))
        self.Statement_btn.setText(_translate("Billing_history", "Statement", None))

