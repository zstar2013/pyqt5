'''

使用线程类（QThread）编写计数器

QThread

def run(self)
    while True:
        self.sleep(1)
        if sec=5:
            break

QLCDNumber

WordThread（QThread）
用到自定义信号

'''



import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal,QThread

sec =0

class WorkThread(QThread):
    timer=pyqtSignal()  #每隔1秒发送一次信号
    end=pyqtSignal()    #计数器完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1)  #休眠1秒
            if sec == 5:
                self.end.emit() #发送end信号
                break
            self.timer.emit()   #发送timer信号



class CounterDemo(QWidget):
    def __init__(self):
        super(CounterDemo, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.initUI()

    def initUI(self):
        layout=QVBoxLayout()
        self.lcdNumber=QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button =QPushButton('开始计数')

        layout.addWidget(button)

        self.workThread=WorkThread()

        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)





    def countTime(self):
        global sec
        sec +=1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self,"消息","计数结束",QMessageBox.Ok)

    def work(self):
        self.workThread.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CounterDemo()
    main.show()

    sys.exit(app.exec_())