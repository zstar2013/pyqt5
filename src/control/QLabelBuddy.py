'''
QLabel 与伙伴关系

'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog,QHBoxLayout, QMainWindow, QLabel,QLineEdit, QApplication, QPushButton, QWidget, QToolTip, QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont, QPixmap

from PyQt5.QtGui import QPalette

class QLabelBuddy(QDialog ):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel =QLabel('&Password',self)
        passwordLineEdit=QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btn=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btn,2,1)
        mainLayout.addWidget(btnCancel,2,2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())