from PyQt5.QtWidgets import QTabWidget, QLayout, QWidget, QGridLayout, QPlainTextEdit
from PyQt5 import QtGui, QtCore
import json
import jsonPy_global


def read_json():
    f = open("jsons/employee.json", "r")
    data = json.loads(f.read())
    f.close()
    return data


def newtab(layout: QLayout, tab_main: QWidget, keys: set, idx_c):
    # define a new tabwidget then add this to main tabwidget's layout
    tabwid_child = QTabWidget(tab_main)
    layout.addWidget(tabwid_child)
    # the tablist is the name of the tabs to be created
    for i in keys:
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, i)



    # set click signal for created tabs & set their layout
    tabwid_child.currentChanged.connect(lambda idx: instance_check(tabwid_child, jsonPy_global.jsondata["feeds"][idx_c], idx))
    # tabwid_child.currentChanged.connect(lambda idx: tabchanced(tabwid_child, jsonPy_global.jsondata["feeds"][idx_c]))

    # tabchanced(tabwid_child, jsonPy_global.jsondata["feeds"][idx_c])

def tabchanced(clickedtab: QTabWidget, data):
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


def instance_check(clickedtab: QTabWidget, data, current_idx):
    check_this = data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))]
    if isinstance(check_this, dict):
        print("DİCT")
    elif isinstance(check_this, list):
        if not clickedtab.currentWidget().layout():
            layout = QGridLayout(clickedtab.currentWidget())
            newtab(layout, clickedtab.currentWidget(), check_this[0].keys(), current_idx)
    else:
        try:
            raise tabchanced(clickedtab, str(check_this))
        except tabchanced as exc:
            print(exc)

        # plaintext.setPlainText(str(data[clickedtab.tabText(clickedtab.indexOf(clickedtab.currentWidget()))]))