from typing import Set
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout,QWidget
import json

def readJson():
    f=open("jsons/employee.json","r")
    data=json.loads(f.read())
    f.close()
    return data

def newTab(layout:QVBoxLayout,tabList:Set):
    tabWid=QTabWidget()
    layout.addWidget(tabWid)
    newTab_lay=QVBoxLayout()
    for i in tabList:
        tab=QWidget()
        tabWid.addTab(tab,i)
        tabWid.currentChanged.connect(lambda: tabChanced(tabWid,readJson()["feeds"]))
        tabWid.currentWidget().setLayout(newTab_lay)

def tabChanced(clickedTab:QTabWidget,data):
    tabLay = QVBoxLayout()
    tabList=set()
    for i in data:
        tabList.add(i)
        if clickedTab.tabText(clickedTab.currentIndex())==str(i):
            #functions.newTab(tabLay,i["name"])
            list=set()
            for j in i:
                list.add(j)
            print(list)
            print(len(list))
            newTab(tabLay,list)
            break

        #tabLay.addWidget(lbl)
        #functions.newTab(tabLay)
        clickedTab.currentWidget().setLayout(tabLay)