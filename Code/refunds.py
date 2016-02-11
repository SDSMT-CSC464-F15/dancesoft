import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from datetime import datetime

class refund(QtGui.QMainWindow):
    def __init__(self):
        #retrive student id for use in other functions
        self.getStudentId()
        self.issueRefund()
       
    def issueRefund(self,className):
        #get the exact length of the class is days
        classQuery = QSqlQuery()
        classQuery.exec("Select DATEDIFF((Select Class_end_date from Class where \
                         Class_name = '%s'),(Select Class_start_date from Class \
                         where Class_name = '%s'))" % (className, className))
        if(classQuery.next())
            record = classQuery.record()
            # divide by 7 since classes meet once a week
            self.classLength = int(record.value(0))/7

        #get the length the student was actually in the class
        dDateQuery = QSqlQuery()
        dDateQuery.exec("Select DATEDIFF(CURRDATE(),(Select Class_start_date \
                         from Class where Class_name = '%s'))" % (className))
        if(dDateQuery.next())
            record = dDateQuery.record()
            #divide by 7 since classes meets once a week
            self.studentLength = int(record.value(0))//7

        # get the days left in the class when the student dropped
        self.daysLeft = self.classLength - self.studentLength
        #and convert to a percent for refund calculations
        self.percentTimeLeft = self.daysLeft/self.classLength

        # retreive the cost of the dropped class, multiply with percent of
        # time left in class and subtract from total class cost
        totalClassCost = costofClass()
        newCredit = classCost - (classCost * self.percentTimeLeft)

        #Get current credit amount
        currentCreditQuery = QSqlQuery()
        currentCreditQuery.exec_("Select Credit_amount from Credits where Student_id = %d" % self.studentId)
        if(currentCreditQuery.next()):
            record = currentCreditQuery.record()
            currentCredit = float(record.value(0))

        # add new credit to current credit and send new credit to database
        newCredit = currentCredit + newCredit

        currentCreditQuery.exec_("Update Credits set Credit_amount = %d where Student_id = %d" %(newCredit, self.studentId))

    def costofClass(self):
        '''
        still need if student had discount
        '''
        discountPercent = 10

        # get the cost of the dropped class
        costQuery = QSqlQuery()
        costQuery.exec_("Select Class_cost from Class where Class_name = '%s'" %(clssName))
        if(costQuery.next()):
            record = costQuery.record()
            classCost = float(record.value(0))
        #if the student had a registation discount take away the discounted amount
        classCost = classCost - (classCost * (discountPercent/100))
        
        return classCost
            
        
                
    def getStudentId(self,index):
        studentQuery = QSqlQuery();
        studentQuery.exec_("Select Student_id from Student where Student_name = '%s'" % index.data())
        if(studentQuery.next()):
            record = studentQuery.record()
            self.studentId = int(record.value(0)

   

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

app = QtGui.QApplication(sys.argv)
window = refund()
window.show()
sys.exit(app.exec_())
