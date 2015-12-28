from PyQt4 import QtGui,QtCore
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.table = QtGui.QTableWidget()
        self.table.setColumnCount(3)
        self.setCentralWidget(self.table)
        data1 = ['orange','apple','banana','lemon']
        data2 = ['3','4','5.5','2']

        self.table.setRowCount(4)

        for i in range(4):
            item1 = QtGui.QTableWidgetItem(data1[i])
            self.table.setItem(i,0,item1)
            item2 = QtGui.QTableWidgetItem(data2[i])
            self.table.setItem(i,1,item2)
            self.button = QtGui.QPushButton('TEST')
            self.button.clicked.connect(self.handleButtonClicked)
            self.table.setCellWidget(i,2,self.button)

    def handleButtonClicked(self):
        button = self.sender()
        item = self.table.itemAt(button.pos())
        if item is not None:
            print (item.row(),item.column())


def Main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()

if __name__ == '__main__':
    Main()
