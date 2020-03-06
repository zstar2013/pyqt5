'''

通过掩码限制QLineEdit输入
'''


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件输入')
        formLayout=QFormLayout()

        ipLineEdit =QLineEdit()
        macLineEdit =QLineEdit()
        dateLineEdit =QLineEdit()
        licenseLineEdit =QLineEdit()

        #192.168.22.22
        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH:HH;_')
        dateLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAA-AAAA-AAAA-AAAA;#')

        formLayout.addRow('ip',ipLineEdit)
        formLayout.addRow('mac',macLineEdit)
        formLayout.addRow('日期',dateLineEdit)
        formLayout.addRow('验证码',licenseLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditMask()
    main.show()

    sys.exit(app.exec_())
