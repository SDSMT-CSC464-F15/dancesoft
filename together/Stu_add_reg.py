# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Stu_add.ui'
#
# Created: Sun Mar 20 13:24:23 2016
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

class Ui_Stu_reg_dialog(object):
    def setupUi(self, Stu_reg_dialog):
        Stu_reg_dialog.setObjectName(_fromUtf8("Stu_reg_dialog"))
        Stu_reg_dialog.resize(784, 491)
        self.Id_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Id_detail_label.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.Id_detail_label.setObjectName(_fromUtf8("Id_detail_label"))
        self.Gender_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Gender_detail_label.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.Gender_detail_label.setObjectName(_fromUtf8("Gender_detail_label"))
        self.Birth_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Birth_detail_label.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.Birth_detail_label.setObjectName(_fromUtf8("Birth_detail_label"))
        self.Pguradian_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Pguradian_detail_label.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.Pguradian_detail_label.setObjectName(_fromUtf8("Pguradian_detail_label"))
        self.Econtact_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Econtact_detail_label.setGeometry(QtCore.QRect(20, 210, 101, 16))
        self.Econtact_detail_label.setObjectName(_fromUtf8("Econtact_detail_label"))
        self.Tuition_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Tuition_detail_label.setGeometry(QtCore.QRect(20, 250, 101, 16))
        self.Tuition_detail_label.setObjectName(_fromUtf8("Tuition_detail_label"))
        self.Address_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Address_detail_label.setGeometry(QtCore.QRect(20, 290, 54, 12))
        self.Address_detail_label.setObjectName(_fromUtf8("Address_detail_label"))
        self.Name_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Name_detail_label.setGeometry(QtCore.QRect(380, 50, 54, 12))
        self.Name_detail_label.setObjectName(_fromUtf8("Name_detail_label"))
        self.Email_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Email_detail_label.setGeometry(QtCore.QRect(380, 90, 54, 12))
        self.Email_detail_label.setObjectName(_fromUtf8("Email_detail_label"))
        self.Phone_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Phone_detail_label.setGeometry(QtCore.QRect(380, 130, 54, 12))
        self.Phone_detail_label.setObjectName(_fromUtf8("Phone_detail_label"))
        self.Sguardian_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Sguardian_detail_label.setGeometry(QtCore.QRect(380, 170, 111, 16))
        self.Sguardian_detail_label.setObjectName(_fromUtf8("Sguardian_detail_label"))
        self.Ephone_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Ephone_detail_label.setGeometry(QtCore.QRect(380, 210, 111, 16))
        self.Ephone_detail_label.setObjectName(_fromUtf8("Ephone_detail_label"))
        self.Id_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Id_detail_lineEdit.setGeometry(QtCore.QRect(130, 50, 221, 20))
        self.Id_detail_lineEdit.setObjectName(_fromUtf8("Id_detail_lineEdit"))
        self.Gender_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Gender_detail_lineEdit.setGeometry(QtCore.QRect(130, 90, 221, 20))
        self.Gender_detail_lineEdit.setObjectName(_fromUtf8("Gender_detail_lineEdit"))
        self.Pguradian_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Pguradian_detail_lineEdit.setGeometry(QtCore.QRect(130, 170, 221, 20))
        self.Pguradian_detail_lineEdit.setObjectName(_fromUtf8("Pguradian_detail_lineEdit"))
        self.Econtact_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Econtact_detail_lineEdit.setGeometry(QtCore.QRect(130, 210, 221, 20))
        self.Econtact_detail_lineEdit.setObjectName(_fromUtf8("Econtact_detail_lineEdit"))
        self.Tuition_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Tuition_detail_lineEdit.setGeometry(QtCore.QRect(130, 250, 221, 20))
        self.Tuition_detail_lineEdit.setObjectName(_fromUtf8("Tuition_detail_lineEdit"))
        self.Phone_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Phone_detail_lineEdit.setGeometry(QtCore.QRect(500, 130, 221, 20))
        self.Phone_detail_lineEdit.setObjectName(_fromUtf8("Phone_detail_lineEdit"))
        self.Name_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Name_detail_lineEdit.setGeometry(QtCore.QRect(500, 50, 221, 20))
        self.Name_detail_lineEdit.setObjectName(_fromUtf8("Name_detail_lineEdit"))
        self.Sguardian_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Sguardian_detail_lineEdit.setGeometry(QtCore.QRect(500, 170, 221, 20))
        self.Sguardian_detail_lineEdit.setObjectName(_fromUtf8("Sguardian_detail_lineEdit"))
        self.Ephone_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Ephone_detail_lineEdit.setGeometry(QtCore.QRect(500, 210, 221, 20))
        self.Ephone_detail_lineEdit.setObjectName(_fromUtf8("Ephone_detail_lineEdit"))
        self.Email_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Email_detail_lineEdit.setGeometry(QtCore.QRect(500, 90, 221, 20))
        self.Email_detail_lineEdit.setObjectName(_fromUtf8("Email_detail_lineEdit"))
        self.List_detail_btn = QtGui.QPushButton(Stu_reg_dialog)
        self.List_detail_btn.setGeometry(QtCore.QRect(540, 460, 91, 21))
        self.List_detail_btn.setObjectName(_fromUtf8("List_detail_btn"))
        self.Medical_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.Medical_detail_label.setGeometry(QtCore.QRect(380, 250, 121, 16))
        self.Medical_detail_label.setObjectName(_fromUtf8("Medical_detail_label"))
        self.Update_detail_btn = QtGui.QPushButton(Stu_reg_dialog)
        self.Update_detail_btn.setGeometry(QtCore.QRect(660, 460, 91, 21))
        self.Update_detail_btn.setObjectName(_fromUtf8("Update_detail_btn"))
        self.Medical_detail_textEdit = QtGui.QTextEdit(Stu_reg_dialog)
        self.Medical_detail_textEdit.setGeometry(QtCore.QRect(500, 250, 221, 141))
        self.Medical_detail_textEdit.setObjectName(_fromUtf8("Medical_detail_textEdit"))
        self.Address_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.Address_detail_lineEdit.setGeometry(QtCore.QRect(130, 290, 221, 20))
        self.Address_detail_lineEdit.setObjectName(_fromUtf8("Address_detail_lineEdit"))
        self.City_detail_label = QtGui.QLabel(Stu_reg_dialog)
        self.City_detail_label.setGeometry(QtCore.QRect(20, 330, 54, 12))
        self.City_detail_label.setObjectName(_fromUtf8("City_detail_label"))
        self.State_detail_label_3 = QtGui.QLabel(Stu_reg_dialog)
        self.State_detail_label_3.setGeometry(QtCore.QRect(20, 370, 54, 12))
        self.State_detail_label_3.setObjectName(_fromUtf8("State_detail_label_3"))
        self.City_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.City_detail_lineEdit.setGeometry(QtCore.QRect(130, 330, 221, 20))
        self.City_detail_lineEdit.setObjectName(_fromUtf8("City_detail_lineEdit"))
        self.State_detail_lineEdit = QtGui.QLineEdit(Stu_reg_dialog)
        self.State_detail_lineEdit.setGeometry(QtCore.QRect(130, 370, 221, 20))
        self.State_detail_lineEdit.setObjectName(_fromUtf8("State_detail_lineEdit"))
        self.Birth_detail_dateEdit = QtGui.QDateEdit(Stu_reg_dialog)
        self.Birth_detail_dateEdit.setGeometry(QtCore.QRect(130, 130, 221, 22))
        self.Birth_detail_dateEdit.setObjectName(_fromUtf8("Birth_detail_dateEdit"))

        self.retranslateUi(Stu_reg_dialog)
        QtCore.QMetaObject.connectSlotsByName(Stu_reg_dialog)

    def retranslateUi(self, Stu_reg_dialog):
        Stu_reg_dialog.setWindowTitle(_translate("Stu_reg_dialog", "Dialog", None))
        self.Id_detail_label.setText(_translate("Stu_reg_dialog", "ID", None))
        self.Gender_detail_label.setText(_translate("Stu_reg_dialog", "Gender", None))
        self.Birth_detail_label.setText(_translate("Stu_reg_dialog", "Date Birth", None))
        self.Pguradian_detail_label.setText(_translate("Stu_reg_dialog", "Primary Guardian", None))
        self.Econtact_detail_label.setText(_translate("Stu_reg_dialog", "Emergency Contact", None))
        self.Tuition_detail_label.setText(_translate("Stu_reg_dialog", "Tuition", None))
        self.Address_detail_label.setText(_translate("Stu_reg_dialog", "Address", None))
        self.Name_detail_label.setText(_translate("Stu_reg_dialog", "Name", None))
        self.Email_detail_label.setText(_translate("Stu_reg_dialog", "Email", None))
        self.Phone_detail_label.setText(_translate("Stu_reg_dialog", "Phone", None))
        self.Sguardian_detail_label.setText(_translate("Stu_reg_dialog", "Secondary Guardian", None))
        self.Ephone_detail_label.setText(_translate("Stu_reg_dialog", "Emergency Phone", None))
        self.List_detail_btn.setText(_translate("Stu_reg_dialog", "List", None))
        self.Medical_detail_label.setText(_translate("Stu_reg_dialog", "Medical Information", None))
        self.Update_detail_btn.setText(_translate("Stu_reg_dialog", "Add", None))
        self.City_detail_label.setText(_translate("Stu_reg_dialog", "City", None))
        self.State_detail_label_3.setText(_translate("Stu_reg_dialog", "State", None))

