# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Credits.ui'
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

class Ui_Credits(object):
    def setupUi(self, Credits):
        Credits.setObjectName(_fromUtf8("Credits"))
        Credits.resize(461, 192)
        self.centralwidget = QtGui.QWidget(Credits)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.creditLabel = QtGui.QLabel(self.centralwidget)
        self.creditLabel.setGeometry(QtCore.QRect(250, 10, 101, 16))
        self.creditLabel.setObjectName(_fromUtf8("creditLabel"))
        self.back_btn = QtGui.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(360, 120, 91, 23))
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.studentLabel = QtGui.QLabel(self.centralwidget)
        self.studentLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.studentLabel.setObjectName(_fromUtf8("studentLabel"))
        self.studentListView = QtGui.QListView(self.centralwidget)
        self.studentListView.setGeometry(QtCore.QRect(10, 30, 201, 111))
        self.studentListView.setObjectName(_fromUtf8("studentListView"))
        self.apply_btn = QtGui.QPushButton(self.centralwidget)
        self.apply_btn.setGeometry(QtCore.QRect(220, 120, 91, 23))
        self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
        self.creditDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.creditDoubleSpinBox.setGeometry(QtCore.QRect(250, 30, 141, 22))
        self.creditDoubleSpinBox.setMaximum(99999.99)
        self.creditDoubleSpinBox.setObjectName(_fromUtf8("creditDoubleSpinBox"))
        Credits.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Credits)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Credits.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Credits)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Credits.setStatusBar(self.statusbar)

        self.retranslateUi(Credits)
        QtCore.QMetaObject.connectSlotsByName(Credits)

    def retranslateUi(self, Credits):
        Credits.setWindowTitle(_translate("Credits", "Student Credits", None))
        self.creditLabel.setText(_translate("Credits", "Update Credit", None))
        self.back_btn.setText(_translate("Credits", "Back", None))
        self.studentLabel.setText(_translate("Credits", "Select a Student", None))
        self.apply_btn.setText(_translate("Credits", "Apply", None))

