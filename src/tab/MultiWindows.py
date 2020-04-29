'''

容纳多文档的窗口

QMdiArea

QMdiSubWindow
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class MultiWindows(QMainWindow):
    count=0
    def __init__(self):
        super(MultiWindows, self).__init__()
        self.setWindowTitle('堆栈窗口控件')
        self.initUI()

    def initUI(self):
        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)
        bar=self.menuBar()
        file= bar.addMenu('File')
        file.addAction("new")
        file.addAction('cascade')
        file.addAction('Tiled')

        file.triggered.connect(self.windowaction)

    def windowaction(self,q):
        if q.text()=='new':
            MultiWindows.count=MultiWindows.count +1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口'+str(MultiWindows.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text()=='cascade':
            self.mdi.cascadeSubWindows()

        elif q.text()=='Tiled':
            self.mdi.tileSubWindows()










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()

    sys.exit(app.exec_())