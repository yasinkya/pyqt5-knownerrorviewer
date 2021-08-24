import glob
import json
from PyQt5.QtWidgets import QComboBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLayout, QPlainTextEdit
from GzIS_Error import global_variables
from GzIS_Error.classes import TableWidget


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_cbx_path(self: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{self.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabwid(json_path, tabwid: QTabWidget):

    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    for key in global_variables.current_jsondata.keys():
        tabwid.addTab(QWidget(tabwid), key)

    tabwid.currentChanged.connect(lambda: init_child_tab(tabwid))


def init_child_tab(tabwid: QTabWidget):

    tabwid_child = QTabWidget(tabwid)

    if tabwid.currentWidget():

        if not tabwid.currentWidget().layout():
            tab_lay = QVBoxLayout(tabwid.currentWidget())
            tab_lay.addWidget(tabwid_child)

            datas = global_variables.current_jsondata.get(tabwid.tabText(tabwid.currentIndex()), {"tests": {}})["tests"]
            for data in datas.keys():
                tab_child = QWidget()
                tabwid_child.addTab(tab_child, data)
                instance_check(tabwid_child, tabwid_child.indexOf(tab_child), datas[data])

            tabwid.currentWidget().setLayout(tab_lay)


def instance_check(tabwid: QTabWidget, idx, data):

    if isinstance(data, dict):
        if not tabwid.widget(idx).layout():
            tablay = QGridLayout(tabwid.widget(idx))
            init_tablewidget(tablay, data)
    else:
        pass


def init_tablewidget(layout: QLayout, data):
    tablewidget = TableWidget.MyTableWidget(data)
    layout.addWidget(tablewidget)
