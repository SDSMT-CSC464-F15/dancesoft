# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_list.ui'
#
# Created: Fri Mar 11 14:13:21 2016
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

class Ui_Admin_list(object):
    def setupUi(self, Admin_list):
        Admin_list.setObjectName(_fromUtf8("Admin_list"))
        Admin_list.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Admin_list)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Admin_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Admin_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Admin_lineEdit.setObjectName(_fromUtf8("Admin_lineEdit"))
        self.Admin_listView = QtGui.QListView(self.centralwidget)
        self.Admin_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Admin_listView.setObjectName(_fromUtf8("Admin_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Detail_btn = QtGui.QPushButton(self.centralwidget)
        self.Detail_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Detail_btn.setObjectName(_fromUtf8("Detail_btn"))
        Admin_list.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Admin_list)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Admin_list.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Admin_list)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Admin_list.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_list)
        QtCore.QMetaObject.connectSlotsByName(Admin_list)

    def retranslateUi(self, Admin_list):
        Admin_list.setWindowTitle(_translate("Admin_list", "MainWindow", None))
        self.Search_btn.setText(_translate("Admin_list", "Search", None))
        self.Detail_btn.setText(_translate("Admin_list", "Detail", None))

