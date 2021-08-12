from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QMainWindow, QTabWidget, QVBoxLayout, QWidget
import uis.mainUI as mainUI,functions,json
from PyQt5.QtGui import QPalette, QColor


class New(QMainWindow):
    def __init__(self, x, y, w, h):
        super(New, self).__init__()
        self.setGeometry(x, y, w, h)
        self.setFixedSize(w,h) # cannot let resize the window
        self.setWindowTitle("Main")
        self.initUI()

    def initUI(self):
        jsonData=functions.readJson()
        # set mainui to window
        self.mainUI = mainUI.Ui_MainWindow()
        self.mainUI.setupUi(self)

        # tabWidget
        self.tab = self.mainUI.tabWidget
        # sync qtabwidget
        self.syncTabs(jsonData)
        # tabbar clicked
        self.tab.currentChanged.connect(lambda: functions.tabChanged(self.tab,jsonData))
        
        

    # Add tabs and change the their text's through json
    def syncTabs(self,data):
        for i in data["feeds"]:
            tab = QWidget()
            self.tab.addTab(tab, str(i["id"]))

"""
    # clicked tabbar
    def tabChanged(self,data): 
        tabLay = QVBoxLayout()
        for i in data["feeds"]:
            if self.tab.tabText(self.tab.currentIndex())==str(i["id"]):
                #functions.newTab(tabLay,i["name"])
                list=set()
                for j in i:
                    list.add(j)
                print(list)
                print(len(list))
                functions.newTab(tabLay,list)
                break

        #tabLay.addWidget(lbl)
        #functions.newTab(tabLay)
        self.tab.currentWidget().setLayout(tabLay)

"""
