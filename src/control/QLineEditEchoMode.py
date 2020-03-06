'''

QLineEdit 控件与回显模式
基本功能 ：输入单行的文本
EchoMode 回显模式

四种回显模式
1、normal 正常模式
2、NoEcho 不回显模式
3、password 密码模式
4、passwordEchoOnEdit

'''

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):

    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout=QFormLayout()

        normalLineEdit=QLineEdit()
        noechoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordEchoOnEdit=QLineEdit()

        formLayout.addRow('normal',normalLineEdit)
        formLayout.addRow('noecho',noechoLineEdit)
        formLayout.addRow('password',passwordLineEdit)
        formLayout.addRow('passwordEchoOnEdit',passwordEchoOnEdit)

        #placeholdertext

        normalLineEdit.setPlaceholderText('normal')
        noechoLineEdit.setPlaceholderText('noecho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEdit.setPlaceholderText('passwordEchoOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noechoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())