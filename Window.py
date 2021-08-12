from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget
import uis.mainUI as mainUI

class New(QMainWindow):
    def __init__(self,x,y,w,h):
        super(New,self).__init__()
        self.setGeometry(x,y,w,h)
        self.setWindowTitle("Main")
        self.initUI()

    def initUI(self):
        self.mainUI= mainUI.Ui_MainWindow()
        self.mainUI.setupUi(self)
        self.tab=self.mainUI.tabWidget

        tab= QWidget()
        self.tab.addTab(tab,"adsdf")
        
        
