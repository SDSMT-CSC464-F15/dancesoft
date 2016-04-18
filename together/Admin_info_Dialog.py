#display admin information
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Admin_info import Ui_Admin_info_dialog
from PyQt4.QtSql import *
from functools import partial


class Admin_info_dialog(QtGui.QDialog):
    def __init__(self, name):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Admin_info_dialog()
        self.ui.setupUi(self)
        self.ui.Close_detail_btn.clicked.connect(self.close)
        
        detail_query = QSqlQuery()
        detail_query.exec_("select * from Admin where Admin_name = '%s'" % name)
        detail_query.next()
        Admin_id = detail_query.value(0)
        Admin_name = detail_query.value(1)
        Admin_home_phone = detail_query.value(2)
        Admin_cell_phone = detail_query.value(3)
        Admin_work_phone = detail_query.value(4)
        Admin_address = detail_query.value(5)
        Admin_email = detail_query.value(6)
        Admin_sex = detail_query.value(7)
        Admin_ssn = detail_query.value(8)
        Admin_pay_rate = detail_query.value(9)
        Admin_medical = detail_query.value(10)
        Admin_birth = detail_query.value(11)

        
        self.ui.Id_detail_lineEdit.setText(str(Admin_id))
        if not isinstance(Admin_name, QtCore.QPyNullVariant):
            self.ui.Name_detail_lineEdit.setText(Admin_name)
        if not isinstance(Admin_sex, QtCore.QPyNullVariant):
            self.ui.Gender_detail_lineEdit.setText(Admin_sex)
        if not isinstance(Admin_email, QtCore.QPyNullVariant):
            self.ui.Email_detail_lineEdit.setText(Admin_email)
        if not isinstance(Admin_birth, QtCore.QPyNullVariant):
            self.ui.Birth_detail_dateEdit.setDate(Admin_birth)
        if not isinstance(Admin_home_phone, QtCore.QPyNullVariant):
            self.ui.Homephone_detail_lineEdit.setText(Admin_home_phone)
        if not isinstance(Admin_cell_phone, QtCore.QPyNullVariant):
            self.ui.Cellphone_detail_lineEdit.setText(Admin_cell_phone)
        if not isinstance(Admin_work_phone, QtCore.QPyNullVariant):
            self.ui.Workphone_detail_lineEdit.setText(Admin_work_phone)
        if not isinstance(Admin_ssn, QtCore.QPyNullVariant):
            self.ui.SSN_detail_lineEdit.setText(Admin_ssn)
        if not isinstance(Admin_pay_rate, QtCore.QPyNullVariant):
            self.ui.Payrate_detail_lineEdit.setText(str(Admin_pay_rate))
        if not isinstance(Admin_medical, QtCore.QPyNullVariant):
            self.ui.Medical_detail_textEdit.setText(Admin_medical)
        
        detail_query.exec_("select * from Address where Address_id = %d" % int(Admin_address))
        detail_query.next()
        Admin_Street = detail_query.value(1)
        Admin_City = detail_query.value(2)
        Admin_State = detail_query.value(3)
        Admin_Zipcode = detail_query.value(4)

        if not isinstance(Admin_Street, QtCore.QPyNullVariant):
            self.ui.Address_detail_lineEdit.setText(Admin_Street)
        if not isinstance(Admin_City, QtCore.QPyNullVariant):
            self.ui.City_detail_lineEdit.setText(Admin_City)
        if not isinstance(Admin_State, QtCore.QPyNullVariant):
            self.ui.State_detail_lineEdit.setText(Admin_State)
        if not isinstance(Admin_Zipcode, QtCore.QPyNullVariant):
            self.ui.Zipcode_detail_lineEdit.setText(str(Admin_Zipcode))

