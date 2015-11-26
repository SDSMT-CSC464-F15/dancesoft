# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'role.ui'
#
# Created: Tue Nov 24 14:43:48 2015
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

class Ui_Role_window(object):
    def setupUi(self, Role_window):
        Role_window.setObjectName(_fromUtf8("Role_window"))
        Role_window.resize(622, 437)
        self.centralwidget = QtGui.QWidget(Role_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Role_listView = QtGui.QListView(self.centralwidget)
        self.Role_listView.setGeometry(QtCore.QRect(20, 20, 151, 211))
        self.Role_listView.setObjectName(_fromUtf8("Role_listView"))
        self.Role_apply_btn = QtGui.QPushButton(self.centralwidget)
        self.Role_apply_btn.setGeometry(QtCore.QRect(50, 270, 91, 21))
        self.Role_apply_btn.setObjectName(_fromUtf8("Role_apply_btn"))
        self.Role_tableView = QtGui.QTableView(self.centralwidget)
        self.Role_tableView.setGeometry(QtCore.QRect(190, 20, 421, 371))
        self.Role_tableView.setObjectName(_fromUtf8("Role_tableView"))
        self.Role_print_btn = QtGui.QPushButton(self.centralwidget)
        self.Role_print_btn.setGeometry(QtCore.QRect(50, 330, 91, 21))
        self.Role_print_btn.setObjectName(_fromUtf8("Role_print_btn"))
        Role_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Role_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Role_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Role_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Role_window.setStatusBar(self.statusbar)

        self.retranslateUi(Role_window)
        QtCore.QMetaObject.connectSlotsByName(Role_window)

    def retranslateUi(self, Role_window):
        Role_window.setWindowTitle(_translate("Role_window", "MainWindow", None))
        self.Role_apply_btn.setText(_translate("Role_window", "Apply", None))
        self.Role_print_btn.setText(_translate("Role_window", "Print", None))

