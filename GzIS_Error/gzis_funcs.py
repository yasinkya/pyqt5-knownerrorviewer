import glob
import json
from PyQt5.QtWidgets import QComboBox, QTabBar, QGridLayout, QVBoxLayout
from GzIS_Error import global_variables
from classes import create_table


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_jsonfiles(self: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{self.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabbar(json_path, tabbar: QTabBar, lay: QVBoxLayout):
    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    for key in global_variables.current_jsondata.keys():
        tabbar.addTab(key)

    if tabbar:
        data = global_variables.current_jsondata[tabbar.tabText(tabbar.currentIndex())]["tests"]
        tabbar.currentChanged.connect(lambda: set_table(data, lay))


def set_table(data, layout: QVBoxLayout):
    pass
    # table = create_table.NewTableWidget(data)
    # layout.addWidget(table)
    # if layout.count() < 1:
    #     layout.addWidget(table)
    # if layout.count() == 1:
    #
    # else:
    #     layout.removeWidget(layout.itemAt(1).widget())
    #     layout.addWidget(table)
