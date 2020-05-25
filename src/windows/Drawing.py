'''

项目实战：实现绘图应用

需要解决3个核心内容：1、如何绘图 2、在哪里绘图 3、如何通过移动鼠标绘图

'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt,QPoint

class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.setWindowTitle("绘图应用")

        self.pix=QPixmap()
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600,600)
        #画布大小为400X400
        self.pix=QPixmap(600,600)
        self.pix.fill(Qt.white)
    def paintEvent(self, QPaintEvent):
        pp=QPainter(self.pix)
        #根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint,self.endPoint)
        #让前一个坐标值等于后一个坐标值,
        #这样就能实现画出连续的线
        self.lastPoint=self.endPoint
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button()== Qt.LeftButton:
            self.lastPoint=QMouseEvent.pos()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.endPoint = QMouseEvent.pos()
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            self.endPoint=QMouseEvent.pos()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Drawing()
    example.show()

    sys.exit(app.exec_())
