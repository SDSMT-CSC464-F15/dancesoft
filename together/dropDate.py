import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from dropDateDialog import Ui_dropDateDialog

class getDropDialog(QtGui.QDialog):    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.drop = Ui_dropDateDialog()
        self.drop.setupUi(self)
        closeFlag = 0

        self.drop.ok_btn.clicked.connect(self.addDate)
        self.drop.cancel_btn.clicked.connect(self.setClose)


    def addDate(self):
        self.dropDate = self.drop.dropDateEdit.date()
        self.drop = self.dropDate.toPyDate()
        self.accept()

    def getDate(self):
        return self.dropDate

    def setClose(self):
        self.closeFlag = 1
        self.accept()

    def getClose(self):
        return self.closeFlag
        
