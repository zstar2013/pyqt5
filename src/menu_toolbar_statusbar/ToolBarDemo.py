'''

创建和使用工具栏

工具栏默认按钮：只显示图标，将文本作为悬停提示展示

工具栏按钮有3种显示状态
只显示图标，文字在旁边，文字在底下

'''


import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300,200)
        tb1=self.addToolBar("File")

        new =QAction(QIcon('./images/1145502.png'),"new",self)
        tb1.addAction(new)

        open=QAction(QIcon('./images/root.png'),"open",self)
        tb1.addAction(open)

        save = QAction(QIcon('./images/1145544.png'), "save", self)
        tb1.addAction(save)

        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        tb2 =self.addToolBar("File1")

        new1 = QAction(QIcon('./images/1145502.png'), "新建", self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonIconOnly)

        tb1.actionTriggered.connect(self.toolbtnPressed)
        tb2.actionTriggered.connect(self.toolbtnPressed)




    def toolbtnPressed(self,a):
        print("按下的工具栏按钮是",a.text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()

    sys.exit(app.exec_())