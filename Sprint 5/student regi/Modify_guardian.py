# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Modify_guardian.ui'
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

class Ui_add_teacher(object):
    def setupUi(self, add_teacher):
        add_teacher.setObjectName(_fromUtf8("add_teacher"))
        add_teacher.resize(698, 298)
        self.formLayoutWidget = QtGui.QWidget(add_teacher)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 681, 271))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.NameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.NameLabel.setObjectName(_fromUtf8("NameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.NameLabel)
        self.nameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameLineEdit)
        self.homePhoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.homePhoneLabel.setObjectName(_fromUtf8("homePhoneLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.homePhoneLabel)
        self.homePhoneLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.homePhoneLineEdit.setObjectName(_fromUtf8("homePhoneLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.homePhoneLineEdit)
        self.cellPhoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.cellPhoneLabel.setObjectName(_fromUtf8("cellPhoneLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.cellPhoneLabel)
        self.cellPhoneLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.cellPhoneLineEdit.setObjectName(_fromUtf8("cellPhoneLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cellPhoneLineEdit)
        self.workPhoneLabel = QtGui.QLabel(self.formLayoutWidget)
        self.workPhoneLabel.setObjectName(_fromUtf8("workPhoneLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.workPhoneLabel)
        self.workPhoneLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.workPhoneLineEdit.setObjectName(_fromUtf8("workPhoneLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.workPhoneLineEdit)
        self.addressLabel = QtGui.QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtGui.QLabel(self.formLayoutWidget)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cityLineEdit)
        self.stateLabel = QtGui.QLabel(self.formLayoutWidget)
        self.stateLabel.setObjectName(_fromUtf8("stateLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.stateLabel)
        self.stateComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.stateComboBox.setObjectName(_fromUtf8("stateComboBox"))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.stateComboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.stateComboBox)
        self.zipcodeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.zipcodeLabel.setObjectName(_fromUtf8("zipcodeLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.zipcodeLabel)
        self.zipcodeLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.zipcodeLineEdit.setObjectName(_fromUtf8("zipcodeLineEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.zipcodeLineEdit)
        self.emailLabel = QtGui.QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.requiredLabel = QtGui.QLabel(self.formLayoutWidget)
        self.requiredLabel.setObjectName(_fromUtf8("requiredLabel"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.requiredLabel)
        self.Submit_btn = QtGui.QPushButton(self.formLayoutWidget)
        self.Submit_btn.setObjectName(_fromUtf8("Submit_btn"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.Submit_btn)

        self.retranslateUi(add_teacher)
        QtCore.QMetaObject.connectSlotsByName(add_teacher)

    def retranslateUi(self, add_teacher):
        add_teacher.setWindowTitle(_translate("add_teacher", "Dialog", None))
        self.NameLabel.setText(_translate("add_teacher", "Name*", None))
        self.homePhoneLabel.setText(_translate("add_teacher", "Home Phone*", None))
        self.cellPhoneLabel.setText(_translate("add_teacher", "Cell Phone", None))
        self.workPhoneLabel.setText(_translate("add_teacher", "Work Phone", None))
        self.addressLabel.setText(_translate("add_teacher", "Address*", None))
        self.cityLabel.setText(_translate("add_teacher", "City*", None))
        self.stateLabel.setText(_translate("add_teacher", "State*", None))
        self.stateComboBox.setItemText(0, _translate("add_teacher", "Alabama", None))
        self.stateComboBox.setItemText(1, _translate("add_teacher", "Alaska", None))
        self.stateComboBox.setItemText(2, _translate("add_teacher", "Arizona", None))
        self.stateComboBox.setItemText(3, _translate("add_teacher", "Arkansas", None))
        self.stateComboBox.setItemText(4, _translate("add_teacher", "California", None))
        self.stateComboBox.setItemText(5, _translate("add_teacher", "Colorado", None))
        self.stateComboBox.setItemText(6, _translate("add_teacher", "Connecticut", None))
        self.stateComboBox.setItemText(7, _translate("add_teacher", "Delaware", None))
        self.stateComboBox.setItemText(8, _translate("add_teacher", "Florida", None))
        self.stateComboBox.setItemText(9, _translate("add_teacher", "Georgia", None))
        self.stateComboBox.setItemText(10, _translate("add_teacher", "Hawaii", None))
        self.stateComboBox.setItemText(11, _translate("add_teacher", "Idaho", None))
        self.stateComboBox.setItemText(12, _translate("add_teacher", "Illinois", None))
        self.stateComboBox.setItemText(13, _translate("add_teacher", "Indiana", None))
        self.stateComboBox.setItemText(14, _translate("add_teacher", "Iowa", None))
        self.stateComboBox.setItemText(15, _translate("add_teacher", "Kansas", None))
        self.stateComboBox.setItemText(16, _translate("add_teacher", "Kentucky", None))
        self.stateComboBox.setItemText(17, _translate("add_teacher", "Louisiana", None))
        self.stateComboBox.setItemText(18, _translate("add_teacher", "Maine", None))
        self.stateComboBox.setItemText(19, _translate("add_teacher", "Maryland", None))
        self.stateComboBox.setItemText(20, _translate("add_teacher", "Massachusetts", None))
        self.stateComboBox.setItemText(21, _translate("add_teacher", "Michigan", None))
        self.stateComboBox.setItemText(22, _translate("add_teacher", "Minnesota", None))
        self.stateComboBox.setItemText(23, _translate("add_teacher", "Mississippi", None))
        self.stateComboBox.setItemText(24, _translate("add_teacher", "Missouri", None))
        self.stateComboBox.setItemText(25, _translate("add_teacher", "Montana", None))
        self.stateComboBox.setItemText(26, _translate("add_teacher", "Nebraska", None))
        self.stateComboBox.setItemText(27, _translate("add_teacher", "Nevada", None))
        self.stateComboBox.setItemText(28, _translate("add_teacher", "New Hampshire", None))
        self.stateComboBox.setItemText(29, _translate("add_teacher", "New Jersey", None))
        self.stateComboBox.setItemText(30, _translate("add_teacher", "New Mexico", None))
        self.stateComboBox.setItemText(31, _translate("add_teacher", "New York", None))
        self.stateComboBox.setItemText(32, _translate("add_teacher", "North Carolina", None))
        self.stateComboBox.setItemText(33, _translate("add_teacher", "North Dakota", None))
        self.stateComboBox.setItemText(34, _translate("add_teacher", "Ohio", None))
        self.stateComboBox.setItemText(35, _translate("add_teacher", "Oklahoma", None))
        self.stateComboBox.setItemText(36, _translate("add_teacher", "Oregon", None))
        self.stateComboBox.setItemText(37, _translate("add_teacher", "Pennsylvania", None))
        self.stateComboBox.setItemText(38, _translate("add_teacher", "Rhode Island", None))
        self.stateComboBox.setItemText(39, _translate("add_teacher", "South Carolina", None))
        self.stateComboBox.setItemText(40, _translate("add_teacher", "South Dakota", None))
        self.stateComboBox.setItemText(41, _translate("add_teacher", "Tennessee", None))
        self.stateComboBox.setItemText(42, _translate("add_teacher", "Texas", None))
        self.stateComboBox.setItemText(43, _translate("add_teacher", "Utah", None))
        self.stateComboBox.setItemText(44, _translate("add_teacher", "Vermont", None))
        self.stateComboBox.setItemText(45, _translate("add_teacher", "Virginia", None))
        self.stateComboBox.setItemText(46, _translate("add_teacher", "Washington", None))
        self.stateComboBox.setItemText(47, _translate("add_teacher", "West Virginia", None))
        self.stateComboBox.setItemText(48, _translate("add_teacher", "Wisconsin", None))
        self.stateComboBox.setItemText(49, _translate("add_teacher", "Wyoming", None))
        self.zipcodeLabel.setText(_translate("add_teacher", "Zipcode*", None))
        self.emailLabel.setText(_translate("add_teacher", "Email", None))
        self.requiredLabel.setText(_translate("add_teacher", "* Required Field", None))
        self.Submit_btn.setText(_translate("add_teacher", "Submit", None))
