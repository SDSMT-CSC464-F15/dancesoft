# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher_schedule.ui'
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

class Ui_Teacher_schedule(object):
    def setupUi(self, Teacher_schedule):
        Teacher_schedule.setObjectName(_fromUtf8("Teacher_schedule"))
        Teacher_schedule.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Teacher_schedule)
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
        self.schedule_btn = QtGui.QPushButton(self.centralwidget)
        self.schedule_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.schedule_btn.setObjectName(_fromUtf8("schedule_btn"))
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(230, 350, 101, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        Teacher_schedule.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Teacher_schedule)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Teacher_schedule.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Teacher_schedule)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Teacher_schedule.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher_schedule)
        QtCore.QMetaObject.connectSlotsByName(Teacher_schedule)

    def retranslateUi(self, Teacher_schedule):
        Teacher_schedule.setWindowTitle(_translate("Teacher_schedule", "Teacher List", None))
        self.Search_btn.setText(_translate("Teacher_schedule", "Search", None))
        self.schedule_btn.setText(_translate("Teacher_schedule", "Schedule", None))
        self.cancel_btn.setText(_translate("Teacher_schedule", "Cancel", None))

