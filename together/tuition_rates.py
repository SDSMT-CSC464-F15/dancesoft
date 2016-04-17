# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tuition_rates.ui'
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

class Ui_tuition_rates(object):
    def setupUi(self, tuition_rates):
        tuition_rates.setObjectName(_fromUtf8("tuition_rates"))
        tuition_rates.resize(536, 295)
        self.centralwidget = QtGui.QWidget(tuition_rates)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tuitionCostLabel = QtGui.QLabel(self.centralwidget)
        self.tuitionCostLabel.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.tuitionCostLabel.setObjectName(_fromUtf8("tuitionCostLabel"))
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(420, 220, 91, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.tuitionDescriptionLabel = QtGui.QLabel(self.centralwidget)
        self.tuitionDescriptionLabel.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.tuitionDescriptionLabel.setObjectName(_fromUtf8("tuitionDescriptionLabel"))
        self.descriptionListView = QtGui.QListView(self.centralwidget)
        self.descriptionListView.setGeometry(QtCore.QRect(10, 30, 201, 211))
        self.descriptionListView.setObjectName(_fromUtf8("descriptionListView"))
        self.add_btn = QtGui.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(220, 130, 91, 23))
        self.add_btn.setObjectName(_fromUtf8("add_btn"))
        self.update_btn = QtGui.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(320, 130, 91, 23))
        self.update_btn.setObjectName(_fromUtf8("update_btn"))
        self.remove_btn = QtGui.QPushButton(self.centralwidget)
        self.remove_btn.setGeometry(QtCore.QRect(420, 130, 91, 23))
        self.remove_btn.setObjectName(_fromUtf8("remove_btn"))
        self.costDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.costDoubleSpinBox.setGeometry(QtCore.QRect(260, 30, 141, 22))
        self.costDoubleSpinBox.setMaximum(99999.99)
        self.costDoubleSpinBox.setObjectName(_fromUtf8("costDoubleSpinBox"))
        self.hoursCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.hoursCheckBox.setGeometry(QtCore.QRect(470, 90, 70, 17))
        self.hoursCheckBox.setObjectName(_fromUtf8("hoursCheckBox"))
        self.minuteCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.minuteCheckBox.setGeometry(QtCore.QRect(410, 90, 70, 17))
        self.minuteCheckBox.setObjectName(_fromUtf8("minuteCheckBox"))
        self.timeFrameSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.timeFrameSpinBox.setGeometry(QtCore.QRect(260, 90, 141, 22))
        self.timeFrameSpinBox.setMaximum(9999)
        self.timeFrameSpinBox.setObjectName(_fromUtf8("timeFrameSpinBox"))
        self.tuitionTimeLabel = QtGui.QLabel(self.centralwidget)
        self.tuitionTimeLabel.setGeometry(QtCore.QRect(260, 70, 101, 16))
        self.tuitionTimeLabel.setObjectName(_fromUtf8("tuitionTimeLabel"))
        self.refresh_btn = QtGui.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(220, 220, 91, 23))
        self.refresh_btn.setObjectName(_fromUtf8("refresh_btn"))
        tuition_rates.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(tuition_rates)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        tuition_rates.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(tuition_rates)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        tuition_rates.setStatusBar(self.statusbar)

        self.retranslateUi(tuition_rates)
        QtCore.QMetaObject.connectSlotsByName(tuition_rates)

    def retranslateUi(self, tuition_rates):
        tuition_rates.setWindowTitle(_translate("tuition_rates", "Tuition Rates", None))
        self.tuitionCostLabel.setText(_translate("tuition_rates", "Tuition Cost", None))
        self.cancel_btn.setText(_translate("tuition_rates", "Cancel", None))
        self.tuitionDescriptionLabel.setText(_translate("tuition_rates", "Tuition Description", None))
        self.add_btn.setText(_translate("tuition_rates", "Add", None))
        self.update_btn.setText(_translate("tuition_rates", "Update", None))
        self.remove_btn.setText(_translate("tuition_rates", "Remove", None))
        self.hoursCheckBox.setText(_translate("tuition_rates", "Hours", None))
        self.minuteCheckBox.setText(_translate("tuition_rates", "Minutes", None))
        self.tuitionTimeLabel.setText(_translate("tuition_rates", "Time", None))
        self.refresh_btn.setText(_translate("tuition_rates", "Refresh List", None))

