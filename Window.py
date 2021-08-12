from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import uis.tabwidget as tab

class New(QMainWindow):
    def __init__(self,x,y,w,h):
        super(New,self).__init__()
        self.setGeometry(x,y,w,h)
        self.setWindowTitle("Main")
        self.initUI()

    def initUI(self):
        self.tab=tab.Ui_MainWindow()
        self.tab.setupUi(self)
