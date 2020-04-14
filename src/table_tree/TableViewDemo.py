'''

显示二维表数据（QTableView控件）

数据源

Model

需要创建QTableView实例和一个数据源（Model）,然后将两者关联
MVC：model viewer Controler

nvc的目的是将后端的数据和前段页面的耦合度降低

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])
        #关联QTableView控件和Model
        self.tableview=QTableView()
        self.tableview.setModel(self.model)

        #添加数据
        item11=QStandardItem('10')
        item12=QStandardItem('雷神')
        item13=QStandardItem('2000')
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)
        item21=QStandardItem('30')
        item22=QStandardItem('死亡女神')
        item23=QStandardItem('3000')
        self.model.setItem(2, 0, item21)
        self.model.setItem(2, 1, item22)
        self.model.setItem(2, 2, item23)




        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


        self.resize(500,300)
        self.setWindowTitle("QTableView表格视图控件演示")

    def process(self,a):
        print(self.sender().text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableViewDemo()
    main.show()

    sys.exit(app.exec_())