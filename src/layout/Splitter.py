'''

拖动控件之间的边界
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Splitter(QWidget):
    def __init__(self):
        super(Splitter,self).__init__()
        hbox = QHBoxLayout(self)
        self.setWindowTitle("表单布局")
        self.setGeometry(300,300,300,200)
        topleft=QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom =QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1=QSplitter()
        textEdit=QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textEdit)
        splitter1.setSizes([200,100])

        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)


        hbox.addWidget(splitter2)
        self.setLayout(hbox)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Splitter()
    main.show()

    sys.exit(app.exec_())
