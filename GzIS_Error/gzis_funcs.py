import glob
import json
from PyQt5.QtWidgets import QComboBox, QWidget, QTabWidget, QVBoxLayout
from PyQt5 import QtWidgets

from GzIS_Error import global_variables
from classes import Main_Window


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_cbx_path(self: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{self.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabwid(json_path, tablewid: QTabWidget):

    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    tablewid.clear()
    for key in global_variables.current_jsondata.keys():
        tablewid.addTab(QWidget(), key)

    tablewid.currentChanged.connect(lambda idx: init_child_tab(idx, tablewid))


def init_child_tab(cur_idx, tabwid: QTabWidget):
    if not tabwid.layout():
        tab_lay = QVBoxLayout()

        # define a new tabwidget then add this to main tabwidget's layout
        tabwid_child = QTabWidget(tabwid)
        tab_lay.addWidget(tabwid_child)

        # the tablist is the name of the tabs to be created
        for i in global_variables.current_jsondata[tabwid.tabText(cur_idx)]["tests"].keys():
            print(i)
            tab_child = QWidget()
            tabwid_child.addTab(tab_child, i)
            # instance_check(tabwid_child, tabwid_child.indexOf(tab_child), data[i])
