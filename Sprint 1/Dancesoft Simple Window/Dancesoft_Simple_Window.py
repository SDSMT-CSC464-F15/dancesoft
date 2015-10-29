import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("DanceSoft Sample Window")
        self.setWindowIcon(QtGui.QIcon('adalogo.png'))


        extractAction = QtGui.QAction("Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the Application")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        OK_btn = QtGui.QPushButton("OK", self)
        btn.clicked.connect(self.close_application)
        
        OK_btn.resize(btn.minimumSizeHint())
        OK_btn.move(320,250)
        btn.resize(btn.minimumSizeHint())
        btn.move(400,250)

        extractAction = QtGui.QAction(QtGui.QIcon('adalogo.png'),'example toolbar',self)
        extractAction.triggered.connect(self.close_application)
        self.toolbar= self.addToolBar("adalogo")
        self.toolbar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista", self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("Windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        

        comboBox.move(50,250)
        self.styleChoice.move(51, 250)
        comboBox.activated[str].connect(self.style_Choice)

        self.show()

    def style_Choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
            
        else:
            self.setGeometry(50,50,500,300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Quit',
                                            "Are you sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        

def run():
    app = QtGui.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())


run()

