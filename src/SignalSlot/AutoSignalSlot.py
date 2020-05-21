'''

信号与槽自动连接

on_objectname_signalname

on_button_clicked

'''
from PyQt5 import QtCore
from PyQt5.QtCore import QThread,pyqtSignal,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit,QWidget,QPushButton,QHBoxLayout

import time
import sys

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot,self).__init__()
        self.okButton=QPushButton("ok",self)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QPushButton("cancel", self)
        self.cancelButton.setObjectName("cancelButton")
        layout=QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)
        #self.okButton.clicked.connect(self.on_okButton_clicked)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()

    sys.exit(app.exec_())