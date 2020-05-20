'''

栅格布局
'''

import sys,math
from PyQt5.QtWidgets import *

class Clac(QWidget):
    def __init__(self):
        super(Clac,self).__init__()
        self.setWindowTitle("栅格布局")

        grid =QGridLayout()
        self.setLayout(grid)

        names=['Cls','Back','','Close',
               '7','8','9','/',
               '4','5','6','-',
               '1','2','3','+']

        positions=[(i,j) for i in range(5) for j in range(4)]
        print(positions)

        for position,name in zip(positions,names):
            if name=='':
                continue
            button=QPushButton(name)
            #x,y=position
            grid.addWidget(button,*position)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Clac()
    main.show()

    sys.exit(app.exec_())
