'''

添加、修改和删除控件中的节点

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(430, 230)
        self.setWindowTitle("TreeWidget 例子")

        operatorLayout=QHBoxLayout()
        addBtn=QPushButton('添加节点')
        updateBtn=QPushButton('修改节点')
        deleteBtn=QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        addBtn.clicked.connect(self.addNode)
        addBtn.clicked.connect(self.addNode)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()

    sys.exit(app.exec_())