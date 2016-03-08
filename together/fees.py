import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from fee_rates import Ui_fee_rates
from Update_fees_window import fee_dialog

class fees(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.fee = Ui_fee_rates()
        self.fee.setupUi(self)

        self.conn() #need exeption
        
        self.fee.update_btn.setEnabled(False)
        self.fee.remove_btn.setEnabled(False)
        self.description_query = QSqlQuery()

        self.description_query.exec_("Select Fee_Description from One_Off_Fees ORDER BY Fee_Description")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.description_query)
        self.fee.descriptionListView.setModel(self.model)
        self.fee.descriptionListView.clicked.connect(self.show_information)
        
        self.fee.add_btn.clicked.connect(self.add)
        self.fee.update_btn.clicked.connect(self.update)
        self.fee.remove_btn.clicked.connect(self.remove)
        self.fee.refresh_btn.clicked.connect(self.refresh_list)
        self.fee.cancel_btn.clicked.connect(self.close)
        

    def show_information(self, index):
        self.selected_decription = index.data()
        
        self.show_query = QSqlQuery()
        self.show_query.exec_("Select Fee_Cost from One_Off_Fees\
                              Where Fee_Description = '%s'" % index.data())
        while self.show_query.next():
            record = self.show_query.record()
            self.fee.costDoubleSpinBox.setValue(float(record.value(0)))
        self.fee.update_btn.setEnabled(True)
        self.fee.remove_btn.setEnabled(True)
        
    def add(self):
        self.fee.dialog =  fee_dialog()
        self.fee.dialog.show()

    def update(self):
        self.fee.dialog = fee_dialog(self.selected_decription)
        self.fee.dialog.show()

    def remove(self):
        results_msg = "Are you sure you want to remove '%s'?" % (self.selected_decription)
                
        reply = QtGui.QMessageBox.question(self, 'Message', results_msg,\
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            Remove_query = QSqlQuery()
         
            if Remove_query.exec_("DELETE FROM One_Off_Fees WHERE Fee_Description = '%s'" % (self.selected_decription)):
                QtGui.QMessageBox.information(self, 'Success', 'Removed fee successfully')

    def refresh_list(self):
        self.description_query.exec_("Select Fee_Description from One_Off_Fees")
        self.model = QSqlQueryModel()
        self.model.setQuery(self.description_query)
        self.fee.descriptionListView.setModel(self.model)

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = fees()
window.show()
sys.exit(app.exec_())
