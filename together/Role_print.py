#print role sheet
from PyQt4 import QtGui, QtCore

class Print_window(QtGui.QWidget):
    def __init__(self, text_msg = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(self.tr('Document Printer'))
        self.resize(640, 480)
        
        self.editor = QtGui.QTextBrowser(self)
        self.editor.setFontPointSize(14);

        
        #populate information to html 
        html = '<p><center><font size="6">Attendance Sheet</font></center></p>'
        
        html += '<table cellpadding="5" border="1" cellspacing = "2" style = "border:1px black;font-size: 12px;">\
                            <tr>\
                                <td>ID</td>\
                                <td>Name</td>\
                                <td>Home Phone</td>\
                                <td>Emergency Contact</td>\
                                <td>Emergency Phone</td>\
                                <th colspan="5">    Month 1   </th>\
                                <th colspan="5">    Month 2   </th>\
                                <th colspan="5">    Month 3   </th>\
                            </tr>'
        
        for i in text_msg:
            temp = i.split(',')
            html += '<tr>\
                      <td>%s</td>\
                      <td>%s</td>\
                      <td>%s</td>\
                      <td>%s</td>\
                      <td>%s</td>\
                     </tr>' % (temp[0], temp[1], temp[2], temp[3], temp[4])
        html += '</table>'
        self.editor.append(html)
        #set up buttons 
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


