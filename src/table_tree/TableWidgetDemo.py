'''

拓展的列表控件（TableWidget）

QTableView

每一个cell(单元格)是一个TableWidgetItem
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        layout=QHBoxLayout()
        tablewidget=QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem=QTableWidgetItem('小明')
        tablewidget.setItem(0,0,nameItem)
        ageItem = QTableWidgetItem('24')
        tablewidget.setItem(0, 1, ageItem)
        jgItem=QTableWidgetItem('北京')
        tablewidget.setItem(0,2,jgItem)

        #禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #调整行和列
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowToContents()

        #tablewidget.horizontalHeader().setVisible(False)
        #tablewidget.verticalHeader().setVisible(False)

        tablewidget.setVerticalHeaderLabels(["a","b"])

        self.setLayout(layout)

        self.resize(430, 230)
        self.setWindowTitle("TableWidgetDemo例子")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()

    sys.exit(app.exec_())