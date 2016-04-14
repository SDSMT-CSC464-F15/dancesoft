import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from removeStudentDialog import Ui_removeStudentDialog
from PyQt4.QtSql import *

'''
class removeStudentData -
# contains the functions and querys
# needed to remove a student and
# all other data linked to the students
# if there are no other links
'''
class removeStudentData(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.removeStu = Ui_removeStudentDialog()
        self.removeStu.setupUi(self)

        self.model = QtGui.QStandardItemModel()

        self.conn()

        self.removeStu.sel_student = QSqlRelationalTableModel(db = self.db)
        self.removeStu.sel_student.setTable("Student")

        if not self.conn():
            QtGui.QMessageBox.warning(
                self, 'Error', 'database contecting error')

        # get student name
        self.student_query = QSqlQuery()
        self.student_query.exec_("Select Student_name FROM Student")
        while self.student_query.next():
            record = self.student_query.record()
            item = QtGui.QStandardItem()
            self.name = str(record.value(0))
            item.setText(self.name)
            self.model.appendRow(item)

        # set up list view model
        self.removeStu.studentListView.setModel(self.model)
        self.removeStu.studentListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        self.removeStu.ok_btn.clicked.connect(self.submit)
        self.removeStu.cancel_btn.clicked.connect(self.close)
        self.removeStu.Search_btn.clicked.connect(self.search)

    def search(self):
        stu_name = self.removeStu.Student_lineEdit.text()
        stu_query = QSqlQuery()
        stu_query.exec_("select Student_name FROM Student where Student_name like '%%%s%%'" % stu_name)
        model = QSqlQueryModel()
        model.setQuery(stu_query)
        self.removeStu.studentListView.setModel(model)
        
    def submit(self):
        studentList = [] #selected student
        stuAddressCounter = 0 # counter to see if address used more then once
        guardCounter = 0 # same for guardian
        secondaryGuardCounter = 0

        # build student
        for selected in self.removeStu.studentListView.selectedIndexes():
            studentList.append(str(selected.data()))
        for student in studentList:
            getId = QSqlQuery()
            getId.exec_("Select Student_id FROM Student WHERE \
                         Student_name = '%s'" % student)
            while getId.next():
                record = getId.record()
                self.id = int(record.value(0))

            # get addresses
            getAddress = QSqlQuery()
            # select address for a single student and then check if others have same address 
            getAddress.exec_("Select Student_address from Student WHERE \
                Student_address = (Select Student_address from Student WHERE\
                Student_name = '%s')" % student)
            while getAddress.next():
                record = getAddress.record()
                addressId = int(record.value(0))
                stuAddressCounter += 1

            # get guardians
            getGuardian = QSqlQuery()
            getGuardian.exec_("Select Guardian_primary, Guardian_secondary from Student WHERE \
                Guardian_primary = (Select Guardian_primary from Student WHERE \
                Student_name = '%s') AND  (Guardian_secondary = (Select Guardian_secondary from Student WHERE \
                Student_name = '%s') OR Guardian_secondary IS NULL) " % (student, student))
            while getGuardian.next():
                record = getGuardian.record()
                guardId = int(record.value(0))
                guardIdSecondary = int(record.value(1))
                guardCounter += 1
                if (guardIdSecondary != None):
                    secondaryGuardCounter += 1
            
            # double check with user before removal 
            self.confirmMessage = "Are you sure you want to remove '%s' from the system? This will remove all relevant information, including payments and billing. This action can not be reversed." \
                                 %(student)
            self.confirmReply = QtGui.QMessageBox.question(self, 'Confirm', 
                self.confirmMessage, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if (self.confirmReply == QtGui.QMessageBox.Yes):
                self.confirm = QSqlQuery()
                self.confirm.exec_("DELETE from Student WHERE Student_name = '%s'" % student)
                self.confirm.exec_("DELETE from Student_Class WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Credits WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Discount WHERE Student_id = %d" % self.id)
                self.confirm.exec_("DELETE from Payment WHERE Student_id = %d" % self.id)

                '''
                # delete if this student is the only student that lives at their address.
                # Prevent delete if someone still in the system lives at the address
                # and make sure not to delete the NONE addreess
                '''
                    
                '''
                # delete if this guardian is the only student that lives at their address.
                # Prevent delete if someone still in the system lives at the address
                # and make sure not to delete the NONE addreess
                '''
                if (guardCounter == 1 and guardId != 0):
                    guardAddressCounter = 0
                    # check guardian addresses
                    getAddress.exec_("Select Guardian_address from Guardian WHERE \
                       Guardian_address = (Select Guardian_address from Guardian WHERE\
                       Graudian_id = %d)" % guardId)
                    while getAddress.next():
                        record = getAddress.record()
                        guardAddressId = int(record.value(0))
                        if (guardAddressId != None):
                            guardAddressCounter += 1

                    
                    # Delete guardian if only one student tied to them    
                    self.confirm.exec_("DELETE from Guardian WHERE Guardian_id = %d" % guardId)

                if (secondaryGuardCounter == 1 and guardIdSecondary != 0):
                    # same for secondary guardian
                    secondaryAddressCounter = 0
                    getAddress.exec_("Select Guardian_address from Guardian WHERE \
                       Guardian_address = (Select Guardian_address from Guardian WHERE\
                       Graudian_id = %d)" % guardIdSecondary)
                    
                    while getAddress.next():
                        record = getAddress.record()
                        secondaryAddressId = int(record.value(0))
                        if (secondaryAddressId != None):
                            secondaryAddressCounter += 1
                    
                    self.confirm.exec_("DELETE from Guardian WHERE Guardian_id = %d" % guardIdSecondary)

                    
                '''
                Here are the three checks to see if the address can be deleted safely
                1. if 1 student and 1 guardian and 1 secondary
                2. 1 student and 1 guardian
                3. 1 student
                Otherwise do not delete address and finsh removal
                '''

                if ((stuAddressCounter == 1 and guardAddressCounter == 1 and secondaryAddressCounter == 1) and addressId != 0):
                    self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)
                elif ((stuAddressCounter == 1 and guardAddressCounter == 1 and secondaryAddressCounter == 0) and addressId != 0):
                    self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)
                elif ((stuAddressCounter == 1 and guardAddressCounter == 0 and secondaryAddressCounter == 0) and addressId != 0):
                    self.confirm.exec_("DELETE from Address WHERE Address_id = %d" % addressId)
                self.message = "Student removed"
                #refresh list
                self.refreshModel()
            
                self.confirmReply = QtGui.QMessageBox.information(self, 'Message', 
                    self.message)

    '''
    refreshModel resets the list view after a removal
    '''
    def refreshModel(self):
        self.model.clear()
        self.student_query = QSqlQuery()
        self.student_query.exec_("Select Student_name FROM Student")
        while self.student_query.next():
            record = self.student_query.record()
            item = QtGui.QStandardItem()
            self.name = str(record.value(0))
            item.setText(self.name)
            self.model.appendRow(item)

        self.removeStu.studentListView.setModel(self.model)
        self.removeStu.studentListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        


    def conn(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("services1.mcs.sdsmt.edu")
        self.db.setDatabaseName("db_dancesoft_f15")
        self.db.setUserName("dancesoft_f15")
        self.db.setPassword("DanceSoft")
        return self.db.open()

        
