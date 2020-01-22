import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
from PyQt5.QtGui import QIcon
class IconForm(QMainWindow):

    def __init__(self):
        super(IconForm,self).__init__()
    def initUI(self):
        self.setGeometry(300,300,250,250)
        #设置主窗口的标题
        self.setWindowTitle("设置窗口图标")
        #设置窗口的图标
        self.setWindowIcon(QIcon("./images/d.ico"))

        self.resize(400,300)

if __name__ == '__main__':
    app =QApplication(sys.argv)

    main=IconForm()
    main.show()
    sys.exit(app.exec_())