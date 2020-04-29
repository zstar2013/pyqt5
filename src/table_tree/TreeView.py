'''

树控件响应事件

'''

import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QStringListModel


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model=QDirModel()
    tree=QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('QTreeView')
    tree.show()

    sys.exit(app.exec_())