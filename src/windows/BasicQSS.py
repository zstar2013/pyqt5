'''

QSS基础

QSS（Qt Style Sheet）
Qt样式表
用于设置控件的样式

CSS
'''
from PyQt5.QtWidgets import *
import sys

class BasicQSS(QWidget):
    def __init__(self):
        super(BasicQSS,self).__init__()
        self.setWindowTitle("QSS样式")
        btn1=QPushButton(self)
        btn1.setText("按钮1")

        btn2 = QPushButton(self)
        btn2.setProperty('name','btn2')
        btn2.setText("按钮2")

        btn3 = QPushButton(self)
        btn3.setText("按钮3")
        btn3.setProperty('name','btn3')



        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.resize(400,200)
        self.setLayout(vbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = BasicQSS()
    qssStyle='''
        QPushButton[name='btn2']{
            background-color:red;
            color:yellow;
            height:120;
            font-size:60px;
        }
        QPushButton[name='btn3']{
            background-color:blue;
            color:yellow;
            height:60;
            font-size:30px;
        }
    '''
    example.setStyleSheet(qssStyle)
    example.show()

    sys.exit(app.exec_())
