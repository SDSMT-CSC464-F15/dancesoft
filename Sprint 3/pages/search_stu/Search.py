# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created: Thu Nov 19 11:00:03 2015
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

class Ui_Search_MainWindow(object):
    def setupUi(self, Search_MainWindow):
        Search_MainWindow.setObjectName(_fromUtf8("Search_MainWindow"))
        Search_MainWindow.resize(800, 629)
        self.centralwidget = QtGui.QWidget(Search_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.Search_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.Search_lineEdit.setGeometry(QtCore.QRect(200, 60, 221, 21))
        self.Search_lineEdit.setObjectName(_fromUtf8("Search_lineEdit"))
        self.Search_btn = QtGui.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(440, 60, 111, 23))
        self.Search_btn.setObjectName(_fromUtf8("Search_btn"))
        self.Adv_search_btn = QtGui.QPushButton(self.centralwidget)
        self.Adv_search_btn.setGeometry(QtCore.QRect(560, 60, 111, 23))
        self.Adv_search_btn.setObjectName(_fromUtf8("Adv_search_btn"))
        self.Student_view = QtGui.QTableView(self.centralwidget)
        self.Student_view.setGeometry(QtCore.QRect(25, 121, 751, 431))
        self.Student_view.setObjectName(_fromUtf8("Student_view"))
        self.Reset_search_btn = QtGui.QPushButton(self.centralwidget)
        self.Reset_search_btn.setGeometry(QtCore.QRect(680, 60, 111, 23))
        self.Reset_search_btn.setObjectName(_fromUtf8("Reset_search_btn"))
        self.Detail_btn = QtGui.QPushButton(self.centralwidget)
        self.Detail_btn.setGeometry(QtCore.QRect(30, 560, 111, 23))
        self.Detail_btn.setObjectName(_fromUtf8("Detail_btn"))
        self.Exact_search_cbox = QtGui.QCheckBox(self.centralwidget)
        self.Exact_search_cbox.setGeometry(QtCore.QRect(120, 50, 71, 41))
        self.Exact_search_cbox.setObjectName(_fromUtf8("Exact_search_cbox"))
        Search_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Search_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Search_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Search_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Search_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Search_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Search_MainWindow)

    def retranslateUi(self, Search_MainWindow):
        Search_MainWindow.setWindowTitle(_translate("Search_MainWindow", "MainWindow", None))
        self.label.setText(_translate("Search_MainWindow", "Enter Student Name", None))
        self.Search_btn.setText(_translate("Search_MainWindow", "Search", None))
        self.Adv_search_btn.setText(_translate("Search_MainWindow", "Advanced Search", None))
        self.Reset_search_btn.setText(_translate("Search_MainWindow", "Refresh", None))
        self.Detail_btn.setText(_translate("Search_MainWindow", "Detail", None))
        self.Exact_search_cbox.setText(_translate("Search_MainWindow", "Exact", None))
