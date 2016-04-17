# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Advsearch.ui'
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

class Ui_advsearch_dialog(object):
    def setupUi(self, advsearch_dialog):
        advsearch_dialog.setObjectName(_fromUtf8("advsearch_dialog"))
        advsearch_dialog.resize(419, 349)
        self.ID_adv_ledit = QtGui.QLineEdit(advsearch_dialog)
        self.ID_adv_ledit.setGeometry(QtCore.QRect(150, 30, 161, 20))
        self.ID_adv_ledit.setObjectName(_fromUtf8("ID_adv_ledit"))
        self.Cost_start_adv_ledit = QtGui.QLineEdit(advsearch_dialog)
        self.Cost_start_adv_ledit.setGeometry(QtCore.QRect(150, 130, 61, 20))
        self.Cost_start_adv_ledit.setObjectName(_fromUtf8("Cost_start_adv_ledit"))
        self.Name_adv_ledit = QtGui.QLineEdit(advsearch_dialog)
        self.Name_adv_ledit.setGeometry(QtCore.QRect(150, 80, 161, 20))
        self.Name_adv_ledit.setObjectName(_fromUtf8("Name_adv_ledit"))
        self.Location_adv_ledit = QtGui.QLineEdit(advsearch_dialog)
        self.Location_adv_ledit.setGeometry(QtCore.QRect(150, 180, 161, 20))
        self.Location_adv_ledit.setObjectName(_fromUtf8("Location_adv_ledit"))
        self.ID_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.ID_cbox.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.ID_cbox.setObjectName(_fromUtf8("ID_cbox"))
        self.Name_cobx = QtGui.QCheckBox(advsearch_dialog)
        self.Name_cobx.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.Name_cobx.setObjectName(_fromUtf8("Name_cobx"))
        self.Cost_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.Cost_cbox.setGeometry(QtCore.QRect(10, 130, 121, 16))
        self.Cost_cbox.setObjectName(_fromUtf8("Cost_cbox"))
        self.Location_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.Location_cbox.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.Location_cbox.setObjectName(_fromUtf8("Location_cbox"))
        self.Time_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.Time_cbox.setGeometry(QtCore.QRect(10, 230, 131, 20))
        self.Time_cbox.setObjectName(_fromUtf8("Time_cbox"))
        self.Seacch_adv_btn = QtGui.QPushButton(advsearch_dialog)
        self.Seacch_adv_btn.setGeometry(QtCore.QRect(80, 290, 75, 23))
        self.Seacch_adv_btn.setObjectName(_fromUtf8("Seacch_adv_btn"))
        self.Cancel_adv_btn = QtGui.QPushButton(advsearch_dialog)
        self.Cancel_adv_btn.setGeometry(QtCore.QRect(210, 290, 75, 23))
        self.Cancel_adv_btn.setObjectName(_fromUtf8("Cancel_adv_btn"))
        self.Id_adv_label = QtGui.QLabel(advsearch_dialog)
        self.Id_adv_label.setGeometry(QtCore.QRect(320, 30, 91, 16))
        self.Id_adv_label.setObjectName(_fromUtf8("Id_adv_label"))
        self.Name_adv_label = QtGui.QLabel(advsearch_dialog)
        self.Name_adv_label.setGeometry(QtCore.QRect(320, 80, 91, 16))
        self.Name_adv_label.setObjectName(_fromUtf8("Name_adv_label"))
        self.Cost_adv_label = QtGui.QLabel(advsearch_dialog)
        self.Cost_adv_label.setGeometry(QtCore.QRect(320, 130, 91, 16))
        self.Cost_adv_label.setObjectName(_fromUtf8("Cost_adv_label"))
        self.Location_adv_label = QtGui.QLabel(advsearch_dialog)
        self.Location_adv_label.setGeometry(QtCore.QRect(320, 180, 91, 16))
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
        self.Location_adv_label.setPalette(palette)
        self.Location_adv_label.setObjectName(_fromUtf8("Location_adv_label"))
        self.Time_to_label = QtGui.QLabel(advsearch_dialog)
        self.Time_to_label.setGeometry(QtCore.QRect(240, 230, 21, 21))
        self.Time_to_label.setObjectName(_fromUtf8("Time_to_label"))
        self.ID_Exact_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.ID_Exact_cbox.setGeometry(QtCore.QRect(80, 30, 71, 16))
        self.ID_Exact_cbox.setObjectName(_fromUtf8("ID_Exact_cbox"))
        self.Name_Exact_cobx = QtGui.QCheckBox(advsearch_dialog)
        self.Name_Exact_cobx.setGeometry(QtCore.QRect(80, 80, 71, 16))
        self.Name_Exact_cobx.setObjectName(_fromUtf8("Name_Exact_cobx"))
        self.Location_Exact_cbox = QtGui.QCheckBox(advsearch_dialog)
        self.Location_Exact_cbox.setGeometry(QtCore.QRect(80, 180, 71, 16))
        self.Location_Exact_cbox.setObjectName(_fromUtf8("Location_Exact_cbox"))
        self.Cost_end_adv_ledit = QtGui.QLineEdit(advsearch_dialog)
        self.Cost_end_adv_ledit.setGeometry(QtCore.QRect(250, 130, 61, 20))
        self.Cost_end_adv_ledit.setObjectName(_fromUtf8("Cost_end_adv_ledit"))
        self.Cost_to_label = QtGui.QLabel(advsearch_dialog)
        self.Cost_to_label.setGeometry(QtCore.QRect(220, 130, 21, 16))
        self.Cost_to_label.setObjectName(_fromUtf8("Cost_to_label"))
        self.Start_timeEdit = QtGui.QTimeEdit(advsearch_dialog)
        self.Start_timeEdit.setGeometry(QtCore.QRect(147, 230, 81, 22))
        self.Start_timeEdit.setObjectName(_fromUtf8("Start_timeEdit"))
        self.End_timeEdit = QtGui.QTimeEdit(advsearch_dialog)
        self.End_timeEdit.setGeometry(QtCore.QRect(260, 230, 81, 22))
        self.End_timeEdit.setObjectName(_fromUtf8("End_timeEdit"))

        self.retranslateUi(advsearch_dialog)
        QtCore.QMetaObject.connectSlotsByName(advsearch_dialog)

    def retranslateUi(self, advsearch_dialog):
        advsearch_dialog.setWindowTitle(_translate("advsearch_dialog", "Advanced Search", None))
        self.ID_cbox.setText(_translate("advsearch_dialog", "ID", None))
        self.Name_cobx.setText(_translate("advsearch_dialog", "Name", None))
        self.Cost_cbox.setText(_translate("advsearch_dialog", "Cost    From", None))
        self.Location_cbox.setText(_translate("advsearch_dialog", "Location", None))
        self.Time_cbox.setText(_translate("advsearch_dialog", "Time    From", None))
        self.Seacch_adv_btn.setText(_translate("advsearch_dialog", "Search", None))
        self.Cancel_adv_btn.setText(_translate("advsearch_dialog", "Cancel", None))
        self.Id_adv_label.setText(_translate("advsearch_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Name_adv_label.setText(_translate("advsearch_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Cost_adv_label.setText(_translate("advsearch_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Location_adv_label.setText(_translate("advsearch_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Required field!</span></p></body></html>", None))
        self.Time_to_label.setText(_translate("advsearch_dialog", "To", None))
        self.ID_Exact_cbox.setText(_translate("advsearch_dialog", "Exact", None))
        self.Name_Exact_cobx.setText(_translate("advsearch_dialog", "Exact", None))
        self.Location_Exact_cbox.setText(_translate("advsearch_dialog", "Exact", None))
        self.Cost_to_label.setText(_translate("advsearch_dialog", "To", None))

