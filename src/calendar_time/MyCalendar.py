'''

日历控件

QCalendarWidget


'''
import sys,math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QMimeData,QDate

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):

        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        #self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.label=QLabel(self)
        date=self.cal.selectedDate()
        self.label.setText(date.toString("yyyy-MM-dd dddd"))
        self.setWindowTitle("日历演示")
        self.resize(300,400)

    def showDate(self,date):
        self.resize()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()

    sys.exit(app.exec_())