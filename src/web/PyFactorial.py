'''

JavaScript 调用Python函数计算阶乘
将Python的一个对象映射到JavaScript中
将槽函数映射到javaScript中



Python+JavaScript+html+Css


'''

import sys,math,os
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal, QThread, QUrl
from Factorial import *

channel =QWebChannel()
factorial=Factorial()

class PyFactorial(QWidget):
    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python 计算阶乘')
        self.resize(600,300)
        self.initUI()

    def initUI(self):
        self.browser=QWebEngineView()
        url=os.getcwd()+'/f.html'
        self.browser.load(QUrl.fromLocalFile(url))
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.browser)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyFactorial()
    main.show()

    sys.exit(app.exec_())