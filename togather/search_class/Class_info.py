# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Classinfo.ui'
#
# Created: Mon Dec 28 12:43:51 2015
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

class Ui_Class_info_dialog(object):
    def setupUi(self, Class_info_dialog):
        Class_info_dialog.setObjectName(_fromUtf8("Class_info_dialog"))
        Class_info_dialog.resize(784, 465)
        self.Id_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Id_detail_label.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.Id_detail_label.setObjectName(_fromUtf8("Id_detail_label"))
        self.Cost_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Cost_detail_label.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.Cost_detail_label.setObjectName(_fromUtf8("Cost_detail_label"))
        self.Day_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Day_detail_label.setGeometry(QtCore.QRect(20, 130, 61, 16))
        self.Day_detail_label.setObjectName(_fromUtf8("Day_detail_label"))
        self.Capacity_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Capacity_detail_label.setGeometry(QtCore.QRect(20, 170, 101, 16))
        self.Capacity_detail_label.setObjectName(_fromUtf8("Capacity_detail_label"))
        self.Date_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Date_detail_label.setGeometry(QtCore.QRect(20, 210, 101, 16))
        self.Date_detail_label.setObjectName(_fromUtf8("Date_detail_label"))
        self.Name_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Name_detail_label.setGeometry(QtCore.QRect(380, 50, 54, 12))
        self.Name_detail_label.setObjectName(_fromUtf8("Name_detail_label"))
        self.Time_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Time_detail_label.setGeometry(QtCore.QRect(380, 90, 54, 12))
        self.Time_detail_label.setObjectName(_fromUtf8("Time_detail_label"))
        self.Location_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Location_detail_label.setGeometry(QtCore.QRect(380, 130, 54, 12))
        self.Location_detail_label.setObjectName(_fromUtf8("Location_detail_label"))
        self.Clothing_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Clothing_detail_label.setGeometry(QtCore.QRect(380, 170, 111, 16))
        self.Clothing_detail_label.setObjectName(_fromUtf8("Clothing_detail_label"))
        self.Age_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Age_detail_label.setGeometry(QtCore.QRect(380, 210, 111, 16))
        self.Age_detail_label.setObjectName(_fromUtf8("Age_detail_label"))
        self.Id_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Id_detail_lineEdit.setGeometry(QtCore.QRect(130, 50, 221, 20))
        self.Id_detail_lineEdit.setObjectName(_fromUtf8("Id_detail_lineEdit"))
        self.Cost_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Cost_detail_lineEdit.setGeometry(QtCore.QRect(130, 90, 221, 20))
        self.Cost_detail_lineEdit.setObjectName(_fromUtf8("Cost_detail_lineEdit"))
        self.Capacity_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Capacity_detail_lineEdit.setGeometry(QtCore.QRect(130, 170, 221, 20))
        self.Capacity_detail_lineEdit.setObjectName(_fromUtf8("Capacity_detail_lineEdit"))
        self.Location_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Location_detail_lineEdit.setGeometry(QtCore.QRect(500, 130, 221, 20))
        self.Location_detail_lineEdit.setObjectName(_fromUtf8("Location_detail_lineEdit"))
        self.Name_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Name_detail_lineEdit.setGeometry(QtCore.QRect(500, 50, 221, 20))
        self.Name_detail_lineEdit.setObjectName(_fromUtf8("Name_detail_lineEdit"))
        self.Clothing_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Clothing_detail_lineEdit.setGeometry(QtCore.QRect(500, 170, 221, 20))
        self.Clothing_detail_lineEdit.setObjectName(_fromUtf8("Clothing_detail_lineEdit"))
        self.Age_start_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Age_start_detail_lineEdit.setGeometry(QtCore.QRect(500, 210, 91, 20))
        self.Age_start_detail_lineEdit.setObjectName(_fromUtf8("Age_start_detail_lineEdit"))
        self.Close_detail_btn = QtGui.QPushButton(Class_info_dialog)
        self.Close_detail_btn.setGeometry(QtCore.QRect(540, 420, 91, 21))
        self.Close_detail_btn.setObjectName(_fromUtf8("Close_detail_btn"))
        self.Description_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Description_detail_label.setGeometry(QtCore.QRect(380, 250, 121, 16))
        self.Description_detail_label.setObjectName(_fromUtf8("Description_detail_label"))
        self.Update_detail_btn = QtGui.QPushButton(Class_info_dialog)
        self.Update_detail_btn.setGeometry(QtCore.QRect(660, 420, 91, 21))
        self.Update_detail_btn.setObjectName(_fromUtf8("Update_detail_btn"))
        self.Description_detail_textEdit = QtGui.QTextEdit(Class_info_dialog)
        self.Description_detail_textEdit.setGeometry(QtCore.QRect(500, 250, 221, 141))
        self.Description_detail_textEdit.setObjectName(_fromUtf8("Description_detail_textEdit"))
        self.Time_start_detail_timeEdit = QtGui.QTimeEdit(Class_info_dialog)
        self.Time_start_detail_timeEdit.setGeometry(QtCore.QRect(500, 90, 91, 22))
        self.Time_start_detail_timeEdit.setObjectName(_fromUtf8("Time_start_detail_timeEdit"))
        self.Time_end_detail_timeEdit = QtGui.QTimeEdit(Class_info_dialog)
        self.Time_end_detail_timeEdit.setGeometry(QtCore.QRect(630, 90, 91, 22))
        self.Time_end_detail_timeEdit.setObjectName(_fromUtf8("Time_end_detail_timeEdit"))
        self.Time_to_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Time_to_detail_label.setGeometry(QtCore.QRect(600, 90, 31, 16))
        self.Time_to_detail_label.setObjectName(_fromUtf8("Time_to_detail_label"))
        self.Day_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Day_detail_lineEdit.setGeometry(QtCore.QRect(130, 130, 221, 20))
        self.Day_detail_lineEdit.setObjectName(_fromUtf8("Day_detail_lineEdit"))
        self.Date_start_detail_dateEdit = QtGui.QDateEdit(Class_info_dialog)
        self.Date_start_detail_dateEdit.setGeometry(QtCore.QRect(130, 210, 91, 22))
        self.Date_start_detail_dateEdit.setObjectName(_fromUtf8("Date_start_detail_dateEdit"))
        self.Date_end_detail_dateEdit = QtGui.QDateEdit(Class_info_dialog)
        self.Date_end_detail_dateEdit.setGeometry(QtCore.QRect(260, 210, 91, 22))
        self.Date_end_detail_dateEdit.setObjectName(_fromUtf8("Date_end_detail_dateEdit"))
        self.Date_to_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Date_to_detail_label.setGeometry(QtCore.QRect(230, 210, 31, 16))
        self.Date_to_detail_label.setObjectName(_fromUtf8("Date_to_detail_label"))
        self.Age_end_detail_lineEdit = QtGui.QLineEdit(Class_info_dialog)
        self.Age_end_detail_lineEdit.setGeometry(QtCore.QRect(630, 210, 91, 20))
        self.Age_end_detail_lineEdit.setObjectName(_fromUtf8("Age_end_detail_lineEdit"))
        self.Age_to_detail_label = QtGui.QLabel(Class_info_dialog)
        self.Age_to_detail_label.setGeometry(QtCore.QRect(600, 210, 21, 16))
        self.Age_to_detail_label.setObjectName(_fromUtf8("Age_to_detail_label"))

        self.retranslateUi(Class_info_dialog)
        QtCore.QMetaObject.connectSlotsByName(Class_info_dialog)

    def retranslateUi(self, Class_info_dialog):
        Class_info_dialog.setWindowTitle(_translate("Class_info_dialog", "Dialog", None))
        self.Id_detail_label.setText(_translate("Class_info_dialog", "ID", None))
        self.Cost_detail_label.setText(_translate("Class_info_dialog", "Cost", None))
        self.Day_detail_label.setText(_translate("Class_info_dialog", "Day", None))
        self.Capacity_detail_label.setText(_translate("Class_info_dialog", "Capacity", None))
        self.Date_detail_label.setText(_translate("Class_info_dialog", "Date", None))
        self.Name_detail_label.setText(_translate("Class_info_dialog", "Name", None))
        self.Time_detail_label.setText(_translate("Class_info_dialog", "Time", None))
        self.Location_detail_label.setText(_translate("Class_info_dialog", "Location", None))
        self.Clothing_detail_label.setText(_translate("Class_info_dialog", "Clothing", None))
        self.Age_detail_label.setText(_translate("Class_info_dialog", "Age", None))
        self.Close_detail_btn.setText(_translate("Class_info_dialog", "Close", None))
        self.Description_detail_label.setText(_translate("Class_info_dialog", "Class Description", None))
        self.Update_detail_btn.setText(_translate("Class_info_dialog", "Update", None))
        self.Time_to_detail_label.setText(_translate("Class_info_dialog", "To", None))
        self.Date_to_detail_label.setText(_translate("Class_info_dialog", "To", None))
        self.Age_to_detail_label.setText(_translate("Class_info_dialog", "To", None))

