'''

树控件的基本用法

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(430, 230)
        self.setWindowTitle("树控件的基本用法")

        self.tree=QTreeWidget()
        #为树制定列数
        self.tree.setColumnCount(2)

        #指定列标签
        self.tree.setHeaderLabels(['Key','Value'])
        root=QTreeWidgetItem(self.tree)
        root.setText(0,"根节点")
        root.setIcon(0,QIcon('./images/root.png'))
        self.tree.setColumnWidth(0,120)
        self.setCentralWidget(self.tree)

        #添加子节点

        child1 =QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点的数据')
        child1.setIcon(0,QIcon('./images/child1.png'))
        child1.setCheckState(0,Qt.Checked)

        #添加第二个子节点
        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('./images/child1.png'))

        #为第二个子节点添加一个子节点

        child3=QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1,'新的值')
        child3.setIcon(0, QIcon('./images/child1.png'))

        self.tree.expandAll()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicTreeWidget()
    main.show()

    sys.exit(app.exec_())