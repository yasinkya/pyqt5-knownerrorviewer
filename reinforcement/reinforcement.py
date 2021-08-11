from PyQt5 import QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
import sys


class NewWindow(QMainWindow):
    def __init__(self,cx,cy,w,h):
        super(NewWindow,self).__init__()

        self.setGeometry(cx,cy,w,h)
        self.setWindowTitle("Reinforcement")

        self.initUI()
    
    def initUI(self):
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setText("reinfr")
        self.lbl.move(50,50)

        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("btn")
        self.btn.clicked.connect(self.clck)
    
    def clck(self):
        self.lbl.setText("clcked")


def window():
    app=QApplication(sys.argv)

    cp=QDesktopWidget().availableGeometry().center()
    scres= app.desktop().availableGeometry()

    w,h=scres.width()/2.5,scres.height()/2.5
    cx,cy= cp.x()-w/2,cp.y()-h/2

    win=NewWindow(cx,cy,w,h)

    win.show()
    sys.exit(app.exec())

window()



