#advance teacher search
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from Advsearch_teacher import Ui_advsearch_dialog
from PyQt4.QtSql import *
from functools import partial

class Advsearch_Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_advsearch_dialog()
        self.ui.setupUi(self)
        
        self.ui.ID_adv_ledit.setDisabled(True)
        self.connect(self.ui.ID_cbox,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 0))

        self.ui.Name_adv_ledit.setDisabled(True)
        self.connect(self.ui.Name_cobx,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 1))

        self.ui.Homephone_adv_ledit.setDisabled(True)
        self.connect(self.ui.Homephone_cbox,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 2))

        self.ui.Cellphone_adv_ledit.setDisabled(True)
        self.connect(self.ui.Cellphone_cbox,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 3))

        self.ui.Start_dateedit.setDisabled(True)
        self.ui.End_dateedit.setDisabled(True)

        self.connect(self.ui.Birth_cbox,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 4))

        self.ui.Workphone_adv_ledit.setDisabled(True)
        self.connect(self.ui.Workphone_cbox,  QtCore.SIGNAL("stateChanged(int)"), partial(self.checkbox_change, index = 5))


        self.ui.Id_adv_label.hide()
        self.ui.Name_adv_label.hide()
        self.ui.Homephone_adv_label.hide()
        self.ui.Cellphone_adv_label.hide()
        self.ui.Workphone_adv_label.hide()

    def checkbox_change(self, index):
        if index == 0:
            if self.ui.ID_cbox.isChecked():
                self.ui.ID_adv_ledit.setDisabled(False)
            else:
                self.ui.ID_adv_ledit.setDisabled(True)
                self.ui.ID_adv_ledit.clear()
        elif index == 1:
            if self.ui.Name_cobx.isChecked():
                self.ui.Name_adv_ledit.setDisabled(False)
            else:
                self.ui.Name_adv_ledit.setDisabled(True)
                self.ui.Name_adv_ledit.clear()
        elif index == 2:
            if self.ui.Homephone_cbox.isChecked():
                self.ui.Homephone_adv_ledit.setDisabled(False)
            else:
                self.ui.Homephone_adv_ledit.setDisabled(True)
                self.ui.Homephone_adv_ledit.clear()
        elif index == 3:
            if self.ui.Cellphone_cbox.isChecked():
                self.ui.Cellphone_adv_ledit.setDisabled(False)
            else:
                self.ui.Cellphone_adv_ledit.setDisabled(True)
                self.ui.Cellphone_adv_ledit.clear()
        elif index == 4:
            if self.ui.Birth_cbox.isChecked():
                self.ui.Start_dateedit.setDisabled(False)
                self.ui.End_dateedit.setDisabled(False)
            else:
                self.ui.Start_dateedit.setDisabled(True)
                self.ui.End_dateedit.setDisabled(True)
        elif index == 5:
            if self.ui.Workphone_cbox.isChecked():
                self.ui.Workphone_adv_ledit.setDisabled(False)
            else:
                self.ui.Workphone_adv_ledit.setDisabled(True)
                self.ui.Workphone_adv_ledit.clear()
         
