import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from datetime import datetime

class refund(QtGui.QMainWindow):
    def __init__(self, className, studentName):
        QtGui.QMainWindow.__init__(self)
        #retrive student id for use in other functions
        self.getStudentId(studentName)

        self.issueRefund(className)
        
       
    def issueRefund(self,className):
        #get the exact length of the class is days
        classQuery = QSqlQuery()
        classQuery.exec("Select DATEDIFF((Select Class_end_date from Class where \
                         Class_name = '%s'),(Select Class_start_date from Class \
                         where Class_name = '%s')) AS DiffDate" % (className, className))
        if(classQuery.next()):
            record = classQuery.record()
            # divide by 7 since classes meet once a week
            self.classLength = int(record.value(0))/7

        #get the length the student was actually in the class
        dDateQuery = QSqlQuery()
        dDateQuery.exec("Select DATEDIFF(CURDATE(),(Select Class_start_date \
                         from Class where Class_name = '%s')) AS DiffDate" % (className))
        if(dDateQuery.next()):
            record = dDateQuery.record()
            #divide by 7 since classes meets once a week
            self.studentLength = int(record.value(0))//7

        # get the days left in the class when the student dropped
        self.daysLeft = self.classLength - self.studentLength
        #and convert to a percent for refund calculations
        self.percentTimeLeft = self.daysLeft/self.classLength

        # retreive the cost of the dropped class, multiply with percent of
        # time left in class and subtract from total class cost
        totalClassCost = self.costofClass(className)
        newCredit = totalClassCost - (totalClassCost * self.percentTimeLeft)
        print(totalClassCost, ' ', (totalClassCost * self.percentTimeLeft), ' ', self.percentTimeLeft)

        #Get current credit amount
        currentCreditQuery = QSqlQuery()
        currentCreditQuery.exec_("Select Credit_amount from Credits where Student_id = %d" % self.studentId)
        if(currentCreditQuery.next()):
            record = currentCreditQuery.record()
            currentCredit = float(record.value(0))

        # add new credit to current credit and send new credit to database
        self.results_msg = "Issue a credit of %f for remainder of class?" % (newCredit)
        self.reply = QtGui.QMessageBox.question(self, 'Confirm Refund',
                                           self.results_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if (self.reply == QtGui.QMessageBox.Yes):
            newCredit = currentCredit + newCredit
            currentCreditQuery.exec_("Update Credits set Credit_amount = %f where Student_id = %d" %(newCredit, self.studentId))
        if (self.reply == QtGui.QMessageBox.No):
            msg = "Student removed without refund"
            msgBox = QtGui.QMessageBox.information(self, 'Dropped', 
                    msg)

    def costofClass(self, className):
        annual = 0
        early = 0
        discount = 0.00
        
        costQuery = QSqlQuery()
        costQuery.exec_("Select Is_annual, Is_early from Discount where Student_id = %d"\
                        %(self.studentId))
        if(costQuery.next()):
            record = costQuery.record()
            annual = int(record.value(0))
            early = int(record.value(1))
            
        if(annual == 1):
            costQuery.exec_("Select Fee_Cost from One_Off_Fees where Fee_Description = 'Annual Discount Percent' ")
            if(costQuery.next()):
                record = costQuery.record()
                discount = float(record.value(0))
        elif(early == 1):
            costQuery.exec_("Select Fee_Cost from One_Off_Fees where Fee_Description = 'Early Discount Percent'")
            if(costQuery.next()):
                record = costQuery.record()
                discount = float(record.value(0))
            


        # get the cost of the dropped class
        costQuery.exec_("Select Class_cost from Class where Class_name = '%s'" %(className))
        if(costQuery.next()):
            record = costQuery.record()
            classCost = float(record.value(0))
        #if the student had a registation discount take away the discounted amount
        classCost = classCost - (classCost * discount)
        
        return classCost
            
        
                
    def getStudentId(self,studentName):
        studentQuery = QSqlQuery();
        studentQuery.exec_("Select Student_id from Student where Student_name = '%s'" % studentName)
        if(studentQuery.next()):
            record = studentQuery.record()
            self.studentId = int(record.value(0))

        return

    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()




        
