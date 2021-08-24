import glob
import json
from PyQt5.QtWidgets import QComboBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLayout, QPlainTextEdit
from GzIS_Error import global_variables


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
        tabwid.addTab(QWidget(), key)

    tabwid.currentChanged.connect(lambda: init_child_tab(tabwid))


def init_child_tab(tabwid: QTabWidget):

    if not tabwid.layout():
        tab_lay = QVBoxLayout()
        tabwid_child = QTabWidget(tabwid)
        tab_lay.addWidget(tabwid_child)

    datas = global_variables.current_jsondata.get(tabwid.tabText(tabwid.currentIndex()), {"tests": {}})["tests"]
    for data in datas.keys():
        print(data)
        tab_child = QWidget()
        tabwid_child.addTab(tab_child, data)
