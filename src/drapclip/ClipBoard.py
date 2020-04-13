'''

使用剪贴板

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QMimeData

class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        textCopyButton=QPushButton('复制文本')
        textPasteButton=QPushButton('粘贴文本')

        htmlCopyButton=QPushButton('复制HTML')
        htmlPasteButton=QPushButton('粘贴HTML')

        imageCopyButton=QPushButton('复制图像')
        imagePasteButton=QPushButton('粘贴图像')

        self.textLabel=QLabel('默认文本')

        self.imageLabel=QLabel()
        #self.imageLabel.setPixmap(QPixmap('./image/1203057.png'))

        layout=QGridLayout()
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(htmlCopyButton,0,1)
        layout.addWidget(imageCopyButton,0,2)
        layout.addWidget(textPasteButton,1,0)
        layout.addWidget(htmlPasteButton,1,1)
        layout.addWidget(imagePasteButton,1,2)

        layout.addWidget(self.textLabel,2,0,1,2)
        layout.addWidget(self.imageLabel,2,2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle("剪贴板演示")

    def copyText(self):
        clipBoard=QApplication.clipboard()
        clipBoard.setText('hello world')

    def pasteText(self):
        clipBoard = QApplication.clipboard()
        self.textLabel.setText(clipBoard.text())

    def copyImage(self):
        clipBoard = QApplication.clipboard()
        clipBoard.setPixmap(QPixmap('./image/1203057.png'))

    def pasteImage(self):
        clipBoard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipBoard.pixmap())

    def copyHtml(self):
        mimeData=QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipBoard = QApplication.clipboard()
        clipBoard.setMimeData(mimeData)

    def pasteHtml(self):
        clipBoard = QApplication.clipboard()
        mimeData = clipBoard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()

    sys.exit(app.exec_())