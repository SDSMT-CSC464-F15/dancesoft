# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher Landing.ui'
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

class Ui_Teacher_Landing(object):
    def setupUi(self, Teacher_Landing):
        Teacher_Landing.setObjectName(_fromUtf8("Teacher_Landing"))
        Teacher_Landing.resize(626, 345)
        self.centralwidget = QtGui.QWidget(Teacher_Landing)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 601, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(510, 250, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 250, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 120, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.groupBox)
        Teacher_Landing.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Teacher_Landing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Teacher_Landing.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Teacher_Landing)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Teacher_Landing.setStatusBar(self.statusbar)

        self.retranslateUi(Teacher_Landing)
        QtCore.QMetaObject.connectSlotsByName(Teacher_Landing)

    def retranslateUi(self, Teacher_Landing):
        Teacher_Landing.setWindowTitle(_translate("Teacher_Landing", "Teacher Landing", None))
        self.groupBox.setTitle(_translate("Teacher_Landing", "Teachers", None))
        self.pushButton.setText(_translate("Teacher_Landing", "Quit", None))
        self.pushButton_2.setText(_translate("Teacher_Landing", "Logout", None))
        self.pushButton_3.setText(_translate("Teacher_Landing", "Student Options", None))
        self.pushButton_4.setText(_translate("Teacher_Landing", "Personal Options", None))
        self.pushButton_6.setText(_translate("Teacher_Landing", "Class Options", None))

