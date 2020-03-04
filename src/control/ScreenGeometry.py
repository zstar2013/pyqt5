import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
def onClick_button():
    print('1')
    print("widget.x()= %d:"% widget.x())  #250 （窗口横坐标）
    print("widget.y()= %d:"% widget.y())  #200  （窗口纵坐标）
    print("widget.width()= %d:"% widget.width())  #300 （工作区宽度）
    print("widget.height()= %d:"% widget.height()) #240 （工作区高度）

    print('2')
    print("widget.geometry().x()= %d:" % widget.geometry().x()) #258 （工作区横坐标）
    print("widget.geometry().y()= %d:" % widget.geometry().y()) #231 （工作区纵坐标）
    print("widget.geometry().width()= %d:" % widget.geometry().width()) #300 （工作区宽度）
    print("widget.geometry().eight()= %d:" % widget.geometry().height()) #240 （工作区高度）

    print('3')
    print("widget.frameGeometry().x()= %d:" % widget.frameGeometry().x()) #250 （窗口横坐标）
    print("widget.frameGeometry().y()= %d:" % widget.frameGeometry().y()) #200  （窗口纵坐标）
    print("widget.frameGeometry().width()= %d:" % widget.frameGeometry().width()) #316（窗口宽度）
    print("widget.frameGeometry().eight()= %d:" % widget.frameGeometry().height()) #279（窗口高度）


app=QApplication(sys.argv)

widget=QWidget()
btn=QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_button)

btn.move(24,52)

widget.resize(300,240)    #设置工作区的尺寸

widget.move(250,200)

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())

