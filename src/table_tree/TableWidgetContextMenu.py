
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
        self.setWindowTitle("PlaceControlInCell例子")

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

        self.button=QPushButton('sort')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType=Qt.DescendingOrder

        self.setLayout(layout)

    def order(self):
        if self.orderType==Qt.DescendingOrder:
            self.orderType=Qt.AscendingOrder
        else:
            self.orderType=Qt.DescendingOrder
        self.tableWidget.sortItems(2,self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetContextMenu()
    main.show()

    sys.exit(app.exec_())