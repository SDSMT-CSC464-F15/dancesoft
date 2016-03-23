# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_history.ui'
#
# Created: Fri Jan 22 01:06:13 2016
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

class Ui_Teacher_history(object):
    def setupUi(self, Teacher_history):
        Teacher_history.setObjectName(_fromUtf8("Teacher_history"))
        Teacher_history.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Teacher_history)
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
        Teacher_history.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Teacher_history)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Teacher_history.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Teacher_history)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Teacher_history.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher_history)
        QtCore.QMetaObject.connectSlotsByName(Teacher_history)

    def retranslateUi(self, Teacher_history):
        Teacher_history.setWindowTitle(_translate("Teacher_history", "MainWindow", None))
        self.Search_btn.setText(_translate("Teacher_history", "search", None))
        self.history_btn.setText(_translate("Teacher_history", "history", None))

