from PyQt4 import QtGui, QtCore

class Print_window(QtGui.QWidget):
    def __init__(self, semester = None, paid = None, due = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.resize(640, 480)

        
        self.editor = QtGui.QTextBrowser(self)
        self.editor.setFontPointSize(14);

        html = '<p><font size="6">Semester: %s</font></p> \
                <p><font size="6">Money paid: %.2f</font></p> \
                <p><font size="6">Money due: %.2f</font></p> \
                <p><font size="6">Remaining balance: %.2f</font></p>' \
               % (semester.replace("_", " Term "), paid, due, (paid-due))
        
        
        self.editor.append(html)
        
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonPrint = QtGui.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtGui.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)
        self.handleTextChanged()

    def handlePrint(self):
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handlePreview(self):
        dialog = QtGui.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.editor.print_)
        dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)
        

