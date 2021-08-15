from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget, QGridLayout, QPlainTextEdit
from PyQt5 import QtGui, QtCore
import json
import jsonPy_global


def read_json():
    f = open("jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QVBoxLayout, tab_main: QWidget, keys: set, current_idx):
    # define a new tabwidget then add this to main tabwidget's layout
    tabwid_child = QTabWidget(tab_main)
    layout.addWidget(tabwid_child)
    # the tablist is the name of the tabs to be created
    for i in keys:
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, i)



    # set click signal for created tabs & set their layout
    tabwid_child.currentChanged.connect(lambda: tabchanced(tabwid_child, jsonPy_global.jsondata["feeds"][current_idx]))
    tabchanced(tabwid_child, jsonPy_global.jsondata["feeds"][current_idx])

def tabchanced(clickedtab: QTabWidget, data):
    # todo: ram usage for created tabs click
    # todo: define layout for tabwidget and then add to another one gridlayout as child

    plaintext = QPlainTextEdit(clickedtab.currentWidget())
    plaintext.setReadOnly(True)
    plaintext.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))

    if isinstance(data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))], dict):
        plaintext.setPlainText("DİCT")
    elif isinstance(data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))], list):
        plaintext.setPlainText("List")
    else:
        plaintext.setPlainText(str(data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))]))

    # todo: when the 'addwidget' outside of this condition, it's creating new layouts
    if not clickedtab.currentWidget().layout():
        clickedtab.currentWidget().setLayout(QGridLayout(clickedtab.currentWidget()))
        clickedtab.currentWidget().layout().addWidget(plaintext)


