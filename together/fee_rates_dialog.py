# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fee_rates_dialog.ui'
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

class Ui_feeRateDialog(object):
    def setupUi(self, feeRateDialog):
        feeRateDialog.setObjectName(_fromUtf8("feeRateDialog"))
        feeRateDialog.resize(441, 135)
        self.feeDescriptionLabel = QtGui.QLabel(feeRateDialog)
        self.feeDescriptionLabel.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.feeDescriptionLabel.setObjectName(_fromUtf8("feeDescriptionLabel"))
        self.descriptionLineEdit = QtGui.QLineEdit(feeRateDialog)
        self.descriptionLineEdit.setGeometry(QtCore.QRect(120, 30, 281, 20))
        self.descriptionLineEdit.setObjectName(_fromUtf8("descriptionLineEdit"))
        self.cancel_btn = QtGui.QPushButton(feeRateDialog)
        self.cancel_btn.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.feeCostLabel = QtGui.QLabel(feeRateDialog)
        self.feeCostLabel.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.feeCostLabel.setObjectName(_fromUtf8("feeCostLabel"))
        self.ok_btn = QtGui.QPushButton(feeRateDialog)
        self.ok_btn.setGeometry(QtCore.QRect(270, 100, 75, 23))
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.costDoubleSpinBox = QtGui.QDoubleSpinBox(feeRateDialog)
        self.costDoubleSpinBox.setGeometry(QtCore.QRect(120, 60, 141, 22))
        self.costDoubleSpinBox.setMaximum(99999.99)
        self.costDoubleSpinBox.setObjectName(_fromUtf8("costDoubleSpinBox"))

        self.retranslateUi(feeRateDialog)
        QtCore.QMetaObject.connectSlotsByName(feeRateDialog)

    def retranslateUi(self, feeRateDialog):
        feeRateDialog.setWindowTitle(_translate("feeRateDialog", "Dialog", None))
        self.feeDescriptionLabel.setText(_translate("feeRateDialog", " Description", None))
        self.cancel_btn.setText(_translate("feeRateDialog", "Cancel", None))
        self.feeCostLabel.setText(_translate("feeRateDialog", " Cost", None))
        self.ok_btn.setText(_translate("feeRateDialog", "OK", None))

