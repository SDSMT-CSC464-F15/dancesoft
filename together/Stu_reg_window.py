# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stu_reg_window.ui'
#
# Created: Tue Mar 15 10:13:22 2016
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

class Ui_Stu_reg(object):
    def setupUi(self, Stu_reg):
        Stu_reg.setObjectName(_fromUtf8("Stu_reg"))
        Stu_reg.resize(348, 414)
        self.centralwidget = QtGui.QWidget(Stu_reg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Stu_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Stu_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Stu_lineEdit.setObjectName(_fromUtf8("Stu_lineEdit"))
        self.Stu_listView = QtGui.QListView(self.centralwidget)
        self.Stu_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Stu_listView.setObjectName(_fromUtf8("Stu_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(240, 350, 91, 21))
        self.Add_btn.setObjectName(_fromUtf8("Add_btn"))
        self.Update_btn = QtGui.QPushButton(self.centralwidget)
        self.Update_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Update_btn.setObjectName(_fromUtf8("Update_btn"))
        Stu_reg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Stu_reg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Stu_reg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Stu_reg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Stu_reg.setStatusBar(self.statusbar)

        self.retranslateUi(Stu_reg)
        QtCore.QMetaObject.connectSlotsByName(Stu_reg)

    def retranslateUi(self, Stu_reg):
        Stu_reg.setWindowTitle(_translate("Stu_reg", "MainWindow", None))
        self.Search_btn.setText(_translate("Stu_reg", "search", None))
        self.Add_btn.setText(_translate("Stu_reg", "Add", None))
        self.Update_btn.setText(_translate("Stu_reg", "Update", None))

