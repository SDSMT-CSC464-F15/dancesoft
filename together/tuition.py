import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from tuition_rates import Ui_tuition_rates
from Update_rates_window import rates_dialog

class tuition(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.tuit = Ui_tuition_rates()
        self.tuit.setupUi(self)

        self.conn() #need exeption
        
        self.tuit.update_btn.setEnabled(False)
        self.tuit.remove_btn.setEnabled(False)
        self.description_query = QSqlQuery()

        self.description_query.exec_("Select Tuition_Description from Tuition_Rates ORDER BY Tuition_Description")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.description_query)
        self.tuit.descriptionListView.setModel(self.model)
        self.tuit.descriptionListView.clicked.connect(self.show_information)

        self.tuit.minuteCheckBox.stateChanged.connect(self.change_min_checkbox)

        self.tuit.hoursCheckBox.stateChanged.connect(self.change_hour_checkbox)
        
        self.tuit.add_btn.clicked.connect(self.add)
        self.tuit.update_btn.clicked.connect(self.update)
        self.tuit.remove_btn.clicked.connect(self.remove)
        self.tuit.refresh_btn.clicked.connect(self.refresh_list)
        self.tuit.cancel_btn.clicked.connect(self.close)
        
        

    def show_information(self, index):
        self.selected_decription = index.data()
        
        self.show_query = QSqlQuery()
        self.show_query.exec_("Select Tuition_Rate, Tuition_Time from Tuition_Rates\
                              Where Tuition_Description = '%s'" % index.data())
        while self.show_query.next():
            record = self.show_query.record()
            self.tuit.costDoubleSpinBox.setValue(float(record.value(0)))
            self.tuit.timeFrameSpinBox.setValue(int(record.value(1)))
            self.tuit.minuteCheckBox.setChecked(True)
        self.tuit.update_btn.setEnabled(True)
        self.tuit.remove_btn.setEnabled(True)

    def change_min_checkbox(self):
        if self.tuit.minuteCheckBox.isChecked():
            self.tuit.hoursCheckBox.setChecked(False)
            
    def change_hour_checkbox(self):
        if self.tuit.hoursCheckBox.isChecked():
            self.tuit.minuteCheckBox.setChecked(False)
        
        

    def add(self):
        self.tuit.dialog =  rates_dialog()
        self.tuit.dialog.show()

    def update(self):
        self.tuit.dialog = rates_dialog(self.selected_decription)
        self.tuit.dialog.show()

    def remove(self):
        results_msg = "Are you sure you want to remove '%s'?" % (self.selected_decription)
                
        reply = QtGui.QMessageBox.question(self, 'Message', results_msg,\
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            Remove_query = QSqlQuery()
         
            if Remove_query.exec_("DELETE FROM Tuition_Rates WHERE Tuition_Description = '%s'" % (self.selected_decription)):
                QtGui.QMessageBox.information(self, 'Success', 'Remove tuition rate successfully')

    def refresh_list(self):
        self.description_query.exec_("Select Tuition_Description from Tuition_Rates")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.description_query)
        self.tuit.descriptionListView.setModel(self.model)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = tuition()
window.show()
sys.exit(app.exec_())
