# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assign_teacher.ui'
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

class Ui_Assign_teacher_window(object):
    def setupUi(self, Assign_teacher_window):
        Assign_teacher_window.setObjectName(_fromUtf8("Assign_teacher_window"))
        Assign_teacher_window.resize(466, 364)
        self.centralwidget = QtGui.QWidget(Assign_teacher_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Class_listView = QtGui.QListView(self.centralwidget)
        self.Class_listView.setGeometry(QtCore.QRect(20, 20, 191, 261))
        self.Class_listView.setObjectName(_fromUtf8("Class_listView"))
        self.Assign_teacher_btn = QtGui.QPushButton(self.centralwidget)
        self.Assign_teacher_btn.setGeometry(QtCore.QRect(300, 290, 91, 21))
        self.Assign_teacher_btn.setObjectName(_fromUtf8("Assign_teacher_btn"))
        self.Select_class_btn = QtGui.QPushButton(self.centralwidget)
        self.Select_class_btn.setGeometry(QtCore.QRect(70, 290, 91, 21))
        self.Select_class_btn.setObjectName(_fromUtf8("Select_class_btn"))
        self.Teacher_listView = QtGui.QListView(self.centralwidget)
        self.Teacher_listView.setGeometry(QtCore.QRect(250, 20, 191, 261))
        self.Teacher_listView.setObjectName(_fromUtf8("Teacher_listView"))
        Assign_teacher_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Assign_teacher_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Assign_teacher_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Assign_teacher_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Assign_teacher_window.setStatusBar(self.statusbar)

        self.retranslateUi(Assign_teacher_window)
        QtCore.QMetaObject.connectSlotsByName(Assign_teacher_window)

    def retranslateUi(self, Assign_teacher_window):
        Assign_teacher_window.setWindowTitle(_translate("Assign_teacher_window", "MainWindow", None))
        self.Assign_teacher_btn.setText(_translate("Assign_teacher_window", "Assign Teacher", None))
        self.Select_class_btn.setText(_translate("Assign_teacher_window", "Select Class", None))

