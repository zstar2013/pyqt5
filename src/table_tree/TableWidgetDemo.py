'''

拓展的列表控件（TableWidget）

QTableView

每一个cell(单元格)是一个TableWidgetItem
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class TableWidgetDemo(QMainWindow):
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


        self.resize(430, 230)
        self.setWindowTitle("TableWidgetDemo例子")
        self.setCentralWidget(self.listwdiget)



    def clicked(self,Index):
        QMessageBox.information(self,"QlistView","您选择了："+self.listwdiget.item(self.listwdiget.row(Index)).text())





    def process(self,a):
        print(self.sender().text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()

    sys.exit(app.exec_())