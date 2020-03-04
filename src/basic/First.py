import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from menu_windows import Ui_MainWindow

# if __name__=='__main__':
#     #创建类实例
#     app=QApplication(sys.argv)
#     w=QWidget()
#     w.resize(300,150)
#     #移动窗口
#     w.move(300,300)
#     #设置窗口标题
#     w.setWindowTitle('第一个基于Pyqt5的桌面应用')
#
#     w.show()
#
#     sys.exit(app.exec_())

if __name__ == '__main__':
    # 创建类实例
    app = QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainwindow)

    mainwindow.show()

    sys.exit(app.exec_())
