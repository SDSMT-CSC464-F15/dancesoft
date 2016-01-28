# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fee_rates.ui'
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

class Ui_fee_rates(object):
    def setupUi(self, fee_rates):
        fee_rates.setObjectName(_fromUtf8("fee_rates"))
        fee_rates.resize(536, 228)
        self.centralwidget = QtGui.QWidget(fee_rates)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.feeCostLabel = QtGui.QLabel(self.centralwidget)
        self.feeCostLabel.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.feeCostLabel.setObjectName(_fromUtf8("feeCostLabel"))
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(420, 150, 91, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.feeDescriptionLabel = QtGui.QLabel(self.centralwidget)
        self.feeDescriptionLabel.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.feeDescriptionLabel.setObjectName(_fromUtf8("feeDescriptionLabel"))
        self.descriptionListView = QtGui.QListView(self.centralwidget)
        self.descriptionListView.setGeometry(QtCore.QRect(10, 30, 201, 151))
        self.descriptionListView.setObjectName(_fromUtf8("descriptionListView"))
        self.add_btn = QtGui.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(220, 70, 91, 23))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.update_btn = QtGui.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(320, 70, 91, 23))
        self.update_btn.setObjectName(_fromUtf8("update_btn"))
        self.remove_btn = QtGui.QPushButton(self.centralwidget)
        self.remove_btn.setGeometry(QtCore.QRect(420, 70, 91, 23))
        self.remove_btn.setObjectName(_fromUtf8("remove_btn"))
        self.costDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.costDoubleSpinBox.setGeometry(QtCore.QRect(260, 30, 141, 22))
        self.costDoubleSpinBox.setMaximum(99999.99)
        self.costDoubleSpinBox.setObjectName(_fromUtf8("costDoubleSpinBox"))
        self.refresh_btn = QtGui.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(220, 150, 91, 23))
        self.refresh_btn.setObjectName(_fromUtf8("refresh_btn"))
        fee_rates.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fee_rates)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fee_rates.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fee_rates)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fee_rates.setStatusBar(self.statusbar)

        self.retranslateUi(fee_rates)
        QtCore.QMetaObject.connectSlotsByName(fee_rates)

    def retranslateUi(self, fee_rates):
        fee_rates.setWindowTitle(_translate("fee_rates", "MainWindow", None))
        self.feeCostLabel.setText(_translate("fee_rates", "Cost", None))
        self.cancel_btn.setText(_translate("fee_rates", "Cancel", None))
        self.feeDescriptionLabel.setText(_translate("fee_rates", "Fee/Discount Description", None))
        self.add_btn.setText(_translate("fee_rates", "Add", None))
        self.update_btn.setText(_translate("fee_rates", "Update", None))
        self.remove_btn.setText(_translate("fee_rates", "Remove", None))
        self.refresh_btn.setText(_translate("fee_rates", "Refresh List", None))

