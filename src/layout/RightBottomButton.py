'''

右下角按钮
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class RightBottomButton(QWidget):
    def __init__(self):
        super(RightBottomButton,self).__init__()
        self.setWindowTitle("右下角按钮")
        self.resize(400,300)

        okButton=QPushButton("确定")
        cancelButton=QPushButton("取消")

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vBox=QVBoxLayout()
        btn1=QPushButton("按钮1")
        btn2=QPushButton("按钮2")
        btn3=QPushButton("按钮3")

        vBox.addStretch(0)
        vBox.addWidget(btn1)
        vBox.addWidget(btn2)
        vBox.addWidget(btn3)
        vBox.addStretch(1)

        vBox.addLayout(hbox)

        self.setLayout(vBox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottomButton()
    main.show()

    sys.exit(app.exec_())
