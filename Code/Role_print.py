from PyQt4 import QtGui, QtCore

class Print_window(QtGui.QWidget):
    def __init__(self, text_msg = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.resize(640, 480)
        self.editor = QtGui.QTextEdit(self)
        self.editor.setFontPointSize(14);
        for i in text_msg:
            self.editor.insertPlainText('%s\n' % i)
        
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QtGui.QPushButton('Open', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonPrint = QtGui.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtGui.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.handleTextChanged()

    def handleOpen(self):
        path = QtGui.QFileDialog.getOpenFileName(
            self, self.tr('Open file'), '',
            self.tr('HTML files (*.html);;Text files (*.txt)'))
        if not path.isEmpty():
            stream = QtCore.QFile(path)
            if stream.open(QtCore.QIODevice.ReadOnly):
                info = QtCore.QFileInfo(path)
                text = QtCore.QString.fromLocal8Bit(stream.readAll())
                if info.completeSuffix() == 'html':
                    self.editor.setHtml(text)
                else:
                    self.editor.setPlainText(text)
            stream.close()

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


