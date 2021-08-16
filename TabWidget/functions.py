from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTabWidget, QLayout, QWidget, QGridLayout, QPlainTextEdit, QStyle
from PyQt5 import QtGui, QtCore, QtWidgets
import json


def read_json():
    f = open("../jsonPy/jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QLayout, tab_main: QWidget, data, whats_type):
    # define a new tabwidget then add this to main tabwidget's layout
    tabwid_child = QTabWidget(tab_main)
    layout.addWidget(tabwid_child)
    k = tab_main.parent().parent()
    k_idx = k.currentIndex()
    tabbar = k.tabBar()
    # the tablist is the name of the tabs to be created
    for i in data.keys():
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, i)

        if whats_type == "tab":
            clr = QColor(15, 125, 15)
            tabbar.setTabTextColor(k_idx, clr)

    # set click signal for created tabs & set their layout
    tabwid_child.currentChanged.connect(lambda: instance_check(tabwid_child, data))
    instance_check(tabwid_child, data)


def tabchanged(clickedtab: QTabWidget, data):
    # todo: ram usage for created tabs click
    # todo: define layout for tabwidget and then add to another one gridlayout as child
    plaintext = QPlainTextEdit(clickedtab.currentWidget())
    plaintext.setReadOnly(True)
    plaintext.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
    plaintext.setPlainText(data)

    # todo: when the 'addwidget' outside of this condition, it's creating new layouts
    if not clickedtab.currentWidget().layout():
        clickedtab.currentWidget().setLayout(QGridLayout(clickedtab.currentWidget()))
        clickedtab.currentWidget().layout().addWidget(plaintext)


def instance_check(clickedtab: QTabWidget, data):
    check_this = data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))]

    if isinstance(check_this, dict):
        if not clickedtab.currentWidget().layout():
            layout = QGridLayout(clickedtab.currentWidget())
            newtab(layout, clickedtab.currentWidget(), check_this, "tab")
    elif isinstance(check_this, list):
        if not clickedtab.currentWidget().layout():
            layout = QGridLayout(clickedtab.currentWidget())
            newtab(layout, clickedtab.currentWidget(), check_this[0], "")
    else:
        tabchanged(clickedtab, str(check_this))
