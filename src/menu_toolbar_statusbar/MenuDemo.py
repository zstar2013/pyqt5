'''

创建和使用菜单

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.initUI()

    def initUI(self):
        bar=self.menuBar()

        file=bar.addMenu("文件")
        file.addAction("新建")

        save=QAction("保存",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        save.triggered.connect(self.process)

        edit=file.addMenu('Edit')
        edit.addAction("copy")
        edit.addAction("paste")
        quit=QAction("退出",self)
        file.addAction(quit)


        self.resize(300,300)
        self.setWindowTitle("设置Pen的样式")

    def process(self,a):
        print(self.sender().text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()

    sys.exit(app.exec_())