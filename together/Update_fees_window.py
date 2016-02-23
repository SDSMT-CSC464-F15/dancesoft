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
        self.update_query = QSqlQuery()
        modify_query = ("Update One_Off_Fees Set Fee_Description = '%s',\
                    Fee_Cost = %d Where Fee_Description = '%s'" \
                         % (self.description, self.newCost,\
                            self.selected_decription))
        self.update_query.exec_(modify_query)
        self.close()


    def add_rate(self):
        self.description = self.fee.descriptionLineEdit.text()
        self.newCost = self.fee.costDoubleSpinBox.value()
        self.add_query = QSqlQuery()

        insert_query = ("Insert into One_Off_Fees (Fee_Description,\
                    Fee_Cost) Values ('%s',%d)" \
                         % (self.description, self.newCost))
        self.add_query.exec_(insert_query)
        self.close()
            

        
