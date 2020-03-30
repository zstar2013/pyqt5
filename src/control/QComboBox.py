'''
下拉框控件
1、如何将列表项天骄到QComboBox控件中
2、如何获取选中的列表项

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator,QFont
from PyQt5.QtCore import QRegExp,Qt
import sys

class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("复选框控件展示")
        self.resize(300,200)
        self.label=QLabel('请选择编程语言')
        self.combobox = QComboBox()
        self.combobox.addItem('c++')
        self.combobox.addItem('Python')
        self.combobox.addItems(['Java','C#','Ruby'])

        self.combobox.currentIndexChanged.connect(self.selectionChange)

        layout=QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.combobox)

        self.setLayout(layout)


    def selectionChange(self,i):
        self.label.setText(self.combobox.currentText())
        self.label.adjustSize()

        for count in range(self.combobox.count()):
            print('item' + str(count) + '=' + self.combobox.itemText(count))
        print('current index', i, 'selection changed',self.combobox.currentText())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()

    sys.exit(app.exec_())