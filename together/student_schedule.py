# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_schedule.ui'
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

class Ui_Student_schedule(object):
    def setupUi(self, Student_schedule):
        Student_schedule.setObjectName(_fromUtf8("Student_schedule"))
        Student_schedule.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Student_schedule)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Student_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Student_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Student_lineEdit.setObjectName(_fromUtf8("Student_lineEdit"))
        self.Student_listView = QtGui.QListView(self.centralwidget)
        self.Student_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Student_listView.setObjectName(_fromUtf8("Student_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.schedule_btn = QtGui.QPushButton(self.centralwidget)
        self.schedule_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.schedule_btn.setObjectName(_fromUtf8("schedule_btn"))
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(230, 350, 101, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        Student_schedule.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Student_schedule)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Student_schedule.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Student_schedule)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Student_schedule.setStatusBar(self.statusbar)

        self.retranslateUi(Student_schedule)
        QtCore.QMetaObject.connectSlotsByName(Student_schedule)

    def retranslateUi(self, Student_schedule):
        Student_schedule.setWindowTitle(_translate("Student_schedule", "MainWindow", None))
        self.Search_btn.setText(_translate("Student_schedule", "search", None))
        self.schedule_btn.setText(_translate("Student_schedule", "schedule", None))
        self.cancel_btn.setText(_translate("Student_schedule", "Cancel", None))

