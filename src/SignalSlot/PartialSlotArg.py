'''

使用Partial对象为槽函数传递参数

'''


from PyQt5.QtWidgets import *
import sys
from functools import partial

class PartialSlotArgs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("使用lambda 表达式为槽函数传递参数")

        button1 = QPushButton("按钮1")
        button2 = QPushButton("按钮2")

        button1.clicked.connect(partial(self.onButtonClicked,10, 20))
        button2.clicked.connect(partial(self.onButtonClicked,40, -20))
        layout = QHBoxLayout()
        layout.addWidget(button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        layout.addWidget(button2)
        self.setCentralWidget(mainFrame)

    def onButtonClicked(self, m, n):
        print("m+n=", m + n)
        QMessageBox.information(self, "结果", str(m + n))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PartialSlotArgs()
    example.show()

    sys.exit(app.exec_())