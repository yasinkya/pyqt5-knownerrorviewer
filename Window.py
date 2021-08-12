from os import name
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLayout, QMainWindow, QVBoxLayout, QWidget
import uis.mainUI as mainUI
from PyQt5.QtGui import QPalette, QColor
import json


class New(QMainWindow):
    def __init__(self, x, y, w, h):
        super(New, self).__init__()
        self.setFixedSize(w,h)
        self.setGeometry(x, y, w, h)
        self.setWindowTitle("Main")
        self.initUI()

    def initUI(self):
        # set mainui to window
        self.mainUI = mainUI.Ui_MainWindow()
        self.mainUI.setupUi(self)

        # tabWidget
        self.tab = self.mainUI.tabWidget
        # sync qtabwidget
        self.syncTabs()
        # tabbar clicked
        self.tab.currentChanged.connect(self.tabChanged)

    def syncTabs(self):
        f = open("jsons/employee.json", "r")
        data = json.loads(f.read())

        for i in data["feeds"]:
            tab = QWidget()

            # if i["id"]==2135:
            #     tabLay=QVBoxLayout()
            #     lbl=QLabel("vertic")
            #     tabLay.addWidget(lbl)
            #     tab.setLayout(tabLay)
            self.tab.addTab(tab, str(i["id"]))

    # clicked tabbar

    def tabChanged(self):
        
        #print(self.tab.tabText(self.tab.currentIndex()))
        #self.tab.setTabText(self.tab.currentIndex(), "chanced")

        f = open("jsons/employee.json", "r")
        data = json.loads(f.read())
        tabLay = QVBoxLayout()
        lbl=QLabel()
        for i in data["feeds"]:
            if self.tab.tabText(self.tab.currentIndex())==str(i["id"]):
                lbl.setText(str(i))
                break
        
        tabLay.addWidget(lbl)
        self.tab.currentWidget().setLayout(tabLay)

        # tab.setLayout(tabLay)
