'''

设置单元格的字体和颜色
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel
from qtpy import QtCore


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(430, 230)
        self.setWindowTitle("PlaceControlInCell例子")

        layout=QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        newItem = QTableWidgetItem('小明')
        newItem.setFont(QFont('Times',14,QFont.Black))
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem('小明2')
        #newItem.setFont(QFont('Times', 14, QFont.Black))
        newItem.setForeground(QBrush(QColor(255, 255, 0)))
        newItem.setBackground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem('160')
        newItem.setFont(QFont('Times', 20, QFont.Black))
        newItem.setForeground(QBrush(QColor(0, 0, 255)))
        tableWidget.setItem(0, 2, newItem)






        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellFontAndColor()
    main.show()

    sys.exit(app.exec_())