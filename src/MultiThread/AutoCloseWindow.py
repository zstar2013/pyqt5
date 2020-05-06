
'''

让程序定时关闭
QTimer.singleShot

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime


class AutoCloseWindow(QWidget):
    def __init__(self):
        super(AutoCloseWindow, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.initUI()

    def initUI(self):
        self.label=QLabel('窗口在5秒后自动关闭')
        self.startBtn=QPushButton('开始')

        layout=QGridLayout()



        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)

        self.startBtn.clicked.connect(self.startTimer)
        self.setLayout(layout)





    def closeWindow(self):
        sys.exit(app.exec_())

    def startTimer(self):
        self.timer = QTimer()
        self.timer.singleShot(5000, app.quit)















if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoCloseWindow()
    main.show()

    sys.exit(app.exec_())