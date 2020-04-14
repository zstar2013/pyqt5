'''

显示列表数据（QListView控件）

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.initUI()

    def initUI(self):

        layout=QVBoxLayout()

        listview=QListView()
        listModel=QStringListModel()
        self.list=["列表项1","列表项2","列表项3"]

        listModel.setStringList(self.list)
        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)
        self.resize(300, 270)
        self.setWindowTitle("QListView例子")

    def clicked(self,item):
        QMessageBox.information(self,"QlistView","您选择了："+self.list[item.row()])





    def process(self,a):
        print(self.sender().text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()

    sys.exit(app.exec_())