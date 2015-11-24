# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Teacher.ui'
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

class Select_teacher(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(398, 81)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 61))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.selectTeacherLabel = QtGui.QLabel(self.formLayoutWidget)
        self.selectTeacherLabel.setObjectName(_fromUtf8("selectTeacherLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.selectTeacherLabel)
        self.selectTeacherComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.selectTeacherComboBox.setObjectName(_fromUtf8("selectTeacherComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.selectTeacherComboBox)
        self.pushButton = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectTeacherLabel.setText(_translate("Dialog", "Select Teacher", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))

