'''

水平布局
'''

import sys,math
from PyQt5.QtWidgets import *

class AbsoluteLayout(QWidget):
    def __init__(self):
        super(AbsoluteLayout,self).__init__()
        self.setWindowTitle("水平布局")

        hlayout=QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))
        hlayout.addWidget(QPushButton('按钮6'))
        hlayout.setSpacing(40)
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbsoluteLayout()
    main.show()

    sys.exit(app.exec_())
