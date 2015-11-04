# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advsearch.ui'
#
# Created: Tue Nov  3 18:42:03 2015
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

class Ui_advsearch_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(378, 349)
        self.ID_adv_ledit = QtGui.QLineEdit(Dialog)
        self.ID_adv_ledit.setGeometry(QtCore.QRect(100, 30, 161, 20))
        self.ID_adv_ledit.setObjectName(_fromUtf8("ID_adv_ledit"))
        self.Phone_adv_ledit = QtGui.QLineEdit(Dialog)
        self.Phone_adv_ledit.setGeometry(QtCore.QRect(100, 130, 161, 20))
        self.Phone_adv_ledit.setObjectName(_fromUtf8("Phone_adv_ledit"))
        self.Name_adv_ledit = QtGui.QLineEdit(Dialog)
        self.Name_adv_ledit.setGeometry(QtCore.QRect(100, 80, 161, 20))
        self.Name_adv_ledit.setObjectName(_fromUtf8("Name_adv_ledit"))
        self.Guardian_adv_ledit = QtGui.QLineEdit(Dialog)
        self.Guardian_adv_ledit.setGeometry(QtCore.QRect(100, 180, 161, 20))
        self.Guardian_adv_ledit.setObjectName(_fromUtf8("Guardian_adv_ledit"))
        self.ID_cbox = QtGui.QCheckBox(Dialog)
        self.ID_cbox.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.ID_cbox.setObjectName(_fromUtf8("ID_cbox"))
        self.Name_cobx = QtGui.QCheckBox(Dialog)
        self.Name_cobx.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.Name_cobx.setObjectName(_fromUtf8("Name_cobx"))
        self.Phone_cbox = QtGui.QCheckBox(Dialog)
        self.Phone_cbox.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.Phone_cbox.setObjectName(_fromUtf8("Phone_cbox"))
        self.Guardian_cbox = QtGui.QCheckBox(Dialog)
        self.Guardian_cbox.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.Guardian_cbox.setObjectName(_fromUtf8("Guardian_cbox"))
        self.Birth_cbox = QtGui.QCheckBox(Dialog)
        self.Birth_cbox.setGeometry(QtCore.QRect(10, 230, 131, 20))
        self.Birth_cbox.setObjectName(_fromUtf8("Birth_cbox"))
        self.Seacch_adv_btn = QtGui.QPushButton(Dialog)
        self.Seacch_adv_btn.setGeometry(QtCore.QRect(80, 290, 75, 23))
        self.Seacch_adv_btn.setObjectName(_fromUtf8("Seacch_adv_btn"))
        self.Cancel_adv_btn = QtGui.QPushButton(Dialog)
        self.Cancel_adv_btn.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.Cancel_adv_btn.setObjectName(_fromUtf8("Cancel_adv_btn"))
        self.Id_adv_label = QtGui.QLabel(Dialog)
        self.Id_adv_label.setGeometry(QtCore.QRect(270, 30, 91, 16))
        self.Id_adv_label.setObjectName(_fromUtf8("Id_adv_label"))
        self.Name_adv_label = QtGui.QLabel(Dialog)
        self.Name_adv_label.setGeometry(QtCore.QRect(270, 80, 91, 16))
        self.Name_adv_label.setObjectName(_fromUtf8("Name_adv_label"))
        self.Phone_adv_label = QtGui.QLabel(Dialog)
        self.Phone_adv_label.setGeometry(QtCore.QRect(270, 130, 91, 16))
        self.Phone_adv_label.setObjectName(_fromUtf8("Phone_adv_label"))
        self.Guardian_adv_label = QtGui.QLabel(Dialog)
        self.Guardian_adv_label.setGeometry(QtCore.QRect(270, 180, 91, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.Guardian_adv_label.setPalette(palette)
        self.Guardian_adv_label.setObjectName(_fromUtf8("Guardian_adv_label"))
        self.Start_dateedit = QtGui.QDateEdit(Dialog)
        self.Start_dateedit.setGeometry(QtCore.QRect(140, 230, 91, 22))
        self.Start_dateedit.setObjectName(_fromUtf8("Start_dateedit"))
        self.End_dateedit = QtGui.QDateEdit(Dialog)
        self.End_dateedit.setGeometry(QtCore.QRect(260, 230, 91, 22))
        self.End_dateedit.setObjectName(_fromUtf8("End_dateedit"))
        self.Birth_to_label = QtGui.QLabel(Dialog)
        self.Birth_to_label.setGeometry(QtCore.QRect(240, 230, 21, 21))
        self.Birth_to_label.setObjectName(_fromUtf8("Birth_to_label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.ID_cbox.setText(_translate("Dialog", "ID", None))
        self.Name_cobx.setText(_translate("Dialog", "Name", None))
        self.Phone_cbox.setText(_translate("Dialog", "Phone", None))
        self.Guardian_cbox.setText(_translate("Dialog", "Guardian", None))
        self.Birth_cbox.setText(_translate("Dialog", "Date of Birth From", None))
        self.Seacch_adv_btn.setText(_translate("Dialog", "Search", None))
        self.Cancel_adv_btn.setText(_translate("Dialog", "Cancel", None))
        self.Id_adv_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Name_adv_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Phone_adv_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Guardian_adv_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Birth_to_label.setText(_translate("Dialog", "To", None))

