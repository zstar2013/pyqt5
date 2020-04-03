'''

绘制各种图形

弧
圆形
矩形
椭圆
多边形
绘制图像

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300,600)
        self.setWindowTitle("绘制各种图形")

    def paintEvent(self, QPaintEvent):
        qp=QPainter()
        qp.begin(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()

    sys.exit(app.exec_())
