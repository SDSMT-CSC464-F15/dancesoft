# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin Landing.ui'
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

class Ui_Admin_Landing(object):
    def setupUi(self, Admin_Landing):
        Admin_Landing.setObjectName(_fromUtf8("Admin_Landing"))
        Admin_Landing.resize(619, 379)
        self.centralwidget = QtGui.QWidget(Admin_Landing)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 551, 321))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.Landing = QtGui.QWidget()
        self.Landing.setObjectName(_fromUtf8("Landing"))
        self.verticalLayoutWidget = QtGui.QWidget(self.Landing)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Employee_btn = QtGui.QPushButton(self.groupBox)
        self.Employee_btn.setGeometry(QtCore.QRect(60, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Employee_btn.setFont(font)
        self.Employee_btn.setObjectName(_fromUtf8("Employee_btn"))
        self.Quit_btn = QtGui.QPushButton(self.groupBox)
        self.Quit_btn.setGeometry(QtCore.QRect(410, 270, 75, 23))
        self.Quit_btn.setObjectName(_fromUtf8("Quit_btn"))
        self.Logout_btn = QtGui.QPushButton(self.groupBox)
        self.Logout_btn.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.Logout_btn.setObjectName(_fromUtf8("Logout_btn"))
        self.Billing_btn = QtGui.QPushButton(self.groupBox)
        self.Billing_btn.setGeometry(QtCore.QRect(60, 210, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Billing_btn.setFont(font)
        self.Billing_btn.setObjectName(_fromUtf8("Billing_btn"))
        self.Student_btn = QtGui.QPushButton(self.groupBox)
        self.Student_btn.setGeometry(QtCore.QRect(60, 150, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Student_btn.setFont(font)
        self.Student_btn.setObjectName(_fromUtf8("Student_btn"))
        self.Class_btn = QtGui.QPushButton(self.groupBox)
        self.Class_btn.setGeometry(QtCore.QRect(60, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.Class_btn.setFont(font)
        self.Class_btn.setObjectName(_fromUtf8("Class_btn"))
        self.verticalLayout.addWidget(self.groupBox)
        self.stackedWidget.addWidget(self.Landing)
        self.Admin_employee = QtGui.QWidget()
        self.Admin_employee.setObjectName(_fromUtf8("Admin_employee"))
        self.Employee_back_btn = QtGui.QPushButton(self.Admin_employee)
        self.Employee_back_btn.setGeometry(QtCore.QRect(350, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Employee_back_btn.setFont(font)
        self.Employee_back_btn.setObjectName(_fromUtf8("Employee_back_btn"))
        self.New_teacher_btn = QtGui.QPushButton(self.Admin_employee)
        self.New_teacher_btn.setGeometry(QtCore.QRect(110, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.New_teacher_btn.setFont(font)
        self.New_teacher_btn.setObjectName(_fromUtf8("New_teacher_btn"))
        self.Search_teacher_btn = QtGui.QPushButton(self.Admin_employee)
        self.Search_teacher_btn.setGeometry(QtCore.QRect(110, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Search_teacher_btn.setFont(font)
        self.Search_teacher_btn.setObjectName(_fromUtf8("Search_teacher_btn"))
        self.Update_teacher_btn = QtGui.QPushButton(self.Admin_employee)
        self.Update_teacher_btn.setGeometry(QtCore.QRect(110, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Update_teacher_btn.setFont(font)
        self.Update_teacher_btn.setObjectName(_fromUtf8("Update_teacher_btn"))
        self.Assign_teacher_btn = QtGui.QPushButton(self.Admin_employee)
        self.Assign_teacher_btn.setGeometry(QtCore.QRect(110, 150, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Assign_teacher_btn.setFont(font)
        self.Assign_teacher_btn.setObjectName(_fromUtf8("Assign_teacher_btn"))
        self.Quit_btn_2 = QtGui.QPushButton(self.Admin_employee)
        self.Quit_btn_2.setGeometry(QtCore.QRect(430, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Quit_btn_2.setFont(font)
        self.Quit_btn_2.setObjectName(_fromUtf8("Quit_btn_2"))
        self.stackedWidget.addWidget(self.Admin_employee)
        self.Admin_class = QtGui.QWidget()
        self.Admin_class.setObjectName(_fromUtf8("Admin_class"))
        self.Class_tuition_btn = QtGui.QPushButton(self.Admin_class)
        self.Class_tuition_btn.setGeometry(QtCore.QRect(120, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Class_tuition_btn.setFont(font)
        self.Class_tuition_btn.setObjectName(_fromUtf8("Class_tuition_btn"))
        self.View_class_btn = QtGui.QPushButton(self.Admin_class)
        self.View_class_btn.setGeometry(QtCore.QRect(120, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.View_class_btn.setFont(font)
        self.View_class_btn.setObjectName(_fromUtf8("View_class_btn"))
        self.Add_Class_btn = QtGui.QPushButton(self.Admin_class)
        self.Add_Class_btn.setGeometry(QtCore.QRect(120, 150, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Add_Class_btn.setFont(font)
        self.Add_Class_btn.setObjectName(_fromUtf8("Add_Class_btn"))
        self.Quit_btn_3 = QtGui.QPushButton(self.Admin_class)
        self.Quit_btn_3.setGeometry(QtCore.QRect(440, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Quit_btn_3.setFont(font)
        self.Quit_btn_3.setObjectName(_fromUtf8("Quit_btn_3"))
        self.Class_back_btn = QtGui.QPushButton(self.Admin_class)
        self.Class_back_btn.setGeometry(QtCore.QRect(360, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Class_back_btn.setFont(font)
        self.Class_back_btn.setObjectName(_fromUtf8("Class_back_btn"))
        self.Modify_class_btn = QtGui.QPushButton(self.Admin_class)
        self.Modify_class_btn.setGeometry(QtCore.QRect(120, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Modify_class_btn.setFont(font)
        self.Modify_class_btn.setObjectName(_fromUtf8("Modify_class_btn"))
        self.stackedWidget.addWidget(self.Admin_class)
        self.Admin_Student = QtGui.QWidget()
        self.Admin_Student.setObjectName(_fromUtf8("Admin_Student"))
        self.Registration_btn = QtGui.QPushButton(self.Admin_Student)
        self.Registration_btn.setGeometry(QtCore.QRect(150, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Registration_btn.setFont(font)
        self.Registration_btn.setObjectName(_fromUtf8("Registration_btn"))
        self.Search_student_btn = QtGui.QPushButton(self.Admin_Student)
        self.Search_student_btn.setGeometry(QtCore.QRect(150, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Search_student_btn.setFont(font)
        self.Search_student_btn.setObjectName(_fromUtf8("Search_student_btn"))
        self.Add_student_btn = QtGui.QPushButton(self.Admin_Student)
        self.Add_student_btn.setGeometry(QtCore.QRect(150, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Add_student_btn.setFont(font)
        self.Add_student_btn.setObjectName(_fromUtf8("Add_student_btn"))
        self.Quit_btn_4 = QtGui.QPushButton(self.Admin_Student)
        self.Quit_btn_4.setGeometry(QtCore.QRect(430, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Quit_btn_4.setFont(font)
        self.Quit_btn_4.setObjectName(_fromUtf8("Quit_btn_4"))
        self.Student_back_btn = QtGui.QPushButton(self.Admin_Student)
        self.Student_back_btn.setGeometry(QtCore.QRect(350, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Student_back_btn.setFont(font)
        self.Student_back_btn.setObjectName(_fromUtf8("Student_back_btn"))
        self.stackedWidget.addWidget(self.Admin_Student)
        self.Admin_Payroll = QtGui.QWidget()
        self.Admin_Payroll.setObjectName(_fromUtf8("Admin_Payroll"))
        self.Family_billing_btn = QtGui.QPushButton(self.Admin_Payroll)
        self.Family_billing_btn.setGeometry(QtCore.QRect(120, 150, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Family_billing_btn.setFont(font)
        self.Family_billing_btn.setObjectName(_fromUtf8("Family_billing_btn"))
        self.Quit_btn_5 = QtGui.QPushButton(self.Admin_Payroll)
        self.Quit_btn_5.setGeometry(QtCore.QRect(440, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Quit_btn_5.setFont(font)
        self.Quit_btn_5.setObjectName(_fromUtf8("Quit_btn_5"))
        self.Hours_btn = QtGui.QPushButton(self.Admin_Payroll)
        self.Hours_btn.setGeometry(QtCore.QRect(120, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Hours_btn.setFont(font)
        self.Hours_btn.setObjectName(_fromUtf8("Hours_btn"))
        self.Payroll_back_btn = QtGui.QPushButton(self.Admin_Payroll)
        self.Payroll_back_btn.setGeometry(QtCore.QRect(360, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.Payroll_back_btn.setFont(font)
        self.Payroll_back_btn.setObjectName(_fromUtf8("Payroll_back_btn"))
        self.Payroll_btn = QtGui.QPushButton(self.Admin_Payroll)
        self.Payroll_btn.setGeometry(QtCore.QRect(120, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.Payroll_btn.setFont(font)
        self.Payroll_btn.setObjectName(_fromUtf8("Payroll_btn"))
        self.stackedWidget.addWidget(self.Admin_Payroll)
        Admin_Landing.setCentralWidget(self.centralwidget)
        self.Admin_menubar = QtGui.QMenuBar(Admin_Landing)
        self.Admin_menubar.setGeometry(QtCore.QRect(0, 0, 619, 21))
        self.Admin_menubar.setObjectName(_fromUtf8("Admin_menubar"))
        self.menuNavigation = QtGui.QMenu(self.Admin_menubar)
        self.menuNavigation.setObjectName(_fromUtf8("menuNavigation"))
        Admin_Landing.setMenuBar(self.Admin_menubar)
        self.Admin_statusbar = QtGui.QStatusBar(Admin_Landing)
        self.Admin_statusbar.setObjectName(_fromUtf8("Admin_statusbar"))
        Admin_Landing.setStatusBar(self.Admin_statusbar)
        self.actionBacon = QtGui.QAction(Admin_Landing)
        self.actionBacon.setObjectName(_fromUtf8("actionBacon"))
        self.actionDouble = QtGui.QAction(Admin_Landing)
        self.actionDouble.setObjectName(_fromUtf8("actionDouble"))
        self.actionVeggie = QtGui.QAction(Admin_Landing)
        self.actionVeggie.setObjectName(_fromUtf8("actionVeggie"))
        self.actionTofu = QtGui.QAction(Admin_Landing)
        self.actionTofu.setObjectName(_fromUtf8("actionTofu"))
        self.Admin_menubar.addAction(self.menuNavigation.menuAction())

        self.retranslateUi(Admin_Landing)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Admin_Landing)

    def retranslateUi(self, Admin_Landing):
        Admin_Landing.setWindowTitle(_translate("Admin_Landing", "Admin Landing", None))
        self.groupBox.setTitle(_translate("Admin_Landing", "Admin", None))
        self.Employee_btn.setText(_translate("Admin_Landing", "Manage Employees", None))
        self.Quit_btn.setText(_translate("Admin_Landing", "Quit", None))
        self.Logout_btn.setText(_translate("Admin_Landing", "Logout", None))
        self.Billing_btn.setText(_translate("Admin_Landing", "Manage Billing and Payroll", None))
        self.Student_btn.setText(_translate("Admin_Landing", "Manage Students", None))
        self.Class_btn.setText(_translate("Admin_Landing", "Manage Classes", None))
        self.Employee_back_btn.setText(_translate("Admin_Landing", "Back", None))
        self.New_teacher_btn.setText(_translate("Admin_Landing", "Enter New Teacher", None))
        self.Search_teacher_btn.setText(_translate("Admin_Landing", "Search For Teacher", None))
        self.Update_teacher_btn.setText(_translate("Admin_Landing", "Update Teacher Information", None))
        self.Assign_teacher_btn.setText(_translate("Admin_Landing", "Assign Teacher to Class", None))
        self.Quit_btn_2.setText(_translate("Admin_Landing", "Quit", None))
        self.Class_tuition_btn.setText(_translate("Admin_Landing", "Class Tuition", None))
        self.View_class_btn.setText(_translate("Admin_Landing", "View Classes", None))
        self.Add_Class_btn.setText(_translate("Admin_Landing", "Add a Class", None))
        self.Quit_btn_3.setText(_translate("Admin_Landing", "Quit", None))
        self.Class_back_btn.setText(_translate("Admin_Landing", "Back", None))
        self.Modify_class_btn.setText(_translate("Admin_Landing", "Modify a Class", None))
        self.Registration_btn.setText(_translate("Admin_Landing", "Registration", None))
        self.Search_student_btn.setText(_translate("Admin_Landing", "Search For Students", None))
        self.Add_student_btn.setText(_translate("Admin_Landing", "Add/Remove Student", None))
        self.Quit_btn_4.setText(_translate("Admin_Landing", "Quit", None))
        self.Student_back_btn.setText(_translate("Admin_Landing", "Back", None))
        self.Family_billing_btn.setText(_translate("Admin_Landing", "Family Billing", None))
        self.Quit_btn_5.setText(_translate("Admin_Landing", "Quit", None))
        self.Hours_btn.setText(_translate("Admin_Landing", "See Teacher Hours", None))
        self.Payroll_back_btn.setText(_translate("Admin_Landing", "Back", None))
        self.Payroll_btn.setText(_translate("Admin_Landing", "Payroll", None))
        self.menuNavigation.setTitle(_translate("Admin_Landing", "Navigation", None))
        self.actionBacon.setText(_translate("Admin_Landing", "Bacon", None))
        self.actionDouble.setText(_translate("Admin_Landing", "Double", None))
        self.actionVeggie.setText(_translate("Admin_Landing", "Veggie", None))
        self.actionTofu.setText(_translate("Admin_Landing", "Tofu", None))
