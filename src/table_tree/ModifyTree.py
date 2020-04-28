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
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, "root")
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)
        mainLayout=QVBoxLayout(self)
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    #添加节点
    def addNode(self):
        print('添加节点')
        item =self.tree.currentItem()
        print(item)
        node =QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新增')

    def updateNode(self):
        print('修改节点')
        item=self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'节点已被修改')

    def deleteNode(self):
        print('删除节点')
        root = self.tree.invisibleRootItem()
        item = self.tree.currentItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)

    def onTreeClicked(self,index):
        item=self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s'%(item.text(0),item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()

    sys.exit(app.exec_())