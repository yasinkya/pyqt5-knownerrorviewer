import glob
import json
from PyQt5.QtWidgets import QComboBox, QWidget, QTabWidget, QVBoxLayout, QGridLayout, QLayout, QPlainTextEdit, QTabBar
from GzIS_Error import global_variables
from classes import table_widget


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_jsonfiles(self: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{self.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabbar(json_path, tabbar: QTabBar):

    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    for key in global_variables.current_jsondata.keys():
        tabbar.addTab(key)

    tabbar.currentChanged.connect(lambda: set_table(global_variables.current_jsondata[tabbar.tabText(tabbar.currentIndex())]))


def set_table(data):
    print(data)

