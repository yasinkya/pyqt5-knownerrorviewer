from os import name
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget
import uis.mainUI as mainUI
import json

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

        self.syncTabs()
        self.tab.currentChanged.connect(self.tabChanged)
        
    def syncTabs(self):
        f= open("jsons/employee.json","r")
        data= json.loads(f.read())

        for i in data["feeds"]:
            tab= QWidget()
            self.tab.addTab(tab,str(i["id"]))
            

    def tabChanged(self):
        print(self.tab.tabText(self.tab.currentIndex()))