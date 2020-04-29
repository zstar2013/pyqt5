
'''

动态显示当前时间

QTimer 定时器
QThread

处理耗时任务
多线程：用于同时完成多个任务

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime


class ShowTime(QWidget):
    def __init__(self):
        super(ShowTime, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.initUI()

    def initUI(self):
        self.label=QLabel('显示当前时间')
        self.startBtn=QPushButton('开始')
        self.endBtn=QPushButton('结束')

        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)





    def showTime(self):
        time=QDateTime.currentDateTime()














if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowTime()
    main.show()

    sys.exit(app.exec_())