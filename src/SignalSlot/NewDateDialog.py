from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class NewDateDialog(QDialog):
    Signal_OneParameter=pyqtSignal(str)
    def __init__(self,parent=None):
        super(NewDateDialog,self).__init__()
        self.setWindowTitle("子窗口，用来发射信号")

        layout = QVBoxLayout(self)

        self.label=QLabel(self)
        self.label.setText("前者发射内置信号\n后者发射自定义信号")
        self.datetime_inner=QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.label)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)

    def dateTime(self):
        return self.datetime.dateTime()

    @staticmethod
    def getDateTime(parent=None):
        dialog=NewDateDialog()
        result=dialog.exec()
        date=dialog.dateTime()
        return (date.date(),date.time(),result== QDialog.Accepted)
