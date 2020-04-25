'''

在表格中快速定位到特定的行

1、数据的定位
2、如果找到满足条件的单元格，会定位到单元格
setCellWidget
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel
from qtpy import QtCore


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(430, 230)
        self.setWindowTitle("PlaceControlInCell例子")

        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                itemContent='(%d,%d)'%(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(layout)

        #搜索满足条件的Cell
        text='(1'
        items=tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)

        if len(items)>0:
            item=items[0]
            item.setBackground(QBrush(QColor(0,255,0)))
            item.setForeground(QBrush(QColor(255,0,0)))

            row=item.row()

            #定位到指定的行
            tableWidget.verticalScrollBar().setSliderPosition(row)



        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DataLocation()
    main.show()

    sys.exit(app.exec_())