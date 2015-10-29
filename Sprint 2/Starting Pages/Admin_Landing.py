# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin Landing.ui'
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

class Ui_Admin_Landing(object):
    def setupUi(self, Admin_Landing):
        Admin_Landing.setObjectName(_fromUtf8("Admin_Landing"))
        Admin_Landing.resize(524, 355)
        self.centralwidget = QtGui.QWidget(Admin_Landing)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 511, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 270, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 210, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 150, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.groupBox)
        Admin_Landing.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Admin_Landing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Admin_Landing.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Admin_Landing)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Admin_Landing.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_Landing)
        QtCore.QMetaObject.connectSlotsByName(Admin_Landing)

    def retranslateUi(self, Admin_Landing):
        Admin_Landing.setWindowTitle(_translate("Admin_Landing", "Admin Landing", None))
        self.groupBox.setTitle(_translate("Admin_Landing", "Admin", None))
        self.pushButton.setText(_translate("Admin_Landing", "Manage Employees", None))
        self.pushButton_2.setText(_translate("Admin_Landing", "Quit", None))
        self.pushButton_3.setText(_translate("Admin_Landing", "Logout", None))
        self.pushButton_4.setText(_translate("Admin_Landing", "Manage Billing and Payroll", None))
        self.pushButton_5.setText(_translate("Admin_Landing", "Manage Students", None))
        self.pushButton_6.setText(_translate("Admin_Landing", "Manage Classes", None))

