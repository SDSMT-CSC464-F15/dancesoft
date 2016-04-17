# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_hours.ui'
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

class Ui_Enter_hours(object):
    def setupUi(self, Enter_hours):
        Enter_hours.setObjectName(_fromUtf8("Enter_hours"))
        Enter_hours.resize(351, 412)
        self.centralwidget = QtGui.QWidget(Enter_hours)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Teacher_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Teacher_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Teacher_lineEdit.setObjectName(_fromUtf8("Teacher_lineEdit"))
        self.Teacher_listView = QtGui.QListView(self.centralwidget)
        self.Teacher_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Teacher_listView.setObjectName(_fromUtf8("Teacher_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Hours_btn = QtGui.QPushButton(self.centralwidget)
        self.Hours_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Hours_btn.setObjectName(_fromUtf8("Hours_btn"))
        Enter_hours.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Enter_hours)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Enter_hours.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Enter_hours)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Enter_hours.setStatusBar(self.statusbar)

        self.retranslateUi(Enter_hours)
        QtCore.QMetaObject.connectSlotsByName(Enter_hours)

    def retranslateUi(self, Enter_hours):
        Enter_hours.setWindowTitle(_translate("Enter_hours", "Enter Hours", None))
        self.Search_btn.setText(_translate("Enter_hours", "search", None))
        self.Hours_btn.setText(_translate("Enter_hours", "Hours", None))

