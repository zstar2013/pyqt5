'''

多窗口交互（1）：使用信号与槽

win1

win2

强耦合、相互访问互相的控件
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NewDateDialog import NewDateDialog

class MultWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,90)
        self.setWindowTitle("多窗口交互（2）：使用信号与槽")

        self.open_btn=QPushButton('获取时间')
        self.lineEdit_inner=QLineEdit(self)
        self.lineEdit_emit=QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText("接收子窗口内置信号的时间")
        self.lineEdit_emit.setText("接收子窗口自定义信号的时间")

        gridLayout=QGridLayout()
        gridLayout.addWidget(self.lineEdit_inner)
        gridLayout.addWidget(self.lineEdit_emit)

        gridLayout.addWidget(self.open_btn)

        self.setLayout(gridLayout)


    def openDialog(self):
        dialog=NewDateDialog(self)
        #连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        #连接子窗口的自定义信号与主窗口的槽函数
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,dateStr):
        self.lineEdit_emit.setText(dateStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = MultWindow2()
    example.show()

    sys.exit(app.exec_())