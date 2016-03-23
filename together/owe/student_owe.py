# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_owe.ui'
#
# Created: Fri Jan 22 22:16:05 2016
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

class Ui_Student_payment(object):
    def setupUi(self, Student_payment):
        Student_payment.setObjectName(_fromUtf8("Student_payment"))
        Student_payment.resize(351, 413)
        self.centralwidget = QtGui.QWidget(Student_payment)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Teacher_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Teacher_lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.Teacher_lineEdit.setObjectName(_fromUtf8("Teacher_lineEdit"))
        self.Student_listView = QtGui.QListView(self.centralwidget)
        self.Student_listView.setGeometry(QtCore.QRect(20, 60, 311, 281))
        self.Student_listView.setObjectName(_fromUtf8("Student_listView"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(240, 20, 91, 21))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Statement_btn = QtGui.QPushButton(self.centralwidget)
        self.Statement_btn.setGeometry(QtCore.QRect(20, 350, 91, 21))
        self.Statement_btn.setObjectName(_fromUtf8("Statement_btn"))
        Student_payment.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Student_payment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Student_payment.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Student_payment)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Student_payment.setStatusBar(self.statusbar)

        self.retranslateUi(Student_payment)
        QtCore.QMetaObject.connectSlotsByName(Student_payment)

    def retranslateUi(self, Student_payment):
        Student_payment.setWindowTitle(_translate("Student_payment", "MainWindow", None))
        self.Search_btn.setText(_translate("Student_payment", "search", None))
        self.Statement_btn.setText(_translate("Student_payment", "Statement", None))

