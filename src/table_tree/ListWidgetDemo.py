'''

拓展的列表控件（QListWidget）

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


class ListViewDemo(QMainWindow):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.listwdiget=QListWidget()
        self.listwdiget.addItem("item1")
        self.listwdiget.addItem("item2")
        self.listwdiget.addItem("item3")
        self.listwdiget.addItem("item4")
        self.listwdiget.addItem("item5")
        self.listwdiget.itemClicked.connect(self.clicked)

        self.resize(300, 270)
        self.setWindowTitle("QListWidget例子")
        self.setCentralWidget(self.listwdiget)



    def clicked(self,Index):
        QMessageBox.information(self,"QlistView","您选择了："+self.listwdiget.item(self.listwdiget.row(Index)).text())





    def process(self,a):
        print(self.sender().text())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()

    sys.exit(app.exec_())