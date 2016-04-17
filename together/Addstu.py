# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addstu.ui'
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

class Ui_Addstu_window(object):
    def setupUi(self, Addstu_window):
        Addstu_window.setObjectName(_fromUtf8("Addstu_window"))
        Addstu_window.resize(524, 419)
        self.centralwidget = QtGui.QWidget(Addstu_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Class_listView = QtGui.QListView(self.centralwidget)
        self.Class_listView.setGeometry(QtCore.QRect(20, 20, 201, 281))
        self.Class_listView.setObjectName(_fromUtf8("Class_listView"))
        self.Remove_stu_btn = QtGui.QPushButton(self.centralwidget)
        self.Remove_stu_btn.setGeometry(QtCore.QRect(80, 330, 91, 21))
        self.Remove_stu_btn.setObjectName(_fromUtf8("Remove_stu_btn"))
        self.Add_stu_btn = QtGui.QPushButton(self.centralwidget)
        self.Add_stu_btn.setGeometry(QtCore.QRect(320, 330, 91, 21))
        self.Add_stu_btn.setObjectName(_fromUtf8("Add_stu_btn"))
        self.Stu_tableView = QtGui.QTableView(self.centralwidget)
        self.Stu_tableView.setGeometry(QtCore.QRect(280, 20, 221, 281))
        self.Stu_tableView.setObjectName(_fromUtf8("Stu_tableView"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 360, 571, 16))
        self.label.setObjectName(_fromUtf8("label"))
        Addstu_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Addstu_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Addstu_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Addstu_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Addstu_window.setStatusBar(self.statusbar)

        self.retranslateUi(Addstu_window)
        QtCore.QMetaObject.connectSlotsByName(Addstu_window)

    def retranslateUi(self, Addstu_window):
        Addstu_window.setWindowTitle(_translate("Addstu_window", "Approve Student", None))
        self.Remove_stu_btn.setText(_translate("Addstu_window", "Remove", None))
        self.Add_stu_btn.setText(_translate("Addstu_window", "Add", None))
        self.label.setText(_translate("Addstu_window", "* Class Approval:   Pending: 0    Approved: 1     Rejected: -1", None))

