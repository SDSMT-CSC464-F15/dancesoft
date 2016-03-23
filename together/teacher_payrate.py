# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_payrate.ui'
#
# Created: Tue Mar  8 13:46:07 2016
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

class Ui_Teacher_payrate(object):
    def setupUi(self, Teacher_payrate):
        Teacher_payrate.setObjectName(_fromUtf8("Teacher_payrate"))
        Teacher_payrate.resize(348, 414)
        self.centralwidget = QtGui.QWidget(Teacher_payrate)
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
        self.history_btn = QtGui.QPushButton(self.centralwidget)
        self.history_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.history_btn.setObjectName(_fromUtf8("history_btn"))
        Teacher_payrate.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Teacher_payrate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Teacher_payrate.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Teacher_payrate)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Teacher_payrate.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher_payrate)
        QtCore.QMetaObject.connectSlotsByName(Teacher_payrate)

    def retranslateUi(self, Teacher_payrate):
        Teacher_payrate.setWindowTitle(_translate("Teacher_payrate", "MainWindow", None))
        self.Search_btn.setText(_translate("Teacher_payrate", "search", None))
        self.history_btn.setText(_translate("Teacher_payrate", "history", None))

