# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_history.ui'
#
# Created: Tue Jan 19 13:04:29 2016
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

class Ui_teacher_history(object):
    def setupUi(self, teacher_history):
        teacher_history.setObjectName(_fromUtf8("teacher_history"))
        teacher_history.resize(425, 358)
        self.centralwidget = QtGui.QWidget(teacher_history)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Teacher_listView = QtGui.QListView(self.centralwidget)
        self.Teacher_listView.setGeometry(QtCore.QRect(10, 20, 191, 291))
        self.Teacher_listView.setObjectName(_fromUtf8("Teacher_listView"))
        self.Class_listView = QtGui.QListView(self.centralwidget)
        self.Class_listView.setGeometry(QtCore.QRect(220, 20, 191, 291))
        self.Class_listView.setObjectName(_fromUtf8("Class_listView"))
        teacher_history.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(teacher_history)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        teacher_history.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(teacher_history)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        teacher_history.setStatusBar(self.statusbar)

        self.retranslateUi(teacher_history)
        QtCore.QMetaObject.connectSlotsByName(teacher_history)

    def retranslateUi(self, teacher_history):
        teacher_history.setWindowTitle(_translate("teacher_history", "MainWindow", None))

