# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Class.ui'
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

class Ui_Add_Class(object):
    def setupUi(self, Add_Class):
        Add_Class.setObjectName(_fromUtf8("Add_Class"))
        Add_Class.resize(786, 571)
        self.centralwidget = QtGui.QWidget(Add_Class)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Name_label = QtGui.QLabel(self.formLayoutWidget)
        self.Name_label.setObjectName(_fromUtf8("Name_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Name_label)
        self.Name_lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.Name_lineEdit.setObjectName(_fromUtf8("Name_lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Name_lineEdit)
        self.Cost_label = QtGui.QLabel(self.formLayoutWidget)
        self.Cost_label.setObjectName(_fromUtf8("Cost_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Cost_label)
        self.Cost_spinBox = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.Cost_spinBox.setObjectName(_fromUtf8("Cost_spinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Cost_spinBox)
        self.Time_label = QtGui.QLabel(self.formLayoutWidget)
        self.Time_label.setObjectName(_fromUtf8("Time_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.Time_label)
        self.Time_timeEdit = QtGui.QTimeEdit(self.formLayoutWidget)
        self.Time_timeEdit.setObjectName(_fromUtf8("Time_timeEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.Time_timeEdit)
        self.Day = QtGui.QLabel(self.formLayoutWidget)
        self.Day.setObjectName(_fromUtf8("Day"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.Day)
        self.Day_comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.Day_comboBox.setObjectName(_fromUtf8("Day_comboBox"))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.Day_comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.Day_comboBox)
        self.Location_label = QtGui.QLabel(self.formLayoutWidget)
        self.Location_label.setObjectName(_fromUtf8("Location_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.Location_label)
        self.Cap = QtGui.QLabel(self.formLayoutWidget)
        self.Cap.setObjectName(_fromUtf8("Cap"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.Cap)
        self.Cap_spinBox = QtGui.QSpinBox(self.formLayoutWidget)
        self.Cap_spinBox.setObjectName(_fromUtf8("Cap_spinBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.Cap_spinBox)
        self.Clothing_label = QtGui.QLabel(self.formLayoutWidget)
        self.Clothing_label.setObjectName(_fromUtf8("Clothing_label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.Clothing_label)
        self.Clothing_textEdit = QtGui.QTextEdit(self.formLayoutWidget)
        self.Clothing_textEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.Clothing_textEdit.setMaximumSize(QtCore.QSize(693, 100))
        self.Clothing_textEdit.setObjectName(_fromUtf8("Clothing_textEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.Clothing_textEdit)
        self.Description = QtGui.QLabel(self.formLayoutWidget)
        self.Description.setObjectName(_fromUtf8("Description"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.Description)
        self.Description_textEdit = QtGui.QTextEdit(self.formLayoutWidget)
        self.Description_textEdit.setMaximumSize(QtCore.QSize(680, 100))
        self.Description_textEdit.setObjectName(_fromUtf8("Description_textEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.Description_textEdit)
        self.Start_date_label = QtGui.QLabel(self.formLayoutWidget)
        self.Start_date_label.setObjectName(_fromUtf8("Start_date_label"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.Start_date_label)
        self.Start_date_dateEdit = QtGui.QDateEdit(self.formLayoutWidget)
        self.Start_date_dateEdit.setObjectName(_fromUtf8("Start_date_dateEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.Start_date_dateEdit)
        self.End_date = QtGui.QLabel(self.formLayoutWidget)
        self.End_date.setObjectName(_fromUtf8("End_date"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.End_date)
        self.End_date_dateEdit = QtGui.QDateEdit(self.formLayoutWidget)
        self.End_date_dateEdit.setObjectName(_fromUtf8("End_date_dateEdit"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.End_date_dateEdit)
        self.Age = QtGui.QLabel(self.formLayoutWidget)
        self.Age.setObjectName(_fromUtf8("Age"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.Age)
        self.Age_spinBox = QtGui.QSpinBox(self.formLayoutWidget)
        self.Age_spinBox.setObjectName(_fromUtf8("Age_spinBox"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.Age_spinBox)
        self.Age_limit = QtGui.QLabel(self.formLayoutWidget)
        self.Age_limit.setObjectName(_fromUtf8("Age_limit"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.Age_limit)
        self.Age_limit_spinBox = QtGui.QSpinBox(self.formLayoutWidget)
        self.Age_limit_spinBox.setObjectName(_fromUtf8("Age_limit_spinBox"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.Age_limit_spinBox)
        self.Location_comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.Location_comboBox.setObjectName(_fromUtf8("Location_comboBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.Location_comboBox)
        self.Submit_btn = QtGui.QPushButton(self.centralwidget)
        self.Submit_btn.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.Submit_btn.setObjectName(_fromUtf8("Submit_btn"))
        self.Back_btn = QtGui.QPushButton(self.centralwidget)
        self.Back_btn.setGeometry(QtCore.QRect(670, 490, 75, 21))
        self.Back_btn.setObjectName(_fromUtf8("Back_btn"))
        Add_Class.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Add_Class)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Add_Class.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Add_Class)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Add_Class.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Class)
        QtCore.QMetaObject.connectSlotsByName(Add_Class)

    def retranslateUi(self, Add_Class):
        Add_Class.setWindowTitle(_translate("Add_Class", "MainWindow", None))
        self.Name_label.setText(_translate("Add_Class", "Name", None))
        self.Cost_label.setText(_translate("Add_Class", "Cost", None))
        self.Time_label.setText(_translate("Add_Class", "Time", None))
        self.Day.setText(_translate("Add_Class", "Day", None))
        self.Day_comboBox.setItemText(0, _translate("Add_Class", "Sunday", None))
        self.Day_comboBox.setItemText(1, _translate("Add_Class", "Monday", None))
        self.Day_comboBox.setItemText(2, _translate("Add_Class", "Tuesday", None))
        self.Day_comboBox.setItemText(3, _translate("Add_Class", "Wednesday", None))
        self.Day_comboBox.setItemText(4, _translate("Add_Class", "Thursday", None))
        self.Day_comboBox.setItemText(5, _translate("Add_Class", "Friday", None))
        self.Day_comboBox.setItemText(6, _translate("Add_Class", "Saturday", None))
        self.Location_label.setText(_translate("Add_Class", "Location", None))
        self.Cap.setText(_translate("Add_Class", "Cap", None))
        self.Clothing_label.setText(_translate("Add_Class", "Clothing", None))
        self.Description.setText(_translate("Add_Class", "Description", None))
        self.Start_date_label.setText(_translate("Add_Class", "Start Date", None))
        self.End_date.setText(_translate("Add_Class", "End Date", None))
        self.Age.setText(_translate("Add_Class", "Age", None))
        self.Age_limit.setText(_translate("Add_Class", "Age Limit", None))
        self.Submit_btn.setText(_translate("Add_Class", "Submit", None))
        self.Back_btn.setText(_translate("Add_Class", "Back", None))

