'''

合并单元格

setSpan(row,col,row_count,col_count)
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel
from qtpy import QtCore


class SpanDemo(QWidget):
    def __init__(self):
        super(SpanDemo, self).__init__()
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


        newItem=QTableWidgetItem('112')
        tableWidget.setItem(0,0,newItem)
        tableWidget.setSpan(0,0,3,1)
        newItem=QTableWidgetItem('男')
        tableWidget.setItem(0,1,newItem)
        tableWidget.setSpan(0, 1, 2, 1)

        newItem = QTableWidgetItem('160')
        tableWidget.setItem(0,2,newItem)
        tableWidget.setSpan(0, 2, 4, 1)



        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SpanDemo()
    main.show()

    sys.exit(app.exec_())