from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QMainWindow, QTabWidget, QVBoxLayout, QWidget
import uis.mainUI as mainUI,functions,json
from PyQt5.QtGui import QPalette, QColor
import jsonPy_global

class New(QMainWindow):
    def __init__(self, x, y, w, h):
        super(New, self).__init__()
        self.setGeometry(x, y, w, h)
        self.setFixedSize(w,h) # cannot let resize the window
        self.setWindowTitle("Main")
        self.initUI()

    def initUI(self):
        jsonPy_global.jsondata=functions.readJson()
        # set mainui to window
        self.mainUI = mainUI.Ui_MainWindow()
        self.mainUI.setupUi(self)

        # tabWidget
        self.tab = self.mainUI.tabWidget
        # sync qtabwidget
        self.syncTabs(jsonPy_global.jsondata)
        # tabbar clicked
        tab:QTabWidget
        self.tab.currentChanged.connect(lambda idx: self.tabChanged(jsonPy_global.jsondata["feeds"][idx]))
        
        

    # Add tabs and change the their text's through json
    def syncTabs(self,data):
        for i in data["feeds"]:
            tab = QWidget()
            self.tab.addTab(tab, str(i["id"]))

    # clicked tabbar
    def tabChanged(self,data): 
        tabLay = QVBoxLayout()
        functions.newTab(tabLay, data.keys())
        # for i in data:
        #     # if self.tab.tabText(self.tab.currentIndex())==i:
        #     #functions.newTab(tabLay,i["name"])
        #     list=set()
        #     for j in i:
        #         list.add(j)
        #
        #     break

        #tabLay.addWidget(lbl)
        #functions.newTab(tabLay)
        self.tab.currentWidget().setLayout(tabLay)


