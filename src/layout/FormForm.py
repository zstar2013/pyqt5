'''

表单布局
'''

import sys,math
from PyQt5.QtWidgets import *

class FormForm(QWidget):
    def __init__(self):
        super(FormForm,self).__init__()
        self.setWindowTitle("表单布局")

        titleLabel =QLabel("标题")
        authorLabel =QLabel("作者")
        contentLabel =QLabel("内容")

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        contentEdit=QTextEdit()


        formlayout =QFormLayout()
        formlayout.addRow(titleLabel,titleEdit)
        formlayout.addRow(authorLabel,authorEdit)
        formlayout.addRow(contentLabel,contentEdit)



        self.setLayout(formlayout)
        self.resize(350,300)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormForm()
    main.show()

    sys.exit(app.exec_())
