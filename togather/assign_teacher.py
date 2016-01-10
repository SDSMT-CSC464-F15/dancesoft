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
        Assign_teacher_window.resize(462, 365)
        self.centralwidget = QtGui.QWidget(Assign_teacher_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Class_listView = QtGui.QListView(self.centralwidget)
        self.Class_listView.setGeometry(QtCore.QRect(20, 20, 191, 261))
        self.Class_listView.setObjectName(_fromUtf8("Class_listView"))
        self.Teacher_listView = QtGui.QListView(self.centralwidget)
        self.Teacher_listView.setGeometry(QtCore.QRect(250, 20, 191, 261))
        self.Teacher_listView.setObjectName(_fromUtf8("Teacher_listView"))
        self.Select_Class_label = QtGui.QLabel(self.centralwidget)
        self.Select_Class_label.setGeometry(QtCore.QRect(20, 0, 191, 20))
        self.Select_Class_label.setObjectName(_fromUtf8("Select_Class_label"))
        self.Select_Teacher_label = QtGui.QLabel(self.centralwidget)
        self.Select_Teacher_label.setGeometry(QtCore.QRect(250, 0, 191, 16))
        self.Select_Teacher_label.setObjectName(_fromUtf8("Select_Teacher_label"))
        self.Assign_teacher_back_btn = QtGui.QPushButton(self.centralwidget)
        self.Assign_teacher_back_btn.setGeometry(QtCore.QRect(360, 290, 75, 21))
        self.Assign_teacher_back_btn.setObjectName(_fromUtf8("Assign_teacher_back_btn"))
        Assign_teacher_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Assign_teacher_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Assign_teacher_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Assign_teacher_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Assign_teacher_window.setStatusBar(self.statusbar)

        self.retranslateUi(Assign_teacher_window)
        QtCore.QMetaObject.connectSlotsByName(Assign_teacher_window)

    def retranslateUi(self, Assign_teacher_window):
        Assign_teacher_window.setWindowTitle(_translate("Assign_teacher_window", "MainWindow", None))
        self.Select_Class_label.setText(_translate("Assign_teacher_window", "Select Class", None))
        self.Select_Teacher_label.setText(_translate("Assign_teacher_window", "Select Teacher", None))
        self.Assign_teacher_back_btn.setText(_translate("Assign_teacher_window", "Back", None))

