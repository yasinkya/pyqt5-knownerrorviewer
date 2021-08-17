from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTabWidget, QLayout, QWidget, QGridLayout, QPlainTextEdit, QTableWidget, QTableWidgetItem
from PyQt5 import QtGui, QtCore
import json


def read_json():
    f = open("../jsons/employee.json", "r")
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
            init_toolbox(tablay, tabwid, idx, data)


    elif isinstance(data, dict):
        colored_tabtext(tabwid, idx, QColor(100, 100, 200))
        if not tabwid.widget(idx).layout():
            tablay = QGridLayout(tabwid.widget(idx))
            newtab(tablay, tabwid.widget(idx), data)

    else:
        init_tab(tabwid, idx, str(data))


def colored_tabtext(tabwid: QTabWidget, idx, color: QColor()):
    tabwid.tabBar().setTabTextColor(idx, color)


def init_toolbox(tablay: QLayout, tabwid: QTabWidget, idx, data):
    tablewidget = QTableWidget(tabwid.widget(idx))
    tablewidget.setRowCount(len(data))
    for i in range(len(data)):
        tablewidget.setColumnCount(len(data[i].keys()))
        item = QTableWidgetItem()
        item.setText(str(i))
        tablewidget.setVerticalHeaderItem(i, item)
        for j in range(len(data[i])):
            item = QTableWidgetItem()
            key = str(list(data[i].keys())[j])
            item.setText(key)
            tablewidget.setHorizontalHeaderItem(j, item)

            insert_item = QTableWidgetItem()
            tablewidget.setItem(i, j, insert_item)
            insert_item.setText(str(data[i][key]))

    tablay.addWidget(tablewidget)