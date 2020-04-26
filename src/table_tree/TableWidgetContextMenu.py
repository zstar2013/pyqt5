
'''

设置单元格的字体和颜色
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel
from qtpy import QtCore


class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 300)
        self.setWindowTitle("在表格中显示上下文菜单")

        layout=QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)

        layout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0,0,newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem('165')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem('144')
        self.tableWidget.setItem(2, 2, newItem)

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(layout)

    def generateMenu(self,pos):
        print(pos)
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum=i.row()
        #如果选择的行索引小于2，则弹出上下文菜单
        if rowNum < 2:
            menu=QMenu()
            item1=menu.addAction("A")
            item2=menu.addAction("B")
            item3=menu.addAction("C")
            screenPos=self.tableWidget.mapToGlobal(pos)
            print(screenPos)
            #被阻塞
            action=menu.exec(screenPos)
            if action ==item1:
                print('选择了第一个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum, 1).text(),
                      self.tableWidget.item(rowNum, 2).text())
            elif action ==item2:
                print('选择了第二个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum, 1).text(),
                      self.tableWidget.item(rowNum, 2).text())
            elif action ==item3:
                print('选择了第三个菜单项',self.tableWidget.item(rowNum,0).text(),
                      self.tableWidget.item(rowNum, 1).text(),
                      self.tableWidget.item(rowNum, 2).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetContextMenu()
    main.show()

    sys.exit(app.exec_())