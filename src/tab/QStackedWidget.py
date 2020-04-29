'''

拓展的列表控件（TableWidget）

QTableView

每一个cell(单元格)是一个TableWidgetItem
'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class QStackedWidgetDemo(QWidget):
    def __init__(self):
        super(QStackedWidgetDemo, self).__init__()
        self.setWindowTitle('堆栈窗口控件')
        self.setGeometry(300,50,10,10)
        self.initUI()

    def initUI(self):

        self.list=QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox=QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)

    def display(self,index):
        self.stack.setCurrentIndex(index)



    def tab1UI(self):

        layout=QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        self.stack1.setLayout(layout)

    def tab2UI(self):

        layout=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))

        layout.addRow(QLabel("性别"),sex)
        layout.addRow('生日',QLineEdit())
        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("项目"))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))
        self.stack3.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QStackedWidgetDemo()
    main.show()

    sys.exit(app.exec_())