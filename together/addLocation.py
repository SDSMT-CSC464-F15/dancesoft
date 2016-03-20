import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *
from locationDialog import Ui_locationDialog

class addLocationDialog(QtGui.QDialog):    
    def __init__(self, selected_decription = None):
        QtGui.QDialog.__init__(self)
        self.location = Ui_locationDialog()
        self.location.setupUi(self)
        self.closeFlag = 0

        self.location.ok_btn.clicked.connect(self.addLocation)
        self.location.cancel_btn.clicked.connect(self.setClose)


    def addLocation(self):
        self.newLocation = self.location.locationLineEdit.text()
        self.newLocation = self.newLocation.upper()
        self.accept()

    def getLocation(self):
        return self.newLocation

    def setClose(self):
        self.closeFlag = 1
        self.accept()

    def getClose(self):
        return self.closeFlag
        
