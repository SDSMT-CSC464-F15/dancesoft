import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from tuition_rates_dialog import Ui_tuitionRateDialog

class rates_dialog(QtGui.QDialog):    
    def __init__(self, selected_decription = None):
        QtGui.QDialog.__init__(self)
        self.rates = Ui_tuitionRateDialog()
        self.rates.setupUi(self)

        self.selected_decription = selected_decription
        self.fill_window()

        self.rates.minuteCheckBox.stateChanged.connect(self.change_min_checkbox)
        
        self.rates.hoursCheckBox.stateChanged.connect(self.change_hour_checkbox)

        if selected_decription == None:
            self.rates.ok_btn.clicked.connect(self.add_rate)
        
        else:
            self.rates.ok_btn.clicked.connect(self.submit_updates)


    def fill_window(self):
        self.query = QSqlQuery()
        self.query.exec_("Select * FROM Tuition_Rates where Tuition_Description = '%s'" % (self.selected_decription))
        while self.query.next():
            self.record = self.query.record()
            self.rates.descriptionLineEdit.setText(str(self.record.value(0)))
            self.rates.costDoubleSpinBox.setValue(float(self.record.value(1)))
            self.rates.timeFrameSpinBox.setValue(int(self.record.value(2)))

    def change_min_checkbox(self):
        if self.rates.minuteCheckBox.isChecked():
            print("min")
            self.rates.hoursCheckBox.setChecked(False)
            
    def change_hour_checkbox(self):
        if self.rates.hoursCheckBox.isChecked():
            print("hour")
            self.rates.minuteCheckBox.setChecked(False)           
                    

    
    def submit_updates(self):
        self.description = self.rates.descriptionLineEdit.text()
        self.time = self.rates.timeFrameSpinBox.value()
        self.newCost = self.rates.costDoubleSpinBox.value()
        self.update_query = QSqlQuery()

        if self.rates.minuteCheckBox.isChecked():
            min_query = ("Update Tuition_Rates Set Tuition_Description = '%s',\
                    Tuition_Rate = %d, Tuition_Time = %d Where \
                    Tuition_Description = '%s'" % (self.description, self.newCost,\
                                                   self.time, self.selected_decription))
            self.update_query.exec_(min_query)
            self.close()
            

        elif self.rates.hoursCheckBox.isChecked():
            self.time = self.time * 60
            hour_query = ("Update Tuition_Rates Set Tuition_Description = '%s',\
                    Tuition_Rate = %d, Tuition_Time = %d Where \
                    Tuition_Description = '%s'" % (self.description, self.newCost,\
                                                   self.time, self.selected_decription))
            self.update_query.exec_(hour_query)
            self.close()

        else:
            reply = QtGui.QMessageBox.warning(self, 'Message', "Please check one of the time checkboxs")
            

    def add_rate(self):
        self.description = self.rates.descriptionLineEdit.text()
        self.newCost = self.rates.costDoubleSpinBox.value()
        self.time = self.rates.timeFrameSpinBox.value()
        self.add_query = QSqlQuery()

        if self.rates.minuteCheckBox.isChecked():
            min_query = ("Insert into Tuition_Rates (Tuition_Description,\
                    Tuition_Rate, Tuition_Time) Values ('%s',%d,%d)" \
                         % (self.description, self.newCost, self.time))
            self.add_query.exec_(min_query)
            self.close()
            

        elif self.rates.hoursCheckBox.isChecked():
            self.time = self.time * 60
            hour_query = ("Insert into Tuition_Rates (Tuition_Description,\
                           Tuition_Rate, Tuition_Time) Values ('%s',%d,%d)" \
                          % (self.description, self.newCost, self.time))
            self.add_query.exec_(hour_query)
            self.close()

        else:
            reply = QtGui.QMessageBox.warning(self, 'Message', "Please check one of the time checkboxs")


        
