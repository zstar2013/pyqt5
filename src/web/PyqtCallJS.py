'''

PyQt5调用js代码


Python+JavaScript+html+Css


'''

import sys,math,os
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QDateTime, pyqtSignal, QThread, QUrl


class PyqtCallJS(QWidget):
    def __init__(self):
        super(PyqtCallJS, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5,30,1355,730)
        self.initUI()

    def initUI(self):
        self.browser=QWebEngineView()
        url=os.getcwd()+'/tt.html'
        self.browser.load(QUrl.fromLocalFile(url))
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.browser)

        button =QPushButton('设置全名')
        button.clicked.connect(self.complete_fullname)
        self.layout.addWidget(button)

    def complete_fullname(self):

        self.value='hello world'
        self.browser.page().runJavaScript('fullname("'+self.value+'");',self.js_callback)

    def js_callback(self,result):
        print(result)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyqtCallJS()
    main.show()

    sys.exit(app.exec_())