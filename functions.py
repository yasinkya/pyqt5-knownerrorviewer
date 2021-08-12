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
        tabWid.currentWidget().setLayout(newTab_lay)