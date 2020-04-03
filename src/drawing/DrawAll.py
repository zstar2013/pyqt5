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
from PyQt5.QtCore import QRect,QPoint

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300,600)
        self.setWindowTitle("绘制各种图形")

    def paintEvent(self, QPaintEvent):
        qp=QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)
        #绘制弧
        rect =QRect(0,10,100,100)
        #alen:1个alen等于1/16度
        qp.drawArc(rect,0,50*16)
        #通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120,10,100,100,0,360*16)

        #绘制带弦的弧
        qp.drawChord(10,120,100,100,12,130*16)

        #绘制扇形
        qp.drawPie(10,240,100,100,12,130*16)

        #椭圆
        qp.drawEllipse(120,120,150,100)
        qp.end()

        #绘制多边形
        point1=QPoint(140,380)
        point2=QPoint(140,380)
        point3=QPoint(140,380)
        point4=QPoint(140,380)
        point5=QPoint(140,380)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()

    sys.exit(app.exec_())
