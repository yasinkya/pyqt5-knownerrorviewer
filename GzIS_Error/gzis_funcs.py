import glob
import json
from PyQt5.QtWidgets import QComboBox, QTabBar, QTableWidget
from GzIS_Error import global_variables


def read_paths():
    for path in glob.glob(f"{global_variables.folder}/*"):
        global_variables.json_paths.append(str(path).split("/")[-1])


def sync_global_jsonfiles(combo_box: QComboBox):
    global_variables.current_path = f"{global_variables.folder}"
    for files in glob.glob(f"{global_variables.folder}/{combo_box.currentText()}/*.json"):
        global_variables.json_files.clear()
        global_variables.json_files.append(str(files).split("/")[-1])


def set_tabbar(json_path, tabbar: QTabBar):
    with open(json_path, "r") as file:
        global_variables.current_jsondata = json.loads(file.read())["testSuites"]

    for key in global_variables.current_jsondata.keys():
        tabbar.addTab(key)


def apply_filter(table: QTableWidget, isaccept):
    if isaccept:
        for row in range(table.rowCount()):
            print(table.item(row, 2))
            tree = table.cellWidget(row, 2)
            # tree.toplevelite(0).child(0).text(0) -> failType fail
