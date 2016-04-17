# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tuition_rates_dialog.ui'
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

class Ui_tuitionRateDialog(object):
    def setupUi(self, tuitionRateDialog):
        tuitionRateDialog.setObjectName(_fromUtf8("tuitionRateDialog"))
        tuitionRateDialog.resize(441, 170)
        self.tuitionTimeLabel = QtGui.QLabel(tuitionRateDialog)
        self.tuitionTimeLabel.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.tuitionTimeLabel.setObjectName(_fromUtf8("tuitionTimeLabel"))
        self.tuitionCostLabel = QtGui.QLabel(tuitionRateDialog)
        self.tuitionCostLabel.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.tuitionCostLabel.setObjectName(_fromUtf8("tuitionCostLabel"))
        self.timeFrameSpinBox = QtGui.QSpinBox(tuitionRateDialog)
        self.timeFrameSpinBox.setGeometry(QtCore.QRect(120, 60, 141, 22))
        self.timeFrameSpinBox.setMaximum(9999)
        self.timeFrameSpinBox.setObjectName(_fromUtf8("timeFrameSpinBox"))
        self.costDoubleSpinBox = QtGui.QDoubleSpinBox(tuitionRateDialog)
        self.costDoubleSpinBox.setGeometry(QtCore.QRect(120, 90, 141, 22))
        self.costDoubleSpinBox.setMaximum(99999.99)
        self.costDoubleSpinBox.setObjectName(_fromUtf8("costDoubleSpinBox"))
        self.timeInfoLabel = QtGui.QLabel(tuitionRateDialog)
        self.timeInfoLabel.setGeometry(QtCore.QRect(20, 130, 171, 16))
        self.timeInfoLabel.setObjectName(_fromUtf8("timeInfoLabel"))
        self.minuteCheckBox = QtGui.QCheckBox(tuitionRateDialog)
        self.minuteCheckBox.setGeometry(QtCore.QRect(270, 60, 70, 17))
        self.minuteCheckBox.setObjectName(_fromUtf8("minuteCheckBox"))
        self.hoursCheckBox = QtGui.QCheckBox(tuitionRateDialog)
        self.hoursCheckBox.setGeometry(QtCore.QRect(350, 60, 70, 17))
        self.hoursCheckBox.setObjectName(_fromUtf8("hoursCheckBox"))
        self.ok_btn = QtGui.QPushButton(tuitionRateDialog)
        self.ok_btn.setGeometry(QtCore.QRect(270, 130, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.cancel_btn = QtGui.QPushButton(tuitionRateDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.tuitionDescriptionLabel = QtGui.QLabel(tuitionRateDialog)
        self.tuitionDescriptionLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.tuitionDescriptionLabel.setObjectName(_fromUtf8("tuitionDescriptionLabel"))
        self.descriptionLineEdit = QtGui.QLineEdit(tuitionRateDialog)
        self.descriptionLineEdit.setGeometry(QtCore.QRect(120, 30, 281, 20))
        self.descriptionLineEdit.setObjectName(_fromUtf8("descriptionLineEdit"))

        self.retranslateUi(tuitionRateDialog)
        QtCore.QMetaObject.connectSlotsByName(tuitionRateDialog)

    def retranslateUi(self, tuitionRateDialog):
        tuitionRateDialog.setWindowTitle(_translate("tuitionRateDialog", "Tuition Rates", None))
        self.tuitionTimeLabel.setText(_translate("tuitionRateDialog", "Time*", None))
        self.tuitionCostLabel.setText(_translate("tuitionRateDialog", "Tuition Cost", None))
        self.timeInfoLabel.setText(_translate("tuitionRateDialog", "*How many min/hrs per week ", None))
        self.minuteCheckBox.setText(_translate("tuitionRateDialog", "Minutes", None))
        self.hoursCheckBox.setText(_translate("tuitionRateDialog", "Hours", None))
        self.ok_btn.setText(_translate("tuitionRateDialog", "OK", None))
        self.cancel_btn.setText(_translate("tuitionRateDialog", "Cancel", None))
        self.tuitionDescriptionLabel.setText(_translate("tuitionRateDialog", "Tuition Description", None))

