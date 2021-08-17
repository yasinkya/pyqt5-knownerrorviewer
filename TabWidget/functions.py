from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTabWidget, QLayout, QWidget, QGridLayout, QPlainTextEdit, QToolBox
from PyQt5 import QtGui, QtCore
import json


def read_json():
    f = open("../jsonPy/jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QLayout, tab_main: QWidget, data):
    # define a new tabwidget then add this to main tabwidget's layout
    tabwid_child = QTabWidget(tab_main)
    layout.addWidget(tabwid_child)

    # the tablist is the name of the tabs to be created
    for i in data.keys():
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, i)
        instance_check(tabwid_child, tabwid_child.indexOf(tab_child), data[i])

    # set click signal for created tabs & set their layout
    # tabwid_child.currentChanged.connect(lambda: instance_check(tabwid_child, data))
    # instance_check(tabwid_child, data)


def init_tab(clickedtab: QTabWidget, idx,  data):
    # todo: ram usage for created tabs click
    # todo: define layout for tabwidget and then add to another one gridlayout as child
    plaintext = QPlainTextEdit(clickedtab.currentWidget())
    plaintext.setReadOnly(True)
    plaintext.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
    plaintext.setPlainText(data)

    # todo: when the 'addwidget' outside of this condition, it's creating new layouts
    if not clickedtab.widget(idx).layout():
        clickedtab.widget(idx).setLayout(QGridLayout(clickedtab.widget(idx)))
        clickedtab.widget(idx).layout().addWidget(plaintext)


def instance_check(tabwid: QTabWidget, idx: None, data):
    if isinstance(data, list):
        colored_tabtext(tabwid, idx, QColor(200, 70, 200))
        if not tabwid.widget(idx).layout():
            tablay = QGridLayout(tabwid.widget(idx))
            tbox = QToolBox(tabwid.widget(idx))
            for i in range(len(data)):
                page = QWidget()
                pagelay = QGridLayout(page)
                tbox.addItem(page, str(i))
                newtab(pagelay, tabwid, data[i])
            tablay.addWidget(tbox)

    elif isinstance(data, dict):
        colored_tabtext(tabwid, idx, QColor(100, 100, 200))
        if not tabwid.widget(idx).layout():
            tablay = QGridLayout(tabwid.widget(idx))
            newtab(tablay, tabwid.widget(idx), data)

    else:
        init_tab(tabwid, idx, str(data))


def colored_tabtext(tabwid: QTabWidget, idx, color: QColor()):
    tabwid.tabBar().setTabTextColor(idx, color)
