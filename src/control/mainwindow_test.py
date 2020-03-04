import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        self.setWindowTitle("第一个应用窗口")
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/1203057.png'))
    main=FirstMainWin()
    main.show()

    sys.exit(app.exec_())


