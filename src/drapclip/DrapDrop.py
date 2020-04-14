'''

让控件支持拖住动作
A.setDrapEnabled(True)
B.setAcceptDrops(True)
需要两个事件
1.dragEnterEvent 将A拖到B触发
2.dropEvent      在B的区域放下A时触发


'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent):
        self.addItem(e.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formlayout=QFormLayout()
        formlayout.addRow(QLabel("请将左边的文本拖拽到右边的下拉列表中"))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)#让QLineEdit控件可拖动

        combo=MyComboBox()
        formlayout.addRow(lineEdit,combo)
        self.setLayout(formlayout)
        self.setWindowTitle('拖拽案例')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()

    sys.exit(app.exec_())