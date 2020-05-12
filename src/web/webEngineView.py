'''

用web浏览器控件（QWebEngineView）显示网页
Pyqt5和web的交互技术
同时使用python和web开发程序，混合开发

Python+JavaScript+html+Css

QWebEngineView

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal,QThread



class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5,30,1355,730)
        self.initUI()

    def initUI(self):
        self.browser=QWebEngineView()
        self.browser.load('https://www.jd.com')
        self.setCentralWidget(self.browser)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WebEngineView()
    main.show()

    sys.exit(app.exec_())