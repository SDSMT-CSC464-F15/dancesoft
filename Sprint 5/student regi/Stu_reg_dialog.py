import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Stu_reg import Ui_Stu_reg_dialog
from PyQt4.QtSql import *
from functools import partial


class Stu_reg_dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Stu_reg_dialog()
        self.ui.setupUi(self)
        self.ui.Update_detail_btn.clicked.connect(self.update)
        self.ui.Id_detail_lineEdit.setEnabled(False)



        
    def update(self):
        self.StuID = self.ui.Id_detail_lineEdit.text()
        self.StuName = self.ui.Name_detail_lineEdit.text()      
        self.StuGender = self.ui.Gender_detail_lineEdit.text()   
        self.StuEmail = self.ui.Email_detail_lineEdit.text()
        self.StuBirth = self.ui.Birth_detail_dateEdit.date()  
        self.StuPhone = self.ui.Phone_detail_lineEdit.text()
        self.StuPG = self.ui.Pguradian_detail_lineEdit.text()  
        self.StuSG = self.ui.Sguardian_detail_lineEdit.text()
        self.StuEcon = self.ui.Econtact_detail_lineEdit.text()
        self.StuEphone = self.ui.Ephone_detail_lineEdit.text()
        self.StuTuition = self.ui.Tuition_detail_lineEdit.text()
        self.StuAddress = self.ui.Address_detail_lineEdit.text()
        self.StuCity = self.ui.City_detail_lineEdit.text()    
        self.StuState = self.ui.State_detail_lineEdit.text()
        self.StuMedical = self.ui.Medical_detail_textEdit.toPlainText()



        update_query = QSqlQuery()
        
        if update_query.exec_("Update Student, Address, Guardian Set Student.Student_name = '%s', Student.Student_sex = '%s', Student.Student_email = '%s', \
                           Student.Student_date_of_birth = '%s', Student.Student_home_phone = '%s', Student.Student_Emergency_contact = '%s', Student.Emergency_contact_phone = '%s', \
                           Student.Student_medical_information = '%s', Student.Tuition = '%s', \
                           Address.Street = '%s', Address.City = '%s', Address.State = '%s', Guardian.Guardian_name = '%s'\
                           Where Student.Student_id = '%d' and Student.Student_address = Address.Address_id and Student.Guardian_primary = Guardian.Guardian_id"\
                           %(self.StuName,  self.StuGender, self.StuEmail, self.StuBirth.toString("yyyy-MM-dd"), self.StuPhone,  self.StuEcon, self.StuEphone,\
                           self.StuMedical, self.StuTuition, self.StuAddress, self.StuCity, self.StuState, self.StuPG, int(self.StuID)))\
            and update_query.exec_("Update Student, Guardian Set Guardian.Guardian_name = '%s '\
                                    Where Student.Student_id = '%d' and Student.Guardian_secondary = Guardian.Guardian_id" \
                                   %(self.StuSG, int(self.StuID))):
            QtGui.QMessageBox.information(
                self, 'Success', 'Update record successfully')
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Update record unsuccessfully')
        
    


app = QtGui.QApplication(sys.argv)
window = Stu_reg_dialog()
window.show()
sys.exit(app.exec_())
