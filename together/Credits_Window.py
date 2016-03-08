import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from Credits import Ui_Credits

class discounts(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.credit = Ui_Credits()
        self.credit.setupUi(self)

        self.conn() 

        #query to fill student list
        self.student_query = QSqlQuery()
        self.student_query.exec_("Select Student_name from Student")

        #set up sql model to display results of the query to the list view widget
        self.model = QSqlQueryModel()
        self.model.setQuery(self.student_query)
        self.credit.studentListView.setModel(self.model)

        # if the list view is clicked populate page with student information
        self.credit.studentListView.clicked.connect(self.showStudentInformation)

        # run insert new credit when apply button is clicked
        self.credit.apply_btn.clicked.connect(self.applyDiscount)
        
        
    
    def applyDiscount(self,index):
        #retrive the credit value in the interface fields
        self.newCredit = self.credit.creditDoubleSpinBox.value()

        # check to see if the selected student already has a credit in the database
        self.findStudentQuery = QSqlQuery()
        self.findStudentQuery.exec_("Select Student_id from Credits where\
                            Student_id = (Select Student_id from Student \
                            where Student_name = '%s')" % self.selectedStudent)
        
        # if they do update the credits
        if self.findStudentQuery.next():
            record = self.findStudentQuery.record()
            self.update_query = QSqlQuery()
            self.update_query.exec_("Update Credits set Credit_amount = %f \
                               where Student_id = (Select Student_id from Student \
                               where Student_name = '%s')" % (self.newCredit,\
                                self.selectedStudent))
        # if not add the student to the credits table
        else:
            #Generate a new credit id va;ue
            self.id_query =QSqlQuery()
            self.id_query.exec_("SELECT Credit_id FROM Credits ORDER BY Credit_id DESC LIMIT 1")
            if self.id_query.next():
                self.record = self.id_query.record()
                self.creditId = int(self.record.value(0))
                self.creditId += 1

            # Get the selected students information
            self.id_query.exec_("Select Student_id from Student where Student_name = '%s'" % self.selectedStudent)
            if self.id_query.next():
                self.record = self.id_query.record()
                self.studentId = int(self.record.value(0))

            # Apply the credit to the students account
            self.apply_query = QSqlQuery()
            self.apply_query.exec_("Insert into Credits (Credit_id, Student_id,\
                                Credit_amount) values(%d,%d,%f)" % (self.creditId,\
                                self.studentId, self.newCredit))

    
    def showStudentInformation(self,index):
        #Get selectd student when the user clicks the list view
        self.selectedStudent = index.data()
        
        # if the selected student already has a credit or a discount retrive the information 
        self.show_query = QSqlQuery()
        self.show_query.exec_("Select Credit_amount from Credits Where Student_id = \
                               (Select Student_id from Student where \
                               Student_name = '%s')" % self.selectedStudent)

        # take the results of the query and set the interface field to the returned results
        # if query returns result get the value, Else set box to zero
        if self.show_query.next():
            self.record = self.show_query.record()
            self.credit.creditDoubleSpinBox.setValue(float(self.record.value(0)))
        else:
            self.credit.creditDoubleSpinBox.setValue(0.00)
            
                  
    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = discounts()
window.show()
sys.exit(app.exec_())
