'''

水平布局
'''

import sys,math
from PyQt5.QtWidgets import *

class QBoxLayout(QWidget):
    def __init__(self):
        super(QBoxLayout,self).__init__()
        self.setWindowTitle("垂直布局")

        layout=QVBoxLayout()
        layout.addWidget(QPushButton('按钮1'))
        layout.addWidget(QPushButton('按钮2'))
        layout.addWidget(QPushButton('按钮3'))
        layout.addWidget(QPushButton('按钮4'))
        layout.addWidget(QPushButton('按钮5'))
        layout.addWidget(QPushButton('按钮6'))
        layout.setSpacing(40)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QBoxLayout()
    main.show()

    sys.exit(app.exec_())
