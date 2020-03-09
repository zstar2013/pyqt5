'''

滑块控件

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QFont
from PyQt5.QtCore import QRegExp,Qt
import sys

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("滑块控件展示")
        self.resize(300,700)

        layout=QVBoxLayout()

        self.label=QLabel('你好，Pyqt5')
        self.label.setAlignment(Qt.AlignCenter)

        self.slider=QSlider(Qt.Horizontal)

        #设置最小值
        self.slider.setMinimum(12)
        #设置最大值
        self.slider.setMaximum(48)

        #步长
        self.slider.setSingleStep(18)

        #设置当前值
        self.slider.setValue(18)

        #设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)

        #设置刻度的间隔
        self.slider.setTickInterval(6)

        self.slider.valueChanged.connect(self.valueChange)

        self.slider1=QSlider(Qt.Vertical)

        # 设置最小值
        self.slider1.setMinimum(10)
        # 设置最大值
        self.slider1.setMaximum(60)

        # 步长
        self.slider1.setSingleStep(5)

        # 设置刻度的位置，刻度在下方
        self.slider1.setTickPosition(QSlider.TicksRight)

        # 设置刻度的间隔
        self.slider.setTickInterval(2)

        # 设置当前值
        self.slider1.setValue(20)

        self.slider1.valueChanged.connect(self.valueChange)

        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)
        self.setLayout(layout)


    def valueChange(self):

        print('当前值： %s' % self.sender().value())
        size=self.sender().value()
        self.label.setFont(QFont('Arial',size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()

    sys.exit(app.exec_())