'''

停靠控件
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class DockWidgetDemo(QMainWindow):
    def __init__(self):
        super(DockWidgetDemo, self).__init__()
        self.setWindowTitle('堆栈窗口控件')
        self.setGeometry(300,50,10,10)
        self.initUI()

    def initUI(self):
        layout=QHBoxLayout()
        self.items=QDockWidget('Dockable',self)
        self.listWidget=QListWidget()
        self.listWidget.insertItem(0, '联系方式')
        self.listWidget.insertItem(1, '个人信息')
        self.listWidget.insertItem(2, '教育程度')

        self.items.setWidget(self.listWidget)

        self.setCentralWidget(QLineEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)

        self.items.setFloating(True)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DockWidgetDemo()
    main.show()

    sys.exit(app.exec_())