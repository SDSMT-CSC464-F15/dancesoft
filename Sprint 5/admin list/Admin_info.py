# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admininfo.ui'
#
# Created: Fri Mar 11 14:34:31 2016
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

class Ui_Admin_info_dialog(object):
    def setupUi(self, Admin_info_dialog):
        Admin_info_dialog.setObjectName(_fromUtf8("Admin_info_dialog"))
        Admin_info_dialog.resize(784, 445)
        self.Id_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Id_detail_label.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.Id_detail_label.setObjectName(_fromUtf8("Id_detail_label"))
        self.Gender_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Gender_detail_label.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.Gender_detail_label.setObjectName(_fromUtf8("Gender_detail_label"))
        self.Birth_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Birth_detail_label.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.Birth_detail_label.setObjectName(_fromUtf8("Birth_detail_label"))
        self.Cellphone_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Cellphone_detail_label.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.Cellphone_detail_label.setObjectName(_fromUtf8("Cellphone_detail_label"))
        self.SNN_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.SNN_detail_label.setGeometry(QtCore.QRect(20, 210, 101, 16))
        self.SNN_detail_label.setObjectName(_fromUtf8("SNN_detail_label"))
        self.Zipcode_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Zipcode_detail_label.setGeometry(QtCore.QRect(20, 250, 101, 16))
        self.Zipcode_detail_label.setObjectName(_fromUtf8("Zipcode_detail_label"))
        self.Address_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Address_detail_label.setGeometry(QtCore.QRect(20, 290, 54, 12))
        self.Address_detail_label.setObjectName(_fromUtf8("Address_detail_label"))
        self.Name_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Name_detail_label.setGeometry(QtCore.QRect(380, 50, 54, 12))
        self.Name_detail_label.setObjectName(_fromUtf8("Name_detail_label"))
        self.Email_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Email_detail_label.setGeometry(QtCore.QRect(380, 90, 54, 12))
        self.Email_detail_label.setObjectName(_fromUtf8("Email_detail_label"))
        self.Homephone_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Homephone_detail_label.setGeometry(QtCore.QRect(380, 130, 81, 16))
        self.Homephone_detail_label.setObjectName(_fromUtf8("Homephone_detail_label"))
        self.Workphone_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Workphone_detail_label.setGeometry(QtCore.QRect(380, 170, 111, 16))
        self.Workphone_detail_label.setObjectName(_fromUtf8("Workphone_detail_label"))
        self.Payrate_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Payrate_detail_label.setGeometry(QtCore.QRect(380, 210, 111, 16))
        self.Payrate_detail_label.setObjectName(_fromUtf8("Payrate_detail_label"))
        self.Id_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Id_detail_lineEdit.setGeometry(QtCore.QRect(130, 50, 221, 20))
        self.Id_detail_lineEdit.setObjectName(_fromUtf8("Id_detail_lineEdit"))
        self.Gender_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Gender_detail_lineEdit.setGeometry(QtCore.QRect(130, 90, 221, 20))
        self.Gender_detail_lineEdit.setObjectName(_fromUtf8("Gender_detail_lineEdit"))
        self.Cellphone_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Cellphone_detail_lineEdit.setGeometry(QtCore.QRect(130, 170, 221, 20))
        self.Cellphone_detail_lineEdit.setObjectName(_fromUtf8("Cellphone_detail_lineEdit"))
        self.SSN_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.SSN_detail_lineEdit.setGeometry(QtCore.QRect(130, 210, 221, 20))
        self.SSN_detail_lineEdit.setObjectName(_fromUtf8("SSN_detail_lineEdit"))
        self.Zipcode_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Zipcode_detail_lineEdit.setGeometry(QtCore.QRect(130, 250, 221, 20))
        self.Zipcode_detail_lineEdit.setObjectName(_fromUtf8("Zipcode_detail_lineEdit"))
        self.Homephone_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Homephone_detail_lineEdit.setGeometry(QtCore.QRect(500, 130, 221, 20))
        self.Homephone_detail_lineEdit.setObjectName(_fromUtf8("Homephone_detail_lineEdit"))
        self.Name_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Name_detail_lineEdit.setGeometry(QtCore.QRect(500, 50, 221, 20))
        self.Name_detail_lineEdit.setObjectName(_fromUtf8("Name_detail_lineEdit"))
        self.Workphone_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Workphone_detail_lineEdit.setGeometry(QtCore.QRect(500, 170, 221, 20))
        self.Workphone_detail_lineEdit.setObjectName(_fromUtf8("Workphone_detail_lineEdit"))
        self.Payrate_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Payrate_detail_lineEdit.setGeometry(QtCore.QRect(500, 210, 221, 20))
        self.Payrate_detail_lineEdit.setObjectName(_fromUtf8("Payrate_detail_lineEdit"))
        self.Email_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Email_detail_lineEdit.setGeometry(QtCore.QRect(500, 90, 221, 20))
        self.Email_detail_lineEdit.setObjectName(_fromUtf8("Email_detail_lineEdit"))
        self.Close_detail_btn = QtGui.QPushButton(Admin_info_dialog)
        self.Close_detail_btn.setGeometry(QtCore.QRect(650, 410, 91, 21))
        self.Close_detail_btn.setObjectName(_fromUtf8("Close_detail_btn"))
        self.Medical_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.Medical_detail_label.setGeometry(QtCore.QRect(380, 250, 121, 16))
        self.Medical_detail_label.setObjectName(_fromUtf8("Medical_detail_label"))
        self.Medical_detail_textEdit = QtGui.QTextEdit(Admin_info_dialog)
        self.Medical_detail_textEdit.setGeometry(QtCore.QRect(500, 250, 221, 141))
        self.Medical_detail_textEdit.setObjectName(_fromUtf8("Medical_detail_textEdit"))
        self.Address_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.Address_detail_lineEdit.setGeometry(QtCore.QRect(130, 290, 221, 20))
        self.Address_detail_lineEdit.setObjectName(_fromUtf8("Address_detail_lineEdit"))
        self.City_detail_label = QtGui.QLabel(Admin_info_dialog)
        self.City_detail_label.setGeometry(QtCore.QRect(20, 330, 54, 12))
        self.City_detail_label.setObjectName(_fromUtf8("City_detail_label"))
        self.State_detail_label_3 = QtGui.QLabel(Admin_info_dialog)
        self.State_detail_label_3.setGeometry(QtCore.QRect(20, 370, 54, 12))
        self.State_detail_label_3.setObjectName(_fromUtf8("State_detail_label_3"))
        self.City_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.City_detail_lineEdit.setGeometry(QtCore.QRect(130, 330, 221, 20))
        self.City_detail_lineEdit.setObjectName(_fromUtf8("City_detail_lineEdit"))
        self.State_detail_lineEdit = QtGui.QLineEdit(Admin_info_dialog)
        self.State_detail_lineEdit.setGeometry(QtCore.QRect(130, 370, 221, 20))
        self.State_detail_lineEdit.setObjectName(_fromUtf8("State_detail_lineEdit"))
        self.Birth_detail_dateEdit = QtGui.QDateEdit(Admin_info_dialog)
        self.Birth_detail_dateEdit.setGeometry(QtCore.QRect(130, 130, 221, 22))
        self.Birth_detail_dateEdit.setObjectName(_fromUtf8("Birth_detail_dateEdit"))

        self.retranslateUi(Admin_info_dialog)
        QtCore.QMetaObject.connectSlotsByName(Admin_info_dialog)

    def retranslateUi(self, Admin_info_dialog):
        Admin_info_dialog.setWindowTitle(_translate("Admin_info_dialog", "Dialog", None))
        self.Id_detail_label.setText(_translate("Admin_info_dialog", "ID", None))
        self.Gender_detail_label.setText(_translate("Admin_info_dialog", "Gender", None))
        self.Birth_detail_label.setText(_translate("Admin_info_dialog", "Date Birth", None))
        self.Cellphone_detail_label.setText(_translate("Admin_info_dialog", "Cell Phone", None))
        self.SNN_detail_label.setText(_translate("Admin_info_dialog", "SSN", None))
        self.Zipcode_detail_label.setText(_translate("Admin_info_dialog", "Zipcode", None))
        self.Address_detail_label.setText(_translate("Admin_info_dialog", "Address", None))
        self.Name_detail_label.setText(_translate("Admin_info_dialog", "Name", None))
        self.Email_detail_label.setText(_translate("Admin_info_dialog", "Email", None))
        self.Homephone_detail_label.setText(_translate("Admin_info_dialog", "Home Phone", None))
        self.Workphone_detail_label.setText(_translate("Admin_info_dialog", "Work Phone", None))
        self.Payrate_detail_label.setText(_translate("Admin_info_dialog", "Pay Rate", None))
        self.Close_detail_btn.setText(_translate("Admin_info_dialog", "Close", None))
        self.Medical_detail_label.setText(_translate("Admin_info_dialog", "Medical Information", None))
        self.City_detail_label.setText(_translate("Admin_info_dialog", "City", None))
        self.State_detail_label_3.setText(_translate("Admin_info_dialog", "State", None))

