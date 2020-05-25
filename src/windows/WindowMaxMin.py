'''

用代码控制窗口的最大化和最小化

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

class WindowMaxMin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用代码控制窗口的最大化和最小化")
        #self.setWindowFlags(Qt.WindowMaximizeButtonHint |Qt.WindowCloseButtonHint|Qt.WindowMinimizeButtonHint)

        layout=QVBoxLayout()
        maxButton1=QPushButton()
        maxButton1.setText("窗口最大化")
        maxButton1.clicked.connect(self.maximized1)
        layout.addWidget(maxButton1)

        maxButton2 = QPushButton()
        maxButton2.setText("窗口最大化")
        maxButton2.clicked.connect(self.showMaximized)
        layout.addWidget(maxButton2)

        maxButton3 = QPushButton()
        maxButton3.setText("窗口最小化")
        maxButton3.clicked.connect(self.showMinimized)
        layout.addWidget(maxButton3)

        self.setLayout(layout)

    def maximized1(self):
        #获得桌面
        destop=QApplication.desktop()
        #获取桌面可用尺寸
        rect=destop.availableGeometry()
        self.setGeometry(rect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = WindowMaxMin()
    example.show()

    sys.exit(app.exec_())
