from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
import sys

class NewWindow(QMainWindow):
    def __init__(self,cx,cy,w,h):
        super(NewWindow,self).__init__()
        self.setWindowTitle("reinforce")
        self.setGeometry(cx,cy,w,h)
        self.initUI()

    def initUI(self):
        self.lbl=QtWidgets.QLabel(self)
        self.lbl.setText("ndn")
        self.lbl.move(100,100)

        self.btn=QtWidgets.QPushButton(self)
        self.btn.setText("btn")
        self.btn.clicked.connect(self.clck)

    def clck(self):
        self.lbl.setText("changed")