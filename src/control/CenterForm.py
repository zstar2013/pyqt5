#QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super(CenterForm,self).__init__(parent)
        self.setWindowTitle("第一个应用窗口")
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)

    def center(self):
        #获取屏幕坐标系
        screen=QDesktopWidget.screenGeometry()
        #获取窗口坐标系
        size=self.geometry()
        newLeft=(screen.width()-size.width())/3
        newTop=(screen.height()-size.height())/3
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./image/1203057.png'))
    main=CenterForm()
    main.show()

    sys.exit(app.exec_())


