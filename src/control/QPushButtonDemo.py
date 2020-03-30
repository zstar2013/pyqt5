'''

按钮控件 （QPushButton）

QPushButton
AToolButton
QradioButton
QcheckBox
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap,QIcon

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout=QVBoxLayout()

        self.button1=QPushButton('第一个按钮')
        self.button1.setText('first button')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)

        layout.addWidget(self.button1)

        #在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./image/1203057.png')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)


        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        #self.button3.clicked.connect(lambda :self.whichButton(self.button3))
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<'+btn.text()+'>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()

    sys.exit(app.exec_())