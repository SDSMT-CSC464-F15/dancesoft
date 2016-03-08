import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from fee_rates_dialog import Ui_feeRateDialog

class fee_dialog(QtGui.QDialog):    
    def __init__(self, selected_decription = None):
        QtGui.QDialog.__init__(self)
        self.fee = Ui_feeRateDialog()
        self.fee.setupUi(self)

        self.selected_decription = selected_decription
        self.fill_window()

        if selected_decription == None:
            self.fee.ok_btn.clicked.connect(self.add_rate)
        
        else:
            self.fee.ok_btn.clicked.connect(self.submit_updates)

        self.fee.flatCheckBox.stateChanged.connect(self.change_flat)
        self.fee.percentCheckBox.stateChanged.connect(self.change_percent)
        self.fee.cancel_btn.clicked.connect(self.close)

    def change_flat(self):
        if self.fee.flatCheckBox.isChecked():
            self.fee.percentCheckBox.setChecked(False)
            
    def change_percent(self):
        if self.fee.percentCheckBox.isChecked():
            self.fee.flatCheckBox.setChecked(False)

    def fill_window(self):
        self.query = QSqlQuery()
        self.query.exec_("Select * FROM One_Off_Fees where Fee_Description = '%s'" % (self.selected_decription))
        while self.query.next():
            self.record = self.query.record()
            self.fee.descriptionLineEdit.setText(str(self.record.value(0)))
            self.fee.costDoubleSpinBox.setValue(float(self.record.value(1)))          
                    

    
    def submit_updates(self):
        self.description = self.fee.descriptionLineEdit.text()
        self.newCost = self.fee.costDoubleSpinBox.value()
        print(self.newCost)
        if(self.fee.percentCheckBox.isChecked() == False and
           self.fee.flatCheckBox.isChecked() == False):
            self.check_msg = "Please check flat rate or percent"
            self.check_reply = QtGui.QMessageBox.information(self, 'Error', 
                        self.check_msg, QtGui.QMessageBox.Ok)
        
        
        elif (self.fee.percentCheckBox.isChecked() and self.newCost >= 1):
            self.percent_msg = "Please enter a number less then one. \n Usage Example: 0.15 is 15 percent"
            self.percent_reply = QtGui.QMessageBox.information(self, 'Enter Percent', 
                        self.percent_msg, QtGui.QMessageBox.Ok)
            
        else:
            self.update_query = QSqlQuery()
            self.update_query.exec_("Update One_Off_Fees Set Fee_Description = '%s',\
                        Fee_Cost = %f Where Fee_Description = '%s'" \
                             % (self.description, self.newCost,\
                                self.selected_decription))
            self.close()


    def add_rate(self):
        self.description = self.fee.descriptionLineEdit.text()
        self.newCost = self.fee.costDoubleSpinBox.value()

        if(self.fee.percentCheckBox.isChecked() == False and
           self.fee.flatCheckBox.isChecked() == False):
            self.check_msg = "Please check flat rate or percent"
            self.check_reply = QtGui.QMessageBox.information(self, 'Error', 
                        self.check_msg, QtGui.QMessageBox.Ok)
        
        
        elif (self.fee.percentCheckBox.isChecked() and self.newCost >= 1):
            self.percent_msg = "Please enter a number less then one. \n Usage Example: 0.15 is 15 percent"
            self.percent_reply = QtGui.QMessageBox.information(self, 'Enter Percent', 
                        self.percent_msg, QtGui.QMessageBox.Ok)
            
        else:
            self.add_query = QSqlQuery()
            self.add_query.exec_("Insert into One_Off_Fees (Fee_Description,\
                    Fee_Cost) Values ('%s',%f)" \
                         % (self.description, self.newCost))
            self.close()
            

        
