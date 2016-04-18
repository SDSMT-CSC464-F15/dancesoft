#print billing history in html
from PyQt4 import QtGui, QtCore

class Print_window(QtGui.QWidget):
    def __init__(self, HistoryList):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.resize(640, 480)

        
        self.editor = QtGui.QTextBrowser(self)
        self.editor.setFontPointSize(14);

        html = '<!doctype html>\
<html>\
<head>\
    <title>Timetable</title>\
    <style type="text/css">\
    body\
    {\
        font-family: arial;\
    }\
    th,td\
    {\
        margin: 0;\
        text-align: center;\
        border-collapse: collapse;\
        outline: 1px solid #e3e3e3;\
    }\
    td\
    {\
        padding: 5px 10px;\
    }\
    th\
    {\
        background: #666;\
        color: white;\
        padding: 5px 10px;\
    }\
    td:hover\
    {\
        cursor: pointer;\
        background: #666;\
        color: white;\
    }\
    </style>\
</head>\
<body>\
    <table border="1" cellspacing = "0" width="80%" align="center" >\
    <div id="head_nav">\
    <tr>\
        <th>PaymentId</th>\
        <th>Name</th>\
        <th>Term</th>\
        <th>Amount paid</th>\
        <th>Date</th>\
    </tr>\
</div>'
        for i in HistoryList:
            html += '<tr>\
                    <td>%s</td>\
                    <td>%s</td>\
                    <td>%s</td>\
                    <td>%s</td>\
                    <td>%s</td>\
                </div>\
            </tr>' % (str(i[0]), i[1], i[2], str(i[3]), i[4])      
        html += '</table>'

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
        

